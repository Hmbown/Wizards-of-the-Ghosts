from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

from gepa_common import (  # noqa: E402
    apply_promotion_patch,
    bootstrap_spell_workspace,
    build_spell_instruction,
    load_rubric_pack,
    load_scoring_contract,
    load_spell_entry,
    load_json,
    score_spell_output,
    score_spell_output_detailed,
    spell_paths,
    validate_spell_workspace,
)


def make_temp_repo(tmp_path: Path) -> Path:
    repo_root = tmp_path / "repo"
    (repo_root / "catalog").mkdir(parents=True, exist_ok=True)
    shutil.copy(REPO_ROOT / "catalog" / "blueprints.json", repo_root / "catalog" / "blueprints.json")
    shutil.copy(REPO_ROOT / "catalog" / "blueprints.schema.json", repo_root / "catalog" / "blueprints.schema.json")
    source_gepa = REPO_ROOT / "catalog" / "gepa"
    if source_gepa.exists():
        target_gepa = repo_root / "catalog" / "gepa"
        target_gepa.mkdir(parents=True, exist_ok=True)
        for rel in ("schema", "rubric-packs"):
            src = source_gepa / rel
            if src.exists():
                shutil.copytree(src, target_gepa / rel)
    return repo_root


def test_bootstrap_spell_workspace_creates_required_files(tmp_path: Path) -> None:
    repo_root = make_temp_repo(tmp_path)
    created = bootstrap_spell_workspace(repo_root, "awaken")
    paths = spell_paths(repo_root, "awaken")

    assert created
    assert paths["spell"].exists()
    assert paths["train"].exists()
    assert paths["eval"].exists()
    assert paths["confusables"].exists()
    assert paths["rubric"].exists()
    assert paths["promotion_patch"].exists()
    assert paths["optimized_module"].exists()

    validation = validate_spell_workspace(repo_root, "awaken")
    assert validation["ok"] is True
    assert validation["dataset_counts"]["train_rows"] == 0


def test_score_spell_output_respects_sections_and_rubric() -> None:
    row = {
        "prompt_id": "awaken-eval-1",
        "prompt": "Wrap this old internal tool in a conversational front end.",
        "must_include": ["intent-to-action map"],
        "must_not_include": ["sentient"],
    }
    rubric = {
        "required_sections": ["Approach", "Workflow", "Deliverables", "Guardrails", "Reality Boundary"],
        "global_must_include": [],
        "global_must_not_include": [],
        "weights": {
            "required_sections": 0.25,
            "must_include": 0.45,
            "must_not_include": 0.30,
        },
    }
    output = """## Approach
Map the supported intents first.

## Workflow
Build the wrapper around an intent-to-action map.

## Deliverables
Return the wrapper plan.

## Guardrails
Do not overclaim what the substrate can do.

## Reality Boundary
Keep the wrapper honest about its limits.
"""
    score, feedback = score_spell_output(output_text=output, row=row, rubric=rubric)
    assert score == 1.0
    assert feedback


def test_score_spell_output_supports_deliverable_presence_checks() -> None:
    deliverable_check = {
        "check_id": "synthetic-deliverable-check",
        "kind": "deliverable_presence",
        "weight": 1.0,
        "phrases_any": ["monitor", "heartbeat", "threshold"],
    }
    rubric = {
        "required_sections": ["Approach", "Workflow", "Deliverables", "Guardrails", "Reality Boundary"],
        "global_must_include": [],
        "global_must_not_include": [],
        "scoring_contract": load_scoring_contract(REPO_ROOT),
        "deterministic_checks": [deliverable_check],
        "judge_model_criteria": [],
        "human_review": {
            "required": False,
            "required_when": {},
            "checklist": [],
        },
        "spell_traits": [],
    }
    row = {
        "prompt_id": "detect-magic-eval-1",
        "prompt": "Design a simple monitor.",
    }
    output = """## Approach
Use existing telemetry and keep the state summary observable.

## Workflow
Capture the current signal, add a threshold, and document the hand-off.

## Deliverables
Return a monitor plan with an alert threshold and heartbeat signal.

## Guardrails
Stay within authorized observation paths and call out false positives.

## Reality Boundary
This does not guarantee perfect visibility or real-time truth.
"""

    detailed = score_spell_output_detailed(output_text=output, row=row, rubric=rubric)

    assert detailed["deterministic_breakdown"]["pack_checks"][0]["kind"] == "deliverable_presence"
    assert detailed["deterministic_breakdown"]["pack_checks"][0]["score"] == 1.0


def test_apply_promotion_patch_updates_blueprint(tmp_path: Path) -> None:
    repo_root = make_temp_repo(tmp_path)
    bootstrap_spell_workspace(repo_root, "awaken")
    patch = {
        "slug": "awaken",
        "reason": "Improve clarity",
        "updated_fields": {
            "tagline": "Give old systems an honest conversational skin.",
            "openai": {
                "short_description": "Design honest conversational wrappers for old systems"
            },
        },
    }

    updated = apply_promotion_patch(repo_root, "awaken", patch)
    assert updated["tagline"] == "Give old systems an honest conversational skin."
    assert updated["openai"]["short_description"] == "Design honest conversational wrappers for old systems"

    blueprints = load_json(repo_root / "catalog" / "blueprints.json")
    awakened = next(entry for entry in blueprints["entries"] if entry["slug"] == "awaken")
    assert awakened["tagline"] == "Give old systems an honest conversational skin."


def test_build_spell_instruction_mentions_required_sections(tmp_path: Path) -> None:
    repo_root = make_temp_repo(tmp_path)
    entry, category = load_spell_entry(repo_root, "awaken")
    instruction = build_spell_instruction(entry, category)
    assert "Approach, Workflow, Deliverables, Guardrails, Reality Boundary" in instruction
    assert entry["description"] in instruction
