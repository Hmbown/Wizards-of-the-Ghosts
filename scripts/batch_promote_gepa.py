#!/usr/bin/env python3
"""
Batch GEPA Promotion Script
Reads optimized_instruction from each spell's optimization_status.json,
intelligently parses it into structured fields, writes promotion_patch.json,
runs the promote script, and reports results.
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
GEPA_SPELLS_DIR = REPO_ROOT / "catalog" / "gepa" / "spells"
BLUEPRINTS_PATH = REPO_ROOT / "catalog" / "blueprints.json"

# Section header patterns that map to blueprint fields
# These are regex patterns that match various ways the optimized instructions
# label their sections
WHEN_TO_USE_PATTERNS = [
    r"activation\s+signals?",
    r"trigger\s+signals?",
    r"when\s+to\s+activate",
    r"activate\s+when",
    r"activate\s+this\s+spell\s+when",
    r"activation\s+triggers?",
    r"when\s+this\s+spell\s+fits",
    r"activation\s+language",
]

ANTI_PATTERN_PATTERNS = [
    r"anti[-\s]?patterns?",
    r"when\s+not\s+to\s+activate",
    r"do\s+not\s+(route|activate|use|trigger)",
    r"explicit\s+anti[-\s]?patterns",
    r"what\s+this\s+spell\s+is\s+not",
    r"never\s+activate",
    r"not\s+\w+\s*\(confusable",
    r"confusable",
    r"when\s+not\s+to\s+activate",
    r"this\s+is\s+not",
    r"this\s+spell\s+is\s+not",
]

WORKFLOW_PATTERNS = [
    r"^workflow",
    r"required\s+workflow",
    r"core\s+workflow",
    r"follow\s+these\s+steps",
]

GUARDRAIL_PATTERNS = [
    r"^guardrails?",
    r"stop\s+conditions?",
    r"key\s+constraints?",
    r"reality\s+boundary",
]

DELIVERABLE_PATTERNS = [
    r"^deliverables?",
    r"output\s+requirements?",
    r"output\s+format",
    r"output\s+contract",
    r"deliverable\s+format",
]

DESCRIPTION_PATTERNS = [
    r"core\s+identity",
    r"core\s+concept",
    r"core\s+distinction",
    r"what\s+makes\s+this\s+spell\s+different",
    r"key\s+differentiator",
    r"key\s+distinction",
    r"^identity$",
]


def load_blueprints():
    return json.loads(BLUEPRINTS_PATH.read_text(encoding="utf-8"))


def get_entry(blueprints, slug):
    for e in blueprints["entries"]:
        if e["slug"] == slug:
            return e
    return None


def split_into_sections(text):
    """Split markdown text into sections based on ## headers or **BOLD** headers."""
    # Find all section boundaries: ## headers or standalone **bold** headers
    # We'll use a pattern that matches both ## Header and **Header** at line start
    section_pattern = re.compile(
        r'^(?:#{1,4}\s+(.+?)(?:\s*$))|(?:^\*\*([A-Z][^*]{3,})\*\*\s*$)',
        re.MULTILINE
    )

    sections = []
    matches = list(section_pattern.finditer(text))

    if not matches:
        # No clear sections, return the whole thing
        return [("full", text)]

    # Content before first header
    if matches[0].start() > 0:
        preamble = text[:matches[0].start()].strip()
        if preamble:
            sections.append(("preamble", preamble))

    for i, match in enumerate(matches):
        header = (match.group(1) or match.group(2) or "").strip()
        # Remove trailing colons, em-dashes, etc
        header = re.sub(r'[\s:—–-]+$', '', header)
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end].strip()
        sections.append((header, body))

    return sections


def classify_section(header):
    """Classify a section header into a blueprint field category."""
    h = header.lower().strip()

    for pattern in WHEN_TO_USE_PATTERNS:
        if re.search(pattern, h, re.IGNORECASE):
            return "when_to_use"

    for pattern in ANTI_PATTERN_PATTERNS:
        if re.search(pattern, h, re.IGNORECASE):
            return "guardrails_anti"

    for pattern in WORKFLOW_PATTERNS:
        if re.search(pattern, h, re.IGNORECASE):
            return "workflow"

    for pattern in GUARDRAIL_PATTERNS:
        if re.search(pattern, h, re.IGNORECASE):
            return "guardrails"

    for pattern in DELIVERABLE_PATTERNS:
        if re.search(pattern, h, re.IGNORECASE):
            return "deliverables"

    for pattern in DESCRIPTION_PATTERNS:
        if re.search(pattern, h, re.IGNORECASE):
            return "description"

    return "unknown"


