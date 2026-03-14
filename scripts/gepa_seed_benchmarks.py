#!/usr/bin/env python3
"""Generate initial benchmark data for GEPA spell workspaces.

This script creates train/eval/confusable JSONL rows from spell metadata
and rubric pack requirements. It does NOT require DSPy — just stdlib + repo data.

Usage:
    python scripts/gepa_seed_benchmarks.py --slug feather-fall
    python scripts/gepa_seed_benchmarks.py --all
    python scripts/gepa_seed_benchmarks.py --all --force  # overwrite existing
"""
from __future__ import annotations

import argparse
import json
import os
import random
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(REPO_ROOT / "scripts"))
from gepa_common import (
    bootstrap_spell_workspace,
    load_blueprints,
    load_spell_entry,
    spell_paths,
)

REFUSAL_SLUGS = {"dominate-person", "dominate-monster", "modify-memory", "geas", "compulsion"}

# --- Prompt templates by scenario type ---

POSITIVE_TEMPLATES = [
    "I need to {action}. Use {spell_cmd} to help me with this.",
    "{situation}. Can you apply {spell_cmd} here?",
    "My team is dealing with {problem}. Walk me through a {spell_cmd} approach.",
    "We have {context}. Use {spell_cmd} to {goal}.",
]

GENERALIZATION_TEMPLATES = [
    "This might be a stretch, but could {spell_cmd} help with {unusual_case}?",
    "I'm not sure which spell fits, but I need to {broad_need}. Would {spell_cmd} work?",
]

BOUNDARY_TEMPLATES = [
    "{edge_case}. Is this within the scope of {spell_cmd}, or should I use something else?",
]

OUT_OF_SCOPE_TEMPLATES = [
    "Use {spell_cmd} to {wrong_task}.",
]

CONFUSABLE_TEMPLATES = [
    "{confusable_prompt} — I think {spell_cmd} is the right tool here.",
    "Should I use {spell_cmd} for {neighbor_task}?",
]


def _category_by_slug(blueprints: dict) -> dict[str, dict]:
    """Map entry slug -> Hermes category dict."""
    result = {}
    for cat in blueprints.get("surfaces", {}).get("hermes", {}).get("categories", []):
        for s in cat.get("entry_slugs", []):
            result[s] = cat
    return result


def _neighbors(slug: str, blueprints: dict, category_map: dict, n: int = 5) -> list[str]:
    """Get neighboring spell slugs from the same category."""
    cat = category_map.get(slug, {})
    entry_slugs = cat.get("entry_slugs", [])
    return [s for s in entry_slugs if s != slug][:n]


def _make_row(
    slug: str,
    idx: int,
    split: str,
    scenario_type: str,
    prompt: str,
    target_outcome: str,
    expected_behavior: list[str],
    neighbors: list[str],
    tags: list[str],
    risk_level: str = "low",
    safety_flags: list[str] | None = None,
    must_include: list[str] | None = None,
    must_not_include: list[str] | None = None,
    judge_focus: list[str] | None = None,
    notes: str = "",
) -> dict:
    return {
        "prompt_id": f"{slug}-{split}-{idx:03d}",
        "dataset_split": split,
        "scenario_type": scenario_type,
        "risk_level": risk_level,
        "prompt": prompt,
        "target_outcome": target_outcome,
        "expected_behavior": expected_behavior,
        "neighboring_spell_slugs": neighbors[:3],
        "tags": tags,
        "safety_flags": safety_flags or [],
        "must_include": must_include or [],
        "must_not_include": must_not_include or [],
        "judge_focus": judge_focus or [],
        "notes": notes,
        "metadata": {},
    }


