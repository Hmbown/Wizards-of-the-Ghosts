#!/usr/bin/env python3
"""Evaluate Phase 3 Hermes routers."""
from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from dspy_common import (
    _relativize,
    artifact_paths,
    category_context,
    classify_runtime_failure,
    collect_eval_rows,
    config_as_dict,
    configure_dspy_lm,
    dependency_info,
    load_json,
    normalize_splits,
    probe_backend,
    resolve_lm_config,
    validate_workspace,
    write_json,
    write_jsonl,
)

TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9-]+")
STOPWORDS = {
    "the",
    "a",
    "an",
    "and",
    "or",
    "to",
    "of",
    "for",
    "with",
    "in",
    "on",
    "at",
    "by",
    "from",
    "this",
    "that",
    "it",
    "is",
    "are",
    "be",
    "as",
    "into",
    "when",
    "you",
    "your",
    "we",
    "they",
    "their",
    "me",
    "my",
    "our",
    "now",
    "not",
    "only",
    "than",
    "more",
    "before",
    "after",
    "across",
    "through",
}


def tokenize(text: str) -> list[str]:
    return [tok for tok in TOKEN_RE.findall(text.lower()) if tok not in STOPWORDS and len(tok) > 1]


def positive_int(value: str) -> int:
    parsed = int(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("must be a positive integer")
    return parsed


def limit_rows(rows: list[dict[str, Any]], limit: int | None) -> list[dict[str, Any]]:
    return rows if limit is None else rows[:limit]


def predict_baseline(query: str, artifact: dict[str, Any]) -> tuple[str, float]:
    idf = artifact["idf"]
    category_vectors = artifact["category_vectors"]
    counts = Counter(tokenize(query))
    total = sum(counts.values()) or 1
    query_vec = {tok: (count / total) * idf.get(tok, 1.0) for tok, count in counts.items()}
    qnorm = math.sqrt(sum(v * v for v in query_vec.values())) or 1.0
    query_vec = {tok: val / qnorm for tok, val in query_vec.items()}

    best_slug = ""
    best_score = -1.0
    for slug, vec in category_vectors.items():
        score = 0.0
        for tok, qval in query_vec.items():
            score += qval * vec.get(tok, 0.0)
        if score > best_score:
            best_slug = slug
            best_score = score
    return best_slug, best_score


def evaluate_baseline(repo_root: Path, splits: list[str], eval_limit: int | None = None) -> dict[str, Any]:
    paths = artifact_paths(repo_root)
    artifact = load_json(paths["baseline_router"])
    all_rows = collect_eval_rows(repo_root, splits)
    rows = limit_rows(all_rows, eval_limit)

    total = len(rows)
    correct = 0
    confusion: dict[str, Counter[str]] = defaultdict(Counter)
    samples: list[dict[str, Any]] = []
    predictions: list[dict[str, Any]] = []
    for row in rows:
        pred, score = predict_baseline(str(row["query"]), artifact)
        gold = str(row["target_category_slug"])
        if pred == gold:
            correct += 1
        confusion[gold][pred] += 1
        prediction = {
            "query_id": row["query_id"],
            "split": row.get("split"),
            "query": row["query"],
            "gold": gold,
            "pred": pred,
            "score": round(score, 6),
        }
        predictions.append(prediction)
        if len(samples) < 15:
            samples.append(prediction)

    write_jsonl(paths["baseline_eval_predictions"], predictions)
    summary = {
        "router": "baseline",
        "status": "evaluated",
        "splits_evaluated": splits,
        "total_eval_rows": total,
        "total_available_rows": len(all_rows),
        "eval_limit": eval_limit,
        "correct": correct,
        "accuracy": (correct / total) if total else 0.0,
        "sample_predictions": samples,
        "predictions_path": _relativize(paths["baseline_eval_predictions"], repo_root),
        "confusion": {gold: dict(counter) for gold, counter in confusion.items()},
    }
    write_json(paths["baseline_eval_summary"], summary)
    return summary


def evaluate_dspy(repo_root: Path, splits: list[str], args: argparse.Namespace) -> tuple[dict[str, Any], int]:
    validation = validate_workspace(repo_root)
    paths = artifact_paths(repo_root)
    dspy, dependency = dependency_info(repo_root)
    config, backend = resolve_lm_config(args)
    all_rows = collect_eval_rows(repo_root, splits) if validation["ok"] else []
    rows = limit_rows(all_rows, args.eval_limit)
    eval_scope = {
        "total_available_rows": len(all_rows),
        "eval_limit": args.eval_limit,
    }

    if not validation["ok"]:
        summary = {
            "router": "dspy",
            "status": "compile_failed",
            "message": "DSPy workspace validation failed; fix dataset issues before evaluation.",
            "splits_evaluated": splits,
            "validation": validation,
            "dependency": dependency,
            "backend": backend,
            **eval_scope,
        }
        write_json(paths["dspy_eval_summary"], summary)
        return summary, 1

    if not paths["dspy_router"].exists():
        summary = {
            "router": "dspy",
            "status": "compile_failed",
            "message": "Compiled DSPy router artifact is missing. Run the compile step first.",
            "splits_evaluated": splits,
            "artifact_path": _relativize(paths["dspy_router"], repo_root),
            "dependency": dependency,
            "backend": backend,
            **eval_scope,
        }
        write_json(paths["dspy_eval_summary"], summary)
        return summary, 1

    if not dependency.get("dspy_installed") or dspy is None:
        summary = {
            "router": "dspy",
            "status": "missing_dependency",
            "message": "dspy is not installed in the current Python environment.",
            "splits_evaluated": splits,
            "dependency": dependency,
            "backend": backend,
            **eval_scope,
        }
        write_json(paths["dspy_eval_summary"], summary)
        return summary, 1

    if config is None:
        summary = {
            "router": "dspy",
            "status": "backend_not_configured",
            "message": str(backend.get("message", "DSPy backend is not configured.")),
            "splits_evaluated": splits,
            "dependency": dependency,
            "backend": backend,
            **eval_scope,
        }
        write_json(paths["dspy_eval_summary"], summary)
        return summary, 1

    backend = dict(backend)
    backend["config"] = config_as_dict(config)
    probe = probe_backend(config, repo_root=repo_root)
    backend["probe"] = probe
    if probe.get("reachable") is False:
        summary = {
            "router": "dspy",
            "status": "backend_unreachable",
            "message": str(probe.get("message", "DSPy backend probe failed.")),
            "splits_evaluated": splits,
            "dependency": dependency,
            "backend": backend,
            **eval_scope,
        }
        write_json(paths["dspy_eval_summary"], summary)
        return summary, 1

    categories = load_json(paths["categories"])
    prompt_context = category_context(categories)

    class RouteCategory(dspy.Signature):
        query = dspy.InputField()
        category_guide = dspy.InputField()
        category_slug = dspy.OutputField()

    try:
        configure_dspy_lm(dspy, config, repo_root)
        module = dspy.ChainOfThought(RouteCategory)
        module.load(str(paths["dspy_router"]))

        total = len(rows)
        correct = 0
        predictions: list[dict[str, Any]] = []
        for row in rows:
            pred = module(query=row["query"], category_guide=prompt_context)
            pred_slug = str(getattr(pred, "category_slug", "")).strip()
            gold = str(row["target_category_slug"])
            if pred_slug == gold:
                correct += 1
            predictions.append(
                {
                    "query_id": row["query_id"],
                    "split": row.get("split"),
                    "query": row["query"],
                    "gold": gold,
                    "pred": pred_slug,
                }
            )
        write_jsonl(paths["dspy_eval_predictions"], predictions)
        summary = {
            "router": "dspy",
            "status": "evaluated",
            "splits_evaluated": splits,
            "total_eval_rows": total,
            **eval_scope,
            "correct": correct,
            "accuracy": (correct / total) if total else 0.0,
            "predictions_path": _relativize(paths["dspy_eval_predictions"], repo_root),
            "dependency": dependency,
            "backend": backend,
        }
        write_json(paths["dspy_eval_summary"], summary)
        return summary, 0
    except Exception as exc:  # noqa: BLE001
        failure_status = classify_runtime_failure(exc)
        summary = {
            "router": "dspy",
            "status": failure_status,
            "message": "DSPy evaluation failed.",
            "error": str(exc),
            "splits_evaluated": splits,
            "dependency": dependency,
            "backend": backend,
            **eval_scope,
        }
        write_json(paths["dspy_eval_summary"], summary)
        return summary, 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Evaluate Phase 3 Hermes routers")
    parser.add_argument("--repo-root", default=".", help="Path to the wizardsoftheghosts repo root")
    parser.add_argument("--baseline-only", action="store_true", help="Evaluate the lexical baseline only")
    parser.add_argument("--dspy-only", action="store_true", help="Evaluate the compiled DSPy router only")
    parser.add_argument(
        "--split",
        dest="splits",
        action="append",
        choices=["eval", "hard_negative"],
        default=None,
        help="Split to evaluate. Repeat for multiple splits. Defaults to eval.",
    )
    parser.add_argument("--dspy-model", default=None, help="Provider-qualified model string, for example openai/qwen3.5:4b")
    parser.add_argument("--dspy-api-base", default=None, help="Optional OpenAI-compatible API base URL")
    parser.add_argument("--dspy-api-key", default=None, help="Optional API key passed through to DSPy/LiteLLM")
    parser.add_argument("--dspy-temperature", default=None, help="Optional sampling temperature override")
    parser.add_argument("--dspy-max-tokens", default=None, help="Optional max tokens override")
    parser.add_argument("--eval-limit", type=positive_int, default=None, help="Optional cap on evaluation rows scored across the requested splits")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()
    splits = normalize_splits(args.splits)

    if args.baseline_only and args.dspy_only:
        raise SystemExit("--baseline-only and --dspy-only are mutually exclusive")

    if args.dspy_only:
        dspy_summary, exit_code = evaluate_dspy(repo_root, splits, args)
        print(json.dumps({"dspy": dspy_summary}, ensure_ascii=False, indent=2))
        return exit_code

    baseline = evaluate_baseline(repo_root, splits, eval_limit=args.eval_limit)
    if args.baseline_only:
        print(json.dumps({"baseline": baseline}, ensure_ascii=False, indent=2))
        return 0

    dspy_summary, exit_code = evaluate_dspy(repo_root, splits, args)
    print(json.dumps({"baseline": baseline, "dspy": dspy_summary}, ensure_ascii=False, indent=2))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