def extract_bullet_items(text):
    """Extract bullet/numbered list items from text, preserving content."""
    items = []
    # Match lines starting with -, *, or numbered lists
    lines = text.split('\n')
    current_item = None

    for line in lines:
        stripped = line.strip()
        if not stripped:
            if current_item:
                items.append(current_item.strip())
                current_item = None
            continue

        # Check if it's a new bullet/numbered item
        bullet_match = re.match(r'^(?:[-*•]\s+|\d+\.\s+)(.*)', stripped)
        if bullet_match:
            if current_item:
                items.append(current_item.strip())
            current_item = bullet_match.group(1)
        elif current_item is not None:
            # Continuation of previous item
            current_item += " " + stripped
        else:
            # Non-bullet text, could be a paragraph
            # Only add if it looks meaningful (not just a header-like line)
            if len(stripped) > 20 and not stripped.startswith('#') and not stripped.startswith('**'):
                if current_item:
                    items.append(current_item.strip())
                current_item = stripped

    if current_item:
        items.append(current_item.strip())

    # Clean up items - remove markdown bold/italic
    cleaned = []
    for item in items:
        item = re.sub(r'\*\*([^*]+)\*\*', r'\1', item)  # Bold
        item = re.sub(r'\*([^*]+)\*', r'\1', item)        # Italic
        item = re.sub(r'`([^`]+)`', r'\1', item)          # Code
        item = item.strip()
        if item and len(item) > 5:
            cleaned.append(item)

    return cleaned


def extract_trigger_phrases(text):
    """Extract trigger phrases from text with quoted or comma-separated lists."""
    # Find quoted phrases
    quoted = re.findall(r'"([^"]+)"', text)
    if quoted:
        return quoted

    # Try to find comma-separated items in quote blocks
    quoted2 = re.findall(r'["""]([^"""]+)["""]', text)
    if quoted2:
        return quoted2

    return []


def parse_optimized_instruction(slug, instruction, existing_entry):
    """Parse an optimized instruction into structured blueprint fields."""
    if not instruction or len(instruction) < 100:
        return None

    sections = split_into_sections(instruction)

    # Accumulate content by category
    when_to_use_content = []
    anti_pattern_content = []
    workflow_content = []
    guardrail_content = []
    deliverable_content = []
    description_parts = []

    for header, body in sections:
        category = classify_section(header)

        if category == "when_to_use":
            when_to_use_content.append(body)
        elif category == "guardrails_anti":
            anti_pattern_content.append(body)
        elif category == "workflow":
            workflow_content.append(body)
        elif category == "guardrails":
            guardrail_content.append(body)
        elif category == "deliverables":
            deliverable_content.append(body)
        elif category == "description":
            description_parts.append(body)

    updated_fields = {}

    # --- when_to_use ---
    when_items = []
    for content in when_to_use_content:
        items = extract_bullet_items(content)
        when_items.extend(items)
        # Also extract trigger phrases
        triggers = extract_trigger_phrases(content)
        for t in triggers:
            phrase = f'User says "{t}" or similar'
            if phrase not in when_items and len(when_items) < 12:
                pass  # Don't add raw trigger phrases, they're too granular

    if when_items:
        # Limit to 8 items, prioritize longer/more specific ones
        when_items = [item for item in when_items if len(item) > 10][:8]
        if when_items:
            updated_fields["when_to_use"] = when_items

    # --- guardrails (combine guardrails + anti-patterns) ---
    guardrail_items = []
    for content in guardrail_content:
        items = extract_bullet_items(content)
        guardrail_items.extend(items)

    anti_items = []
    for content in anti_pattern_content:
        items = extract_bullet_items(content)
        anti_items.extend(items)

    # Prefix anti-pattern items to make them guardrail-style
    for item in anti_items:
        if not item.lower().startswith("do not") and not item.lower().startswith("never"):
            item = f"Do not use for: {item}"
        guardrail_items.append(item)

    if guardrail_items:
        guardrail_items = [item for item in guardrail_items if len(item) > 10][:10]
        if guardrail_items:
            updated_fields["guardrails"] = guardrail_items

    # --- workflow ---
    workflow_items = []
    for content in workflow_content:
        items = extract_bullet_items(content)
        workflow_items.extend(items)

    if workflow_items:
        workflow_items = [item for item in workflow_items if len(item) > 10][:8]
        if workflow_items:
            updated_fields["workflow"] = workflow_items

    # --- deliverables ---
    deliverable_items = []
    for content in deliverable_content:
        items = extract_bullet_items(content)
        deliverable_items.extend(items)

    if deliverable_items:
        deliverable_items = [item for item in deliverable_items if len(item) > 10][:6]
        if deliverable_items:
            updated_fields["deliverables"] = deliverable_items

    # --- description ---
    if description_parts:
        # Take the first description section, clean it up
        desc = description_parts[0]
        # Take first paragraph or two
        paragraphs = [p.strip() for p in desc.split('\n\n') if p.strip()]
        if paragraphs:
            desc_text = ' '.join(paragraphs[:2])
            # Clean markdown
            desc_text = re.sub(r'\*\*([^*]+)\*\*', r'\1', desc_text)
            desc_text = re.sub(r'\*([^*]+)\*', r'\1', desc_text)
            desc_text = re.sub(r'`([^`]+)`', r'\1', desc_text)
            desc_text = desc_text.strip()
            if len(desc_text) > 50 and desc_text != existing_entry.get("description", ""):
                updated_fields["description"] = desc_text

    return updated_fields if updated_fields else None


