from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path
from typing import Any

import pytest
from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

import gepa_common  # noqa: E402


INDEXED_PACKS = [
    pack["category_slug"]
    for pack in gepa_common.load_rubric_pack_index(REPO_ROOT)["packs"]
]

PILOT_SPELLS = [
    "light",
    "detect-magic",
    "comprehend-languages",
    "identify",
    "mage-hand",
    "forcecage",
    "charm-person",
]


def require_attr(module: Any, name: str) -> Any:
    value = getattr(module, name, None)
    assert value is not None, f"gepa_common is expected to define {name}()"
    return value


def assert_valid_json_document(instance: dict[str, Any], schema: dict[str, Any]) -> None:
    errors = sorted(
        Draft202012Validator(schema).iter_errors(instance),
        key=lambda err: ([str(part) for part in err.absolute_path], err.message),
    )
    assert not errors, "; ".join(
        f"{list(error.absolute_path) or ['$']}: {error.message}" for error in errors[:3]
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


def test_shared_gepa_contract_files_load_and_distinguish_scoring_modes() -> None:
    load_benchmark_schema = require_attr(gepa_common, "load_benchmark_schema")
    load_scoring_contract = require_attr(gepa_common, "load_scoring_contract")

    benchmark_schema = load_benchmark_schema(REPO_ROOT)
    scoring_contract = load_scoring_contract(REPO_ROOT)

    assert benchmark_schema["type"] == "object"
    assert {"prompt_id", "prompt"}.issubset(set(benchmark_schema.get("required", [])))
    assert "must_include" in benchmark_schema.get("properties", {})
    assert "must_not_include" in benchmark_schema.get("properties", {})
    assert "notes" in benchmark_schema.get("properties", {})

    assert isinstance(scoring_contract.get("deterministic_checks"), list)
    assert scoring_contract["deterministic_checks"]
    assert scoring_contract["deterministic_checks"] == scoring_contract["deterministic_bucket"]["criteria"]
    assert isinstance(scoring_contract.get("judge_model_criteria"), list)
    assert scoring_contract["judge_model_criteria"]
    assert scoring_contract["judge_model_criteria"] == scoring_contract["judge_model_bucket"]["criteria"]
    assert scoring_contract["raw_contract"]["judge_model"]["criteria"] == scoring_contract["judge_model_criteria"]

    human_review = scoring_contract.get("human_review")
    assert isinstance(human_review, dict)
    assert human_review.get("required_when") or human_review.get("checklist")


def test_scoring_contract_raw_document_matches_schema() -> None:
    scoring_contract = gepa_common.load_json(REPO_ROOT / "catalog" / "gepa" / "schema" / "scoring-contract.json")
    scoring_schema = gepa_common.load_json(REPO_ROOT / "catalog" / "gepa" / "schema" / "scoring-contract.schema.json")

    assert_valid_json_document(scoring_contract, scoring_schema)


def test_rubric_pack_index_matches_schema_and_points_to_real_packs() -> None:
    raw_index = gepa_common.load_json(REPO_ROOT / "catalog" / "gepa" / "rubric-packs" / "index.json")
    index_schema = gepa_common.load_json(REPO_ROOT / "catalog" / "gepa" / "schema" / "rubric-pack-index.schema.json")

    assert_valid_json_document(raw_index, index_schema)

    index_payload = gepa_common.load_rubric_pack_index(REPO_ROOT)
    indexed_categories = [pack["category_slug"] for pack in index_payload["packs"]]
    indexed_priorities = [pack["priority"] for pack in index_payload["packs"]]

    assert indexed_categories
    assert len(indexed_categories) == len(set(indexed_categories))
    assert indexed_priorities == sorted(indexed_priorities)

    for pack in index_payload["packs"]:
        assert pack["path"] == f"{pack['category_slug']}.json"
        pack_path = REPO_ROOT / "catalog" / "gepa" / "rubric-packs" / pack["path"]
        assert pack_path.exists()
        loaded = gepa_common.load_rubric_pack(REPO_ROOT, pack["category_slug"])
        assert loaded["raw_pack"]["category_slug"] == pack["category_slug"]


@pytest.mark.parametrize("category_slug", INDEXED_PACKS)
def test_indexed_rubric_packs_validate_and_normalize(category_slug: str) -> None:
    load_rubric_pack = require_attr(gepa_common, "load_rubric_pack")
    raw_pack = gepa_common.load_json(REPO_ROOT / "catalog" / "gepa" / "rubric-packs" / f"{category_slug}.json")
    pack_schema = gepa_common.load_json(REPO_ROOT / "catalog" / "gepa" / "schema" / "rubric-pack.schema.json")

    assert_valid_json_document(raw_pack, pack_schema)

    pack = load_rubric_pack(REPO_ROOT, category_slug)

    assert pack["category_slug"] == category_slug
    assert pack["raw_pack"] == raw_pack
    assert pack["pack_version"] == raw_pack["schema_version"]
    assert pack["title"] == raw_pack["category_title"]
    assert pack["benchmark_row_schema"] == raw_pack["schema_refs"]["benchmark_row"]
    assert pack["scoring_contract"] == raw_pack["schema_refs"]["scoring_contract"]
    assert pack["inherits_scoring_contract"] is True
    assert pack["spell_rubric_template"]["rubric_pack"] == category_slug
    assert pack["spell_rubric_template"]["row_overrides"]["required_sections"] == raw_pack["response_contract"]["required_sections"]
    assert pack["benchmark_expectations"]["minimum_rows"] == raw_pack["benchmark_defaults"]["minimum_rows"]
    assert pack["judge_model_criteria"] == raw_pack["judge_criteria"]
    assert pack["human_review_overrides"]["add_safety_flags"] == raw_pack["human_review"]["triggers"]
    assert pack["human_review_overrides"]["review_notes"] == raw_pack["human_review"]["checklist"]


def test_load_rubric_pack_rejects_invalid_raw_shape(tmp_path: Path) -> None:
    repo_root = make_temp_repo(tmp_path)
    pack_path = repo_root / "catalog" / "gepa" / "rubric-packs" / "actions-access-and-automation.json"
    pack = gepa_common.load_json(pack_path)
    del pack["response_contract"]
    pack_path.write_text(json.dumps(pack, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    with pytest.raises(ValueError, match="response_contract"):
        gepa_common.load_rubric_pack(repo_root, "actions-access-and-automation")


def test_load_rubric_pack_index_rejects_duplicate_category_slug(tmp_path: Path) -> None:
    repo_root = make_temp_repo(tmp_path)
    index_path = repo_root / "catalog" / "gepa" / "rubric-packs" / "index.json"
    index_payload = gepa_common.load_json(index_path)
    index_payload["packs"][1]["category_slug"] = index_payload["packs"][0]["category_slug"]
    index_path.write_text(json.dumps(index_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    with pytest.raises(ValueError, match="duplicate category_slug"):
        gepa_common.load_rubric_pack_index(repo_root)


def test_load_rubric_pack_index_rejects_path_mismatch(tmp_path: Path) -> None:
    repo_root = make_temp_repo(tmp_path)
    index_path = repo_root / "catalog" / "gepa" / "rubric-packs" / "index.json"
    index_payload = gepa_common.load_json(index_path)
    index_payload["packs"][0]["path"] = "wrong-name.json"
    index_path.write_text(json.dumps(index_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    with pytest.raises(ValueError, match="must point to"):
        gepa_common.load_rubric_pack_index(repo_root)


def test_awaken_workspace_inherits_actions_access_and_automation_pack() -> None:
    load_rubric_pack = require_attr(gepa_common, "load_rubric_pack")

    spell = gepa_common.load_json(REPO_ROOT / "catalog" / "gepa" / "spells" / "awaken" / "spell.json")
    rubric = gepa_common.load_json(REPO_ROOT / "catalog" / "gepa" / "spells" / "awaken" / "rubric.json")
    pack_slug = rubric.get("rubric_pack", spell["category_slug"])
    pack = load_rubric_pack(REPO_ROOT, pack_slug)

    assert spell["category_slug"] == "actions-access-and-automation"
    assert pack_slug == spell["category_slug"]
    assert pack["category_slug"] == spell["category_slug"]
    assert pack["raw_pack"]["category_slug"] == spell["category_slug"]
    assert pack["spell_rubric_template"]["row_overrides"]["required_sections"]


def test_bootstrap_spell_workspace_seeds_category_rubric_pack_reference(tmp_path: Path) -> None:
    repo_root = make_temp_repo(tmp_path)
    gepa_common.bootstrap_spell_workspace(repo_root, "awaken", force=True)

    rubric = gepa_common.load_json(gepa_common.spell_paths(repo_root, "awaken")["rubric"])

    assert rubric.get("rubric_pack") == "actions-access-and-automation"
    validation = gepa_common.validate_spell_workspace(repo_root, "awaken")
    assert validation["ok"] is True


@pytest.mark.parametrize("slug", PILOT_SPELLS)
def test_pilot_workspaces_validate_against_shared_contracts(slug: str) -> None:
    validation = gepa_common.validate_spell_workspace(REPO_ROOT, slug)
    assert validation["ok"] is True
    assert validation["warnings"] == []

    resolved = gepa_common.resolve_spell_rubric(REPO_ROOT, slug)
    assert resolved["confusable_with"]
    assert resolved["judge_examples"]

    minimum_rows = resolved["pack"]["benchmark_defaults"]["minimum_rows"]
    assert validation["dataset_counts"]["train_rows"] >= int(minimum_rows["train"])
    assert validation["dataset_counts"]["eval_rows"] >= int(minimum_rows["eval"])
    assert validation["dataset_counts"]["confusable_rows"] >= int(minimum_rows["confusables"])


@pytest.mark.parametrize("slug", PILOT_SPELLS)
def test_pilot_benchmark_rows_match_shared_row_schema(slug: str) -> None:
    benchmark_schema = gepa_common.load_benchmark_schema(REPO_ROOT)

    for split in ("train", "eval", "confusables"):
        rows = gepa_common.load_jsonl(gepa_common.spell_paths(REPO_ROOT, slug)[split])
        assert rows
        for row in rows:
            assert_valid_json_document(row, benchmark_schema)
