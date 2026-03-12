#!/usr/bin/env python3
"""Run spell-level GEPA optimization for a single spell."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from dspy_common import _relativize
from gepa_common import (
    build_gepa_status,
    build_spell_instruction,
    bootstrap_spell_workspace,
    classify_runtime_failure,
    config_as_dict,
    dependency_info,
    instantiate_lm,
    load_json,
    load_jsonl,
    load_spell_entry,
    make_examples,
    probe_backend,
    resolve_spell_rubric,
    resolve_lm_config,
    resolve_reflection_lm_config,
    score_spell_output,
    spell_paths,
    validate_spell_workspace,
    write_gepa_status,
    write_json,
)


def positive_int(value: str) -> int:
    parsed = int(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("must be a positive integer")
    return parsed


def limit_rows(rows: list[dict[str, Any]], limit: int | None) -> list[dict[str, Any]]:
    return rows if limit is None else rows[:limit]


def optimize_spell(repo_root: Path, args: argparse.Namespace) -> tuple[dict[str, Any], int]:
    slug = args.slug
    created = bootstrap_spell_workspace(repo_root, slug, force=args.force_bootstrap)
    validation = validate_spell_workspace(repo_root, slug)
    dspy, dependency = dependency_info(repo_root)
    task_config, task_backend = resolve_lm_config(args)
    reflection_config, reflection_backend = resolve_reflection_lm_config(args, task_config)

    if task_config is not None:
        task_backend = dict(task_backend)
        task_backend["config"] = config_as_dict(task_config)
        task_backend["probe"] = probe_backend(task_config, repo_root=repo_root)
    if reflection_config is not None:
        reflection_backend = dict(reflection_backend)
        reflection_backend["config"] = config_as_dict(reflection_config)
        reflection_backend["probe"] = probe_backend(reflection_config, repo_root=repo_root)

    status_extra = {"bootstrapped_files": created}

    if args.bootstrap_only:
        status = build_gepa_status(
            repo_root,
            slug=slug,
            status="bootstrapped",
            message="Bootstrapped spell GEPA workspace.",
            validation=validation,
            dependency=dependency,
            task_backend=task_backend,
            reflection_backend=reflection_backend,
            extra=status_extra,
        )
        write_gepa_status(repo_root, slug, status)
        return status, 0

    if args.validate_only:
        status = build_gepa_status(
            repo_root,
            slug=slug,
            status="ok" if validation["ok"] else "workspace_invalid",
            message="Spell GEPA workspace validation complete.",
            validation=validation,
            dependency=dependency,
            task_backend=task_backend,
            reflection_backend=reflection_backend,
            extra=status_extra,
        )
        write_gepa_status(repo_root, slug, status)
        return status, 0 if validation["ok"] else 1

    if not validation["ok"]:
        status = build_gepa_status(
            repo_root,
            slug=slug,
            status="workspace_invalid",
            message="Spell GEPA workspace is incomplete or invalid.",
            validation=validation,
            dependency=dependency,
            task_backend=task_backend,
            reflection_backend=reflection_backend,
            extra=status_extra,
        )
        write_gepa_status(repo_root, slug, status)
        return status, 1

    if not dependency.get("dspy_installed") or dspy is None:
        status = build_gepa_status(
            repo_root,
            slug=slug,
            status="missing_dependency",
            message="dspy is not installed in the current Python environment.",
            validation=validation,
            dependency=dependency,
            task_backend=task_backend,
            reflection_backend=reflection_backend,
            extra=status_extra,
        )
        write_gepa_status(repo_root, slug, status)
        return status, 1

    if task_config is None or reflection_config is None:
        status = build_gepa_status(
            repo_root,
            slug=slug,
            status="backend_not_configured",
            message="Both task and reflection LMs must be configured before GEPA optimization can run.",
            validation=validation,
            dependency=dependency,
            task_backend=task_backend,
            reflection_backend=reflection_backend,
            extra=status_extra,
        )
        write_gepa_status(repo_root, slug, status)
        return status, 1

    if task_backend.get("probe", {}).get("reachable") is False or reflection_backend.get("probe", {}).get("reachable") is False:
        status = build_gepa_status(
            repo_root,
            slug=slug,
            status="backend_unreachable",
            message="Task or reflection backend probe failed.",
            validation=validation,
            dependency=dependency,
            task_backend=task_backend,
            reflection_backend=reflection_backend,
            extra=status_extra,
        )
        write_gepa_status(repo_root, slug, status)
        return status, 1

    paths = spell_paths(repo_root, slug)
    entry, category = load_spell_entry(repo_root, slug)
    rubric = resolve_spell_rubric(repo_root, slug)
    train_rows = limit_rows(load_jsonl(paths["train"]), args.train_limit)
    eval_rows = limit_rows(load_jsonl(paths["eval"]), args.eval_limit)
    confusable_rows = limit_rows(load_jsonl(paths["confusables"]), args.confusable_limit)
    val_rows = eval_rows + confusable_rows
    if not train_rows:
        status = build_gepa_status(
            repo_root,
            slug=slug,
            status="workspace_invalid",
            message="train.jsonl must contain at least one example before optimization.",
            validation=validation,
            dependency=dependency,
            task_backend=task_backend,
            reflection_backend=reflection_backend,
            extra=status_extra,
        )
        write_gepa_status(repo_root, slug, status)
        return status, 1
    if not val_rows:
        status = build_gepa_status(
            repo_root,
            slug=slug,
            status="workspace_invalid",
            message="eval.jsonl or confusables.jsonl must contain at least one example before optimization.",
            validation=validation,
            dependency=dependency,
            task_backend=task_backend,
            reflection_backend=reflection_backend,
            extra=status_extra,
        )
        write_gepa_status(repo_root, slug, status)
        return status, 1

    baseline_instruction = build_spell_instruction(entry, category)
    trainset = make_examples(dspy, entry["name"], baseline_instruction, train_rows)
    valset = make_examples(dspy, entry["name"], baseline_instruction, val_rows)

    class RunSpell(dspy.Signature):
        user_request: str = dspy.InputField(desc="The user prompt that should trigger this spell.")
        spell_name: str = dspy.InputField(desc="The spell name being optimized.")
        spell_brief: str = dspy.InputField(desc="The current spell brief from the blueprint.")
        response: str = dspy.OutputField(
            desc="A markdown response with sections: Approach, Workflow, Deliverables, Guardrails, Reality Boundary."
        )

    SpellSignature = RunSpell.with_instructions(baseline_instruction)

    def metric(
        gold: Any,
        pred: Any,
        trace: Any = None,
        pred_name: str | None = None,
        pred_trace: Any = None,
    ) -> float | dict[str, Any]:
        response = str(getattr(pred, "response", "")).strip()
        score, feedback = score_spell_output(output_text=response, row=dict(gold), rubric=rubric)
        if pred_name is None:
            return score
        return {"score": score, "feedback": "\n".join(feedback)}

    try:
        task_lm = instantiate_lm(dspy, task_config, repo_root)
        dspy.configure(lm=task_lm)
        reflection_lm = instantiate_lm(dspy, reflection_config, repo_root)
        student = dspy.ChainOfThought(SpellSignature)
        gepa_kwargs: dict[str, Any] = {
            "metric": metric,
            "reflection_lm": reflection_lm,
            "track_stats": True,
            "seed": args.seed,
            "log_dir": str(paths["optimized_module"].parent / "logs"),
        }
        if args.max_metric_calls is not None:
            gepa_kwargs["max_metric_calls"] = args.max_metric_calls
        elif args.max_full_evals is not None:
            gepa_kwargs["max_full_evals"] = args.max_full_evals
        else:
            gepa_kwargs["auto"] = args.auto

        optimizer = dspy.GEPA(**gepa_kwargs)
        optimized = optimizer.compile(student, trainset=trainset, valset=valset)
        optimized.save(str(paths["optimized_module"]))

        predictor = optimized.predictors()[0]
        optimized_instruction = getattr(predictor.signature, "instructions", "")
        write_json(
            paths["status"],
            build_gepa_status(
                repo_root,
                slug=slug,
                status="optimized",
                message="GEPA spell optimization completed successfully.",
                validation=validation,
                dependency=dependency,
                task_backend=task_backend,
                reflection_backend=reflection_backend,
                extra={
                    **status_extra,
                    "train_rows_used": len(train_rows),
                    "val_rows_used": len(val_rows),
                    "optimized_module": _relativize(paths["optimized_module"], repo_root),
                    "optimized_instruction": optimized_instruction,
                },
            ),
        )
        return load_json(paths["status"]), 0
    except Exception as exc:  # noqa: BLE001
        status = build_gepa_status(
            repo_root,
            slug=slug,
            status=classify_runtime_failure(exc),
            message="GEPA spell optimization failed.",
            validation=validation,
            dependency=dependency,
            task_backend=task_backend,
            reflection_backend=reflection_backend,
            extra={**status_extra, "error": str(exc)},
        )
        write_gepa_status(repo_root, slug, status)
        return status, 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Run spell-level GEPA optimization for one spell")
    parser.add_argument("--repo-root", default=".", help="Path to the wizardsoftheghosts repo root")
    parser.add_argument("--slug", required=True, help="Spell slug to optimize")
    parser.add_argument("--bootstrap-only", action="store_true", help="Create the spell workspace and exit")
    parser.add_argument("--force-bootstrap", action="store_true", help="Overwrite bootstrap artifacts if they exist")
    parser.add_argument("--validate-only", action="store_true", help="Validate the spell workspace and exit")
    parser.add_argument("--dspy-model", default=None, help="Provider-qualified task model string, e.g. codex-exec/default")
    parser.add_argument("--dspy-api-base", default=None, help="Optional API base for the task model")
    parser.add_argument("--dspy-api-key", default=None, help="Optional API key for the task model")
    parser.add_argument("--dspy-temperature", default=None, help="Optional task model temperature override")
    parser.add_argument("--dspy-max-tokens", default=None, help="Optional task model max token override")
    parser.add_argument("--reflection-model", default=None, help="Optional provider-qualified reflection model string")
    parser.add_argument("--reflection-api-base", default=None, help="Optional API base for the reflection model")
    parser.add_argument("--reflection-api-key", default=None, help="Optional API key for the reflection model")
    parser.add_argument("--reflection-temperature", default=None, help="Optional reflection model temperature override")
    parser.add_argument("--reflection-max-tokens", default=None, help="Optional reflection model max token override")
    parser.add_argument("--train-limit", type=positive_int, default=None, help="Optional cap on train rows")
    parser.add_argument("--eval-limit", type=positive_int, default=None, help="Optional cap on eval rows")
    parser.add_argument("--confusable-limit", type=positive_int, default=None, help="Optional cap on confusable rows")
    parser.add_argument("--auto", choices=("light", "medium", "heavy"), default="light", help="GEPA budget preset")
    parser.add_argument("--max-full-evals", type=positive_int, default=None, help="Override GEPA full-eval budget")
    parser.add_argument("--max-metric-calls", type=positive_int, default=None, help="Override GEPA metric-call budget")
    parser.add_argument("--seed", type=int, default=0, help="GEPA random seed")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    payload, exit_code = optimize_spell(repo_root, args)
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