def _extract_scenarios(entry: dict) -> dict:
    """Extract scenario material from spell entry metadata."""
    when_to_use = entry.get("when_to_use", [])
    deliverables = entry.get("deliverables", [])
    guardrails = entry.get("guardrails", [])
    workflow = entry.get("workflow", [])
    tagline = entry.get("tagline", "")
    description = entry.get("description", "")
    name = entry.get("name", entry["slug"])

    # Build concrete scenario prompts from when_to_use
    positive_prompts = []
    for wtu in when_to_use:
        positive_prompts.append(f"{wtu} Use ${entry['slug']} to handle this.")

    # If not enough when_to_use items, add from description
    if len(positive_prompts) < 4:
        positive_prompts.append(f"{tagline} Apply ${entry['slug']} here.")
        if description:
            positive_prompts.append(f"{description}")

    # Build target outcomes from deliverables
    target_outcomes = []
    if deliverables:
        target_outcomes.append(
            f"The response should provide: {'; '.join(deliverables[:3])}. "
            f"It should use the {name} spell framing with clear sections."
        )
    else:
        target_outcomes.append(
            f"The response should behave like {name}, not like a generic assistant."
        )

    # Build guardrail focus
    guardrail_keywords = []
    for g in guardrails:
        # Extract key words from guardrail text
        words = g.lower().split()
        for w in words:
            if len(w) > 5 and w not in ("should", "always", "never", "before", "without"):
                guardrail_keywords.append(w)
                break

    return {
        "positive_prompts": positive_prompts,
        "target_outcomes": target_outcomes,
        "guardrail_keywords": guardrail_keywords[:5],
        "workflow_steps": workflow[:4],
        "deliverables": deliverables[:4],
        "guardrails": guardrails[:4],
    }


def generate_train_rows(
    slug: str, entry: dict, category: dict, neighbors: list[str], scenarios: dict
) -> list[dict]:
    rows = []
    spell_cmd = f"${slug}"
    name = entry.get("name", slug)
    idx = 1

    # 4 positive-fit rows from when_to_use
    for prompt_text in scenarios["positive_prompts"][:4]:
        target = scenarios["target_outcomes"][0] if scenarios["target_outcomes"] else f"Respond as {name}."
        rows.append(_make_row(
            slug, idx, "train", "positive-fit",
            prompt=prompt_text,
            target_outcome=target,
            expected_behavior=["answer-directly"],
            neighbors=neighbors,
            tags=[f"subject_type:{category.get('slug', 'general')}", "evidence_quality:standard"],
            must_include=[slug.replace("-", " ") if "-" not in slug else slug.split("-")[0]],
            judge_focus=[f"{name} spell fit", "deliverable completeness"],
            notes=f"Positive case {idx} for {name}.",
        ))
        idx += 1

    # 2 generalization rows
    gen_prompts = [
        f"I have an unconventional situation: I need something like {spell_cmd} but applied to a {random.choice(['startup', 'legacy system', 'personal project', 'team workflow'])}. Can it work?",
        f"Would {spell_cmd} be appropriate for {random.choice(['a non-technical audience', 'a CI/CD pipeline context', 'an API design review', 'a data migration scenario'])}?",
    ]
    for gp in gen_prompts:
        rows.append(_make_row(
            slug, idx, "train", "generalization",
            prompt=gp,
            target_outcome=f"Adapt {name} to the unusual context while maintaining spell identity.",
            expected_behavior=["answer-directly"],
            neighbors=neighbors,
            tags=["subject_type:generalization", "uncertainty_level:medium"],
            notes=f"Generalization case for {name}.",
        ))
        idx += 1

    # 1 boundary row
    rows.append(_make_row(
        slug, idx, "train", "boundary",
        prompt=f"I'm not sure if {spell_cmd} is the right fit. My situation is at the boundary between {name} and something else — {random.choice(['should I use a different spell?', 'what are the tradeoffs?', 'help me decide.'])}",
        target_outcome=f"Acknowledge the boundary case, explain where {name} fits and where it doesn't, suggest alternatives if appropriate.",
        expected_behavior=["answer-directly"],
        neighbors=neighbors,
        tags=["subject_type:boundary", "uncertainty_level:high"],
        notes=f"Boundary case for {name}.",
    ))
    idx += 1

    # 1 out-of-scope row
    if neighbors:
        neighbor_name = neighbors[0]
        rows.append(_make_row(
            slug, idx, "train", "out-of-scope",
            prompt=f"Use {spell_cmd} to do something that actually sounds more like ${neighbor_name}.",
            target_outcome=f"Recognize the mismatch and redirect to ${neighbor_name} or clarify what {name} actually does.",
            expected_behavior=["redirect-to-neighbor"],
            neighbors=neighbors,
            tags=["subject_type:out-of-scope"],
            notes=f"Out-of-scope redirect for {name}.",
        ))
    else:
        rows.append(_make_row(
            slug, idx, "train", "out-of-scope",
            prompt=f"Use {spell_cmd} to completely redesign the system architecture from scratch.",
            target_outcome=f"Explain that {name} is scoped differently and suggest what would actually help.",
            expected_behavior=["redirect-to-neighbor"],
            neighbors=neighbors,
            tags=["subject_type:out-of-scope"],
            notes=f"Out-of-scope case for {name}.",
        ))

    return rows


