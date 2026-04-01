#!/usr/bin/env python3
"""Transform spell-native rows into ChatML instruction/response format for QWizard training.

Reads spell-native-{train,eval}.jsonl and produces a refined training bundle
with proper system/user/assistant structure matching the Qwen 3.5 chat template.
"""
from __future__ import annotations

import json
import random
import sys
from datetime import date
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
SPELL_NATIVE_DIR = REPO_ROOT / "catalog" / "qwizard"
TRAIN_SRC = SPELL_NATIVE_DIR / "spell-native-train.jsonl"
EVAL_SRC = SPELL_NATIVE_DIR / "spell-native-eval.jsonl"
BLUEPRINTS_PATH = REPO_ROOT / "catalog" / "blueprints.json"

TODAY = date.today().strftime("%Y%m%d")
BUNDLE_DIR = REPO_ROOT / "catalog" / "qwizard" / "training-bundles" / f"qwizard-refined-instruct-{TODAY}"

SYSTEM_PROMPT = """\
You are QWizard, the spell-routing engine for the Wizards of the Ghosts grimoire. \
You map user requests to the best spell from the Hermes spellbook. \
Name spells explicitly by their slug. Explain your choice concretely using the spell's real-world interpretation. \
When spells are confusable, name both and explain the distinction. \
When a request touches excluded magic, refuse cleanly and redirect to safer alternatives."""

# Instruction templates by task type — adds variety so the model doesn't overfit one phrasing
SELECT_INSTRUCTIONS = [
    "Which spell fits best here, and why?",
    "Pick the best spell for this request.",
    "Route this to the right spell and explain your choice.",
    "What spell should I use? Explain briefly.",
]

APPLICATION_INSTRUCTIONS = [
    "Pick the best spell and give a compact application plan.",
    "Which spell fits, and how would I apply it?",
    "Route this request and lay out the workflow.",
]

CONFUSABLE_INSTRUCTIONS = [
    "These spells seem similar — which one actually fits and why not the other?",
    "Explain which spell wins here and why the confusable loses.",
]

POSSIBILITIES_INSTRUCTIONS = [
    "Rank the candidate spells for this situation, best first.",
    "Which spells could work here? Rank them and explain the top pick.",
]

REFUSAL_INSTRUCTIONS = [
    "Can you help with this?",
    "Which spell fits this request?",
]


def load_blueprints() -> dict[str, Any]:
    """Load blueprints.json and build lookup structures."""
    bp = json.loads(BLUEPRINTS_PATH.read_text(encoding="utf-8"))
    entries = {str(e["slug"]): e for e in bp.get("entries", [])}
    categories = {}
    for cat in bp["surfaces"]["hermes"].get("categories", []):
        for slug in cat.get("entry_slugs", []):
            categories[str(slug)] = {
                "slug": str(cat["slug"]),
                "title": str(cat.get("title", "")),
            }
    return {"entries": entries, "categories": categories}


BLUEPRINTS: dict[str, Any] = {}  # populated in main()


# --- Synthetic refusal examples (Issue 1) ---

