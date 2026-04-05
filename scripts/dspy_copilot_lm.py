#!/usr/bin/env python3
"""DSPy backend that shells out to the GitHub Copilot CLI."""
from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path
from types import SimpleNamespace
from typing import Any

from dspy_codex_lm import build_prompt


def copilot_cli_path() -> str | None:
    return shutil.which("gh")


def copilot_exec_timeout_seconds(default: int = 180) -> int:
    raw_value = os.environ.get("DSPY_COPILOT_TIMEOUT_SECONDS")
    if raw_value is None:
        return default
    try:
        parsed = int(raw_value)
    except ValueError:
        return default
    return parsed if parsed > 0 else default


class CopilotRuntimeInfo:
    __slots__ = ("cli_path", "credentials_configured", "credential_sources")

    def __init__(self, **kwargs: Any):
        for attr in self.__slots__:
            setattr(self, attr, kwargs.get(attr))


class CopilotProbeResult:
    __slots__ = ("transport", "session_id", "resolved_model", "usage", "content")

    def __init__(self, **kwargs: Any):
        for attr in self.__slots__:
            setattr(self, attr, kwargs.get(attr))


def _resolve_copilot_model(model: str | None) -> str | None:
    if model is None:
        return None

    raw = model.strip()
    if raw.startswith("copilot/"):
        raw = raw[len("copilot/") :]

    if raw in {"", "default", "auto"}:
        return None

    aliases = {
        "codex-5.3": "gpt-5.3-codex",
        "gpt-5.3-codex": "gpt-5.3-codex",
    }
    return aliases.get(raw, raw)


def inspect_copilot_runtime() -> CopilotRuntimeInfo:
    cli = copilot_cli_path()
    return CopilotRuntimeInfo(
        cli_path=cli,
        credentials_configured=cli is not None,
        credential_sources=["gh-copilot"] if cli else [],
    )


def probe_copilot_runtime(
    *,
    repo_root: Path,
    model: str = "default",
    timeout_seconds: int = 60,
) -> CopilotProbeResult:
    text, usage, resolved_model = run_copilot_prompt(
        prompt="Reply with a single word: ready",
        repo_root=repo_root,
        model=model,
        timeout_seconds=timeout_seconds,
    )
    return CopilotProbeResult(
        transport="cli",
        session_id=None,
        resolved_model=resolved_model or "default",
        usage=usage,
        content=text[:120],
    )


def run_copilot_prompt(
    *,
    prompt: str,
    repo_root: Path,
    model: str | None = None,
    timeout_seconds: int | None = None,
) -> tuple[str, dict[str, int], str | None]:
    """Run a prompt through gh copilot and return (text, usage_dict, resolved_model)."""
    cli = copilot_cli_path()
    if not cli:
        raise RuntimeError("gh is not installed or not on PATH.")

    resolved_timeout = timeout_seconds or copilot_exec_timeout_seconds()
    resolved_model = _resolve_copilot_model(model)

    cmd = [
        cli,
        "copilot",
        "--",
        "-p",
        prompt,
        "--output-format",
        "json",
        "--no-custom-instructions",
    ]
    if resolved_model:
        cmd.extend(["--model", resolved_model])

    result = subprocess.run(
        cmd,
        cwd=str(repo_root),
        capture_output=True,
        text=True,
        timeout=resolved_timeout,
        check=False,
        env={**os.environ, "NO_COLOR": "1"},
    )

    if result.returncode != 0:
        message = (
            result.stderr.strip()
            or result.stdout.strip()
            or f"gh copilot exited with code {result.returncode}"
        )
        raise RuntimeError(message)

    text = ""
    output_tokens = 0
    model_from_session = resolved_model
    for line in result.stdout.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue

        if event.get("type") == "session.tools_updated":
            data = event.get("data", {})
            if isinstance(data, dict) and data.get("model"):
                model_from_session = str(data["model"])

        if event.get("type") == "assistant.message":
            data = event.get("data", {})
            if isinstance(data, dict):
                text = str(data.get("content", "")).strip() or text
                output_tokens = int(data.get("outputTokens", 0) or 0)

    if not text:
        raise RuntimeError("gh copilot returned no text output.")

    usage = {
        "prompt_tokens": 0,
        "completion_tokens": output_tokens,
        "total_tokens": output_tokens,
    }
    return text, usage, model_from_session


def create_copilot_lm(dspy_module: Any, model: str, repo_root: Path, **kwargs: Any) -> Any:
    """Create a DSPy BaseLM subclass that routes through GitHub Copilot CLI."""

    class CopilotCLILM(dspy_module.BaseLM):
        def __init__(self, model: str, repo_root: Path, **lm_kwargs: Any) -> None:
            lm_kwargs.pop("isolate_home", None)
            super().__init__(model=model, model_type="chat", cache=False, **lm_kwargs)
            self._repo_root = repo_root

        def forward(
            self,
            prompt: str | None = None,
            messages: list[dict[str, Any]] | None = None,
            **call_kwargs: Any,
        ) -> Any:
            rendered = build_prompt(prompt=prompt, messages=messages)
            timeout = int(call_kwargs.pop("timeout_seconds", copilot_exec_timeout_seconds()))
            text, usage, resolved_model = run_copilot_prompt(
                prompt=rendered,
                repo_root=self._repo_root,
                model=self.model,
                timeout_seconds=timeout,
            )
            return SimpleNamespace(
                choices=[SimpleNamespace(message=SimpleNamespace(content=text))],
                usage=usage,
                model=resolved_model or self.model,
                _hidden_params={},
            )

    kwargs.pop("isolate_home", None)
    return CopilotCLILM(model=model, repo_root=repo_root, **kwargs)