def parse_flat_instruction(slug, instruction, existing_entry):
    """Parse instructions that follow the flat 'When this spell fits:' format."""
    updated_fields = {}

    # Extract "When this spell fits:" section
    when_match = re.search(
        r'When this spell fits:\s*\n((?:[-*]\s+.+\n?)+)',
        instruction, re.MULTILINE
    )
    if when_match:
        items = extract_bullet_items(when_match.group(1))
        if items:
            updated_fields["when_to_use"] = items[:8]

    # Extract "Expected workflow elements:" section
    workflow_match = re.search(
        r'Expected workflow elements:\s*\n((?:[-*]\s+.+\n?)+)',
        instruction, re.MULTILINE
    )
    if workflow_match:
        items = extract_bullet_items(workflow_match.group(1))
        if items:
            updated_fields["workflow"] = items[:8]

    # Extract "Expected deliverables:" section
    deliv_match = re.search(
        r'Expected deliverables:\s*\n((?:[-*]\s+.+\n?)+)',
        instruction, re.MULTILINE
    )
    if deliv_match:
        items = extract_bullet_items(deliv_match.group(1))
        if items:
            updated_fields["deliverables"] = items[:6]

    # Extract "Guardrails that must remain visible:" section
    guard_match = re.search(
        r'Guardrails that must remain visible:\s*\n((?:[-*]\s+.+\n?)+)',
        instruction, re.MULTILINE
    )
    if guard_match:
        items = extract_bullet_items(guard_match.group(1))
        if items:
            updated_fields["guardrails"] = items[:10]

    return updated_fields if updated_fields else None


