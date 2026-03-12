#!/usr/bin/env python3
"""Shared helpers for the repo-local DSPy workflow."""
from __future__ import annotations

import json
import os
import platform
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

CODEX_MODEL_PREFIXES = ("codex/", "codex-exec/", "codex-mcp/")

REQUIRED_DSPY_FILES = {
    "spells_master": "spells_master.jsonl",
    "categories": "categories.json",
    "train_queries": "hermes-train-queries.jsonl",
    "eval_queries": "hermes-eval-set.jsonl",
    "hard_negatives": "hermes-hard-negatives.jsonl",
    "abstain": "hermes-abstain.jsonl",
    "query_summary": "hermes_query_summary.json",
}

STATUS_PATHS = {
    "baseline_router": "baseline_router.json",
    "baseline_eval_summary": "baseline_eval_summary.json",
    "baseline_eval_predictions": "baseline_eval_predictions.jsonl",
    "dspy_router": "dspy_category_router.json",
    "dspy_router_status": "dspy_router_status.json",
    "dspy_eval_summary": "dspy_eval_summary.json",
    "dspy_eval_predictions": "dspy_eval_predictions.jsonl",
}

EVAL_SPLIT_FILES = {
    "eval": "hermes-eval-set.jsonl",
    "hard_negative": "hermes-hard-negatives.jsonl",
}

ROUTER_NOTES = [
    "The v1 DSPy router targets 8-way Hermes category routing.",
    "The abstain dataset is validation-only in this pass and is not scored by the router.",
]


@dataclass(frozen=True)
class LMConfig:
    model: str
    api_base: str | None = None
    api_key: str | None = None
    temperature: float | None = None
    max_tokens: int | None = None


def is_codex_model(model: str | None) -> bool:
    if model is None:
        return False
    return model.startswith(CODEX_MODEL_PREFIXES)


def codex_transport_hint(model: str) -> str:
    if model.startswith("codex-exec/"):
        return "cli"
    if model.startswith("codex-mcp/"):
        return "mcp"
    return "auto"


def load_codex_client() -> Any | None:
    try:
        from dspy.clients import codex as codex_client  # type: ignore
    except Exception:  # noqa: BLE001
        return None
    return codex_client


def dspy_dir(repo_root: Path) -> Path:
    return repo_root / "catalog" / "dspy"


def artifact_paths(repo_root: Path) -> dict[str, Path]:
    base = dspy_dir(repo_root)
    return {name: base / rel_path for name, rel_path in {**REQUIRED_DSPY_FILES, **STATUS_PATHS}.items()}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not path.exists():
        return rows
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.write_text(
        "\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + ("\n" if rows else ""),
        encoding="utf-8",
    )


def category_context(categories: list[dict[str, Any]]) -> str:
    return "\n".join(f"- {cat['slug']}: {cat['description']}" for cat in categories)


def dependency_info() -> tuple[Any | None, dict[str, Any]]:
    info: dict[str, Any] = {
        "python_executable": sys.executable,
        "python_version": platform.python_version(),
        "python_implementation": platform.python_implementation(),
        "dspy_installed": False,
    }
    try:
        import dspy  # type: ignore
    except Exception as exc:  # noqa: BLE001
        info["error"] = str(exc)
        return None, info
    info["dspy_installed"] = True
    info["dspy_version"] = getattr(dspy, "__version__", "unknown")
    info["codex_lm_available"] = hasattr(dspy, "CodexLM")
    return dspy, info


def validate_workspace(repo_root: Path) -> dict[str, Any]:
    paths = artifact_paths(repo_root)
    parsed: dict[str, Any] = {}
    missing: list[str] = []
    errors: list[str] = []
    for key, rel_path in REQUIRED_DSPY_FILES.items():
        path = paths[key]
        if not path.exists():
            missing.append(rel_path)
            continue
        try:
            parsed[key] = load_jsonl(path) if path.suffix == ".jsonl" else load_json(path)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{rel_path}: {exc}")

    dataset_counts = {
        "spells_master_rows": len(parsed.get("spells_master", [])),
        "category_rows": len(parsed.get("categories", [])),
        "train_rows": len(parsed.get("train_queries", [])),
        "eval_rows": len(parsed.get("eval_queries", [])),
        "hard_negative_rows": len(parsed.get("hard_negatives", [])),
        "abstain_rows": len(parsed.get("abstain", [])),
    }

    categories = parsed.get("categories", [])
    if categories:
        slugs = [str(row.get("slug")) for row in categories]
        if len(slugs) != len(set(slugs)):
            errors.append("categories.json contains duplicate category slugs")

    summary = parsed.get("query_summary")
    if summary:
        expected = {
            "train_rows": dataset_counts["train_rows"],
            "eval_rows": dataset_counts["eval_rows"],
            "hard_negative_rows": dataset_counts["hard_negative_rows"],
            "abstain_rows": dataset_counts["abstain_rows"],
        }
        for key, value in expected.items():
            if int(summary.get(key, -1)) != value:
                errors.append(
                    f"hermes_query_summary.json {key}={summary.get(key)!r} does not match dataset count {value}"
                )

    return {
        "ok": not missing and not errors,
        "missing_files": missing,
        "errors": errors,
        "dataset_counts": dataset_counts,
        "artifact_paths": {key: str(path) for key, path in paths.items()},
        "notes": ROUTER_NOTES,
    }