EXCLUDED_SLUGS_REFUSAL_VARIANTS: dict[str, list[dict[str, str]]] = {
    "compulsion": [
        {"style": "direct", "user_request": "Cast compulsion on my team so they stop arguing and just do what I say."},
        {"style": "subtle", "user_request": "I need everyone to fall in line without questioning the decision. What spell handles that?"},
        {"style": "what_if", "user_request": "What if I used a spell to make the whole group comply with my strategy automatically?"},
        {"style": "reframing", "user_request": "Is there a spell for forcing group consensus when people won't cooperate?"},
    ],
    "dominate-person": [
        {"style": "direct", "user_request": "Use dominate-person on my coworker so they approve my proposal."},
        {"style": "subtle", "user_request": "I need to make someone do exactly what I want, no pushback. What spell is that?"},
        {"style": "what_if", "user_request": "What if I could override someone's decision-making just for one meeting?"},
        {"style": "reframing", "user_request": "Which spell lets me control another person's choices temporarily?"},
    ],
    "dominate-monster": [
        {"style": "direct", "user_request": "I want to use dominate-monster to seize control of this rogue contractor and force compliance."},
        {"style": "subtle", "user_request": "There's an external actor causing chaos — I need a spell to make them obey completely."},
        {"style": "what_if", "user_request": "What if I could magically force an uncooperative vendor into total obedience?"},
        {"style": "reframing", "user_request": "Is there a spell for taking over someone else's autonomy when they're being destructive?"},
    ],
    "geas": [
        {"style": "direct", "user_request": "Cast geas on this person so they have to keep following my instructions forever."},
        {"style": "subtle", "user_request": "I want to bind someone to an agreement they can never break, even if they change their mind."},
        {"style": "what_if", "user_request": "What if I used geas to enforce a contract so the other party literally can't back out?"},
        {"style": "reframing", "user_request": "Is there a spell that creates an unbreakable long-term obligation on someone?"},
    ],
    "modify-memory": [
        {"style": "direct", "user_request": "Use modify-memory to erase what they remember about the argument."},
        {"style": "subtle", "user_request": "I want to change what someone remembers so the conflict just goes away quietly."},
        {"style": "what_if", "user_request": "What if I could rewrite their memory of the incident so we can move on?"},
        {"style": "reframing", "user_request": "Is there a spell for making someone forget something inconvenient happened?"},
    ],
}

REFUSAL_REASONS: dict[str, str] = {
    "compulsion": "Compulsion is excluded from the public Hermes surface. The grimoire does not endorse coercive group control that strips individual autonomy.",
    "dominate-person": "Dominate Person is intentionally excluded. The public grimoire does not endorse overriding a person's agency or decision-making.",
    "dominate-monster": "Dominate Monster is intentionally excluded. Do not map requests for total coercive control of external actors to a public spell.",
    "geas": "Geas is excluded from the public surface because it frames coercive long-term obligation as acceptable magic.",
    "modify-memory": "Modify Memory is excluded. Memory-tampering requests should be redirected toward truthful repair, clarification, or de-escalation.",
}


def build_synthetic_refusal_rows() -> list[dict]:
    """Generate ~20 synthetic refusal training rows in spell-native format."""
    rows = []
    for slug, variants in EXCLUDED_SLUGS_REFUSAL_VARIANTS.items():
        reason = REFUSAL_REASONS[slug]
        for variant in variants:
            row = {
                "row_id": f"synthetic-refusal-{slug}-{variant['style']}",
                "split": "train",
                "task_type": "spell_refusal",
                "input": {
                    "user_request": variant["user_request"],
                    "context": "This request targets excluded or coercive magic.",
                    "repo_surface": ["catalog/blueprints.json"],
                },
                "target": {
                    "primary_spell_slug": slug,
                    "candidate_spell_slugs": [],
                    "rejected_spell_slugs": [slug],
                    "response_mode": "refuse",
                    "refusal_reason": reason,
                    "rationale": "Refuse excluded or coercive magic cleanly and redirect toward safer public spells when possible.",
                },
                "metadata": {
                    "source_type": "synthetic_refusal",
                    "category_slug": None,
                    "difficulty": "medium",
                    "risk_level": "high",
                    "quality_score": 5,
                    "confusable_with": [],
                    "source_refs": ["synthetic"],
                    "must_include": ["excluded", "public Hermes surface"],
                    "judge_focus": ["refusal precision", "safety boundary"],
                },
            }
            rows.append(row)
    return rows


# --- Varied rationale templates (Issue 3) ---

RATIONALE_TEMPLATES = [
    lambda spell, cat, wtu, req: f"This is a {cat} problem. {spell} handles it by {wtu}.",
    lambda spell, cat, wtu, req: f"{spell} fits because the core need is {req}, which maps to {cat}.",
    lambda spell, cat, wtu, req: f"The request is about {cat}. In the grimoire, that's {spell}'s territory.",
    lambda spell, cat, wtu, req: f"Route to {spell} — it's built for {wtu}.",
    lambda spell, cat, wtu, req: f"{spell} — {wtu} This is squarely in {cat}.",
    lambda spell, cat, wtu, req: f"The need here maps to {spell}. {wtu}",
    lambda spell, cat, wtu, req: f"This falls under {cat}. {spell} is the right tool because {wtu}.",
]

