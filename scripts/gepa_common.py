#!/usr/bin/env python3
"""Shared helpers for spell-level GEPA optimization."""
from __future__ import annotations

import copy
import json
import os
import re
from functools import lru_cache
from pathlib import Path
from typing import Any

from dspy_common import (
    LMConfig,
    classify_runtime_failure,
    config_as_dict,
    configure_dspy_lm,
    dependency_info,
    instantiate_dspy_lm,
    probe_backend,
    resolve_lm_config,
)

try:
    from jsonschema import Draft202012Validator
except ImportError:  # pragma: no cover - surfaced by _require_jsonschema_validator()
    Draft202012Validator = None

REQUIRED_SECTIONS = [
    "Approach",
    "Workflow",
    "Deliverables",
    "Guardrails",
    "Reality Boundary",
]

BENCHMARK_CONTRACT_VERSION = 1
SCORING_CONTRACT_VERSION = 1

BENCHMARK_SCENARIOS = {
    "positive",
    "confusable",
    "boundary",
    "out_of_scope",
    "risky",
    "regression",
}

EXPECTED_OUTCOMES = {
    "comply",
    "comply_with_guardrails",
    "clarify",
    "redirect",
    "refuse",
}

RISK_FLAGS = {
    "account-access",
    "coercion",
    "credential-access",
    "deception",
    "device-control",
    "live-system",
    "privacy",
    "surveillance",
}

DETERMINISTIC_CHECK_KINDS = {
    "required_sections",
    "phrase_presence",
    "phrase_absence",
    "deliverable_presence",
}

REQUIRED_SPELL_FILES = {
    "spell": "spell.json",
    "train": "train.jsonl",
    "eval": "eval.jsonl",
    "confusables": "confusables.jsonl",
    "rubric": "rubric.json",
    "promotion_patch": "promotion_patch.json",
    "status": "optimization_status.json",
    "baseline_eval": "baseline_eval.json",
    "optimized_eval": "optimized_eval.json",
    "optimized_module": "optimized_module.json",
}

ROW_REQUIRED_FIELDS = {"prompt_id", "prompt"}

ALLOWED_PROMOTION_FIELDS = {
    "tagline",
    "description",
    "when_to_use",
    "workflow",
    "deliverables",
    "guardrails",
    "default_prompt",
    "openai",
}


def gepa_dir(repo_root: Path) -> Path:
    return repo_root / "catalog" / "gepa"


def gepa_schema_dir(repo_root: Path) -> Path:
    return gepa_dir(repo_root) / "schema"


def rubric_pack_dir(repo_root: Path) -> Path:
    return gepa_dir(repo_root) / "rubric-packs"


def spell_dir(repo_root: Path, slug: str) -> Path:
    return gepa_dir(repo_root) / "spells" / slug


def spell_paths(repo_root: Path, slug: str) -> dict[str, Path]:
    base = spell_dir(repo_root, slug)
    return {name: base / rel for name, rel in REQUIRED_SPELL_FILES.items()}


def scoring_contract_path(repo_root: Path) -> Path:
    return gepa_schema_dir(repo_root) / "scoring-contract.json"


def scoring_contract_schema_path(repo_root: Path) -> Path:
    return gepa_schema_dir(repo_root) / "scoring-contract.schema.json"


def benchmark_row_schema_path(repo_root: Path) -> Path:
    return gepa_schema_dir(repo_root) / "benchmark-row.schema.json"


def spell_rubric_schema_path(repo_root: Path) -> Path:
    return gepa_schema_dir(repo_root) / "spell-rubric.schema.json"


def rubric_pack_schema_path(repo_root: Path) -> Path:
    return gepa_schema_dir(repo_root) / "rubric-pack.schema.json"


def rubric_pack_index_path(repo_root: Path) -> Path:
    return rubric_pack_dir(repo_root) / "index.json"


def rubric_pack_index_schema_path(repo_root: Path) -> Path:
    return gepa_schema_dir(repo_root) / "rubric-pack-index.schema.json"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


@lru_cache(maxsize=None)
def _load_cached_json(path_str: str) -> Any:
    return json.loads(Path(path_str).read_text(encoding="utf-8"))


def _load_schema(path: Path) -> dict[str, Any]:
    payload = _load_cached_json(str(path))
    if not isinstance(payload, dict):
        raise ValueError(f"schema file {path} must contain a JSON object")
    return payload


def _require_jsonschema_validator() -> Any:
    if Draft202012Validator is None:
        raise RuntimeError("GEPA shared contract validation requires the jsonschema package")
    return Draft202012Validator


def _format_json_path(parts: list[Any]) -> str:
    rendered = "$"
    for part in parts:
        if isinstance(part, int):
            rendered += f"[{part}]"
        else:
            rendered += f".{part}"
    return rendered


def _validate_schema_instance(*, label: str, instance: Any, schema: dict[str, Any]) -> None:
    validator_cls = _require_jsonschema_validator()
    errors = sorted(
        validator_cls(schema).iter_errors(instance),
        key=lambda err: ([str(part) for part in err.absolute_path], err.message),
    )
    if not errors:
        return
    first = errors[0]
    raise ValueError(
        f"{label} failed schema validation at {_format_json_path(list(first.absolute_path))}: {first.message}"
    )


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not path.exists():
        return rows
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + ("\n" if rows else ""),
        encoding="utf-8",
    )


def load_blueprints(repo_root: Path) -> dict[str, Any]:
    return load_json(repo_root / "catalog" / "blueprints.json")


def load_benchmark_schema(repo_root: Path) -> dict[str, Any]:
    return load_json(benchmark_row_schema_path(repo_root))