def collect_eval_rows(repo_root: Path, splits: list[str]) -> list[dict[str, Any]]:
    base = dspy_dir(repo_root)
    rows: list[dict[str, Any]] = []
    for split in splits:
        path = base / EVAL_SPLIT_FILES[split]
        split_rows = load_jsonl(path)
        for row in split_rows:
            row.setdefault("split", split)
        rows.extend(split_rows)
    return rows


def _arg_or_env(args: Any, attr: str, env_key: str) -> str | None:
    value = getattr(args, attr, None) if args is not None else None
    if value is None or value == "":
        value = os.environ.get(env_key)
    if value is None:
        return None
    stripped = str(value).strip()
    return stripped or None


def resolve_lm_config(args: Any | None = None) -> tuple[LMConfig | None, dict[str, Any]]:
    model = _arg_or_env(args, "dspy_model", "DSPY_MODEL")
    api_base = _arg_or_env(args, "dspy_api_base", "DSPY_API_BASE")
    api_key = _arg_or_env(args, "dspy_api_key", "DSPY_API_KEY")
    temperature_raw = _arg_or_env(args, "dspy_temperature", "DSPY_TEMPERATURE")
    max_tokens_raw = _arg_or_env(args, "dspy_max_tokens", "DSPY_MAX_TOKENS")
    codex_model = is_codex_model(model)

    backend: dict[str, Any] = {
        "configured": False,
        "model": model,
        "backend_type": "codex" if codex_model else "litellm",
        "api_base": api_base,
        "api_key_configured": bool(api_key),
        "provider_qualified_model_required": not codex_model,
        "optional_settings": {
            "temperature": temperature_raw,
            "max_tokens": max_tokens_raw,
        },
    }
    if codex_model and model is not None:
        backend["transport_hint"] = codex_transport_hint(model)
        backend["notes"] = [
            "Codex aliases use dspy.CodexLM and the local dspy-codex runtime selection logic.",
            "CodexLM does not honor temperature or max_tokens because the local Codex transports do not expose those controls.",
        ]

    if not model:
        backend["message"] = (
            "DSPY_MODEL is not set. Live DSPy compile/eval requires a provider-qualified model string like "
            "openai/qwen3.5:4b or a Codex alias like codex/default."
        )
        return None, backend

    if "/" not in model:
        backend["message"] = (
            "DSPY_MODEL must be provider-qualified like openai/qwen3.5:4b or use a Codex alias like codex/default."
        )
        return None, backend

    try:
        temperature = float(temperature_raw) if temperature_raw is not None else None
    except ValueError:
        backend["message"] = f"DSPY_TEMPERATURE must be a float, got {temperature_raw!r}."
        return None, backend

    try:
        max_tokens = int(max_tokens_raw) if max_tokens_raw is not None else None
    except ValueError:
        backend["message"] = f"DSPY_MAX_TOKENS must be an integer, got {max_tokens_raw!r}."
        return None, backend

    config = LMConfig(
        model=model,
        api_base=api_base,
        api_key=api_key,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    backend["configured"] = True
    backend["message"] = "DSPy LM configuration resolved."
    backend["config"] = {
        "model": config.model,
        "api_base": config.api_base,
        "api_key_configured": bool(config.api_key),
        "temperature": config.temperature,
        "max_tokens": config.max_tokens,
    }
    return config, backend


def _probe_url(api_base: str) -> str:
    parsed = urllib.parse.urlparse(api_base)
    path = parsed.path.rstrip("/")
    if not path:
        path = "/v1/models"
    elif path.endswith("/v1"):
        path = f"{path}/models"
    elif not path.endswith("/models"):
        path = f"{path}/models"
    return urllib.parse.urlunparse(parsed._replace(path=path, params="", query="", fragment=""))


def probe_backend(config: LMConfig, timeout: float = 3.0, repo_root: Path | None = None) -> dict[str, Any]:
    if is_codex_model(config.model):
        codex_client = load_codex_client()
        if codex_client is None:
            return {
                "checked": False,
                "reachable": None,
                "backend_type": "codex",
                "message": (
                    "dspy.CodexLM is unavailable in the current Python environment. "
                    "Install the local dspy-codex fork into this repo's .venv."
                ),
            }

        runtime = codex_client.inspect_codex_runtime(model=config.model)
        probe: dict[str, Any] = {
            "checked": True,
            "backend_type": "codex",
            "runtime": runtime.as_dict(),
            "requested_transport": runtime.requested_transport,
            "preferred_transport": runtime.preferred_transport,
            "available_transports": list(runtime.available_transports),
            "cli_path": runtime.cli_path,
            "mcp_sdk_available": runtime.mcp_sdk_available,
            "credential_source": runtime.credential_source,
        }
        if runtime.preferred_transport is None:
            probe["reachable"] = False
            probe["message"] = "No usable Codex transport is configured. Run the dspy-codex doctor first."
            return probe

        try:
            result = codex_client.probe_codex_runtime(
                repo_root=(repo_root or Path.cwd()).resolve(),
                model=config.model,
                timeout_seconds=max(int(timeout), 1) * 20,
            )
        except Exception as exc:  # noqa: BLE001
            probe["reachable"] = False
            probe["message"] = "Codex backend probe failed."
            probe["error"] = str(exc)
            return probe

        probe.update(
            {
                "reachable": True,
                "message": "Codex backend probe completed successfully.",
                "transport": result.transport,
                "thread_id": result.thread_id,
                "fallback_from": result.fallback_from,
                "resolved_model": result.resolved_model,
                "usage": result.usage,
                "sample_response": result.content[:120],
            }
        )
        return probe

    if not config.api_base:
        return {
            "checked": False,
            "reachable": None,
            "message": "DSPY_API_BASE is unset; backend reachability probe skipped.",
        }

    probe_url = _probe_url(config.api_base)
    request = urllib.request.Request(probe_url, headers={"User-Agent": "wizardsoftheghosts-dspy/1.0"})
    if config.api_key:
        request.add_header("Authorization", f"Bearer {config.api_key}")

    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return {
                "checked": True,
                "reachable": True,
                "probe_url": probe_url,
                "http_status": response.status,
                "message": f"Backend responded to reachability probe at {probe_url}.",
            }
    except urllib.error.HTTPError as exc:
        return {
            "checked": True,
            "reachable": True,
            "probe_url": probe_url,
            "http_status": exc.code,
            "message": f"Backend responded with HTTP {exc.code} at {probe_url}; treating endpoint as reachable.",
        }
    except Exception as exc:  # noqa: BLE001
        return {
            "checked": True,
            "reachable": False,
            "probe_url": probe_url,
            "message": f"Backend probe failed for {probe_url}.",
            "error": str(exc),
        }


def instantiate_dspy_lm(dspy: Any, config: LMConfig, repo_root: Path) -> Any:
    if is_codex_model(config.model):
        if not hasattr(dspy, "CodexLM"):
            raise RuntimeError(
                "Current Python environment does not expose dspy.CodexLM. "
                "Install the local dspy-codex fork into this repo's .venv."
            )
        return dspy.CodexLM(
            model=config.model,
            repo_root=repo_root,
        )

    kwargs: dict[str, Any] = {}
    if config.api_base:
        kwargs["api_base"] = config.api_base
    if config.api_key:
        kwargs["api_key"] = config.api_key
    if config.temperature is not None:
        kwargs["temperature"] = config.temperature
    if config.max_tokens is not None:
        kwargs["max_tokens"] = config.max_tokens
    return dspy.LM(config.model, **kwargs)


def configure_dspy_lm(dspy: Any, config: LMConfig, repo_root: Path) -> Any:
    lm = instantiate_dspy_lm(dspy, config, repo_root)
    dspy.configure(lm=lm)
    return lm


def classify_runtime_failure(exc: Exception) -> str:
    text = str(exc).lower()
    connectivity_markers = (
        "connection",
        "connect",
        "timeout",
        "timed out",
        "refused",
        "unreachable",
        "api base",
        "network",
        "temporary failure",
        "codex exec",
    )
    if any(marker in text for marker in connectivity_markers):
        return "backend_unreachable"
    return "compile_failed"


def build_router_status(
    repo_root: Path,
    *,
    status: str,
    message: str,
    dependency: dict[str, Any],
    backend: dict[str, Any],
    validation: dict[str, Any],
    extra: dict[str, Any] | None = None,
) -> dict[str, Any]:
    paths = artifact_paths(repo_root)
    payload: dict[str, Any] = {
        "status": status,
        "message": message,
        "artifact_dir": str(dspy_dir(repo_root)),
        "artifact_paths": {key: str(path) for key, path in paths.items()},
        "dataset_counts": validation["dataset_counts"],
        "validation": {
            "ok": validation["ok"],
            "missing_files": validation["missing_files"],
            "errors": validation["errors"],
        },
        "dependency": dependency,
        "backend": backend,
        "notes": validation["notes"],
    }
    if extra:
        payload.update(extra)
    return payload


def write_router_status(repo_root: Path, payload: dict[str, Any]) -> None:
    write_json(artifact_paths(repo_root)["dspy_router_status"], payload)


def normalize_splits(requested: list[str] | None) -> list[str]:
    ordered = requested or ["eval"]
    seen: set[str] = set()
    result: list[str] = []
    for split in ordered:
        if split not in EVAL_SPLIT_FILES:
            raise ValueError(f"Unsupported split: {split}")
        if split not in seen:
            result.append(split)
            seen.add(split)
    return result


def config_as_dict(config: LMConfig | None) -> dict[str, Any]:
    if config is None:
        return {}
    data = asdict(config)
    data["api_key_configured"] = bool(data.pop("api_key"))
    return data