def write_promotion_patch(slug, updated_fields, spell_dir):
    """Write the promotion_patch.json file."""
    patch = {
        "slug": slug,
        "reason": "GEPA manual optimization via Qwen 3.6",
        "updated_fields": updated_fields
    }
    patch_path = spell_dir / "promotion_patch.json"
    patch_path.write_text(
        json.dumps(patch, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8"
    )
    return patch_path


def run_promote_script(slug):
    """Run the promotion script for a spell. Returns (success, output)."""
    try:
        result = subprocess.run(
            [
                str(REPO_ROOT / ".venv" / "bin" / "python"),
                str(REPO_ROOT / "scripts" / "gepa_promote_spell.py"),
                "--repo-root", str(REPO_ROOT),
                "--slug", slug,
            ],
            capture_output=True, text=True, timeout=30,
            cwd=str(REPO_ROOT),
            env={**os.environ, "PYTHONPATH": str(REPO_ROOT / "scripts")}
        )
        if result.returncode == 0:
            return True, result.stdout.strip()
        else:
            return False, (result.stderr or result.stdout).strip()
    except Exception as e:
        return False, str(e)


def direct_promote(slug, updated_fields):
    """Directly apply promotion to blueprints.json (for skills or when script fails)."""
    blueprints = load_blueprints()
    entry = get_entry(blueprints, slug)
    if not entry:
        return False, f"Entry {slug} not found in blueprints.json"

    for field, value in updated_fields.items():
        if field == "openai":
            entry.setdefault("openai", {})
            entry["openai"].update(value)
        else:
            entry[field] = value

    BLUEPRINTS_PATH.write_text(
        json.dumps(blueprints, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8"
    )
    return True, f"Directly promoted {slug} (kind={entry['kind']})"


def main():
    print("=" * 70)
    print("GEPA Batch Promotion Script")
    print("=" * 70)

    blueprints = load_blueprints()

    # Collect all spells with optimization_status.json
    spell_dirs = sorted(GEPA_SPELLS_DIR.iterdir())
    slugs = []
    for d in spell_dirs:
        status_path = d / "optimization_status.json"
        if status_path.exists():
            slugs.append(d.name)

    print(f"\nFound {len(slugs)} spell workspaces with optimization_status.json")

    results = {
        "promoted": [],
        "skipped": [],
        "failed": [],
        "direct_promoted": [],
    }
    field_changes = {}  # slug -> list of changed fields

    for slug in slugs:
        spell_path = GEPA_SPELLS_DIR / slug
        status_path = spell_path / "optimization_status.json"

        print(f"\n--- Processing: {slug} ---")

        try:
            status = json.loads(status_path.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"  ERROR reading status: {e}")
            results["failed"].append((slug, str(e)))
            continue

        instruction = status.get("optimized_instruction", "")
        if not instruction or len(instruction) < 50:
            print(f"  SKIP: No optimized instruction (or too short)")
            results["skipped"].append((slug, "no instruction"))
            continue

        entry = get_entry(blueprints, slug)
        if not entry:
            print(f"  SKIP: Not found in blueprints.json")
            results["skipped"].append((slug, "not in blueprints"))
            continue

        # Try structured parse first, then flat format
        updated_fields = parse_optimized_instruction(slug, instruction, entry)
        if not updated_fields:
            updated_fields = parse_flat_instruction(slug, instruction, entry)

        if not updated_fields:
            print(f"  SKIP: Could not extract structured fields from instruction")
            results["skipped"].append((slug, "no extractable fields"))
            continue

        # Write promotion patch
        patch_path = write_promotion_patch(slug, updated_fields, spell_path)
        print(f"  Wrote promotion_patch.json with fields: {sorted(updated_fields.keys())}")

        # Count items per field
        for field, value in updated_fields.items():
            if isinstance(value, list):
                print(f"    {field}: {len(value)} items")
            else:
                print(f"    {field}: (string, {len(str(value))} chars)")

        # Try the promote script
        is_skill = entry.get("kind") != "spell"

        if is_skill:
            print(f"  Entry is kind={entry['kind']}, using direct promotion...")
            ok, msg = direct_promote(slug, updated_fields)
            if ok:
                print(f"  OK: {msg}")
                results["direct_promoted"].append(slug)
                field_changes[slug] = sorted(updated_fields.keys())
                # Reload blueprints after direct write
                blueprints = load_blueprints()
            else:
                print(f"  FAIL: {msg}")
                results["failed"].append((slug, msg))
        else:
            ok, msg = run_promote_script(slug)
            if ok:
                print(f"  PROMOTED via script")
                results["promoted"].append(slug)
                field_changes[slug] = sorted(updated_fields.keys())
                # Reload blueprints after promotion
                blueprints = load_blueprints()
            else:
                print(f"  Script failed: {msg}")
                print(f"  Falling back to direct promotion...")
                ok2, msg2 = direct_promote(slug, updated_fields)
                if ok2:
                    print(f"  OK (direct): {msg2}")
                    results["direct_promoted"].append(slug)
                    field_changes[slug] = sorted(updated_fields.keys())
                    blueprints = load_blueprints()
                else:
                    print(f"  FAIL (direct): {msg2}")
                    results["failed"].append((slug, f"script: {msg}, direct: {msg2}"))

    # Summary
    print("\n" + "=" * 70)
    print("PROMOTION SUMMARY")
    print("=" * 70)
    print(f"  Promoted via script:  {len(results['promoted'])}")
    print(f"  Promoted directly:    {len(results['direct_promoted'])}")
    print(f"  Skipped:              {len(results['skipped'])}")
    print(f"  Failed:               {len(results['failed'])}")
    total = len(results['promoted']) + len(results['direct_promoted'])
    print(f"  TOTAL PROMOTED:       {total}/{len(slugs)}")

    if results["promoted"]:
        print(f"\n  Via script: {', '.join(results['promoted'])}")
    if results["direct_promoted"]:
        print(f"\n  Via direct: {', '.join(results['direct_promoted'])}")
    if results["skipped"]:
        print(f"\n  Skipped:")
        for slug, reason in results["skipped"]:
            print(f"    {slug}: {reason}")
    if results["failed"]:
        print(f"\n  Failed:")
        for slug, reason in results["failed"]:
            print(f"    {slug}: {reason}")

    # Field change summary
    print(f"\n  Field changes by spell:")
    for slug in sorted(field_changes.keys()):
        print(f"    {slug}: {field_changes[slug]}")

    # Count total field changes
    all_fields = {}
    for fields in field_changes.values():
        for f in fields:
            all_fields[f] = all_fields.get(f, 0) + 1
    print(f"\n  Fields changed across all spells:")
    for f in sorted(all_fields.keys()):
        print(f"    {f}: {all_fields[f]} spells")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