def _normalize_scoring_contract(raw_contract: dict[str, Any]) -> dict[str, Any]:
    contract = dict(raw_contract)
    deterministic_bucket = dict(raw_contract.get("deterministic_checks", {}))
    judge_bucket = dict(raw_contract.get("judge_model", {}))
    contract["deterministic_checks"] = list(deterministic_bucket.get("criteria", []))
    contract["deterministic_bucket"] = deterministic_bucket
    contract["judge_model_criteria"] = list(judge_bucket.get("criteria", []))
    contract["judge_model_bucket"] = judge_bucket
    contract["raw_contract"] = raw_contract
    return contract


def load_scoring_contract(repo_root: Path) -> dict[str, Any]:
    raw_contract = load_json(scoring_contract_path(repo_root))
    _validate_schema_instance(
        label="scoring contract",
        instance=raw_contract,
        schema=_load_schema(scoring_contract_schema_path(repo_root)),
    )
    return _normalize_scoring_contract(raw_contract)


def _validate_rubric_pack_index(repo_root: Path, raw_index: dict[str, Any]) -> None:
    packs = raw_index.get("packs", [])
    if not isinstance(packs, list):
        raise ValueError("rubric pack index packs must be a list")

    seen_categories: set[str] = set()
    seen_paths: set[str] = set()
    seen_priorities: set[int] = set()

    for idx, pack in enumerate(packs, start=1):
        if not isinstance(pack, dict):
            raise ValueError(f"rubric pack index entry {idx} must be an object")

        category_slug = str(pack.get("category_slug", "")).strip()
        rel_path = str(pack.get("path", "")).strip()
        priority = pack.get("priority")

        if category_slug in seen_categories:
            raise ValueError(f"rubric pack index contains duplicate category_slug {category_slug!r}")
        seen_categories.add(category_slug)

        if rel_path in seen_paths:
            raise ValueError(f"rubric pack index contains duplicate path {rel_path!r}")
        seen_paths.add(rel_path)

        if isinstance(priority, int):
            if priority in seen_priorities:
                raise ValueError(f"rubric pack index contains duplicate priority {priority}")
            seen_priorities.add(priority)

        expected_name = f"{category_slug}.json"
        if rel_path != expected_name:
            raise ValueError(
                f"rubric pack index entry {category_slug!r} must point to {expected_name!r}, got {rel_path!r}"
            )

        pack_path = rubric_pack_dir(repo_root) / rel_path
        if not pack_path.exists():
            raise ValueError(f"rubric pack index entry {category_slug!r} points to missing file {rel_path!r}")


def load_rubric_pack_index(repo_root: Path) -> dict[str, Any]:
    raw_index = load_json(rubric_pack_index_path(repo_root))
    _validate_schema_instance(
        label="rubric pack index",
        instance=raw_index,
        schema=_load_schema(rubric_pack_index_schema_path(repo_root)),
    )
    _validate_rubric_pack_index(repo_root, raw_index)
    return raw_index


def _normalize_rubric_pack(raw_pack: dict[str, Any], category_slug: str) -> dict[str, Any]:
    pack = dict(raw_pack)
    response_contract = dict(pack.get("response_contract", {}))
    benchmark_defaults = dict(pack.get("benchmark_defaults", {}))
    schema_refs = dict(pack.get("schema_refs", {}))
    human_review = dict(pack.get("human_review", {}))
    pack.setdefault("pack_version", str(pack.get("schema_version", "1.0")))
    pack.setdefault("title", str(pack.get("category_title", category_slug)))
    pack.setdefault("benchmark_row_schema", schema_refs.get("benchmark_row"))
    pack.setdefault("scoring_contract", schema_refs.get("scoring_contract"))
    pack.setdefault("inherits_scoring_contract", True)
    pack.setdefault(
        "spell_rubric_template",
        {
            "rubric_pack": category_slug,
            "category_slug": category_slug,
            "spell_slug": "<spell-slug>",
            "spell_focus": "Spell-specific objective and operational boundary.",
            "confusable_with": list(pack.get("example_spell_slugs", [])[:3]),
            "judge_examples": [
                "One or two concrete examples of what excellent spell behavior looks like for this spell."
            ],
            "row_overrides": {
                "required_sections": list(response_contract.get("required_sections", REQUIRED_SECTIONS)),
                "global_must_include": [],
                "global_must_not_include": [],
                "deterministic_checks": [],
                "judge_criteria": [],
                "human_review": {},
            },
        },
    )
    pack.setdefault(
        "benchmark_expectations",
        {
            "minimum_rows": dict(benchmark_defaults.get("minimum_rows", {})),
            "required_scenario_types": list(benchmark_defaults.get("coverage", [])),
            "default_tags": list(benchmark_defaults.get("required_row_tags", [])),
            "default_safety_flags": [],
        },
    )
    pack.setdefault(
        "judge_focus_areas",
        [str(item.get("question", item.get("criterion_id", ""))) for item in pack.get("judge_criteria", []) if item],
    )
    pack.setdefault(
        "human_review_overrides",
        {
            "add_safety_flags": list(human_review.get("triggers", [])),
            "review_notes": list(human_review.get("checklist", [])),
        },
    )
    pack.setdefault("judge_model_criteria", list(pack.get("judge_criteria", [])))
    pack["raw_pack"] = raw_pack
    return pack


def load_rubric_pack(repo_root: Path, category_slug: str) -> dict[str, Any]:
    raw_pack = load_json(rubric_pack_dir(repo_root) / f"{category_slug}.json")
    _validate_schema_instance(
        label=f"rubric pack {category_slug}",
        instance=raw_pack,
        schema=_load_schema(rubric_pack_schema_path(repo_root)),
    )
    if raw_pack.get("category_slug") != category_slug:
        raise ValueError(f"rubric pack {category_slug!r} declares category_slug {raw_pack.get('category_slug')!r}")
    return _normalize_rubric_pack(raw_pack, category_slug)


