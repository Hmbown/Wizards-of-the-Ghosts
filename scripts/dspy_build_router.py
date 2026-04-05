#!/usr/bin/env python3
"""Build Phase 3 routing artifacts for Hermes spells.

This script always supports the lexical baseline router. The DSPy router path is
explicitly configurable and writes a structured status artifact whether compile
succeeds or not.
"""
from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from dspy_common import (
    artifact_paths,
    build_router_status,
    category_context,
    classify_runtime_failure,
    config_as_dict,
    configure_dspy_lm,
    dependency_info,
    load_json,
    load_jsonl,
    probe_backend,
    resolve_lm_config,
    validate_workspace,
    write_json,
    write_router_status,
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


def build_baseline(repo_root: Path) -> dict[str, Any]:
    paths = artifact_paths(repo_root)
    spells = load_jsonl(paths["spells_master"])
    categories = load_json(paths["categories"])
    train_queries = load_jsonl(paths["train_queries"])

    category_docs: dict[str, list[str]] = defaultdict(list)
    for category in categories:
        slug = str(category["slug"])
        category_docs[slug].append(str(category.get("title", "")))
        category_docs[slug].append(str(category.get("description", "")))

    for spell in spells:
        slug = str(spell["category_slug"])
        category_docs[slug].extend(
            [
                str(spell.get("name", "")),
                str(spell.get("tagline", "")),
                str(spell.get("description", "")),
                str(spell.get("default_prompt", "")),
                " ".join(str(x) for x in spell.get("when_to_use", [])),
            ]
        )

    for row in train_queries:
        slug = str(row["target_category_slug"])
        category_docs[slug].append(str(row.get("query", "")))

    vocabulary_counter: Counter[str] = Counter()
    category_term_counts: dict[str, Counter[str]] = {}
    for slug, docs in category_docs.items():
        tokens: list[str] = []
        for doc in docs:
            tokens.extend(tokenize(doc))
        counter = Counter(tokens)
        category_term_counts[slug] = counter
        vocabulary_counter.update(counter.keys())

    idf: dict[str, float] = {}
    num_categories = max(len(category_term_counts), 1)
    for token, doc_freq in vocabulary_counter.items():
        idf[token] = math.log((1 + num_categories) / (1 + doc_freq)) + 1.0

    category_vectors: dict[str, dict[str, float]] = {}
    for slug, counts in category_term_counts.items():
        total = sum(counts.values()) or 1
        vec = {tok: (count / total) * idf.get(tok, 1.0) for tok, count in counts.items()}
        norm = math.sqrt(sum(v * v for v in vec.values())) or 1.0
        category_vectors[slug] = {tok: val / norm for tok, val in vec.items()}

    artifact = {
        "router_type": "lexical_baseline",
        "categories": sorted(category_vectors.keys()),
        "idf": idf,
        "category_vectors": category_vectors,
        "build_summary": {
            "num_spells": len(spells),
            "num_categories": len(category_vectors),
            "num_train_queries": len(train_queries),
            "vocab_size": len(idf),
        },
    }
    write_json(paths["baseline_router"], artifact)
    return artifact


def validate_dspy_runtime(repo_root: Path, args: argparse.Namespace) -> dict[str, Any]:
    validation = validate_workspace(repo_root)
    _, dependency = dependency_info()
    config, backend = resolve_lm_config(args)
    if config is not None:
        backend = dict(backend)
        backend["config"] = config_as_dict(config)
        backend["probe"] = probe_backend(config, repo_root=repo_root)

    if not validation["ok"]:
        status = build_router_status(
            repo_root,
            status="compile_failed",
            message="DSPy workspace validation failed.",
            dependency=dependency,
            backend=backend,
            validation=validation,
        )
    elif config is None:
        status = build_router_status(
            repo_root,
            status="backend_not_configured",
            message=str(backend.get("message", "DSPy backend is not configured.")),
            dependency=dependency,
            backend=backend,
            validation=validation,
        )
    elif not dependency.get("dspy_installed"):
        status = build_router_status(
            repo_root,
            status="missing_dependency",
            message="dspy is not installed in the current Python environment.",
            dependency=dependency,
            backend=backend,
            validation=validation,
        )
    elif backend.get("probe", {}).get("reachable") is False:
        status = build_router_status(
            repo_root,
            status="backend_unreachable",
            message=str(backend["probe"].get("message", "DSPy backend probe failed.")),
            dependency=dependency,
            backend=backend,
            validation=validation,
        )
    else:
        status = build_router_status(
            repo_root,
            status="ok",
            message="DSPy dependency, dataset, and backend configuration checks passed.",
            dependency=dependency,
            backend=backend,
            validation=validation,
        )

    write_router_status(repo_root, status)
    return status


def compile_dspy_router(repo_root: Path, args: argparse.Namespace) -> tuple[dict[str, Any], int]:
    validation = validate_workspace(repo_root)
    dspy, dependency = dependency_info()
    config, backend = resolve_lm_config(args)

    backend = dict(backend)
    paths = artifact_paths(repo_root)
    train_queries_all = load_jsonl(paths["train_queries"])
    eval_queries = load_jsonl(paths["eval_queries"])
    compile_scope = {
        "train_limit": args.train_limit,
        "train_rows_available": len(train_queries_all),
        "train_rows_used": len(limit_rows(train_queries_all, args.train_limit)),
        "eval_rows_available": len(eval_queries),
        "limited_train_compile": args.train_limit is not None,
    }

    if not validation["ok"]:
        status = build_router_status(
            repo_root,
            status="compile_failed",
            message="DSPy workspace validation failed; fix dataset issues before compiling.",
            dependency=dependency,
            backend=backend,
            validation=validation,
            extra=compile_scope,
        )
        write_router_status(repo_root, status)
        return status, 1

    if config is None:
        status = build_router_status(
            repo_root,
            status="backend_not_configured",
            message=str(backend.get("message", "DSPy backend is not configured.")),
            dependency=dependency,
            backend=backend,
            validation=validation,
            extra=compile_scope,
        )
        write_router_status(repo_root, status)
        return status, 1

    if not dependency.get("dspy_installed") or dspy is None:
        status = build_router_status(
            repo_root,
            status="missing_dependency",
            message="dspy is not installed in the current Python environment.",
            dependency=dependency,
            backend=backend,
            validation=validation,
            extra=compile_scope,
        )
        write_router_status(repo_root, status)
        return status, 1

    backend["config"] = config_as_dict(config)

    probe = probe_backend(config, repo_root=repo_root)
    backend["probe"] = probe
    if probe.get("reachable") is False:
        status = build_router_status(
            repo_root,
            status="backend_unreachable",
            message=str(probe.get("message", "DSPy backend probe failed.")),
            dependency=dependency,
            backend=backend,
            validation=validation,
            extra=compile_scope,
        )
        write_router_status(repo_root, status)
        return status, 1

    categories = load_json(paths["categories"])
    train_queries = limit_rows(train_queries_all, args.train_limit)

    category_choices = [str(cat["slug"]) for cat in categories]
    prompt_context = category_context(categories)

    class RouteCategory(dspy.Signature):
        """Route a user request to the best Hermes spell category."""

        query = dspy.InputField()
        category_guide = dspy.InputField()
        category_slug = dspy.OutputField(desc=f"One of: {', '.join(category_choices)}")

    module = dspy.ChainOfThought(RouteCategory)
    trainset = [
        dspy.Example(
            query=row["query"],
            category_guide=prompt_context,
            category_slug=row["target_category_slug"],
        ).with_inputs("query", "category_guide")
        for row in train_queries
    ]

    def metric(example: Any, pred: Any, trace: Any = None) -> bool:
        return str(example.category_slug).strip() == str(getattr(pred, "category_slug", "")).strip()

    try:
        configure_dspy_lm(dspy, config, repo_root)
        from dspy.teleprompt import BootstrapFewShot  # type: ignore

        optimizer = BootstrapFewShot(metric=metric, max_bootstrapped_demos=8)
        optimized = optimizer.compile(module, trainset=trainset)
        optimized.save(str(paths["dspy_router"]))
        status = build_router_status(
            repo_root,
            status="ok",
            message=(
                "Compiled DSPy category router using a limited train subset."
                if args.train_limit is not None
                else "Compiled DSPy category router."
            ),
            dependency=dependency,
            backend=backend,
            validation=validation,
            extra={
                **compile_scope,
                "saved_model": str(paths["dspy_router"]),
                "categories": category_choices,
            },
        )
        write_router_status(repo_root, status)
        return status, 0
    except Exception as exc:  # noqa: BLE001
        failure_status = classify_runtime_failure(exc)
        status = build_router_status(
            repo_root,
            status=failure_status,
            message="DSPy router compile failed.",
            dependency=dependency,
            backend=backend,
            validation=validation,
            extra={
                **compile_scope,
                "error": str(exc),
            },
        )
        write_router_status(repo_root, status)
        return status, 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build baseline and DSPy router artifacts for Hermes spell routing")
    parser.add_argument("--repo-root", default=".", help="Path to the wizardsoftheghosts repo root")
    parser.add_argument("--validate-only", action="store_true", help="Validate dataset and backend configuration only")
    parser.add_argument("--baseline-only", action="store_true", help="Build the lexical baseline only")
    parser.add_argument(
        "--dspy-model",
        default=None,
        help="Provider-qualified model string or local alias, for example openai/<model>, hermes/default, qwen/default, opencode/default, or copilot/codex-5.3",
    )
    parser.add_argument("--dspy-api-base", default=None, help="Optional OpenAI-compatible API base URL")
    parser.add_argument("--dspy-api-key", default=None, help="Optional API key passed through to DSPy/LiteLLM")
    parser.add_argument("--dspy-temperature", default=None, help="Optional sampling temperature override")
    parser.add_argument("--dspy-max-tokens", default=None, help="Optional max tokens override")
    parser.add_argument("--train-limit", type=positive_int, default=None, help="Optional cap on training rows used for DSPy compile")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()

    if args.validate_only and args.baseline_only:
        raise SystemExit("--validate-only and --baseline-only are mutually exclusive")

    if args.validate_only:
        status = validate_dspy_runtime(repo_root, args)
        print(json.dumps({"dspy": status}, ensure_ascii=False, indent=2))
        return 0

    baseline = build_baseline(repo_root)
    if args.baseline_only:
        print(json.dumps({"baseline": baseline["build_summary"]}, ensure_ascii=False, indent=2))
        return 0

    dspy_status, exit_code = compile_dspy_router(repo_root, args)
    print(json.dumps({"baseline": baseline["build_summary"], "dspy": dspy_status}, ensure_ascii=False, indent=2))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