def generate_eval_rows(
    slug: str, entry: dict, category: dict, neighbors: list[str], scenarios: dict
) -> list[dict]:
    rows = []
    spell_cmd = f"${slug}"
    name = entry.get("name", slug)
    tagline = entry.get("tagline", "")
    idx = 1

    # 3 positive-fit (held out, different from train)
    eval_prompts = [
        f"Apply {spell_cmd}: {tagline}",
        f"I need {name} for a production scenario. {random.choice(scenarios['positive_prompts'][:2]) if scenarios['positive_prompts'] else tagline}",
        f"Walk me through how {spell_cmd} would handle {random.choice(['a real-world incident', 'an unfamiliar codebase', 'a cross-team coordination challenge', 'a debugging session'])}.",
    ]
    for ep in eval_prompts[:3]:
        target = scenarios["target_outcomes"][0] if scenarios["target_outcomes"] else f"Respond as {name}."
        rows.append(_make_row(
            slug, idx, "eval", "positive-fit",
            prompt=ep,
            target_outcome=target,
            expected_behavior=["answer-directly"],
            neighbors=neighbors,
            tags=["subject_type:eval-positive", "evidence_quality:standard"],
            judge_focus=[f"{name} spell fidelity", "section completeness"],
            notes=f"Held-out positive case {idx} for {name}.",
        ))
        idx += 1

    # 1 generalization
    rows.append(_make_row(
        slug, idx, "eval", "generalization",
        prompt=f"Can {spell_cmd} be adapted for {random.choice(['a hardware debugging context', 'a policy review process', 'a content strategy audit', 'a supply chain analysis'])}?",
        target_outcome=f"Thoughtfully adapt {name} to the unusual domain while maintaining spell identity.",
        expected_behavior=["answer-directly"],
        neighbors=neighbors,
        tags=["subject_type:generalization", "uncertainty_level:medium"],
        notes=f"Held-out generalization for {name}.",
    ))
    idx += 1

    # 1 boundary
    rows.append(_make_row(
        slug, idx, "eval", "boundary",
        prompt=f"This is tricky — I need {spell_cmd} but my situation also involves {random.choice(['live system changes', 'multiple stakeholders', 'competing priorities', 'unclear ownership'])}. How far can {name} stretch?",
        target_outcome=f"Name the boundary clearly, explain what {name} handles vs what needs a different approach.",
        expected_behavior=["answer-directly"],
        neighbors=neighbors,
        tags=["subject_type:boundary", "uncertainty_level:high"],
        notes=f"Held-out boundary case for {name}.",
    ))
    idx += 1

    # 1 out-of-scope
    rows.append(_make_row(
        slug, idx, "eval", "out-of-scope",
        prompt=f"I want {spell_cmd} to {random.choice(['completely automate my workflow end to end', 'replace our entire monitoring system', 'handle all communication for my team', 'rewrite the system from scratch'])}.",
        target_outcome=f"Recognize the scope mismatch and explain what {name} actually provides.",
        expected_behavior=["redirect-to-neighbor"],
        neighbors=neighbors,
        tags=["subject_type:out-of-scope"],
        notes=f"Held-out out-of-scope for {name}.",
    ))

    return rows