def category_by_entry_slug(blueprints: dict[str, Any]) -> dict[str, dict[str, Any]]:
    mapping: dict[str, dict[str, Any]] = {}
    for category in blueprints["surfaces"]["hermes"]["categories"]:
        for slug in category["entry_slugs"]:
            mapping[str(slug)] = category
    return mapping


def load_spell_entry(repo_root: Path, slug: str) -> tuple[dict[str, Any], dict[str, Any]]:
    blueprints = load_blueprints(repo_root)
    entry = next((row for row in blueprints["entries"] if row["slug"] == slug), None)
    if entry is None:
        raise ValueError(f"Unknown spell slug: {slug}")
    if entry["kind"] != "spell":
        raise ValueError(f"{slug} is a {entry['kind']}, not a spell")
    category_map = category_by_entry_slug(blueprints)
    category = category_map.get(slug)
    if category is None:
        raise ValueError(f"{slug} is not assigned to a Hermes category")
    return entry, category


def build_spell_instruction(entry: dict[str, Any], category: dict[str, Any]) -> str:
    def _bullets(lines: list[str]) -> str:
        return "\n".join(f"- {line}" for line in lines)

    return "\n".join(
        [
            f"You are casting the {entry['name']} spell from Wizards of the Ghosts.",
            f"Category: {category['title']} ({category['slug']}).",
            f"Reality tier: {entry['reality_tier']}. Literalness: {entry['literalness']}.",
            f"Spell concept: {entry['description']}",
            "Respond to the user's request using these exact markdown headings: Approach, Workflow, Deliverables, Guardrails, Reality Boundary.",
            "The response should behave like the spell, not like a generic assistant answer.",
            "When this spell fits:",
            _bullets(list(entry.get("when_to_use", []))),
            "Expected workflow elements:",
            _bullets(list(entry.get("workflow", []))),
            "Expected deliverables:",
            _bullets(list(entry.get("deliverables", []))),
            "Guardrails that must remain visible:",
            _bullets(list(entry.get("guardrails", []))),
            "Default invocation language:",
            f"- {entry['default_prompt']}",
        ]
    )


def _merge_unique_strings(*groups: list[str]) -> list[str]:
    merged: list[str] = []
    seen: set[str] = set()
    for group in groups:
        for item in group:
            value = str(item).strip()
            if value and value not in seen:
                seen.add(value)
                merged.append(value)
    return merged


