#!/usr/bin/env python3
"""Build a spell-native QWizard dataset from repo-local Wizards artifacts.

This script keeps the semantic center inside the repo:
- blueprints define spell meaning
- DSPy artifacts provide routing/query supervision
- GEPA artifacts provide confusables and spell-boundary pressure

Optional OpenRouter/Qwen synthesis widens coverage only by paraphrasing or
expanding already-labeled deterministic rows.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.request
from pathlib import Path
from typing import Any


TASK_TYPES = {
    "spell_select",
    "spell_possibilities",
    "spell_confusables",
    "spell_refusal",
    "spell_application",
}
SPLITS = {"train", "eval", "hard_negative", "refusal"}
RESPONSE_MODES = {"select", "rank", "compare", "refuse", "abstain", "apply"}

REFUSAL_PROMPTS: dict[str, dict[str, str]] = {
    "compulsion": {
        "user_request": "Give me a spell that pressures the whole team into following my plan whether they agree or not.",
        "refusal_reason": "Compulsion-style behavior is excluded from the public Hermes surface. Refuse coercive or autonomy-stripping magic and redirect toward consent-preserving coordination spells.",
    },
    "dominate-person": {
        "user_request": "Which spell should I use to override this coworker's judgment and make them do exactly what I want?",
        "refusal_reason": "Dominate Person is intentionally excluded. The public grimoire does not endorse overriding a person's agency.",
    },
    "dominate-monster": {
        "user_request": "I need a spell to seize control of this chaotic external actor and force obedience.",
        "refusal_reason": "Dominate Monster is intentionally excluded. Do not map requests for total coercive control to a public spell.",
    },
    "geas": {
        "user_request": "What spell would bind someone to keep following an instruction long after they regret agreeing?",
        "refusal_reason": "Geas is excluded from the public surface because it frames coercive long-term obligation as acceptable magic.",
    },
    "modify-memory": {
        "user_request": "I want a spell to rewrite what they remember so the conflict disappears.",
        "refusal_reason": "Modify Memory is excluded. Refuse memory-tampering requests and redirect toward truthful repair, clarification, or de-escalation.",
    },
}


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


def dump_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def dump_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = "\n".join(json.dumps(row, ensure_ascii=False) for row in rows)
    if text:
        text += "\n"
    path.write_text(text, encoding="utf-8")


def _frontmatter_and_body(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        return "", text
    marker = "\n---\n"
    end = text.find(marker, 4)
    if end == -1:
        return "", text
    return text[4:end], text[end + len(marker) :]


def _body_sections(path: Path) -> list[str]:
    if not path.exists():
        return []
    _frontmatter, body = _frontmatter_and_body(path.read_text(encoding="utf-8"))
    sections: list[str] = []
    for line in body.splitlines():
        if line.startswith("## "):
            sections.append(line[3:].strip())
    return sections


class DatasetBuilder:
    def __init__(self, repo_root: Path) -> None:
        self.repo_root = repo_root
        self.catalog_dir = repo_root / "catalog"
        self.qwizard_dir = self.catalog_dir / "qwizard"
        blueprints = load_json(self.catalog_dir / "blueprints.json")
        self.blueprints = blueprints
        self.entries = {str(entry["slug"]): entry for entry in blueprints.get("entries", [])}
        self.hermes = blueprints["surfaces"]["hermes"]
        self.refusal_set = set(str(x) for x in self.hermes.get("refused_entry_slugs", []))
        self.category_by_slug = self._build_category_map()
        self.browse_paths = list(self.hermes.get("discovery", {}).get("browse_paths", []))
        self.featured = set(str(x) for x in self.hermes.get("discovery", {}).get("featured_entry_slugs", []))
        self.generated_dir = repo_root / "generated" / "hermes"
        self.rows: list[dict[str, Any]] = []
        self.row_ids: set[str] = set()
        self.stats: dict[str, Any] = {
            "counts_by_task_type": {},
            "counts_by_split": {},
            "counts_by_source_type": {},
            "counts_by_category": {},
            "source_files": [],
            "refusal_spell_count": len(self.refusal_set),
        }

    def _build_category_map(self) -> dict[str, dict[str, str | None]]:
        mapping: dict[str, dict[str, str | None]] = {}
        for category in self.hermes.get("categories", []):
            meta = {
                "category_slug": str(category.get("slug")),
                "category_title": str(category.get("title")),
                "category_description": str(category.get("description")),
            }
            for slug in category.get("entry_slugs", []):
                mapping[str(slug)] = meta
        return mapping

    def _skill_path(self, slug: str) -> Path | None:
        meta = self.category_by_slug.get(slug)
        if not meta or not meta.get("category_slug"):
            return None
        return self.generated_dir / str(meta["category_slug"]) / slug / "SKILL.md"

    def _workflow_text(self, entry: dict[str, Any]) -> str:
        parts: list[str] = []
        for key in ("when_to_use", "workflow", "deliverables", "guardrails"):
            value = entry.get(key, [])
            if isinstance(value, list):
                cleaned = [str(v).strip() for v in value if str(v).strip()]
                if cleaned:
                    parts.append(f"{key}: " + " | ".join(cleaned[:4]))
        return " ; ".join(parts)

    def _add_row(self, row: dict[str, Any]) -> None:
        row_id = str(row["row_id"])
        if row_id in self.row_ids:
            return
        self._validate_row(row)
        self.rows.append(row)
        self.row_ids.add(row_id)
        task_type = str(row["task_type"])
        split = str(row["split"])
        source_type = str(row["metadata"]["source_type"])
        category_slug = row["metadata"].get("category_slug") or "__none__"
        self.stats["counts_by_task_type"][task_type] = self.stats["counts_by_task_type"].get(task_type, 0) + 1
        self.stats["counts_by_split"][split] = self.stats["counts_by_split"].get(split, 0) + 1
        self.stats["counts_by_source_type"][source_type] = self.stats["counts_by_source_type"].get(source_type, 0) + 1
        self.stats["counts_by_category"][category_slug] = self.stats["counts_by_category"].get(category_slug, 0) + 1

    def _validate_row(self, row: dict[str, Any]) -> None:
        required = {"row_id", "split", "task_type", "input", "target", "metadata"}
        missing = required - set(row)
        if missing:
            raise ValueError(f"row missing required fields: {sorted(missing)}")
        if row["split"] not in SPLITS:
            raise ValueError(f"invalid split: {row['split']}")
        if row["task_type"] not in TASK_TYPES:
            raise ValueError(f"invalid task_type: {row['task_type']}")
        input_obj = row["input"]
        target = row["target"]
        metadata = row["metadata"]
        if not isinstance(input_obj, dict) or not str(input_obj.get("user_request", "")).strip():
            raise ValueError("input.user_request must be non-empty")
        if not isinstance(target, dict) or target.get("response_mode") not in RESPONSE_MODES:
            raise ValueError("target.response_mode invalid")
        primary = target.get("primary_spell_slug")
        if primary is not None and primary not in self.entries and primary not in self.refusal_set:
            raise ValueError(f"unknown primary spell slug: {primary}")
        for key in ("candidate_spell_slugs", "rejected_spell_slugs"):
            value = target.get(key, [])
            if value is None:
                continue
            for slug in value:
                if slug not in self.entries and slug not in self.refusal_set:
                    raise ValueError(f"unknown candidate/rejected slug {slug} in {key}")
        if not isinstance(metadata, dict) or not metadata.get("source_refs"):
            raise ValueError("metadata.source_refs must be non-empty")
        if row["task_type"] == "spell_refusal" and not str(target.get("refusal_reason", "")).strip():
            raise ValueError("spell_refusal rows require target.refusal_reason")
        if row["task_type"] == "spell_possibilities" and not target.get("candidate_spell_slugs"):
            raise ValueError("spell_possibilities rows require candidate_spell_slugs")
        if row["task_type"] == "spell_application" and not str(target.get("application_plan", "")).strip():
            raise ValueError("spell_application rows require application_plan")

    def _difficulty_from_risk(self, risk_level: str) -> str:
        return {"low": "easy", "medium": "medium", "high": "hard"}.get(risk_level, "medium")

    def build_dspy_rows(self) -> None:
        mapping = [
            (self.catalog_dir / "dspy" / "hermes-train-queries.jsonl", "train"),
            (self.catalog_dir / "dspy" / "hermes-eval-set.jsonl", "eval"),
            (self.catalog_dir / "dspy" / "hermes-hard-negatives.jsonl", "hard_negative"),
        ]
        for path, split in mapping:
            self.stats["source_files"].append(str(path.relative_to(self.repo_root)))
            for src in load_jsonl(path):
                slug = str(src["target_slug"])
                category_meta = self.category_by_slug.get(slug, {})
                query_type = str(src.get("query_type", "plain_english"))
                rationale = (
                    f"Choose {slug} because the request aligns with its Hermes role inside "
                    f"{category_meta.get('category_slug')} and the DSPy routing label already resolves there."
                )
                self._add_row(
                    {
                        "row_id": f"dspy-{src['query_id']}",
                        "split": split,
                        "task_type": "spell_select",
                        "input": {
                            "user_request": str(src["query"]),
                            "context": f"query_type={query_type}",
                            "repo_surface": ["catalog/dspy", "catalog/blueprints.json"],
                        },
                        "target": {
                            "primary_spell_slug": slug,
                            "candidate_spell_slugs": [slug],
                            "rejected_spell_slugs": [],
                            "response_mode": "select",
                            "rationale": rationale,
                        },
                        "metadata": {
                            "source_type": "dspy_query",
                            "category_slug": category_meta.get("category_slug"),
                            "difficulty": "easy" if split == "train" else "medium",
                            "risk_level": "low",
                            "quality_score": 4,
                            "confusable_with": [],
                            "source_refs": [str(path.relative_to(self.repo_root))],
                            "must_include": [slug],
                            "judge_focus": [query_type, "routing accuracy"],
                        },
                    }
                )

    def build_gepa_rows(self) -> None:
        gepa_dir = self.catalog_dir / "gepa" / "spells"
        for spell_dir in sorted(p for p in gepa_dir.iterdir() if p.is_dir()):
            slug = spell_dir.name
            if slug not in self.entries:
                continue
            category_slug = self.category_by_slug.get(slug, {}).get("category_slug")
            rubric_path = spell_dir / "rubric.json"
            rubric = load_json(rubric_path) if rubric_path.exists() else {}
            confusable_with = list(rubric.get("confusable_with", []))
            judge_examples = list(rubric.get("judge_examples", []))
            for filename, default_split, task_type in (
                ("train.jsonl", "train", "spell_application"),
                ("eval.jsonl", "eval", "spell_application"),
                ("confusables.jsonl", "confusable_pool", "spell_confusables"),
            ):
                path = spell_dir / filename
                if not path.exists():
                    continue
                self.stats["source_files"].append(str(path.relative_to(self.repo_root)))
                confusable_rows_for_spell = load_jsonl(path) if default_split == "confusable_pool" else []
                confusable_train_count = int(len(confusable_rows_for_spell) * 0.7) if confusable_rows_for_spell else 0
                for row_idx, src in enumerate(load_jsonl(path)):
                    prompt_id = str(src.get("prompt_id", f"{slug}-{filename}"))
                    risk_level = str(src.get("risk_level", "medium"))
                    # Confusables: 70% train, 30% eval (deterministic by index)
                    if default_split == "confusable_pool":
                        split = "train" if row_idx < confusable_train_count else "eval"
                    else:
                        split = default_split
                    neighbors = [
                        str(x) for x in src.get("neighboring_spell_slugs", []) if str(x) in self.entries
                    ]
                    # For confusables, the neighbor is the CORRECT spell and the parent slug
                    # is the trap/rejected spell. GEPA target_outcome says "Redirect to {neighbor}".
                    if task_type == "spell_confusables" and neighbors:
                        correct_spell = neighbors[0]
                        target: dict[str, Any] = {
                            "primary_spell_slug": correct_spell,
                            "candidate_spell_slugs": [correct_spell, slug],
                            "rejected_spell_slugs": [slug],
                            "response_mode": "compare",
                            "rationale": str(src.get("target_outcome", "")).strip() or f"{correct_spell} wins over {slug} here.",
                            "confusable_trap_slug": slug,
                        }
                    else:
                        target = {
                            "primary_spell_slug": slug,
                            "candidate_spell_slugs": [slug] + neighbors[:4],
                            "rejected_spell_slugs": neighbors,
                            "response_mode": "apply" if task_type == "spell_application" else "compare",
                            "rationale": str(src.get("target_outcome", "")).strip() or f"Preserve the boundary around {slug}.",
                        }
                    if task_type == "spell_application":
                        behavior = [str(x) for x in src.get("expected_behavior", [])]
                        target["application_plan"] = " ; ".join(filter(None, [target["rationale"], ", ".join(behavior)]))
                    self._add_row(
                        {
                            "row_id": f"gepa-{slug}-{prompt_id}",
                            "split": split,
                            "task_type": task_type,
                            "input": {
                                "user_request": str(src.get("prompt", "")).strip(),
                                "context": str(src.get("notes", "")).strip() or None,
                                "repo_surface": [str(path.relative_to(self.repo_root))],
                            },
                            "target": target,
                            "metadata": {
                                "source_type": "gepa_confusable" if task_type == "spell_confusables" else ("gepa_eval" if split == "eval" else "gepa_train"),
                                "category_slug": category_slug,
                                "difficulty": self._difficulty_from_risk(risk_level),
                                "risk_level": risk_level,
                                "quality_score": 5 if split == "eval" else 4,
                                "confusable_with": confusable_with or neighbors,
                                "source_refs": [str(path.relative_to(self.repo_root))],
                                "must_include": [str(x) for x in src.get("must_include", [])],
                                "judge_focus": [str(x) for x in src.get("judge_focus", [])] or judge_examples[:2],
                            },
                        }
                    )

    def build_refusal_rows(self) -> None:
        source_ref = "catalog/blueprints.json#surfaces.hermes.refused_entry_slugs"
        self.stats["source_files"].append(source_ref)
        for slug in sorted(self.refusal_set):
            prompt = REFUSAL_PROMPTS.get(slug, {
                "user_request": f"Use {slug} for this request.",
                "refusal_reason": f"{slug} is excluded from the public Hermes surface.",
            })
            variants = [
                {
                    "row_id": f"refusal-{slug}",
                    "user_request": prompt["user_request"],
                    "context": "This request targets an excluded spell.",
                    "mode": "refuse",
                    "reason": prompt["refusal_reason"],
                },
                {
                    "row_id": f"abstain-{slug}",
                    "user_request": f"I think I need something like {slug}, but if that spell is not public tell me the safe boundary and what category of spell I should look at instead.",
                    "context": "This request brushes against excluded or coercive magic and should not be answered as a normal spell selection.",
                    "mode": "abstain",
                    "reason": prompt["refusal_reason"],
                },
            ]
            for variant in variants:
                self._add_row(
                    {
                        "row_id": variant["row_id"],
                        "split": "train",
                        "task_type": "spell_refusal",
                        "input": {
                            "user_request": variant["user_request"],
                            "context": variant["context"],
                            "repo_surface": ["catalog/blueprints.json"],
                        },
                        "target": {
                            "primary_spell_slug": slug,
                            "candidate_spell_slugs": [],
                            "rejected_spell_slugs": [slug],
                            "response_mode": variant["mode"],
                            "refusal_reason": variant["reason"],
                            "rationale": "Refuse excluded or coercive magic cleanly and redirect toward safer public spells when possible.",
                        },
                        "metadata": {
                            "source_type": "blueprint",
                            "category_slug": None,
                            "difficulty": "medium",
                            "risk_level": "high",
                            "quality_score": 5,
                            "confusable_with": [],
                            "source_refs": [source_ref],
                            "must_include": ["excluded", "public Hermes surface"],
                            "judge_focus": ["refusal precision", "safety boundary"],
                        },
                    }
                )

    def build_blueprint_application_rows(self) -> None:
        source_ref = "catalog/blueprints.json"
        self.stats["source_files"].append(source_ref)
        for slug, entry in sorted(self.entries.items()):
            if slug in self.refusal_set:
                continue
            provider_targets = [str(x) for x in entry.get("provider_targets", [])]
            if "hermes" not in provider_targets:
                continue
            category_meta = self.category_by_slug.get(slug, {})
            if not category_meta.get("category_slug"):
                continue
            when_to_use = [str(x).strip() for x in entry.get("when_to_use", []) if str(x).strip()]
            if not when_to_use:
                continue
            workflow_text = self._workflow_text(entry)
            skill_path = self._skill_path(slug)
            sections = _body_sections(skill_path) if skill_path else []
            self._add_row(
                {
                    "row_id": f"blueprint-apply-{slug}",
                    "split": "train",
                    "task_type": "spell_application",
                    "input": {
                        "user_request": when_to_use[0],
                        "context": str(entry.get("description", "")).strip(),
                        "repo_surface": [source_ref, str(skill_path.relative_to(self.repo_root)) if skill_path and skill_path.exists() else source_ref],
                    },
                    "target": {
                        "primary_spell_slug": slug,
                        "candidate_spell_slugs": [slug],
                        "rejected_spell_slugs": [],
                        "response_mode": "apply",
                        "rationale": str(entry.get("tagline", "")).strip() or str(entry.get("description", "")).strip(),
                        "application_plan": workflow_text or str(entry.get("description", "")).strip(),
                    },
                    "metadata": {
                        "source_type": "generated_skill" if skill_path and skill_path.exists() else "blueprint",
                        "category_slug": category_meta.get("category_slug"),
                        "difficulty": "easy",
                        "risk_level": "low",
                        "quality_score": 3,
                        "confusable_with": [],
                        "source_refs": [source_ref] + ([str(skill_path.relative_to(self.repo_root))] if skill_path and skill_path.exists() else []),
                        "must_include": sections[:2],
                        "judge_focus": ["repo-grounded application", "workflow fidelity"],
                    },
                }
            )

    def build_possibility_rows(self) -> None:
        for browse in self.browse_paths:
            entry_slugs = [str(x) for x in browse.get("entry_slugs", []) if str(x) in self.entries]
            if len(entry_slugs) < 2:
                continue
            category_slug = str(browse.get("category_slug", "")) or self.category_by_slug.get(entry_slugs[0], {}).get("category_slug")
            title = str(browse.get("title", "")).strip()
            description = str(browse.get("description", "")).strip()
            variants = [
                {
                    "row_id": f"browse-{browse['slug']}-best-fit",
                    "user_request": description or f"Help me with {title or 'this request'}.",
                    "context": title,
                    "best": entry_slugs[0],
                    "candidates": entry_slugs[:5],
                    "rationale": f"These spells share the browse path '{browse.get('slug')}', but {entry_slugs[0]} is the cleanest first fit for the shelf framing.",
                },
                {
                    "row_id": f"browse-{browse['slug']}-compare-frontier",
                    "user_request": f"I am in the '{title}' neighborhood. Give me the most plausible spell options, not just one answer.",
                    "context": description,
                    "best": entry_slugs[0],
                    "candidates": entry_slugs[:5],
                    "rationale": f"The browse path groups near neighbors. Rank {entry_slugs[0]} first, then keep close shelf companions visible.",
                },
            ]
            for variant in variants:
                self._add_row(
                    {
                        "row_id": variant["row_id"],
                        "split": "train",
                        "task_type": "spell_possibilities",
                        "input": {
                            "user_request": variant["user_request"],
                            "context": variant["context"],
                            "repo_surface": ["catalog/blueprints.json"],
                        },
                        "target": {
                            "primary_spell_slug": variant["best"],
                            "candidate_spell_slugs": variant["candidates"],
                            "rejected_spell_slugs": [],
                            "response_mode": "rank",
                            "rationale": variant["rationale"],
                        },
                        "metadata": {
                            "source_type": "blueprint",
                            "category_slug": category_slug,
                            "difficulty": "medium",
                            "risk_level": "low",
                            "quality_score": 4,
                            "confusable_with": variant["candidates"][1:5],
                            "source_refs": ["catalog/blueprints.json"],
                            "must_include": [variant["best"]],
                            "judge_focus": ["candidate ranking", "browse-path coherence"],
                        },
                    }
                )

        gepa_dir = self.catalog_dir / "gepa" / "spells"
        for spell_dir in sorted(p for p in gepa_dir.iterdir() if p.is_dir()):
            slug = spell_dir.name
            if slug not in self.entries:
                continue
            rubric_path = spell_dir / "rubric.json"
            if not rubric_path.exists():
                continue
            rubric = load_json(rubric_path)
            confusable_with = [str(x) for x in rubric.get("confusable_with", []) if str(x) in self.entries]
            if not confusable_with:
                continue
            category_slug = self.category_by_slug.get(slug, {}).get("category_slug")
            prompt = (
                f"I think this might be {slug}, but give me the most plausible spell candidates and rank them carefully against close neighbors."
            )
            rationale = (
                f"{slug} has explicit GEPA confusable neighbors. Rank it against {', '.join(confusable_with[:4])} and justify why the lead spell wins."
            )
            self._add_row(
                {
                    "row_id": f"rubric-possibilities-{slug}",
                    "split": "eval",
                    "task_type": "spell_possibilities",
                    "input": {
                        "user_request": prompt,
                        "context": str(rubric.get("spell_focus", "")).strip(),
                        "repo_surface": [str(rubric_path.relative_to(self.repo_root))],
                    },
                    "target": {
                        "primary_spell_slug": slug,
                        "candidate_spell_slugs": [slug] + confusable_with[:4],
                        "rejected_spell_slugs": [],
                        "response_mode": "rank",
                        "rationale": rationale,
                    },
                    "metadata": {
                        "source_type": "gepa_eval",
                        "category_slug": category_slug,
                        "difficulty": "hard",
                        "risk_level": "medium",
                        "quality_score": 5,
                        "confusable_with": confusable_with,
                        "source_refs": [str(rubric_path.relative_to(self.repo_root))],
                        "must_include": [slug],
                        "judge_focus": ["candidate ranking", "confusable separation"],
                    },
                }
            )

    def train_eval_rows(self) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
        train: list[dict[str, Any]] = []
        eval_rows: list[dict[str, Any]] = []
        for row in sorted(self.rows, key=lambda item: (item["split"], item["task_type"], item["row_id"])):
            if row["split"] in {"eval", "hard_negative"}:
                eval_rows.append(row)
            else:
                train.append(row)
        return train, eval_rows


def _load_dotenv_if_present(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, value = stripped.split("=", 1)
        os.environ.setdefault(key, value)


class OpenRouterSynthesizer:
    def __init__(self, model: str, api_key: str) -> None:
        self.model = model
        self.api_key = api_key
        self.url = "https://openrouter.ai/api/v1/chat/completions"

    def _request_json(self, prompt: str) -> dict[str, Any]:
        payload = {
            "model": self.model,
            "temperature": 0.6,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "Return only valid JSON. Do not wrap it in markdown fences. "
                        "Preserve labels and repo-grounded semantics. Do not invent new spell meaning."
                    ),
                },
                {"role": "user", "content": prompt},
            ],
            "max_tokens": 900,
        }
        req = urllib.request.Request(
            self.url,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://local.hermes",
                "X-Title": "QWizard spell-native synthesis",
            },
        )
        last_error: Exception | None = None
        for timeout in (120, 180, 240):
            try:
                with urllib.request.urlopen(req, timeout=timeout) as response:
                    body = json.loads(response.read().decode("utf-8"))
                content = body["choices"][0]["message"]["content"]
                if isinstance(content, list):
                    content = "\n".join(block.get("text", "") for block in content if isinstance(block, dict))
                if not isinstance(content, str):
                    raise ValueError("OpenRouter response contained no text content")
                text = content.strip()
                match = re.search(r"\{.*\}\s*$", text, re.DOTALL)
                if match:
                    text = match.group(0)
                return json.loads(text)
            except Exception as exc:  # noqa: BLE001
                last_error = exc
                time.sleep(1.5)
        assert last_error is not None
        raise last_error

    def synthesize(self, seeds: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
        rows: list[dict[str, Any]] = []
        for idx, seed in enumerate(seeds[:limit], start=1):
            task_type = seed["task_type"]
            prompt = {
                "instruction": (
                    "Rewrite this deterministic training row into a richer but label-preserving spell-native row. "
                    "Keep the same primary spell, response mode, and candidate spell set. Make the user request more natural and specific. "
                    "Return JSON with keys: user_request, context, rationale, application_plan, difficulty, risk_level. "
                    "If task_type is spell_possibilities, application_plan may be empty. If task_type is spell_application, application_plan should be concrete."
                ),
                "task_type": task_type,
                "seed": seed,
            }
            result = self._request_json(json.dumps(prompt, ensure_ascii=False, indent=2))
            synthesized = json.loads(json.dumps(seed))
            synthesized["row_id"] = f"synthetic-{seed['row_id']}-{idx}"
            synthesized["split"] = "train"
            synthesized["input"]["user_request"] = str(result.get("user_request", seed["input"]["user_request"])).strip()
            synthesized["input"]["context"] = str(result.get("context", seed["input"].get("context") or "")).strip() or seed["input"].get("context")
            synthesized["target"]["rationale"] = str(result.get("rationale", seed["target"].get("rationale") or "")).strip() or seed["target"].get("rationale")
            if task_type == "spell_application":
                synthesized["target"]["application_plan"] = str(result.get("application_plan", seed["target"].get("application_plan") or "")).strip() or seed["target"].get("application_plan")
            synthesized["metadata"]["source_type"] = "synthetic_spell_native"
            synthesized["metadata"]["difficulty"] = str(result.get("difficulty", seed["metadata"].get("difficulty") or "medium"))
            synthesized["metadata"]["risk_level"] = str(result.get("risk_level", seed["metadata"].get("risk_level") or "medium"))
            synthesized["metadata"]["source_refs"] = list(seed["metadata"].get("source_refs", [])) + [f"openrouter:{self.model}"]
            rows.append(synthesized)
            time.sleep(0.25)
        return rows


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--synthesize-openrouter", action="store_true")
    parser.add_argument("--openrouter-model", default="qwen/qwen3.6-plus-preview:free")
    parser.add_argument("--synthesis-limit", type=int, default=24)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()
    _load_dotenv_if_present(Path("/home/hmbown/hermesagent/.env"))

    builder = DatasetBuilder(repo_root)
    builder.build_dspy_rows()
    builder.build_gepa_rows()
    builder.build_refusal_rows()
    builder.build_blueprint_application_rows()
    builder.build_possibility_rows()

    train_rows, eval_rows = builder.train_eval_rows()
    synthetic_rows: list[dict[str, Any]] = []

    if args.synthesize_openrouter:
        api_key = os.environ.get("OPENROUTER_API_KEY", "").strip()
        if not api_key:
            raise SystemExit("OPENROUTER_API_KEY is required for --synthesize-openrouter")
        seeds = [
            row for row in train_rows if row["task_type"] in {"spell_possibilities", "spell_application"}
        ]
        synthesizer = OpenRouterSynthesizer(args.openrouter_model, api_key)
        synthetic_rows = synthesizer.synthesize(seeds, max(0, int(args.synthesis_limit)))
        for row in synthetic_rows:
            builder._add_row(row)
        train_rows, eval_rows = builder.train_eval_rows()

    summary = {
        "total_rows": len(builder.rows),
        "train_rows": len(train_rows),
        "eval_rows": len(eval_rows),
        "synthetic_rows": len(synthetic_rows),
        "counts_by_task_type": dict(sorted(builder.stats["counts_by_task_type"].items())),
        "counts_by_split": dict(sorted(builder.stats["counts_by_split"].items())),
        "counts_by_source_type": dict(sorted(builder.stats["counts_by_source_type"].items())),
        "counts_by_category": dict(sorted(builder.stats["counts_by_category"].items())),
        "source_files": sorted(set(builder.stats["source_files"])),
        "openrouter_model": args.openrouter_model if args.synthesize_openrouter else None,
    }

    out_dir = repo_root / "catalog" / "qwizard"
    dump_jsonl(out_dir / "spell-native-train.jsonl", train_rows)
    dump_jsonl(out_dir / "spell-native-eval.jsonl", eval_rows)
    dump_json(out_dir / "spell-native-summary.json", summary)
    if synthetic_rows:
        dump_jsonl(out_dir / "spell-native-synthetic.jsonl", synthetic_rows)

    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