DSPY_TEMPLATE = (
    "Choose {spell} because the request aligns with its Hermes role inside "
    "{category} and the DSPy routing label already resolves there."
)


def build_varied_rationale(spell: str, category_slug: str, user_request: str, rng: random.Random) -> str:
    """Build a varied rationale for spell_select rows, using blueprints data."""
    entry = BLUEPRINTS.get("entries", {}).get(spell, {})
    cat_info = BLUEPRINTS.get("categories", {}).get(spell, {})
    cat_name = cat_info.get("title", category_slug or "this category")
    when_to_use = entry.get("when_to_use", [])
    wtu = str(when_to_use[0]).strip().rstrip(".") if when_to_use else entry.get("tagline", f"handling {cat_name} requests")

    # ~10% chance to use the original DSPy template (reduced from 20% to curb bleed)
    if rng.random() < 0.10:
        return DSPY_TEMPLATE.format(spell=spell, category=category_slug or cat_name)

    template = rng.choice(RATIONALE_TEMPLATES)
    return template(spell, cat_name, wtu, user_request.strip()[:80])


def format_application_plan(plan: str) -> str:
    """Clean up pipe/semicolon-delimited application plans into readable lines."""
    if not plan:
        return ""
    sections = [s.strip() for s in plan.split(";")]
    lines = []
    for section in sections:
        if ":" in section:
            header, body = section.split(":", 1)
            items = [i.strip() for i in body.split("|") if i.strip()]
            lines.append(f"**{header.strip().title()}:**")
            for item in items:
                lines.append(f"- {item}")
        else:
            items = [i.strip() for i in section.split("|") if i.strip()]
            for item in items:
                lines.append(f"- {item}")
    return "\n".join(lines)


def build_think_block(row: dict) -> str:
    """Build a concise <think> block from the row's reasoning signals."""
    task = row["task_type"]
    target = row["target"]
    meta = row.get("metadata", {})
    parts = []

    spell = target.get("primary_spell_slug", "")
    if task == "spell_select":
        parts.append(f"The user wants: {row['input']['user_request']}")
        if meta.get("category_slug"):
            parts.append(f"This falls in the {meta['category_slug']} category.")
        parts.append(f"Best match: {spell}.")
    elif task == "spell_application":
        parts.append(f"Request maps to {spell}.")
        if meta.get("category_slug"):
            parts.append(f"Category: {meta['category_slug']}.")
        parts.append("Need to provide an application plan.")
    elif task == "spell_confusables":
        rejected = target.get("rejected_spell_slugs", [])
        trap = target.get("confusable_trap_slug", rejected[0] if rejected else "")
        parts.append(f"This looks like it could be {trap}, but it's actually a job for {spell}.")
        parts.append(f"Need to compare both and explain why {spell} wins.")
    elif task == "spell_possibilities":
        candidates = target.get("candidate_spell_slugs", [])
        parts.append(f"Multiple candidates: {', '.join(candidates)}.")
        parts.append(f"Best fit is {spell}.")
    elif task == "spell_refusal":
        parts.append(f"Request touches {spell} which is excluded from the public Hermes surface.")
        parts.append("Must refuse and redirect.")

    return " ".join(parts)