def _normalize_weighted_items(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    normalized = [dict(item) for item in items]
    total = sum(float(item.get("weight", 0.0)) for item in normalized)
    if total <= 0:
        return normalized
    for item in normalized:
        item["normalized_weight"] = float(item.get("weight", 0.0)) / total
    return normalized


def default_spell_rubric(entry: dict[str, Any], category: dict[str, Any]) -> dict[str, Any]:
    return {
        "rubric_pack": category["slug"],
        "category_slug": category["slug"],
        "spell_slug": entry["slug"],
        "spell_focus": entry["description"],
        "confusable_with": [],
        "judge_examples": [
            f"Keep {entry['name']} precise, useful, and distinct from neighboring spells.",
            "Preserve clear deliverables, visible guardrails, and an honest reality boundary.",
        ],
        "row_overrides": {
            "required_sections": list(REQUIRED_SECTIONS),
            "global_must_include": [],
            "global_must_not_include": [],
            "deterministic_checks": [],
            "judge_criteria": [],
            "human_review": {},
        },
        "notes": [
            "Inherit the category rubric pack by default and add only spell-specific overrides here.",
            "Use row_overrides.global_must_include and row_overrides.global_must_not_include before inventing a new custom check.",
            f"Default deliverables for {entry['name']}: {entry['deliverables']}",
            f"Default guardrails for {entry['name']}: {entry['guardrails']}",
        ],
    }


def default_spell_metadata(entry: dict[str, Any], category: dict[str, Any], blueprints: dict[str, Any]) -> dict[str, Any]:
    category_map = category_by_entry_slug(blueprints)
    same_category = [
        other["slug"]
        for other in blueprints["entries"]
        if other["kind"] == "spell" and other["slug"] != entry["slug"] and category_map.get(other["slug"], {}).get("slug") == category["slug"]
    ]
    return {
        "slug": entry["slug"],
        "name": entry["name"],
        "category_slug": category["slug"],
        "category_title": category["title"],
        "rubric_pack": category["slug"],
        "benchmark_contract_version": BENCHMARK_CONTRACT_VERSION,
        "scoring_contract_version": SCORING_CONTRACT_VERSION,
        "reality_tier": entry["reality_tier"],
        "literalness": entry["literalness"],
        "provider_targets": entry["provider_targets"],
        "tagline": entry["tagline"],
        "suggested_confusables": same_category[:5],
        "baseline_instruction": build_spell_instruction(entry, category),
    }


def bootstrap_spell_workspace(repo_root: Path, slug: str, force: bool = False) -> dict[str, str]:
    blueprints = load_blueprints(repo_root)
    entry, category = load_spell_entry(repo_root, slug)
    paths = spell_paths(repo_root, slug)
    paths["spell"].parent.mkdir(parents=True, exist_ok=True)

    created: dict[str, str] = {}

    def _write_if_missing(path: Path, content: str, key: str) -> None:
        if force or not path.exists():
            path.write_text(content, encoding="utf-8")
            created[key] = str(path)

    _write_if_missing(
        paths["spell"],
        json.dumps(default_spell_metadata(entry, category, blueprints), ensure_ascii=False, indent=2) + "\n",
        "spell",
    )
    _write_if_missing(paths["train"], "", "train")
    _write_if_missing(paths["eval"], "", "eval")
    _write_if_missing(paths["confusables"], "", "confusables")
    _write_if_missing(
        paths["rubric"],
        json.dumps(default_spell_rubric(entry, category), ensure_ascii=False, indent=2) + "\n",
        "rubric",
    )
    _write_if_missing(
        paths["promotion_patch"],
        json.dumps(
            {
                "slug": slug,
                "reason": "",
                "updated_fields": {},
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        "promotion_patch",
    )

    for empty_key in ("status", "baseline_eval", "optimized_eval", "optimized_module"):
        _write_if_missing(paths[empty_key], "{}\n", empty_key)

    return created


def _validate_string_list(row: dict[str, Any], field: str) -> None:
    if field not in row:
        return
    value = row[field]
    if not isinstance(value, list) or any(not isinstance(item, str) or not item.strip() for item in value):
        raise ValueError(f"{field} must be a list of non-empty strings when present")


def _validate_row(row: dict[str, Any], dataset_key: str | None = None) -> None:
    missing = ROW_REQUIRED_FIELDS - set(row.keys())
    if missing:
        raise ValueError(f"row missing required fields: {sorted(missing)}")
    if not str(row["prompt_id"]).strip():
        raise ValueError("prompt_id must be non-empty")
    if not str(row["prompt"]).strip():
        raise ValueError("prompt must be non-empty")

    scenario_type = row.get("scenario_type")
    if scenario_type is not None and scenario_type not in {
        "positive-fit",
        "generalization",
        "confusable",
        "boundary",
        "refusal",
        "risky",
        "out-of-scope",
    }:
        raise ValueError(f"invalid scenario_type: {scenario_type!r}")

    risk_level = row.get("risk_level")
    if risk_level is not None and risk_level not in {"none", "low", "medium", "high", "critical"}:
        raise ValueError(f"invalid risk_level: {risk_level!r}")

    if dataset_key == "confusables" and scenario_type not in {None, "confusable"}:
        raise ValueError("confusables rows must use scenario_type 'confusable' when present")

    if "dataset_split" in row:
        split = row["dataset_split"]
        if split not in {"train", "eval", "confusables"}:
            raise ValueError(f"invalid dataset_split: {split!r}")
        if dataset_key is not None and split != dataset_key:
            raise ValueError(f"dataset_split {split!r} does not match {dataset_key!r}")

    if "expected_behavior" in row:
        expected_behavior = row["expected_behavior"]
        if not isinstance(expected_behavior, list) or any(item not in {
            "answer-directly",
            "clarify-first",
            "refuse",
            "redirect-to-neighbor",
            "offer-safe-alternative",
            "act-on-live-system",
        } for item in expected_behavior):
            raise ValueError("expected_behavior must be a list of allowed behavior labels when present")

    for field in (
        "neighboring_spell_slugs",
        "tags",
        "safety_flags",
        "required_sections",
        "must_include",
        "must_not_include",
        "judge_focus",
    ):
        _validate_string_list(row, field)

    for field in ("target_outcome", "human_review_hint", "notes"):
        if field in row and (not isinstance(row[field], str) or (field != "notes" and not row[field].strip())):
            raise ValueError(f"{field} must be a non-empty string when present")

    if "metadata" in row and not isinstance(row["metadata"], dict):
        raise ValueError("metadata must be an object when present")


def _validate_pack_check(check: dict[str, Any]) -> None:
    if not isinstance(check.get("check_id"), str) or not check["check_id"].strip():
        raise ValueError("deterministic check must include check_id")
    if check.get("kind") not in DETERMINISTIC_CHECK_KINDS:
        raise ValueError(f"unsupported deterministic check kind: {check.get('kind')!r}")
    if float(check.get("weight", 0.0)) <= 0:
        raise ValueError("deterministic check weight must be positive")
    phrases_any = check.get("phrases_any")
    phrases_all = check.get("phrases_all")
    has_valid_phrases_any = isinstance(phrases_any, list) and bool(phrases_any) and all(
        isinstance(item, str) and item.strip() for item in phrases_any
    )
    has_valid_phrases_all = isinstance(phrases_all, list) and bool(phrases_all) and all(
        isinstance(item, str) and item.strip() for item in phrases_all
    )
    if check["kind"] in {"phrase_presence", "deliverable_presence"} and not (has_valid_phrases_any or has_valid_phrases_all):
        raise ValueError("presence-based deterministic checks require phrases_any or phrases_all")
    if check["kind"] == "phrase_absence" and not has_valid_phrases_any:
        raise ValueError("phrase_absence checks require phrases_any")


def _validate_pack_criterion(criterion: dict[str, Any]) -> None:
    if not isinstance(criterion.get("criterion_id"), str) or not criterion["criterion_id"].strip():
        raise ValueError("judge criterion must include criterion_id")
    if not isinstance(criterion.get("question"), str) or not criterion["question"].strip():
        raise ValueError("judge criterion must include question")
    if float(criterion.get("weight", 0.0)) <= 0:
        raise ValueError("judge criterion weight must be positive")


def _validate_spell_rubric_definition(rubric: dict[str, Any], slug: str) -> None:
    if not isinstance(rubric.get("rubric_pack"), str) or not rubric["rubric_pack"].strip():
        raise ValueError("rubric.json must include rubric_pack")
    if rubric.get("spell_slug") != slug:
        raise ValueError("rubric.json spell_slug does not match requested spell")
    if not isinstance(rubric.get("spell_focus"), str) or not rubric["spell_focus"].strip():
        raise ValueError("rubric.json must include spell_focus")
    if not isinstance(rubric.get("confusable_with"), list):
        raise ValueError("rubric.json confusable_with must be a list")
    if not isinstance(rubric.get("judge_examples"), list):
        raise ValueError("rubric.json judge_examples must be a list")
    if not isinstance(rubric.get("row_overrides"), dict):
        raise ValueError("rubric.json row_overrides must be an object")


def _spell_traits(entry: dict[str, Any], category_slug: str) -> list[str]:
    traits = [str(entry.get("literalness", "")), str(entry.get("reality_tier", ""))]
    if category_slug == "influence-and-behavior":
        traits.append("influence-heavy")
    return [trait for trait in traits if trait]


def resolve_spell_rubric(repo_root: Path, slug: str) -> dict[str, Any]:
    entry, category = load_spell_entry(repo_root, slug)
    paths = spell_paths(repo_root, slug)
    spell_meta = load_json(paths["spell"]) if paths["spell"].exists() else {}
    spell_rubric = load_json(paths["rubric"]) if paths["rubric"].exists() else default_spell_rubric(entry, category)
    _validate_spell_rubric_definition(spell_rubric, slug)
    scoring_contract = load_scoring_contract(repo_root)
    pack_slug = str(spell_rubric.get("rubric_pack") or spell_meta.get("rubric_pack") or category["slug"])
    pack = load_rubric_pack(repo_root, pack_slug)
    if pack.get("category_slug") != category["slug"]:
        raise ValueError(f"rubric pack {pack_slug!r} does not match spell category {category['slug']!r}")

    row_overrides = dict(spell_rubric.get("row_overrides", {}))
    response_contract = dict(pack.get("response_contract", {}))
    required_sections = list(
        row_overrides.get("required_sections")
        or response_contract.get("required_sections")
        or scoring_contract.get("required_sections", REQUIRED_SECTIONS)
    )

    deterministic_checks = _normalize_weighted_items(
        [dict(check) for check in pack.get("deterministic_checks", [])]
        + [dict(check) for check in row_overrides.get("deterministic_checks", [])]
    )
    judge_criteria = _normalize_weighted_items(
        [dict(check) for check in pack.get("judge_model_criteria", [])]
        + [dict(check) for check in row_overrides.get("judge_criteria", [])]
    )
    for check in deterministic_checks:
        _validate_pack_check(check)
    for criterion in judge_criteria:
        _validate_pack_criterion(criterion)
    human_review = {
        "required": bool(pack.get("human_review", {}).get("required", False) or row_overrides.get("human_review", {}).get("required", False)),
        "required_when": dict(scoring_contract.get("human_review", {}).get("required_when", {})),
        "pack_triggers": list(pack.get("human_review", {}).get("triggers", [])),
        "checklist": _merge_unique_strings(
            [str(item.get("label", item)) for item in scoring_contract.get("human_review", {}).get("checklist", [])],
            list(pack.get("human_review", {}).get("checklist", [])),
            list(row_overrides.get("human_review", {}).get("checklist", [])),
        ),
    }

    return {
        "spell_slug": slug,
        "category_slug": category["slug"],
        "pack_slug": pack_slug,
        "spell_focus": spell_rubric["spell_focus"],
        "confusable_with": list(spell_rubric.get("confusable_with", [])),
        "judge_examples": list(spell_rubric.get("judge_examples", [])),
        "required_sections": required_sections,
        "global_must_include": _merge_unique_strings(list(row_overrides.get("global_must_include", []))),
        "global_must_not_include": _merge_unique_strings(list(row_overrides.get("global_must_not_include", []))),
        "scoring_contract": scoring_contract,
        "pack": pack,
        "deterministic_checks": deterministic_checks,
        "judge_model_criteria": judge_criteria,
        "human_review": human_review,
        "spell_traits": _spell_traits(entry, category["slug"]),
        "notes": _merge_unique_strings(list(pack.get("review_escalation", {}).get("automerge_allowed_if", [])), list(spell_rubric.get("notes", []))),
    }


def validate_spell_workspace(repo_root: Path, slug: str) -> dict[str, Any]:
    entry, category = load_spell_entry(repo_root, slug)
    paths = spell_paths(repo_root, slug)
    missing: list[str] = []
    errors: list[str] = []
    warnings: list[str] = []
    benchmark_schema: dict[str, Any] | None = None

    parsed_rows: dict[str, list[dict[str, Any]]] = {}
    for key in ("spell", "rubric", "promotion_patch", "status", "baseline_eval", "optimized_eval", "optimized_module"):
        if not paths[key].exists():
            missing.append(paths[key].name)

    if benchmark_row_schema_path(repo_root).exists():
        try:
            benchmark_schema = load_benchmark_schema(repo_root)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"shared benchmark schema: {exc}")
    else:
        errors.append("missing catalog/gepa/schema/benchmark-row.schema.json")

    if scoring_contract_path(repo_root).exists():
        try:
            load_scoring_contract(repo_root)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"shared GEPA contract: {exc}")
    else:
        errors.append("missing catalog/gepa/schema/scoring-contract.json")

    for key in ("train", "eval", "confusables"):
        if not paths[key].exists():
            missing.append(paths[key].name)
            continue
        try:
            rows = load_jsonl(paths[key])
            for index, row in enumerate(rows, start=1):
                _validate_row(row, key)
                if benchmark_schema is not None:
                    _validate_schema_instance(
                        label=f"{paths[key].name} row {index}",
                        instance=row,
                        schema=benchmark_schema,
                    )
            parsed_rows[key] = rows
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{paths[key].name}: {exc}")

    if paths["rubric"].exists():
        try:
            resolve_spell_rubric(repo_root, slug)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"rubric.json: {exc}")

    if paths["promotion_patch"].exists():
        try:
            patch = load_json(paths["promotion_patch"])
            if patch.get("slug") != slug:
                errors.append("promotion_patch.json slug does not match requested spell")
            updates = patch.get("updated_fields", {})
            if not isinstance(updates, dict):
                errors.append("promotion_patch.json updated_fields must be an object")
        except Exception as exc:  # noqa: BLE001
            errors.append(f"promotion_patch.json: {exc}")

    try:
        resolved = resolve_spell_rubric(repo_root, slug)
        minimum_rows = dict(resolved.get("pack", {}).get("benchmark_defaults", {}).get("minimum_rows", {}))
        for dataset_key in ("train", "eval", "confusables"):
            expected = int(minimum_rows.get(dataset_key, 0))
            actual = len(parsed_rows.get(dataset_key, []))
            if actual and actual < expected:
                warnings.append(f"{dataset_key}.jsonl has {actual} rows; pack recommends at least {expected}.")
    except Exception:
        pass

    return {
        "ok": not missing and not errors,
        "slug": slug,
        "spell_name": entry["name"],
        "category_slug": category["slug"],
        "missing_files": missing,
        "errors": errors,
        "warnings": warnings,
        "artifact_dir": str(paths["spell"].parent),
        "artifact_paths": {key: str(path) for key, path in paths.items()},
        "dataset_counts": {
            "train_rows": len(parsed_rows.get("train", [])),
            "eval_rows": len(parsed_rows.get("eval", [])),
            "confusable_rows": len(parsed_rows.get("confusables", [])),
        },
    }


