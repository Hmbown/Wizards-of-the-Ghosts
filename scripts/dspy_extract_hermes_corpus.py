#!/usr/bin/env python3
"""Deterministically extract a DSPy-friendly Hermes spell corpus.

Reads the Wizards of the Ghosts source-of-truth artifacts plus generated Hermes
skills and emits normalized JSON artifacts under catalog/dspy/.

This script intentionally uses only Python stdlib so it can run in the existing
repo without introducing Python package requirements.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

SECTION_RE = re.compile(r"^##\s+(?P<title>.+?)\s*$", re.MULTILINE)
EXPLICIT_CONFIRMATION_RE = re.compile(
    r"\b(confirm|confirmation|ask first|explicit approval|approval required|consent)\b",
    re.IGNORECASE,
)
ENV_VAR_RE = re.compile(r"\b[A-Z][A-Z0-9_]{2,}\b")


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _slug_to_category(categories: list[dict[str, Any]]) -> dict[str, dict[str, str]]:
    mapping: dict[str, dict[str, str]] = {}
    for category in categories:
        category_meta = {
            "category_slug": str(category["slug"]),
            "category_title": str(category["title"]),
            "category_description": str(category["description"]),
        }
        for slug in category.get("entry_slugs", []):
            mapping[str(slug)] = category_meta
    return mapping


def _slug_to_browse_paths(discovery: dict[str, Any]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for path in discovery.get("browse_paths", []):
        path_slug = str(path.get("slug", ""))
        for entry_slug in path.get("entry_slugs", []):
            mapping.setdefault(str(entry_slug), []).append(path_slug)
    return mapping


def _frontmatter_and_body(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        return "", text
    marker = "\n---\n"
    end = text.find(marker, 4)
    if end == -1:
        return "", text
    frontmatter = text[4:end]
    body = text[end + len(marker) :]
    return frontmatter, body


def _extract_tags(frontmatter: str) -> list[str]:
    lines = frontmatter.splitlines()
    tags: list[str] = []
    in_tags = False
    tags_indent = None
    for line in lines:
        if not in_tags:
            if re.match(r"^\s*tags:\s*$", line):
                in_tags = True
                tags_indent = len(line) - len(line.lstrip())
            continue
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip())
        if indent <= (tags_indent or 0):
            break
        stripped = line.strip()
        if stripped.startswith("-"):
            tags.append(stripped[1:].strip().strip('"'))
    return tags


def _extract_sections(body: str) -> list[str]:
    return [match.group("title").strip() for match in SECTION_RE.finditer(body)]


def _extract_example_invocation(body: str) -> str | None:
    marker = "## Example Invocation"
    idx = body.find(marker)
    if idx == -1:
        return None
    snippet = body[idx + len(marker) :].strip()
    fence_start = snippet.find("```")
    if fence_start == -1:
        return None
    snippet = snippet[fence_start + 3 :]
    newline_idx = snippet.find("\n")
    if newline_idx == -1:
        return None
    snippet = snippet[newline_idx + 1 :]
    fence_end = snippet.find("```")
    if fence_end == -1:
        return None
    return snippet[:fence_end].strip() or None


def _scan_skill_file(skill_path: Path) -> dict[str, Any]:
    text = skill_path.read_text(encoding="utf-8")
    frontmatter, body = _frontmatter_and_body(text)
    sections = _extract_sections(body)
    tags = _extract_tags(frontmatter)
    env_vars = sorted(
        {
            token
            for token in ENV_VAR_RE.findall(text)
            if token.startswith(("SLACK_", "HOMEASSISTANT_", "HASS_", "OPENAI_", "ANTHROPIC_", "GOOGLE_"))
        }
    )
    return {
        "generated_skill_path": str(skill_path),
        "tags": tags,
        "sections": sections,
        "has_setup_section": "Setup" in sections,
        "requires_explicit_confirmation": bool(EXPLICIT_CONFIRMATION_RE.search(text)),
        "requires_env": env_vars,
        "example_invocation": _extract_example_invocation(body),
    }


def build_corpus(repo_root: Path) -> dict[str, Any]:
    catalog_dir = repo_root / "catalog"
    generated_hermes_dir = repo_root / "generated" / "hermes"

    canon = _load_json(catalog_dir / "canon.json")
    blueprints = _load_json(catalog_dir / "blueprints.json")

    canon_by_slug = {str(entry["slug"]): entry for entry in canon.get("entries", [])}
    hermes_surface = blueprints["surfaces"]["hermes"]
    refusal_set = {str(slug) for slug in hermes_surface.get("refused_entry_slugs", [])}
    category_by_slug = _slug_to_category(hermes_surface.get("categories", []))
    browse_paths_by_slug = _slug_to_browse_paths(hermes_surface.get("discovery", {}))
    featured_entry_slugs = {str(slug) for slug in hermes_surface.get("discovery", {}).get("featured_entry_slugs", [])}

    rows: list[dict[str, Any]] = []
    for entry in blueprints.get("entries", []):
        slug = str(entry["slug"])
        provider_targets = [str(item) for item in entry.get("provider_targets", [])]
        if "hermes" not in provider_targets or slug in refusal_set:
            continue
        category_meta = category_by_slug.get(slug, {
            "category_slug": None,
            "category_title": None,
            "category_description": None,
        })
        canonical = canon_by_slug.get(slug, {})
        skill_path = generated_hermes_dir / str(category_meta["category_slug"]) / slug / "SKILL.md"
        skill_meta = _scan_skill_file(skill_path) if skill_path.exists() else {
            "generated_skill_path": str(skill_path),
            "tags": [],
            "sections": [],
            "has_setup_section": False,
            "requires_explicit_confirmation": False,
            "requires_env": [],
            "example_invocation": None,
        }
        openai_meta = entry.get("openai", {}) if isinstance(entry.get("openai"), dict) else {}
        openclaw_meta = entry.get("openclaw", {}) if isinstance(entry.get("openclaw"), dict) else {}
        openclaw_requires = openclaw_meta.get("requires", {}) if isinstance(openclaw_meta.get("requires"), dict) else {}
        row = {
            "slug": slug,
            "name": entry.get("name"),
            "kind": entry.get("kind"),
            "canonical_id": entry.get("canonical_id"),
            "category_slug": category_meta.get("category_slug"),
            "category_title": category_meta.get("category_title"),
            "category_description": category_meta.get("category_description"),
            "reality_tier": entry.get("reality_tier"),
            "literalness": entry.get("literalness"),
            "provider_targets": provider_targets,
            "tagline": entry.get("tagline"),
            "description": entry.get("description"),
            "when_to_use": entry.get("when_to_use", []),
            "workflow": entry.get("workflow", []),
            "deliverables": entry.get("deliverables", []),
            "guardrails": entry.get("guardrails", []),
            "default_prompt": entry.get("default_prompt"),
            "openai_short_description": openai_meta.get("short_description"),
            "tags": skill_meta["tags"],
            "requires_env": openclaw_requires.get("env", []) or skill_meta["requires_env"],
            "requires_bins": openclaw_requires.get("bins", []),
            "primary_env": openclaw_requires.get("primaryEnv"),
            "has_setup_section": skill_meta["has_setup_section"],
            "requires_explicit_confirmation": skill_meta["requires_explicit_confirmation"],
            "featured_entry": slug in featured_entry_slugs,
            "browse_paths": browse_paths_by_slug.get(slug, []),
            "refused_for_hermes": False,
            "canon_source_id": canonical.get("source_id"),
            "canon_source_version": canonical.get("source_version"),
            "canon_source_url": canonical.get("source_url"),
            "generated_skill_path": skill_meta["generated_skill_path"],
            "skill_sections": skill_meta["sections"],
            "example_invocation": skill_meta["example_invocation"],
        }
        rows.append(row)

    rows.sort(key=lambda item: (str(item.get("category_slug") or ""), str(item["slug"])))
    return {
        "rows": rows,
        "categories": hermes_surface.get("categories", []),
        "browse_paths": hermes_surface.get("discovery", {}).get("browse_paths", []),
        "featured_entry_slugs": sorted(featured_entry_slugs),
        "refusal_set": sorted(refusal_set),
        "summary": {
            "total_canon_entries": len(canon.get("entries", [])),
            "total_blueprint_entries": len(blueprints.get("entries", [])),
            "total_hermes_entries": len(rows),
            "refused_for_hermes": len(refusal_set),
            "categories": {str(category['slug']): len(category.get('entry_slugs', [])) for category in hermes_surface.get('categories', [])},
        },
    }


def write_outputs(repo_root: Path, corpus: dict[str, Any]) -> None:
    out_dir = repo_root / "catalog" / "dspy"
    out_dir.mkdir(parents=True, exist_ok=True)

    rows = corpus["rows"]
    (out_dir / "spells_master.jsonl").write_text(
        "\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n",
        encoding="utf-8",
    )
    (out_dir / "categories.json").write_text(
        json.dumps(corpus["categories"], ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (out_dir / "browse_paths.json").write_text(
        json.dumps(corpus["browse_paths"], ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (out_dir / "refusal_set.json").write_text(
        json.dumps(corpus["refusal_set"], ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (out_dir / "hermes_phase1_summary.json").write_text(
        json.dumps(corpus["summary"], ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract deterministic Hermes spell corpus artifacts for DSPy")
    parser.add_argument("--repo-root", default=".", help="Path to the wizardsoftheghosts repo root")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    corpus = build_corpus(repo_root)
    write_outputs(repo_root, corpus)

    print(json.dumps(corpus["summary"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
