#!/usr/bin/env python3
"""Evaluate the baseline and optimized versions of a GEPA spell workspace."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from gepa_common import (
    build_spell_instruction,
    classify_runtime_failure,
    config_as_dict,
    configure_dspy_lm,
    dependency_info,
    load_json,
    load_jsonl,
    load_spell_entry,
    make_examples,
    probe_backend,
    resolve_spell_rubric,
    resolve_lm_config,
    score_spell_output_detailed,
    score_spell_output,
    spell_paths,
    validate_spell_workspace,
    write_json,
)


def positive_int(value: str) -> int:
    parsed = int(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("must be a positive integer")
    return parsed


def limit_rows(rows: list[dict[str, Any]], limit: int | None) -> list[dict[str, Any]]:
    return rows if limit is None else rows[:limit]


def evaluate_module(
    *,
    dspy: Any,
    repo_root: Path,
    module: Any,
    spell_name: str,
    spell_brief: str,
    rubric: dict[str, Any],
    rows: list[dict[str, Any]],
) -> dict[str, Any]:
    scored_rows: list[dict[str, Any]] = []
    total = len(rows)
    score_sum = 0.0

    for row in rows:
        pred = module(user_request=row["prompt"], spell_name=spell_name, spell_brief=spell_brief)
        response = str(getattr(pred, "response", "")).strip()
        detailed = score_spell_output_detailed(output_text=response, row=row, rubric=rubric)
        score = float(detailed["score"])
        score_sum += score
        scored_rows.append(
            {
                "prompt_id": row["prompt_id"],
                "prompt": row["prompt"],
                "score": round(score, 6),
                "feedback": detailed["feedback"],
                "deterministic_breakdown": detailed["deterministic_breakdown"],
                "judge_model_criteria": detailed["judge_model_criteria"],
                "human_review": detailed["human_review"],
                "response": response,
            }
        )

    return {
        "total_examples": total,
        "average_score": (score_sum / total) if total else 0.0,
        "examples": scored_rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate baseline and optimized spell behavior on the GEPA benchmark")
    parser.add_argument("--repo-root", default=".", help="Path to the wizardsoftheghosts repo root")
    parser.add_argument("--slug", required=True, help="Spell slug to evaluate")
    parser.add_argument("--dspy-model", default=None, help="Provider-qualified task model string")
    parser.add_argument("--dspy-api-base", default=None, help="Optional API base for the task model")
    parser.add_argument("--dspy-api-key", default=None, help="Optional API key for the task model")
    parser.add_argument("--dspy-temperature", default=None, help="Optional task model temperature override")
    parser.add_argument("--dspy-max-tokens", default=None, help="Optional task model max token override")
    parser.add_argument("--eval-limit", type=positive_int, default=None, help="Optional cap on eval rows")
    parser.add_argument("--confusable-limit", type=positive_int, default=None, help="Optional cap on confusable rows")
    parser.add_argument("--skip-confusables", action="store_true", help="Evaluate only eval.jsonl rows")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    slug = args.slug
    validation = validate_spell_workspace(repo_root, slug)
    dspy, dependency = dependency_info()
    config, backend = resolve_lm_config(args)

    if config is not None:
        backend = dict(backend)
        backend["config"] = config_as_dict(config)
        backend["probe"] = probe_backend(config, repo_root=repo_root)

    paths = spell_paths(repo_root, slug)
    if not validation["ok"]:
        summary = {
            "slug": slug,
            "status": "workspace_invalid",
            "message": "Spell GEPA workspace is incomplete or invalid.",
            "validation": validation,
            "dependency": dependency,
            "backend": backend,
        }
        write_json(paths["optimized_eval"], summary)
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 1

    if not dependency.get("dspy_installed") or dspy is None:
        summary = {
            "slug": slug,
            "status": "missing_dependency",
            "message": "dspy is not installed in the current Python environment.",
            "validation": validation,
            "dependency": dependency,
            "backend": backend,
        }
        write_json(paths["optimized_eval"], summary)
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 1

    if config is None or backend.get("probe", {}).get("reachable") is False:
        summary = {
            "slug": slug,
            "status": "backend_not_configured" if config is None else "backend_unreachable",
            "message": "Task model configuration is required before spell eval can run.",
            "validation": validation,
            "dependency": dependency,
            "backend": backend,
        }
        write_json(paths["optimized_eval"], summary)
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 1

    entry, category = load_spell_entry(repo_root, slug)
    rubric = resolve_spell_rubric(repo_root, slug)
    eval_rows = limit_rows(load_jsonl(paths["eval"]), args.eval_limit)
    confusable_rows = [] if args.skip_confusables else limit_rows(load_jsonl(paths["confusables"]), args.confusable_limit)
    rows = eval_rows + confusable_rows
    if not rows:
        summary = {
            "slug": slug,
            "status": "workspace_invalid",
            "message": "eval.jsonl or confusables.jsonl must contain at least one row before evaluation.",
            "validation": validation,
            "dependency": dependency,
            "backend": backend,
        }
        write_json(paths["optimized_eval"], summary)
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 1

    baseline_instruction = build_spell_instruction(entry, category)

    class RunSpell(dspy.Signature):
        user_request: str = dspy.InputField(desc="The user prompt that should trigger this spell.")
        spell_name: str = dspy.InputField(desc="The spell name being optimized.")
        spell_brief: str = dspy.InputField(desc="The current spell brief from the blueprint.")
        response: str = dspy.OutputField(
            desc="A markdown response with sections: Approach, Workflow, Deliverables, Guardrails, Reality Boundary."
        )

    SpellSignature = RunSpell.with_instructions(baseline_instruction)

    try:
        configure_dspy_lm(dspy, config, repo_root)
        baseline_module = dspy.ChainOfThought(SpellSignature)
        baseline_summary = evaluate_module(
            dspy=dspy,
            repo_root=repo_root,
            module=baseline_module,
            spell_name=entry["name"],
            spell_brief=baseline_instruction,
            rubric=rubric,
            rows=rows,
        )
        write_json(
            paths["baseline_eval"],
            {
                "slug": slug,
                "status": "evaluated",
                "variant": "baseline",
                "backend": backend,
                **baseline_summary,
            },
        )

        optimized_payload: dict[str, Any]
        if not paths["optimized_module"].exists():
            optimized_payload = {
                "slug": slug,
                "status": "optimized_module_missing",
                "message": "No optimized module artifact was found. Run gepa_optimize_spell.py first.",
                "backend": backend,
                "dependency": dependency,
                "baseline_average_score": baseline_summary["average_score"],
            }
            write_json(paths["optimized_eval"], optimized_payload)
            print(json.dumps(optimized_payload, ensure_ascii=False, indent=2))
            return 1

        optimized_module = dspy.ChainOfThought(SpellSignature)
        optimized_module.load(str(paths["optimized_module"]))
        optimized_summary = evaluate_module(
            dspy=dspy,
            repo_root=repo_root,
            module=optimized_module,
            spell_name=entry["name"],
            spell_brief=baseline_instruction,
            rubric=rubric,
            rows=rows,
        )
        optimized_payload = {
            "slug": slug,
            "status": "evaluated",
            "variant": "optimized",
            "backend": backend,
            "dependency": dependency,
            "baseline_average_score": baseline_summary["average_score"],
            "optimized_average_score": optimized_summary["average_score"],
            "delta": optimized_summary["average_score"] - baseline_summary["average_score"],
            **optimized_summary,
        }
        write_json(paths["optimized_eval"], optimized_payload)
        print(json.dumps(optimized_payload, ensure_ascii=False, indent=2))
        return 0
    except Exception as exc:  # noqa: BLE001
        summary = {
            "slug": slug,
            "status": classify_runtime_failure(exc),
            "message": "Spell GEPA evaluation failed.",
            "dependency": dependency,
            "backend": backend,
            "error": str(exc),
        }
        write_json(paths["optimized_eval"], summary)
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