def _lower_lines(text: str) -> list[str]:
    return [line.strip().lower() for line in text.splitlines() if line.strip()]


def normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip().lower())


def _avg(values: list[float]) -> float:
    return sum(values) / len(values) if values else 1.0


def _score_section_presence(output_text: str, required_sections: list[str]) -> tuple[float, list[str]]:
    lower_lines = _lower_lines(output_text)
    section_hits = []
    missing_sections = []
    for section in required_sections:
        present = any(line.startswith(f"{section.lower()}:") or line == section.lower() or line.startswith(f"## {section.lower()}") for line in lower_lines)
        section_hits.append(1.0 if present else 0.0)
        if not present:
            missing_sections.append(section)
    feedback = []
    if missing_sections:
        feedback.append(f"Missing required sections: {', '.join(missing_sections)}.")
    return _avg(section_hits), feedback


def _score_phrase_set(normalized_text: str, phrases: list[str], should_be_present: bool, label: str) -> tuple[float, list[str]]:
    if not phrases:
        return 1.0, []
    hits = []
    missing: list[str] = []
    forbidden: list[str] = []
    for phrase in phrases:
        found = normalize_text(str(phrase)) in normalized_text
        hits.append(1.0 if (found == should_be_present) else 0.0)
        if should_be_present and not found:
            missing.append(str(phrase))
        if not should_be_present and found:
            forbidden.append(str(phrase))
    feedback: list[str] = []
    if missing:
        feedback.append(f"Missing {label}: {', '.join(missing[:6])}.")
    if forbidden:
        feedback.append(f"Included forbidden {label}: {', '.join(forbidden[:6])}.")
    return _avg(hits), feedback


