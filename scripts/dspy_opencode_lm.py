#!/usr/bin/env python3
"""Experimental DSPy backend that shells out to local OpenCode CLI."""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
from pathlib import Path
from types import SimpleNamespace
from typing import Any


def is_opencode_exec_model(model: str) -> bool:
    return model.startswith("opencode/")


def _normalize_opencode_model(model: str | None) -> str | None:
    if model is None:
        return None
    raw = model.strip()
    if raw.startswith("opencode/"):
        raw = raw[len("opencode/") :]
    if raw in {"", "default", "auto"}:
        return None
    return raw


def opencode_cli_path() -> str | None:
    return shutil.which("opencode")


def opencode_exec_timeout_seconds(default: int = 300) -> int:
    """Get timeout for OpenCode CLI calls.
    
    Default is 300s (5 minutes) for GEPA optimization which sends large prompts.
    Can be overridden via DSPY_OPENCODE_TIMEOUT_SECONDS or OPENCODE_EXEC_TIMEOUT_SECONDS.
    """
    raw_value = os.environ.get("DSPY_OPENCODE_TIMEOUT_SECONDS") or os.environ.get(
        "OPENCODE_EXEC_TIMEOUT_SECONDS"
    )
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


def extract_structured_output(text: str, output_fields: list[str]) -> dict[str, str]:
    """Extract structured output fields from free-form text.
    
    DSPy's ChatAdapter expects outputs with field markers like:
        [[ ## response ## ]]
        [[ ## reasoning ## ]]
    
    This function extracts field values when the model doesn't follow the format exactly.
    
    Args:
        text: The raw model output
        output_fields: List of expected output field names
        
    Returns:
        Dictionary mapping field names to extracted values
    """
    result: dict[str, str] = {}
    
    # First try to extract using field markers
    field_pattern = re.compile(r"\[\[\s*##\s*(\w+)\s*##\s*\]\]\s*\n?(.*?)(?=\[\[|$)", re.DOTALL | re.IGNORECASE)
    for match in field_pattern.finditer(text):
        field_name = match.group(1).lower()
        field_value = match.group(2).strip()
        if field_name in [f.lower() for f in output_fields]:
            result[field_name] = field_value
    
    # If we got all fields via markers, return
    if len(result) == len(output_fields):
        return result
    
    # Fallback: try to extract common DSPy fields heuristically
    lower_text = text.lower()
    
    # Look for "reasoning" or "thought" sections
    if "reasoning" in [f.lower() for f in output_fields] and "reasoning" not in result:
        reasoning_patterns = [
            r"(?:reasoning|thought|analysis|thinking)[:\s]+(.*?)(?=\n\s*(?:response|answer|output|##|$))",
            r"^(.*?)\n+(?=response|answer|output)",
        ]
        for pattern in reasoning_patterns:
            match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
            if match:
                result["reasoning"] = match.group(1).strip()
                break
    
    # Look for "response" section
    if "response" in [f.lower() for f in output_fields] and "response" not in result:
        response_patterns = [
            r"(?:response|answer|output)[:\s]+(.*?)(?=\n\s*(?:##|$))",
            r"(?:##\s*)?(?:response|answer|output)\s*##\s*\n?(.*?)(?=\[\[|$)",
        ]
        for pattern in response_patterns:
            match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
            if match:
                result["response"] = match.group(1).strip()
                break
    
    # If still missing fields, use the entire text as "response"
    if "response" in [f.lower() for f in output_fields] and "response" not in result:
        result["response"] = text.strip()
    
    return result


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


