#!/usr/bin/env python3
"""DSPy backend that shells out to the local Qwen CLI."""
from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path
from types import SimpleNamespace
from typing import Any

from dspy_codex_lm import build_prompt


def qwen_cli_path() -> str | None:
    return shutil.which("qwen")


def qwen_exec_timeout_seconds(default: int = 180) -> int:
    raw_value = os.environ.get("DSPY_QWEN_TIMEOUT_SECONDS")
    if raw_value is None:
        return default
    try:
        parsed = int(raw_value)
    except ValueError:
        return default
    return parsed if parsed > 0 else default


class QwenRuntimeInfo:
    __slots__ = (
        "cli_path", "credentials_configured", "credential_sources",
        "qwen_home", "settings_file", "oauth_file", "mcp_oauth_file",
        "installation_id_file",
    )

    def __init__(self, **kwargs: Any):
        for attr in self.__slots__:
            setattr(self, attr, kwargs.get(attr))


class QwenProbeResult:
    __slots__ = ("transport", "session_id", "resolved_model", "usage", "content")

    def __init__(self, **kwargs: Any):
        for attr in self.__slots__:
            setattr(self, attr, kwargs.get(attr))


def inspect_qwen_runtime() -> QwenRuntimeInfo:
    cli = qwen_cli_path()
    qwen_home = os.environ.get("QWEN_HOME") or os.path.expanduser("~/.qwen")
    return QwenRuntimeInfo(
        cli_path=cli,
        credentials_configured=cli is not None,
        credential_sources=["cli"] if cli else [],
        qwen_home=qwen_home,
        settings_file=os.path.join(qwen_home, "settings.json") if qwen_home else None,
        oauth_file=None,
        mcp_oauth_file=None,
        installation_id_file=None,
    )


def probe_qwen_runtime(
    *,
    repo_root: Path,
    model: str = "qwen/default",
    timeout_seconds: int = 30,
) -> QwenProbeResult:
    text, usage = run_qwen_prompt(
        prompt="Reply with a single word: ready",
        repo_root=repo_root,
        timeout_seconds=timeout_seconds,
    )
    return QwenProbeResult(
        transport="cli",
        session_id=None,
        resolved_model=model,
        usage=usage,
        content=text[:120],
    )


def run_qwen_prompt(
    *,
    prompt: str,
    repo_root: Path,
    model: str | None = None,
    timeout_seconds: int | None = None,
) -> tuple[str, dict[str, int]]:
    """Run a prompt through Qwen CLI and return (text, usage_dict)."""
    cli = qwen_cli_path()
    if not cli:
        raise RuntimeError("qwen CLI is not installed or not on PATH.")

    resolved_timeout = timeout_seconds or qwen_exec_timeout_seconds()

    cmd = [
        cli,
        "--approval-mode", "plan",
        "--chat-recording=false",
        "-p", prompt,
    ]
    if model and model not in {"default", "auto", "qwen/default"}:
        qwen_model = model.split("/", 1)[1] if "/" in model else model
        cmd.extend(["-m", qwen_model])

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
        message = result.stderr.strip() or result.stdout.strip() or f"qwen exited with code {result.returncode}"
        raise RuntimeError(message)

    # Parse the response text - Qwen CLI outputs the response directly
    text = result.stdout.strip()
    if not text:
        raise RuntimeError("qwen CLI returned no output.")

    # Estimate tokens (rough: 4 chars per token)
    input_tokens = len(prompt) // 4
    output_tokens = len(text) // 4
    usage = {
        "prompt_tokens": input_tokens,
        "completion_tokens": output_tokens,
        "total_tokens": input_tokens + output_tokens,
    }
    return text, usage


def create_qwen_lm(dspy_module: Any, model: str, repo_root: Path, **kwargs: Any) -> Any:
    """Create a DSPy BaseLM subclass that routes through the Qwen CLI."""

    class QwenCLILM(dspy_module.BaseLM):
        def __init__(self, model: str, repo_root: Path, **lm_kwargs: Any) -> None:
            # Remove non-BaseLM kwargs
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
            timeout = int(call_kwargs.pop("timeout_seconds", qwen_exec_timeout_seconds()))
            text, usage = run_qwen_prompt(
                prompt=rendered,
                repo_root=self._repo_root,
                timeout_seconds=timeout,
            )
            return SimpleNamespace(
                choices=[SimpleNamespace(message=SimpleNamespace(content=text))],
                usage=usage,
                model=self.model,
                _hidden_params={},
            )

    kwargs.pop("isolate_home", None)
    return QwenCLILM(model=model, repo_root=repo_root, **kwargs)