def _score_behavioral_gate(normalized_text: str, row: dict[str, Any]) -> tuple[float, list[str]]:
    behaviors = list(row.get("expected_behavior", []))
    if not behaviors:
        return 1.0, []

    heuristics = {
        "clarify-first": any(token in normalized_text for token in ["?", "clarify", "confirm", "before proceeding"]),
        "refuse": any(token in normalized_text for token in ["cannot", "can't", "won't", "refuse", "should not"]),
        "redirect-to-neighbor": any(token in normalized_text for token in ["better fit", "instead", "use ", "neighboring spell"]),
        "offer-safe-alternative": any(token in normalized_text for token in ["alternative", "safer", "instead", "fallback"]),
        "act-on-live-system": any(token in normalized_text for token in ["approval", "permission", "authorized", "confirm"]),
        "answer-directly": True,
    }
    hits = []
    missing = []
    for behavior in behaviors:
        satisfied = heuristics.get(behavior, True)
        hits.append(1.0 if satisfied else 0.0)
        if not satisfied:
            missing.append(behavior)
    feedback = []
    if missing:
        feedback.append(f"Behavioral expectations not clearly satisfied: {', '.join(missing)}.")
    return _avg(hits), feedback


def _score_pack_check(output_text: str, normalized_text: str, rubric: dict[str, Any], check: dict[str, Any]) -> tuple[float, list[str]]:
    kind = check.get("kind")
    if kind == "required_sections":
        return _score_section_presence(output_text, rubric.get("required_sections", REQUIRED_SECTIONS))

    phrases_any = [str(item) for item in check.get("phrases_any", []) if str(item).strip()]
    phrases_all = [str(item) for item in check.get("phrases_all", []) if str(item).strip()]
    if kind in {"phrase_presence", "deliverable_presence"}:
        if phrases_all:
            missing = [phrase for phrase in phrases_all if normalize_text(phrase) not in normalized_text]
            missing_label = "deliverable signal" if kind == "deliverable_presence" else "required phrase signal"
            return (1.0 if not missing else 0.0), ([] if not missing else [f"Missing {missing_label} for {check.get('check_id', 'check')}: {', '.join(missing[:4])}."])
        if not phrases_any:
            return 1.0, []
        found = any(normalize_text(phrase) in normalized_text for phrase in phrases_any)
        missing_label = "deliverable signal" if kind == "deliverable_presence" else "custom phrase signal"
        return (1.0 if found else 0.0), ([] if found else [f"Missing {missing_label} for {check.get('check_id', 'check')}."])
    if kind == "phrase_absence":
        if not phrases_any:
            return 1.0, []
        found = [phrase for phrase in phrases_any if normalize_text(phrase) in normalized_text]
        return (0.0 if found else 1.0), ([] if not found else [f"Included forbidden phrase for {check.get('check_id', 'check')}: {', '.join(found[:4])}."])

    return 1.0, []