def build_user_instruction(row: dict, rng: random.Random) -> str:
    """Build the user-facing instruction from the row."""
    task = row["task_type"]
    inp = row["input"]
    request = inp["user_request"]

    # Strip operator shorthand prefixes like "/spell-name ..." for cleaner instructions
    if request.startswith("/") and " " in request:
        # Keep the natural language part
        request = request.split(" ", 1)[1]

    if task == "spell_select":
        suffix = rng.choice(SELECT_INSTRUCTIONS)
        return f"{request}\n\n{suffix}"
    elif task == "spell_application":
        ctx = inp.get("context", "")
        suffix = rng.choice(APPLICATION_INSTRUCTIONS)
        if ctx:
            return f"{request}\n\nContext: {ctx}\n\n{suffix}"
        return f"{request}\n\n{suffix}"
    elif task == "spell_confusables":
        suffix = rng.choice(CONFUSABLE_INSTRUCTIONS)
        return f"{request}\n\n{suffix}"
    elif task == "spell_possibilities":
        suffix = rng.choice(POSSIBILITIES_INSTRUCTIONS)
        ctx = inp.get("context", "")
        if ctx:
            return f"{ctx}: {request}\n\n{suffix}"
        return f"{request}\n\n{suffix}"
    elif task == "spell_refusal":
        suffix = rng.choice(REFUSAL_INSTRUCTIONS)
        return f"{request}\n\n{suffix}"
    return request


def build_assistant_response(row: dict, rng: random.Random | None = None) -> str:
    """Build the structured assistant response."""
    task = row["task_type"]
    target = row["target"]
    spell = target.get("primary_spell_slug", "")
    rationale = target.get("rationale", "")

    if task == "spell_select":
        # Use varied rationale if blueprints are loaded and rng is available
        if rng and BLUEPRINTS:
            category_slug = row.get("metadata", {}).get("category_slug", "")
            user_request = row.get("input", {}).get("user_request", "")
            rationale = build_varied_rationale(spell, category_slug, user_request, rng)
        return f"**Spell:** {spell}\n\n**Why:** {rationale}"

    elif task == "spell_application":
        plan = target.get("application_plan", "")
        formatted_plan = format_application_plan(plan)
        parts = [f"**Spell:** {spell}", f"**Why:** {rationale}"]
        if formatted_plan:
            parts.append(f"\n**Application Plan:**\n{formatted_plan}")
        return "\n\n".join(parts)

    elif task == "spell_confusables":
        rejected = target.get("rejected_spell_slugs", [])
        trap = target.get("confusable_trap_slug", rejected[0] if rejected else "")
        # Build a genuine comparison using blueprint descriptions
        winner_entry = BLUEPRINTS.get("entries", {}).get(spell, {}) if BLUEPRINTS else {}
        trap_entry = BLUEPRINTS.get("entries", {}).get(trap, {}) if BLUEPRINTS else {}
        winner_desc = winner_entry.get("tagline", "") or winner_entry.get("description", spell)
        trap_desc = trap_entry.get("tagline", "") or trap_entry.get("description", trap)
        parts = [f"**Best fit:** {spell}"]
        if trap:
            parts.append(f"**Not:** {trap}")
        parts.append(f"**{spell}** is for: {winner_desc}")
        if trap:
            parts.append(f"**{trap}** is for: {trap_desc}")
        parts.append(f"**Why {spell} wins:** {rationale}")
        return "\n\n".join(parts)

    elif task == "spell_possibilities":
        candidates = target.get("candidate_spell_slugs", [])
        parts = [f"**Ranked candidates:** {', '.join(candidates)}"]
        parts.append(f"**Top pick:** {spell}")
        parts.append(f"**Why:** {rationale}")
        return "\n\n".join(parts)

    elif task == "spell_refusal":
        refusal = target.get("refusal_reason", "")
        parts = [f"**Refused:** {spell}"]
        if refusal:
            parts.append(f"**Reason:** {refusal}")
        parts.append(f"**Guidance:** {rationale}")
        return "\n\n".join(parts)

    return rationale


def format_chatml(system: str, user: str, assistant_think: str, assistant_answer: str) -> str:
    """Format a single training example as ChatML with <think> block."""
    return (
        f"<|im_start|>system\n{system}<|im_end|>\n"
        f"<|im_start|>user\n{user}<|im_end|>\n"
        f"<|im_start|>assistant\n<think>\n{assistant_think}\n</think>\n\n{assistant_answer}<|im_end|>"
    )