def run_opencode_exec(
    *,
    prompt: str,
    repo_root: Path,
    opencode_model: str | None = None,
    timeout_seconds: int | None = None,
) -> tuple[str, dict[str, int], str]:
    cli = opencode_cli_path()
    if not cli:
        raise RuntimeError("opencode CLI is not installed or not on PATH.")

    resolved_timeout_seconds = (
        timeout_seconds
        if timeout_seconds is not None
        else opencode_exec_timeout_seconds()
    )
    resolved_model = _normalize_opencode_model(opencode_model) or _normalize_opencode_model(
        os.environ.get("DSPY_OPENCODE_MODEL")
    )

    cmd = [
        cli,
        "run",
        "--format",
        "json",
        "--dir",
        str(repo_root),
    ]
    if resolved_model:
        cmd.extend(["-m", resolved_model])
    cmd.append(prompt)

    result = subprocess.run(
        cmd,
        cwd=str(repo_root),
        capture_output=True,
        text=True,
        timeout=resolved_timeout_seconds,
        check=False,
        env={**os.environ, "NO_COLOR": "1"},
    )
    if result.returncode != 0:
        message = (
            result.stderr.strip()
            or result.stdout.strip()
            or f"opencode run exited with code {result.returncode}"
        )
        raise RuntimeError(message)

    final_text = ""
    output_tokens = 0
    input_tokens = 0
    total_tokens = 0
    for line in result.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        event_type = event.get("type")
        if event_type == "text":
            part = event.get("part", {})
            text = str(part.get("text", ""))
            if text.strip():
                final_text += text
        elif event_type == "step_finish":
            tokens = event.get("part", {}).get("tokens", {})
            if not tokens:
                tokens = event.get("tokens", {})
            output_tokens = int(
                tokens.get("output", tokens.get("completion_tokens", 0))
            )
            input_tokens = int(tokens.get("input", tokens.get("prompt_tokens", 0)))
            total_tokens = int(tokens.get("total", 0))

    if not final_text.strip():
        raise RuntimeError("opencode run returned no final text.")

    usage = {
        "prompt_tokens": input_tokens,
        "completion_tokens": output_tokens,
        "total_tokens": total_tokens if total_tokens else input_tokens + output_tokens,
    }
    return final_text, usage, result.stderr


def create_opencode_exec_lm(
    dspy: Any, model: str, repo_root: Path, **kwargs: Any
) -> Any:
    """Create a real `dspy.BaseLM` subclass instance around `opencode run`."""
    import re

    class OpenCodeExecLM(dspy.BaseLM):
        def __init__(self, model: str, repo_root: Path, **lm_kwargs: Any) -> None:
            super().__init__(model=model, model_type="chat", cache=False, **lm_kwargs)
            self._repo_root = repo_root
            self._opencode_model = model

        def forward(
            self,
            prompt: str | None = None,
            messages: list[dict[str, Any]] | None = None,
            **call_kwargs: Any,
        ) -> Any:
            rendered_prompt = build_prompt(prompt=prompt, messages=messages)
            timeout_seconds = int(
                call_kwargs.pop("timeout_seconds", opencode_exec_timeout_seconds())
            )
            raw_text, usage, stderr = run_opencode_exec(
                prompt=rendered_prompt,
                repo_root=self._repo_root,
                opencode_model=self._opencode_model,
                timeout_seconds=timeout_seconds,
            )
            
            # Model may echo the full DSPy template including field markers.
            # Extract just the response field content.
            text = extract_response_field(raw_text)
            
            # Wrap in DSPy format for the adapter
            text = f"[[ ## response ## ]]\n{text}\n\n[[ ## completed ## ]]"
            
            return SimpleNamespace(
                choices=[SimpleNamespace(message=SimpleNamespace(content=text))],
                usage=usage,
                model=self.model,
                _hidden_params={"stderr": stderr},
            )

    return OpenCodeExecLM(model=model, repo_root=repo_root, **kwargs)


def extract_response_field(text: str) -> str:
    """Extract the response field value from model output that may echo DSPy format.
    
    Models sometimes echo the full template like:
        [[ ## user_request ## ]]
        <input>
        [[ ## response ## ]]
        <actual response>
        [[ ## completed ## ]]
    
    This extracts just the <actual response> part.
    """
    # Look for response field pattern
    pattern = r'\[\[\s*##\s*response\s*##\s*\]\]\s*\n(.*?)(?=\[\[\s*##\s*\w+\s*##\s*\]\]|$)'
    match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
    
    if match:
        # Found response field, extract and clean it
        response = match.group(1).strip()
        # Remove any trailing completed marker that might be captured
        response = re.sub(r'\n\s*\[\[\s*##\s*completed\s*##\s*\]\]\s*$', '', response)
        return response
    
    # No response field found, return text as-is (model didn't follow format)
    return text.strip()
