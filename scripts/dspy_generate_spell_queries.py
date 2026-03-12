#!/usr/bin/env python3
"""Merge and validate Phase 2 DSPy query shards.

This script reads manually or subagent-generated JSONL shard files under
catalog/dspy/shards/ and produces consolidated train/eval/hard-negative files.

It intentionally uses only Python stdlib.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

REQUIRED_FIELDS = {
    "query_id",
    "split",
    "query_type",
    "query",
    "target_slug",
    "target_category_slug",
    "target_kind",
}
ALLOWED_SPLITS = {"train", "eval", "hard_negative", "abstain"}


def _load_master(master_path: Path) -> dict[str, dict[str, Any]]:
    rows: dict[str, dict[str, Any]] = {}
    for line in master_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        rows[str(row["slug"])] = row
    return rows


def _iter_shard_rows(shards_dir: Path) -> list[tuple[Path, int, dict[str, Any]]]:
    records: list[tuple[Path, int, dict[str, Any]]] = []
    for path in sorted(shards_dir.glob("*.jsonl")):
        for idx, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if not line.strip():
                continue
            records.append((path, idx, json.loads(line)))
    return records


def _validate_row(row: dict[str, Any], master: dict[str, dict[str, Any]]) -> None:
    missing = REQUIRED_FIELDS - set(row.keys())
    if missing:
        raise ValueError(f"row missing required fields: {sorted(missing)}")
    if row["split"] not in ALLOWED_SPLITS:
        raise ValueError(f"invalid split: {row['split']}")
    slug = str(row["target_slug"])
    if slug not in master:
        raise ValueError(f"unknown target_slug: {slug}")
    master_row = master[slug]
    if row["target_category_slug"] != master_row["category_slug"]:
        raise ValueError(
            f"category mismatch for {slug}: {row['target_category_slug']} != {master_row['category_slug']}"
        )
    if row["target_kind"] != master_row["kind"]:
        raise ValueError(f"kind mismatch for {slug}: {row['target_kind']} != {master_row['kind']}")
    if not str(row["query"]).strip():
        raise ValueError("query must be non-empty")


def merge(repo_root: Path) -> dict[str, Any]:
    dspy_dir = repo_root / "catalog" / "dspy"
    shards_dir = dspy_dir / "shards"
    shards_dir.mkdir(parents=True, exist_ok=True)

    master = _load_master(dspy_dir / "spells_master.jsonl")
    records = _iter_shard_rows(shards_dir)

    seen_ids: set[str] = set()
    merged: list[dict[str, Any]] = []
    for path, line_no, row in records:
        try:
            _validate_row(row, master)
        except Exception as exc:  # noqa: BLE001
            raise ValueError(f"{path}:{line_no}: {exc}") from exc
        query_id = str(row["query_id"])
        if query_id in seen_ids:
            raise ValueError(f"duplicate query_id detected: {query_id}")
        seen_ids.add(query_id)
        merged.append(row)

    merged.sort(key=lambda item: (str(item["split"]), str(item["target_category_slug"]), str(item["target_slug"]), str(item["query_id"])))

    train_rows = [row for row in merged if row["split"] == "train"]
    eval_rows = [row for row in merged if row["split"] == "eval"]
    hard_negative_rows = [row for row in merged if row["split"] == "hard_negative"]
    abstain_rows = [row for row in merged if row["split"] == "abstain"]

    def _dump(path: Path, rows: list[dict[str, Any]]) -> None:
        path.write_text("\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + ("\n" if rows else ""), encoding="utf-8")

    _dump(dspy_dir / "hermes-train-queries.jsonl", train_rows)
    _dump(dspy_dir / "hermes-eval-set.jsonl", eval_rows)
    _dump(dspy_dir / "hermes-hard-negatives.jsonl", hard_negative_rows)
    _dump(dspy_dir / "hermes-abstain.jsonl", abstain_rows)

    summary = {
        "total_rows": len(merged),
        "train_rows": len(train_rows),
        "eval_rows": len(eval_rows),
        "hard_negative_rows": len(hard_negative_rows),
        "abstain_rows": len(abstain_rows),
        "categories_covered": sorted({row["target_category_slug"] for row in merged}),
        "query_types": dict(sorted(Counter(str(row["query_type"]) for row in merged).items())),
        "shards_processed": sorted(path.name for path in shards_dir.glob("*.jsonl")),
    }
    (dspy_dir / "hermes_query_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description="Merge Phase 2 DSPy query shards into consolidated JSONL datasets")
    parser.add_argument("--repo-root", default=".", help="Path to the wizardsoftheghosts repo root")
    args = parser.parse_args()
    summary = merge(Path(args.repo_root).resolve())
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
