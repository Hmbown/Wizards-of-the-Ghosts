#!/usr/bin/env python3
"""Apply a spell promotion patch back into catalog/blueprints.json."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from gepa_common import apply_promotion_patch, load_json, spell_paths


def main() -> int:
    parser = argparse.ArgumentParser(description="Promote a spell optimization patch into catalog/blueprints.json")
    parser.add_argument("--repo-root", default=".", help="Path to the wizardsoftheghosts repo root")
    parser.add_argument("--slug", required=True, help="Spell slug to promote")
    parser.add_argument("--patch", default=None, help="Optional explicit path to the promotion patch JSON")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    patch_path = Path(args.patch).resolve() if args.patch else spell_paths(repo_root, args.slug)["promotion_patch"]
    patch = load_json(patch_path)
    entry = apply_promotion_patch(repo_root, args.slug, patch)
    payload = {
        "slug": args.slug,
        "status": "promoted",
        "patch_path": str(patch_path),
        "updated_fields": sorted((patch.get("updated_fields") or {}).keys()),
        "entry_name": entry["name"],
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