def generate_confusable_rows(
    slug: str, entry: dict, category: dict, neighbors: list[str], all_entries: dict[str, dict]
) -> list[dict]:
    rows = []
    spell_cmd = f"${slug}"
    name = entry.get("name", slug)
    idx = 1

    # Generate confusable rows for up to 5 neighbors
    for neighbor_slug in neighbors[:5]:
        neighbor_entry = all_entries.get(neighbor_slug, {})
        neighbor_name = neighbor_entry.get("name", neighbor_slug)
        neighbor_tagline = neighbor_entry.get("tagline", f"what {neighbor_name} does")

        rows.append(_make_row(
            slug, idx, "confusables", "confusable",
            prompt=f"I think I need {spell_cmd}, but what I actually want is: {neighbor_tagline}",
            target_outcome=f"Recognize this is a better fit for ${neighbor_slug} ({neighbor_name}) and redirect.",
            expected_behavior=["redirect-to-neighbor"],
            neighbors=[neighbor_slug],
            tags=[f"confusable_with:{neighbor_slug}"],
            judge_focus=[f"spell boundary recognition", f"redirect to {neighbor_name}"],
            notes=f"Confusable with {neighbor_name}.",
        ))
        idx += 1

    return rows


def seed_spell(slug: str, force: bool = False) -> dict:
    """Generate and write benchmark data for a single spell."""
    repo_root = REPO_ROOT
    paths = spell_paths(repo_root, slug)

    # Check if already seeded (non-empty train.jsonl)
    if not force and paths["train"].exists() and paths["train"].stat().st_size > 10:
        return {"slug": slug, "status": "skipped", "reason": "already seeded"}

    try:
        entry, category = load_spell_entry(repo_root, slug)
    except ValueError as e:
        return {"slug": slug, "status": "error", "reason": str(e)}

    blueprints = load_blueprints(repo_root)
    category_map = _category_by_slug(blueprints)
    neighbors = _neighbors(slug, blueprints, category_map)
    all_entries = {e["slug"]: e for e in blueprints["entries"]}
    scenarios = _extract_scenarios(entry)

    # Generate rows
    random.seed(hash(slug))  # Deterministic per spell
    train_rows = generate_train_rows(slug, entry, category, neighbors, scenarios)
    eval_rows = generate_eval_rows(slug, entry, category, neighbors, scenarios)
    confusable_rows = generate_confusable_rows(slug, entry, category, neighbors, all_entries)

    # Write JSONL files
    for path, rows in [
        (paths["train"], train_rows),
        (paths["eval"], eval_rows),
        (paths["confusables"], confusable_rows),
    ]:
        lines = [json.dumps(row, ensure_ascii=False) for row in rows]
        path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")

    return {
        "slug": slug,
        "status": "seeded",
        "train_rows": len(train_rows),
        "eval_rows": len(eval_rows),
        "confusable_rows": len(confusable_rows),
    }


def main():
    parser = argparse.ArgumentParser(description="Seed GEPA benchmark data for spells")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--slug", help="Seed a single spell")
    group.add_argument("--all", action="store_true", help="Seed all non-refusal spells")
    parser.add_argument("--force", action="store_true", help="Overwrite existing data")
    args = parser.parse_args()

    if args.slug:
        result = seed_spell(args.slug, force=args.force)
        print(json.dumps(result, indent=2))
    else:
        blueprints = load_blueprints(REPO_ROOT)
        results = {"seeded": 0, "skipped": 0, "errors": 0}
        for entry in blueprints["entries"]:
            slug = entry["slug"]
            if slug in REFUSAL_SLUGS:
                continue
            result = seed_spell(slug, force=args.force)
            status = result["status"]
            results[status] = results.get(status, 0) + 1
            if status == "error":
                print(f"  ERROR {slug}: {result['reason']}", file=sys.stderr)
            elif status == "seeded":
                print(f"  Seeded {slug}: {result['train_rows']}t/{result['eval_rows']}e/{result['confusable_rows']}c")

        print(f"\nDone: {results['seeded']} seeded, {results['skipped']} skipped, {results.get('errors', results.get('error', 0))} errors")


if __name__ == "__main__":
    main()
