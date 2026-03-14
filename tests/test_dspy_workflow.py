from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

from dspy_common import classify_runtime_failure, resolve_lm_config, validate_workspace  # noqa: E402

BUILD_SCRIPT = REPO_ROOT / "scripts" / "dspy_build_router.py"
EVAL_SCRIPT = REPO_ROOT / "scripts" / "dspy_eval_router.py"


def make_temp_repo(tmp_path: Path) -> Path:
    repo_root = tmp_path / "repo"
    (repo_root / "catalog").mkdir(parents=True, exist_ok=True)
    shutil.copytree(REPO_ROOT / "catalog" / "dspy", repo_root / "catalog" / "dspy")
    return repo_root


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def run_script(script: Path, *args: str, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    merged_env = os.environ.copy()
    for key in list(merged_env):
        if key.startswith("DSPY_"):
            merged_env.pop(key, None)
    if env:
        merged_env.update(env)
    return subprocess.run(
        [sys.executable, str(script), *args],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        env=merged_env,
        check=False,
    )


def test_validate_workspace_counts(tmp_path: Path) -> None:
    repo_root = make_temp_repo(tmp_path)
    validation = validate_workspace(repo_root)
    assert validation["ok"] is True
    assert validation["dataset_counts"]["train_rows"] == 208
    assert validation["dataset_counts"]["eval_rows"] == 104
    assert validation["dataset_counts"]["hard_negative_rows"] == 104
    assert validation["dataset_counts"]["abstain_rows"] == 16


def test_resolve_lm_config_requires_provider_prefix(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DSPY_MODEL", "qwen3.5:4b")
    config, backend = resolve_lm_config()
    assert config is None
    assert backend["configured"] is False
    assert "provider-qualified" in backend["message"]


@pytest.mark.parametrize(
    ("model", "transport_hint", "backend_type"),
    [
        ("codex/default", "auto", "codex"),
        ("codex-exec/default", "cli", "codex"),
        ("codex-mcp/default", "mcp", "codex"),
        ("qwen/default", "cli", "qwen"),
    ],
)
def test_resolve_lm_config_accepts_local_aliases(
    monkeypatch: pytest.MonkeyPatch,
    model: str,
    transport_hint: str,
    backend_type: str,
) -> None:
    monkeypatch.setenv("DSPY_MODEL", model)
    config, backend = resolve_lm_config()
    assert config is not None
    assert config.model == model
    assert backend["configured"] is True
    assert backend["backend_type"] == backend_type
    assert backend["transport_hint"] == transport_hint


def test_classify_runtime_failure_marks_connectivity() -> None:
    status = classify_runtime_failure(RuntimeError("connection refused by upstream endpoint"))
    assert status == "backend_unreachable"


def test_validate_cli_without_backend_config(tmp_path: Path) -> None:
    repo_root = make_temp_repo(tmp_path)
    result = run_script(BUILD_SCRIPT, "--repo-root", str(repo_root), "--validate-only")
    assert result.returncode == 0, result.stderr

    status = load_json(repo_root / "catalog" / "dspy" / "dspy_router_status.json")
    assert status["status"] == "backend_not_configured"
    assert status["dataset_counts"]["eval_rows"] == 104


def test_baseline_build_and_eval(tmp_path: Path) -> None:
    repo_root = make_temp_repo(tmp_path)

    build_result = run_script(BUILD_SCRIPT, "--repo-root", str(repo_root), "--baseline-only")
    assert build_result.returncode == 0, build_result.stderr

    eval_result = run_script(EVAL_SCRIPT, "--repo-root", str(repo_root), "--baseline-only")
    assert eval_result.returncode == 0, eval_result.stderr

    summary = load_json(repo_root / "catalog" / "dspy" / "baseline_eval_summary.json")
    predictions = (repo_root / "catalog" / "dspy" / "baseline_eval_predictions.jsonl").read_text(encoding="utf-8").splitlines()
    assert summary["status"] == "evaluated"
    assert summary["total_eval_rows"] == 104
    assert summary["accuracy"] == pytest.approx(82 / 104)
    assert len(predictions) == 104


def test_baseline_eval_limit(tmp_path: Path) -> None:
    repo_root = make_temp_repo(tmp_path)

    build_result = run_script(BUILD_SCRIPT, "--repo-root", str(repo_root), "--baseline-only")
    assert build_result.returncode == 0, build_result.stderr

    eval_result = run_script(EVAL_SCRIPT, "--repo-root", str(repo_root), "--baseline-only", "--eval-limit", "7")
    assert eval_result.returncode == 0, eval_result.stderr

    summary = load_json(repo_root / "catalog" / "dspy" / "baseline_eval_summary.json")
    predictions = (repo_root / "catalog" / "dspy" / "baseline_eval_predictions.jsonl").read_text(encoding="utf-8").splitlines()
    assert summary["status"] == "evaluated"
    assert summary["total_eval_rows"] == 7
    assert summary["total_available_rows"] == 104
    assert summary["eval_limit"] == 7
    assert len(predictions) == 7


def test_compile_requires_backend_config(tmp_path: Path) -> None:
    repo_root = make_temp_repo(tmp_path)
    result = run_script(BUILD_SCRIPT, "--repo-root", str(repo_root), "--train-limit", "5")
    assert result.returncode == 1

    status = load_json(repo_root / "catalog" / "dspy" / "dspy_router_status.json")
    assert status["status"] == "backend_not_configured"
    assert status["train_limit"] == 5
    assert status["train_rows_available"] == 208
    assert status["train_rows_used"] == 5
    assert (repo_root / "catalog" / "dspy" / "baseline_router.json").exists()


def test_dspy_eval_requires_compiled_artifact(tmp_path: Path) -> None:
    repo_root = make_temp_repo(tmp_path)
    (repo_root / "catalog" / "dspy" / "dspy_category_router.json").unlink(missing_ok=True)
    result = run_script(EVAL_SCRIPT, "--repo-root", str(repo_root), "--dspy-only")
    assert result.returncode == 1

    summary = load_json(repo_root / "catalog" / "dspy" / "dspy_eval_summary.json")
    assert summary["status"] == "compile_failed"
    assert "compile step first" in summary["message"].lower()