def _legacy_score_spell_output(output_text: str, row: dict[str, Any], rubric: dict[str, Any]) -> dict[str, Any]:
    required_sections = rubric.get("required_sections", REQUIRED_SECTIONS)
    weights = rubric.get("weights", {})
    global_must_include = list(rubric.get("global_must_include", []))
    global_must_not_include = list(rubric.get("global_must_not_include", []))
    must_include = global_must_include + list(row.get("must_include", []))
    must_not_include = global_must_not_include + list(row.get("must_not_include", []))

    section_score, section_feedback = _score_section_presence(output_text, required_sections)
    include_score, include_feedback = _score_phrase_set(normalize_text(output_text), must_include, True, "required content")
    exclude_score, exclude_feedback = _score_phrase_set(normalize_text(output_text), must_not_include, False, "content")
    score = (
        section_score * float(weights.get("required_sections", 0.25))
        + include_score * float(weights.get("must_include", 0.45))
        + exclude_score * float(weights.get("must_not_include", 0.30))
    )
    feedback = section_feedback + include_feedback + exclude_feedback
    if not feedback:
        feedback.append(f"Trajectory scored {score:.3f} and satisfied the current rubric.")
    return {
        "score": max(0.0, min(1.0, score)),
        "feedback": feedback,
        "deterministic_breakdown": {
            "contract_score": round(score, 6),
            "pack_score": round(score, 6),
            "contract_criteria": [],
            "pack_checks": [],
            "fatal_failed": False,
        },
        "judge_model_criteria": [],
        "human_review": {
            "required": False,
            "reasons": [],
            "checklist": [],
        },
    }


def score_spell_output_detailed(
    *,
    output_text: str,
    row: dict[str, Any],
    rubric: dict[str, Any],
) -> dict[str, Any]:
    if not rubric.get("scoring_contract") and "weights" in rubric:
        return _legacy_score_spell_output(output_text=output_text, row=row, rubric=rubric)

    normalized = normalize_text(output_text)
    scoring_contract = rubric.get("scoring_contract", {})
    contract_criteria = list(scoring_contract.get("deterministic_checks", []))
    contract_breakdown: list[dict[str, Any]] = []
    feedback: list[str] = []

    fatal_failed = False
    contract_scores: list[float] = []
    for criterion in contract_criteria:
        criterion_id = criterion.get("id")
        criterion_feedback: list[str]
        if criterion_id == "required-sections-present":
            criterion_score, criterion_feedback = _score_section_presence(
                output_text,
                list(row.get("required_sections", [])) or list(rubric.get("required_sections", REQUIRED_SECTIONS)),
            )
        elif criterion_id == "must-include-covered":
            phrases = _merge_unique_strings(list(rubric.get("global_must_include", [])), list(row.get("must_include", [])))
            criterion_score, criterion_feedback = _score_phrase_set(normalized, phrases, True, "required content")
        elif criterion_id == "must-not-include-respected":
            phrases = _merge_unique_strings(list(rubric.get("global_must_not_include", [])), list(row.get("must_not_include", [])))
            criterion_score, criterion_feedback = _score_phrase_set(normalized, phrases, False, "content")
        elif criterion_id == "behavioral-gates-respected":
            criterion_score, criterion_feedback = _score_behavioral_gate(normalized, row)
        else:
            criterion_score, criterion_feedback = 1.0, []
        if criterion_feedback:
            feedback.extend(criterion_feedback)
        if criterion.get("fatal_if_failed") and criterion_score < 1.0:
            fatal_failed = True
        contract_scores.append(criterion_score)
        contract_breakdown.append(
            {
                "id": criterion_id,
                "score": round(criterion_score, 6),
                "feedback": criterion_feedback,
                "fatal_if_failed": bool(criterion.get("fatal_if_failed")),
            }
        )

    pack_breakdown: list[dict[str, Any]] = []
    pack_scores: list[float] = []
    pack_weights: list[float] = []
    for check in rubric.get("deterministic_checks", []):
        score, check_feedback = _score_pack_check(output_text, normalized, rubric, check)
        if check_feedback:
            feedback.extend(check_feedback)
        weight = float(check.get("normalized_weight", check.get("weight", 0.0)))
        pack_scores.append(score)
        pack_weights.append(weight)
        pack_breakdown.append(
            {
                "id": check.get("check_id"),
                "kind": check.get("kind"),
                "score": round(score, 6),
                "weight": round(weight, 6),
                "feedback": check_feedback,
            }
        )

    contract_score = _avg(contract_scores)
    if pack_scores and sum(pack_weights) > 0:
        pack_score = sum(score * weight for score, weight in zip(pack_scores, pack_weights, strict=False))
        deterministic_score = (contract_score + pack_score) / 2
    else:
        pack_score = contract_score
        deterministic_score = contract_score

    if fatal_failed:
        deterministic_score = 0.0

    human_review_required = bool(rubric.get("human_review", {}).get("required"))
    human_review_reasons = []
    review_rules = dict(rubric.get("human_review", {}).get("required_when", {}))
    safety_flags = set(str(item) for item in row.get("safety_flags", []))
    if safety_flags.intersection(review_rules.get("any_safety_flags", [])):
        human_review_required = True
        human_review_reasons.append("row safety flags trigger human review")
    if row.get("risk_level") in set(review_rules.get("any_risk_levels", [])):
        human_review_required = True
        human_review_reasons.append("row risk level triggers human review")
    if set(str(item) for item in row.get("expected_behavior", [])).intersection(review_rules.get("any_expected_behavior", [])):
        human_review_required = True
        human_review_reasons.append("expected behavior triggers human review")
    if row.get("scenario_type") in set(review_rules.get("any_scenario_types", [])):
        human_review_required = True
        human_review_reasons.append("scenario type triggers human review")
    if set(str(item) for item in rubric.get("spell_traits", [])).intersection(review_rules.get("any_spell_traits", [])):
        human_review_required = True
        human_review_reasons.append("spell traits trigger human review")
    if row.get("human_review_hint"):
        human_review_required = True
        human_review_reasons.append(str(row["human_review_hint"]))

    if not feedback:
        feedback.append(f"Trajectory scored {deterministic_score:.3f} and satisfied the deterministic rubric checks.")

    return {
        "score": max(0.0, min(1.0, deterministic_score)),
        "feedback": feedback,
        "deterministic_breakdown": {
            "contract_score": round(contract_score, 6),
            "pack_score": round(pack_score, 6),
            "contract_criteria": contract_breakdown,
            "pack_checks": pack_breakdown,
            "fatal_failed": fatal_failed,
        },
        "judge_model_criteria": list(rubric.get("judge_model_criteria", [])),
        "human_review": {
            "required": human_review_required,
            "reasons": _merge_unique_strings(human_review_reasons, list(rubric.get("human_review", {}).get("pack_triggers", []))),
            "checklist": list(rubric.get("human_review", {}).get("checklist", [])),
        },
    }


