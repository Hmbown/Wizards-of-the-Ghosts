#!/usr/bin/env python3
"""Manual GEPA optimization — uses a single LLM call per spell instead of DSPy's
iterative optimizer. Reads the spell definition + training data, asks the model
to produce an improved instruction, then writes the result back.

Usage:
    python scripts/gepa_manual_optimize.py --repo-root . --slug knock
    python scripts/gepa_manual_optimize.py --repo-root . --all
    
Uses opencode CLI by default (GEPA_CLI=opencode), or set GEPA_CLI=hermes.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

def load_jsonl(path: Path) -> list[dict]:
    rows = []
    if not path.exists():
        return rows
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows

def load_json(path: Path) -> dict:
    with open(path) as f:
        return json.load(f)

def write_json(path: Path, data: dict):
    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

def get_spell_instruction(repo_root: Path, slug: str) -> str:
    """Extract the current instruction/description from blueprints.json."""
    bp_path = repo_root / "catalog" / "blueprints.json"
    bp = load_json(bp_path)
    entries = bp.get("entries", bp) if isinstance(bp, dict) else bp
    for entry in entries:
        if entry.get("slug") == slug:
            parts = []
            parts.append(f"Name: {entry.get('name', slug)}")
            parts.append(f"Tagline: {entry.get('tagline', '')}")
            parts.append(f"Description: {entry.get('description', '')}")
            when = entry.get("when_to_use", [])
            if when:
                parts.append("When to use:")
                for w in when:
                    parts.append(f"  - {w}")
            workflow = entry.get("workflow", [])
            if workflow:
                parts.append("Workflow:")
                for i, step in enumerate(workflow, 1):
                    parts.append(f"  {i}. {step}")
            deliverables = entry.get("deliverables", [])
            if deliverables:
                parts.append("Deliverables:")
                for d in deliverables:
                    parts.append(f"  - {d}")
            guardrails = entry.get("guardrails", [])
            if guardrails:
                parts.append("Guardrails:")
                for g in guardrails:
                    parts.append(f"  - {g}")
            return "\n".join(parts)
    return f"[No blueprint found for {slug}]"

def get_skill_content(slug: str) -> str:
    """Read the deployed SKILL.md."""
    skills_dir = Path.home() / ".hermes" / "skills"
    for cat in skills_dir.iterdir():
        skill_path = cat / slug / "SKILL.md"
        if skill_path.exists():
            return skill_path.read_text()[:3000]  # truncate for prompt size
    return ""

def build_optimization_prompt(slug: str, instruction: str, train: list, eval_data: list, confusables: list, skill_content: str) -> str:
    """Build the prompt for the optimizer model."""
    train_prompts = "\n".join(f"  - {r['prompt']}" for r in train[:10])
    eval_prompts = "\n".join(f"  - {r['prompt']}" for r in eval_data[:8])
    conf_prompts = "\n".join(f"  - {r['prompt']}" for r in confusables[:6])
    
    return f"""You are optimizing a spell instruction for an AI coding assistant's skill routing system.

The spell "{slug}" currently has this definition:

{instruction}

Here is a summary of the deployed skill (truncated):
{skill_content[:1500]}

TRAINING DATA (prompts that SHOULD trigger this spell):
{train_prompts}

EVALUATION DATA (harder prompts that should also trigger this spell):
{eval_prompts}

CONFUSABLE DATA (prompts that look similar but should NOT trigger this spell):
{conf_prompts}

Your task: Write an improved spell instruction that would help a small language model (9B parameters) correctly:
1. Recognize when this spell should be activated
2. Distinguish it from confusable spells
3. Follow the spell's specific workflow (not generic advice)