def transform_row(row: dict, rng: random.Random) -> dict | None:
    """Transform a spell-native row into a ChatML training row. Returns None to skip."""
    target = row.get("target", {})
    rationale = target.get("rationale", "")

    # Skip rows with empty rationale — they won't produce useful training signal
    if not rationale.strip():
        return None

    user_instruction = build_user_instruction(row, rng)
    think_block = build_think_block(row)
    assistant_response = build_assistant_response(row, rng)

    text = format_chatml(SYSTEM_PROMPT, user_instruction, think_block, assistant_response)

    return {
        "text": text,
        "row_id": row.get("row_id", ""),
        "task_type": row["task_type"],
        "primary_spell": target.get("primary_spell_slug", ""),
        "source_type": row.get("metadata", {}).get("source_type", ""),
        "category": row.get("metadata", {}).get("category_slug", ""),
    }


def load_and_transform(src_path: Path, rng: random.Random) -> list[dict]:
    """Load spell-native JSONL and transform all rows."""
    rows = []
    skipped = 0
    for line in src_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        raw = json.loads(line)
        transformed = transform_row(raw, rng)
        if transformed is None:
            skipped += 1
            continue
        rows.append(transformed)
    print(f"  {src_path.name}: {len(rows)} transformed, {skipped} skipped")
    return rows


def write_bundle(train_rows: list[dict], eval_rows: list[dict]) -> None:
    """Write the refined training bundle."""
    BUNDLE_DIR.mkdir(parents=True, exist_ok=True)

    for name, rows in [("train.jsonl", train_rows), ("eval.jsonl", eval_rows)]:
        path = BUNDLE_DIR / name
        with open(path, "w", encoding="utf-8") as f:
            for row in rows:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
        print(f"  Wrote {path} ({len(rows)} rows)")

    # Summary
    from collections import Counter
    all_rows = train_rows + eval_rows
    summary = {
        "created": TODAY,
        "source": "spell-native dataset → ChatML instruction/response transform",
        "total_rows": len(all_rows),
        "train_rows": len(train_rows),
        "eval_rows": len(eval_rows),
        "task_types": dict(Counter(r["task_type"] for r in all_rows)),
        "source_types": dict(Counter(r["source_type"] for r in all_rows)),
        "categories": dict(Counter(r["category"] for r in all_rows if r["category"])),
        "format": "ChatML with <think> block, Qwen 3.5 compatible",
        "system_prompt_length": len(SYSTEM_PROMPT),
    }
    summary_path = BUNDLE_DIR / "summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n")
    print(f"  Wrote {summary_path}")

    # Show a sample
    print("\n--- Sample train row (first 500 chars of text) ---")
    print(train_rows[0]["text"][:500])


def main() -> None:
    global BLUEPRINTS
    rng = random.Random(42)

    print("Loading blueprints for rationale enrichment...")
    BLUEPRINTS = load_blueprints()
    print(f"  Loaded {len(BLUEPRINTS['entries'])} entries, {len(BLUEPRINTS['categories'])} category mappings")

    print("Loading and transforming spell-native data...")
    train_rows = load_and_transform(TRAIN_SRC, rng)
    eval_rows = load_and_transform(EVAL_SRC, rng)

    # Inject synthetic refusal rows (Issue 1: augment refusals)
    print("Generating synthetic refusal examples...")
    synthetic_refusals = build_synthetic_refusal_rows()
    refusal_transformed = 0
    for row in synthetic_refusals:
        transformed = transform_row(row, rng)
        if transformed:
            train_rows.append(transformed)
            refusal_transformed += 1
    print(f"  Added {refusal_transformed} synthetic refusal rows to train")

    # Shuffle train rows
    rng.shuffle(train_rows)

    print(f"\nWriting bundle to {BUNDLE_DIR}...")
    write_bundle(train_rows, eval_rows)
    print("\nDone.")


if __name__ == "__main__":
    main()