def score_spell_output(
    *,
    output_text: str,
    row: dict[str, Any],
    rubric: dict[str, Any],
) -> tuple[float, list[str]]:
    detailed = score_spell_output_detailed(output_text=output_text, row=row, rubric=rubric)
    return float(detailed["score"]), list(detailed["feedback"])


def make_examples(dspy: Any, spell_name: str, spell_brief: str, rows: list[dict[str, Any]]) -> list[Any]:
    examples = []
    for row in rows:
        example = dspy.Example(
            prompt_id=row["prompt_id"],
            user_request=row["prompt"],
            spell_name=spell_name,
            spell_brief=spell_brief,
            must_include=list(row.get("must_include", [])),
            must_not_include=list(row.get("must_not_include", [])),
            notes=str(row.get("notes", "")),
        ).with_inputs("user_request", "spell_name", "spell_brief")
        examples.append(example)
    return examples


def resolve_reflection_lm_config(args: Any, task_config: LMConfig | None) -> tuple[LMConfig | None, dict[str, Any]]:
    model = (
        getattr(args, "reflection_model", None)
        or os.environ.get("GEPA_REFLECTION_MODEL")
        or getattr(args, "dspy_model", None)
        or os.environ.get("DSPY_MODEL")
    )
    api_base = (
        getattr(args, "reflection_api_base", None)
        or os.environ.get("GEPA_REFLECTION_API_BASE")
        or getattr(args, "dspy_api_base", None)
        or os.environ.get("DSPY_API_BASE")
    )
    api_key = (
        getattr(args, "reflection_api_key", None)
        or os.environ.get("GEPA_REFLECTION_API_KEY")
        or getattr(args, "dspy_api_key", None)
        or os.environ.get("DSPY_API_KEY")
    )
    temperature = (
        getattr(args, "reflection_temperature", None)
        or os.environ.get("GEPA_REFLECTION_TEMPERATURE")
    )
    max_tokens = (
        getattr(args, "reflection_max_tokens", None)
        or os.environ.get("GEPA_REFLECTION_MAX_TOKENS")
    )

    if model is None and task_config is not None:
        return task_config, {
            "configured": True,
            "message": "Using the task LM config as the GEPA reflection LM.",
            "config": config_as_dict(task_config),
        }

    temp_args = type(
        "ReflectionArgs",
        (),
        {
            "dspy_model": model,
            "dspy_api_base": api_base,
            "dspy_api_key": api_key,
            "dspy_temperature": temperature,
            "dspy_max_tokens": max_tokens,
        },
    )()
    return resolve_lm_config(temp_args)


def instantiate_lm(dspy: Any, config: LMConfig, repo_root: Path) -> Any:
    return instantiate_dspy_lm(dspy, config, repo_root)


def build_gepa_status(
    repo_root: Path,
    *,
    slug: str,
    status: str,
    message: str,
    validation: dict[str, Any],
    dependency: dict[str, Any],
    task_backend: dict[str, Any],
    reflection_backend: dict[str, Any],
    extra: dict[str, Any] | None = None,
) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "slug": slug,
        "status": status,
        "message": message,
        "validation": validation,
        "dependency": dependency,
        "task_backend": task_backend,
        "reflection_backend": reflection_backend,
    }
    if extra:
        payload.update(extra)
    return payload


def write_gepa_status(repo_root: Path, slug: str, payload: dict[str, Any]) -> None:
    write_json(spell_paths(repo_root, slug)["status"], payload)


def apply_promotion_patch(repo_root: Path, slug: str, patch: dict[str, Any]) -> dict[str, Any]:
    if patch.get("slug") != slug:
        raise ValueError(f"promotion patch slug {patch.get('slug')!r} does not match {slug!r}")
    updates = patch.get("updated_fields")
    if not isinstance(updates, dict):
        raise ValueError("promotion patch updated_fields must be an object")

    invalid = sorted(set(updates.keys()) - ALLOWED_PROMOTION_FIELDS)
    if invalid:
        raise ValueError(f"promotion patch contains unsupported fields: {invalid}")

    blueprints = load_blueprints(repo_root)
    entry = next((row for row in blueprints["entries"] if row["slug"] == slug), None)
    if entry is None:
        raise ValueError(f"Unknown spell slug: {slug}")
    if entry["kind"] != "spell":
        raise ValueError(f"{slug} is not a spell entry")

    for field, value in updates.items():
        if field == "openai":
            if not isinstance(value, dict):
                raise ValueError("openai update must be an object")
            short_description = value.get("short_description")
            if short_description is None:
                raise ValueError("openai update must include short_description")
            if not isinstance(short_description, str) or len(short_description.strip()) < 25:
                raise ValueError("openai.short_description must be a non-empty string of at least 25 chars")
            entry.setdefault("openai", {})
            entry["openai"]["short_description"] = short_description
            continue

        if field in {"when_to_use", "workflow", "deliverables", "guardrails"}:
            if not isinstance(value, list) or not value or any(not isinstance(item, str) or not item.strip() for item in value):
                raise ValueError(f"{field} must be a non-empty list of non-empty strings")
            entry[field] = value
            continue

        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{field} must be a non-empty string")
        entry[field] = value

    (repo_root / "catalog" / "blueprints.json").write_text(
        json.dumps(blueprints, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return entry
