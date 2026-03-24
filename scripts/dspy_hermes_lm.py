#!/usr/bin/env python3
"""DSPy backend that uses the Hermes Agent API for inference.

This is the default backend for wizardsoftheghosts — the grimoire optimizes
its own spells through the same agent runtime that serves them.

Supports two transport modes:
  - CLI:  shells out to `hermes run --format json`
  - HTTP: POSTs to a Hermes API endpoint (HERMES_API_BASE)

Configure via environment:
  DSPY_MODEL=hermes/default          # or hermes/<model-name>
  HERMES_API_BASE=http://localhost:3000  # optional, for HTTP transport
  HERMES_API_KEY=...                     # optional, for authenticated endpoints
  HERMES_TIMEOUT_SECONDS=300             # default 300s for GEPA optimization
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from types import SimpleNamespace
from typing import Any


HERMES_MODEL_PREFIX = "hermes/"


def is_hermes_model(model: str) -> bool:
    return model.startswith(HERMES_MODEL_PREFIX)


def hermes_cli_path() -> str | None:
    return shutil.which("hermes")


def hermes_timeout_seconds(default: int = 300) -> int:
    """Get timeout for Hermes calls.

    Default is 300s for GEPA optimization which sends large prompts.
    """
    raw = os.environ.get("HERMES_TIMEOUT_SECONDS")
    if raw is None:
        return default
    try:
        parsed = int(raw)
    except ValueError:
        return default
    return parsed if parsed > 0 else default


def hermes_api_base() -> str | None:
    return os.environ.get("HERMES_API_BASE")


def hermes_api_key() -> str | None:
    return os.environ.get("HERMES_API_KEY")


def _coerce_content(content: Any) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts: list[str] = []
        for item in content:
            if isinstance(item, dict):
                text = item.get("text")
                if text:
                    parts.append(str(text))
            else:
                parts.append(str(item))
        return "\n".join(part for part in parts if part)
    return str(content)


def build_prompt(
    prompt: str | None = None, messages: list[dict[str, Any]] | None = None
) -> str:
    if messages:
        chunks: list[str] = []
        for message in messages:
            role = str(message.get("role", "user")).upper()
            content = _coerce_content(message.get("content", ""))
            if content:
                chunks.append(f"{role}:\n{content}")
        if prompt:
            chunks.append(f"PROMPT:\n{prompt}")
        return "\n\n".join(chunks).strip()
    return (prompt or "").strip()


def extract_response_field(text: str) -> str:
    """Extract the response field from model output that may echo DSPy format."""
    pattern = r"\[\[\s*##\s*response\s*##\s*\]\]\s*\n(.*?)(?=\[\[\s*##\s*\w+\s*##\s*\]\]|$)"
    match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
    if match:
        response = match.group(1).strip()
        response = re.sub(
            r"\n\s*\[\[\s*##\s*completed\s*##\s*\]\]\s*$", "", response
        )
        return response
    return text.strip()


# ---------------------------------------------------------------------------
# CLI transport
# ---------------------------------------------------------------------------


def run_hermes_cli(
    *,
    prompt: str,
    repo_root: Path,
    model: str | None = None,
    timeout_seconds: int | None = None,
) -> tuple[str, dict[str, int], str]:
    cli = hermes_cli_path()
    if not cli:
        raise RuntimeError(
            "hermes CLI is not installed or not on PATH. "
            "Install Hermes Agent or set HERMES_API_BASE for HTTP transport."
        )

    resolved_timeout = (
        timeout_seconds if timeout_seconds is not None else hermes_timeout_seconds()
    )

    # Hermes CLI uses: hermes chat -q "prompt" -Q (quiet/programmatic mode)
    cmd = [cli, "chat", "-q", prompt, "-Q"]
    if model:
        bare_model = model.removeprefix(HERMES_MODEL_PREFIX)
        if bare_model and bare_model != "default":
            cmd.extend(["-m", bare_model])

    result = subprocess.run(
        cmd,
        cwd=str(repo_root),
        capture_output=True,
        text=True,
        timeout=resolved_timeout,
        check=False,
    )
    if result.returncode != 0:
        message = (
            result.stderr.strip()
            or result.stdout.strip()
            or f"hermes chat exited with code {result.returncode}"
        )
        raise RuntimeError(message)

    # Quiet mode output: response text followed by "session_id: <id>" line
    lines = result.stdout.strip().splitlines()
    text_lines: list[str] = []
    for line in lines:
        if line.startswith("session_id:"):
            continue
        text_lines.append(line)

    final_text = "\n".join(text_lines).strip()
    if not final_text:
        raise RuntimeError("hermes chat returned no response text.")

    # Hermes CLI doesn't expose token counts in quiet mode
    usage = {
        "prompt_tokens": 0,
        "completion_tokens": 0,
        "total_tokens": 0,
    }
    return final_text, usage, result.stderr


# ---------------------------------------------------------------------------
# HTTP transport
# ---------------------------------------------------------------------------


def run_hermes_http(
    *,
    prompt: str,
    api_base: str,
    api_key: str | None = None,
    model: str | None = None,
    timeout_seconds: int | None = None,
) -> tuple[str, dict[str, int], str]:
    resolved_timeout = (
        timeout_seconds if timeout_seconds is not None else hermes_timeout_seconds()
    )

    bare_model = (model or "default").removeprefix(HERMES_MODEL_PREFIX)

    url = f"{api_base.rstrip('/')}/v1/chat/completions"
    payload = json.dumps(
        {
            "model": bare_model,
            "messages": [{"role": "user", "content": prompt}],
        }
    ).encode("utf-8")

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "wizardsoftheghosts-dspy/1.0",
    }
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    request = urllib.request.Request(url, data=payload, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(request, timeout=resolved_timeout) as response:
            body = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        error_body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(
            f"Hermes API returned HTTP {exc.code}: {error_body}"
        ) from exc

    choices = body.get("choices", [])
    if not choices:
        raise RuntimeError("Hermes API returned no choices.")

    text = choices[0].get("message", {}).get("content", "")
    if not text.strip():
        raise RuntimeError("Hermes API returned empty content.")

    usage_raw = body.get("usage", {})
    usage = {
        "prompt_tokens": int(usage_raw.get("prompt_tokens", 0)),
        "completion_tokens": int(usage_raw.get("completion_tokens", 0)),
        "total_tokens": int(usage_raw.get("total_tokens", 0)),
    }
    return text, usage, ""


# ---------------------------------------------------------------------------
# Unified dispatch
# ---------------------------------------------------------------------------


def run_hermes(
    *,
    prompt: str,
    repo_root: Path,
    model: str | None = None,
    timeout_seconds: int | None = None,
) -> tuple[str, dict[str, int], str]:
    """Run a prompt through Hermes, auto-selecting CLI or HTTP transport."""
    api_base = hermes_api_base()
    if api_base:
        return run_hermes_http(
            prompt=prompt,
            api_base=api_base,
            api_key=hermes_api_key(),
            model=model,
            timeout_seconds=timeout_seconds,
        )
    return run_hermes_cli(
        prompt=prompt,
        repo_root=repo_root,
        model=model,
        timeout_seconds=timeout_seconds,
    )


# ---------------------------------------------------------------------------
# DSPy LM class
# ---------------------------------------------------------------------------


def create_hermes_lm(
    dspy: Any, model: str, repo_root: Path, **kwargs: Any
) -> Any:
    """Create a `dspy.BaseLM` subclass instance around the Hermes Agent API."""

    class HermesLM(dspy.BaseLM):
        def __init__(self, model: str, repo_root: Path, **lm_kwargs: Any) -> None:
            super().__init__(model=model, model_type="chat", cache=False, **lm_kwargs)
            self._repo_root = repo_root
            self._hermes_model = model

        def forward(
            self,
            prompt: str | None = None,
            messages: list[dict[str, Any]] | None = None,
            **call_kwargs: Any,
        ) -> Any:
            rendered_prompt = build_prompt(prompt=prompt, messages=messages)
            timeout_seconds = int(
                call_kwargs.pop("timeout_seconds", hermes_timeout_seconds())
            )
            raw_text, usage, stderr = run_hermes(
                prompt=rendered_prompt,
                repo_root=self._repo_root,
                model=self._hermes_model,
                timeout_seconds=timeout_seconds,
            )

            text = extract_response_field(raw_text)
            text = f"[[ ## response ## ]]\n{text}\n\n[[ ## completed ## ]]"

            return SimpleNamespace(
                choices=[SimpleNamespace(message=SimpleNamespace(content=text))],
                usage=usage,
                model=self.model,
                _hidden_params={"stderr": stderr},
            )

    return HermesLM(model=model, repo_root=repo_root, **kwargs)


# ---------------------------------------------------------------------------
# Probe
# ---------------------------------------------------------------------------


def probe_hermes(
    model: str, repo_root: Path, timeout: float = 3.0
) -> dict[str, Any]:
    """Check whether the Hermes backend is reachable."""
    api_base = hermes_api_base()
    transport = "http" if api_base else "cli"

    probe: dict[str, Any] = {
        "checked": True,
        "backend_type": "hermes",
        "transport": transport,
    }

    if transport == "http":
        probe["api_base"] = api_base
        probe_url = f"{api_base.rstrip('/')}/v1/models"
        headers = {"User-Agent": "wizardsoftheghosts-dspy/1.0"}
        api_key = hermes_api_key()
        if api_key:
            headers["Authorization"] = f"Bearer {api_key}"
        request = urllib.request.Request(probe_url, headers=headers)
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                probe["reachable"] = True
                probe["http_status"] = response.status
                probe["message"] = "Hermes API is reachable."
        except urllib.error.HTTPError as exc:
            probe["reachable"] = True
            probe["http_status"] = exc.code
            probe["message"] = f"Hermes API responded with HTTP {exc.code}; treating as reachable."
        except Exception as exc:  # noqa: BLE001
            probe["reachable"] = False
            probe["message"] = "Hermes API probe failed."
            probe["error"] = str(exc)
        return probe

    # CLI transport
    cli = hermes_cli_path()
    probe["cli_available"] = cli is not None
    if cli is None:
        probe["reachable"] = False
        probe["message"] = (
            "hermes CLI is not installed or not on PATH. "
            "Set HERMES_API_BASE for HTTP transport, or install Hermes Agent."
        )
        return probe

    probe_timeout = hermes_timeout_seconds(default=max(int(timeout), 1) * 20)
    try:
        text, usage, stderr = run_hermes_cli(
            prompt="Respond with exactly one word: ready",
            repo_root=repo_root,
            model=model,
            timeout_seconds=probe_timeout,
        )
    except Exception as exc:  # noqa: BLE001
        probe["reachable"] = False
        probe["message"] = "Hermes CLI probe failed."
        probe["error"] = str(exc)
        return probe

    probe.update(
        {
            "reachable": True,
            "message": "Hermes backend probe completed successfully.",
            "resolved_model": model,
            "usage": usage,
            "sample_response": text[:120],
        }
    )
    return probe
