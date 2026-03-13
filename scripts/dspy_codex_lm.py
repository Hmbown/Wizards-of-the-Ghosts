#!/usr/bin/env python3
"""Experimental DSPy backend that shells out to local Codex CLI."""
from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path
from types import SimpleNamespace
from typing import Any


def is_codex_exec_model(model: str) -> bool:
    return model.startswith("codex-exec/")


def codex_cli_path() -> str | None:
    return shutil.which("codex")


def codex_exec_timeout_seconds(default: int = 120) -> int:
    raw_value = os.environ.get("DSPY_CODEX_TIMEOUT_SECONDS") or os.environ.get("CODEX_EXEC_TIMEOUT_SECONDS")
    if raw_value is None:
        return default
    try:
        parsed = int(raw_value)
    except ValueError:
        return default
    return parsed if parsed > 0 else default


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


def build_prompt(prompt: str | None = None, messages: list[dict[str, Any]] | None = None) -> str:
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


def run_codex_exec(
    *,
    prompt: str,
    repo_root: Path,
    codex_model: str | None = None,
    timeout_seconds: int | None = None,
) -> tuple[str, dict[str, int], str]:
    cli = codex_cli_path()
    if not cli:
        raise RuntimeError("codex CLI is not installed or not on PATH.")

    resolved_timeout_seconds = timeout_seconds if timeout_seconds is not None else codex_exec_timeout_seconds()

    cmd = [
        cli,
        "exec",
        "--json",
        "--skip-git-repo-check",
        "--sandbox",
        "read-only",
        "--ephemeral",
        "-C",
        str(repo_root),
    ]
    if codex_model and codex_model not in {"default", "auto"}:
        cmd.extend(["-m", codex_model])
    cmd.append(prompt)

    result = subprocess.run(
        cmd,
        cwd=str(repo_root),
        capture_output=True,
        text=True,
        timeout=resolved_timeout_seconds,
        check=False,
    )
    if result.returncode != 0:
        message = result.stderr.strip() or result.stdout.strip() or f"codex exec exited with code {result.returncode}"
        raise RuntimeError(message)

    final_text = ""
    output_tokens = 0
    input_tokens = 0
    for line in result.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        event = json.loads(line)
        if event.get("type") == "item.completed":
            item = event.get("item", {})
            if item.get("type") == "agent_message":
                final_text = str(item.get("text", ""))
        elif event.get("type") == "turn.completed":
            usage = event.get("usage", {})
            output_tokens = int(usage.get("output_tokens", 0))
            input_tokens = int(usage.get("input_tokens", 0))

    if not final_text.strip():
        raise RuntimeError("codex exec returned no final agent message.")

    usage = {
        "prompt_tokens": input_tokens,
        "completion_tokens": output_tokens,
        "total_tokens": input_tokens + output_tokens,
    }
    return final_text, usage, result.stderr


def create_codex_exec_lm(dspy: Any, model: str, repo_root: Path, **kwargs: Any) -> Any:
    """Create a real `dspy.BaseLM` subclass instance around `codex exec`."""

    class CodexExecLM(dspy.BaseLM):
        def __init__(self, model: str, repo_root: Path, **lm_kwargs: Any) -> None:
            super().__init__(model=model, model_type="chat", cache=False, **lm_kwargs)
            self._repo_root = repo_root
            self._codex_model = model.split("/", 1)[1] if "/" in model else None

        def forward(
            self,
            prompt: str | None = None,
            messages: list[dict[str, Any]] | None = None,
            **call_kwargs: Any,
        ) -> Any:
            rendered_prompt = build_prompt(prompt=prompt, messages=messages)
            timeout_seconds = int(call_kwargs.pop("timeout_seconds", codex_exec_timeout_seconds()))
            text, usage, stderr = run_codex_exec(
                prompt=rendered_prompt,
                repo_root=self._repo_root,
                codex_model=self._codex_model,
                timeout_seconds=timeout_seconds,
            )
            return SimpleNamespace(
                choices=[SimpleNamespace(message=SimpleNamespace(content=text))],
                usage=usage,
                model=self.model,
                _hidden_params={"stderr": stderr},
            )

    return CodexExecLM(model=model, repo_root=repo_root, **kwargs)