The improved instruction should:
- Be specific about what makes this spell DIFFERENT from similar ones
- Include concrete trigger signals (what words/patterns in user requests indicate this spell)
- List explicit anti-patterns (what looks like this spell but isn't)
- Keep the workflow steps actionable and distinctive
- Be concise (under 500 words) — a small model needs clear signal, not volume

Output ONLY the improved instruction text, nothing else. No preamble, no explanation."""

def run_opencode(prompt: str, model: str = "opencode/qwen3.6-plus-free") -> str:
    """Run a single opencode call."""
    import re
    cli = shutil.which("opencode")
    if not cli:
        raise RuntimeError("opencode CLI not found")
    
    cmd = [cli, "run", "-m", model, prompt]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    if result.returncode != 0:
        raise RuntimeError(f"opencode failed: {result.stderr[:500]}")
    
    # Strip ANSI escape codes
    text = re.sub(r'\x1b\[[0-9;]*[a-zA-Z]', '', result.stdout)
    # Split lines, skip the "> build" header line and any empty lines around it
    lines = text.strip().split("\n")
    response_lines = []
    past_header = False
    for line in lines:
        stripped = line.strip()
        if not past_header:
            if stripped.startswith(">") or stripped == "":
                continue
            past_header = True
        response_lines.append(line)
    return "\n".join(response_lines).strip()

def run_hermes(prompt: str) -> str:
    """Run a single hermes CLI call."""
    cli = shutil.which("hermes")
    if not cli:
        raise RuntimeError("hermes CLI not found")
    cmd = [cli, "chat", "-q", prompt, "-Q"]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    if result.returncode != 0:
        raise RuntimeError(f"hermes failed: {result.stderr[:500]}")
    return result.stdout.strip()

def optimize_spell(repo_root: Path, slug: str, cli: str = "opencode", model: str = "opencode/qwen3.6-plus-free") -> dict:
    """Optimize a single spell."""
    gepa_dir = repo_root / "catalog" / "gepa" / "spells" / slug
    
    if not gepa_dir.exists():
        return {"slug": slug, "status": "error", "message": f"No GEPA workspace for {slug}"}
    
    train = load_jsonl(gepa_dir / "train.jsonl")
    eval_data = load_jsonl(gepa_dir / "eval.jsonl")
    confusables = load_jsonl(gepa_dir / "confusables.jsonl")
    
    if not train:
        return {"slug": slug, "status": "skipped", "message": "Empty training data"}
    
    instruction = get_spell_instruction(repo_root, slug)
    skill_content = get_skill_content(slug)
    prompt = build_optimization_prompt(slug, instruction, train, eval_data, confusables, skill_content)
    
    print(f"  Optimizing {slug}... ({len(train)} train, {len(eval_data)} eval, {len(confusables)} conf)")
    
    if cli == "opencode":
        optimized = run_opencode(prompt, model)
    else:
        optimized = run_hermes(prompt)
    
    if not optimized or len(optimized) < 50:
        return {"slug": slug, "status": "error", "message": f"Model returned too-short response: {optimized[:100]}"}
    
    # Write the optimized instruction to status
    status_path = gepa_dir / "optimization_status.json"
    status = load_json(status_path) if status_path.exists() else {}
    status["status"] = "optimized"
    status["optimized_instruction"] = optimized
    status["optimizer"] = f"manual-{cli}"
    status["model"] = model
    write_json(status_path, status)
    
    return {"slug": slug, "status": "optimized", "instruction_length": len(optimized)}

def main():
    parser = argparse.ArgumentParser(description="Manual GEPA spell optimization")
    parser.add_argument("--repo-root", required=True, help="Repository root")
    parser.add_argument("--slug", help="Single spell to optimize")
    parser.add_argument("--all", action="store_true", help="Optimize all populated workspaces")
    parser.add_argument("--unoptimized-only", action="store_true", help="Skip already-optimized spells")
    parser.add_argument("--cli", default=os.environ.get("GEPA_CLI", "opencode"), choices=["opencode", "hermes"])
    parser.add_argument("--model", default="opencode/qwen3.6-plus-free")
    args = parser.parse_args()
    
    repo_root = Path(args.repo_root).resolve()
    
    if args.slug:
        slugs = [args.slug]
    elif args.all:
        gepa_dir = repo_root / "catalog" / "gepa" / "spells"
        slugs = sorted([
            d.name for d in gepa_dir.iterdir()
            if d.is_dir() and d.name != ".gitkeep"
        ])
    else:
        parser.error("Must specify --slug or --all")
    
    results = []
    for slug in slugs:
        if args.unoptimized_only:
            status_path = repo_root / "catalog" / "gepa" / "spells" / slug / "optimization_status.json"
            if status_path.exists():
                status = load_json(status_path)
                if status.get("status") == "optimized" and status.get("optimized_instruction"):
                    print(f"  Skipping {slug} (already optimized)")
                    continue
        
        try:
            result = optimize_spell(repo_root, slug, cli=args.cli, model=args.model)
            results.append(result)
            print(f"  -> {result['status']}: {result.get('message', result.get('instruction_length', ''))}")
        except Exception as e:
            results.append({"slug": slug, "status": "error", "message": str(e)[:200]})
            print(f"  -> ERROR: {e}")
    
    print(f"\nDone: {len([r for r in results if r['status'] == 'optimized'])} optimized, "
          f"{len([r for r in results if r['status'] == 'error'])} errors, "
          f"{len([r for r in results if r['status'] == 'skipped'])} skipped")
    
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
