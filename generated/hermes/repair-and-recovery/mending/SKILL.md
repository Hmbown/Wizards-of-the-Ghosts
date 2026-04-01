---
name: mending
description: "Mending is surgical repair of a known-working artifact that has a specific, identifiable break. It is NOT:\n- Triage/diagnosis: If the problem is \"API is throwing 500s, figure out why\" — that's investigation, not mending. Mending requires the break to already be identified.\n- Formatting/cleanup: If the data is correct but looks messy (sort keys, normalize indentation) — that's formatting, not repair.\n- State reset: If a flag is stuck or an alert needs clearing — that's an operational toggle, not a file repair.\n- Refactoring/redesign: If the system is \"fundamentally flawed\" and needs redesign — that's rebuilding, not mending.\n- Comprehensive cleanup: If there are \"years of orphaned records\" across tables — that's a data integrity project, not a surgical fix."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - shipping-now
      - metaphorical
      - repair-and-recovery
      - recovery
      - repair
      - triage
      - stabilization
---
# Mending
Repair a single broken artifact - a config, a file, a build, a migration - without redesigning it.
## What This Skill Does
Mending is surgical repair of a known-working artifact that has a specific, identifiable break. It is NOT:
- Triage/diagnosis: If the problem is "API is throwing 500s, figure out why" — that's investigation, not mending. Mending requires the break to already be identified.
- Formatting/cleanup: If the data is correct but looks messy (sort keys, normalize indentation) — that's formatting, not repair.
- State reset: If a flag is stuck or an alert needs clearing — that's an operational toggle, not a file repair.
- Refactoring/redesign: If the system is "fundamentally flawed" and needs redesign — that's rebuilding, not mending.
- Comprehensive cleanup: If there are "years of orphaned records" across tables — that's a data integrity project, not a surgical fix.
In this grimoire, Mending is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Mending (spell).
## When To Use

- Trigger this spell when the request contains:
- A specific file or artifact named (e.g., .gitignore, docker-compose.yml, Makefile, package.json, migration script, manifest)
- A localized break: syntax error, typo, missing character, wrong reference, indentation issue, unclosed bracket, trailing comma, misspelled key
- Evidence the artifact was working before ("broke yesterday", "was fine last week", "worked before the merge")
- Language like: "just fix", "repair", "fix the typo", "missing semicolon", "broken reference", "indentation error", "without changing"

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Confirm the break is specific and localized — name the exact file, the exact error, and what "working" looked like before.
3. Apply the minimal change that restores the original behavior — fix the typo, add the missing character, correct the reference, move the misplaced directive. Do not improve, modernize, or restructure.
4. Show a before/after diff so the repair is auditable and reversible.
5. If the break reveals a deeper structural problem (e.g., the same typo appears in 12 files, or the config format is fundamentally unsound), report it — do not paper over it with repeated patches.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- The repaired artifact in working condition.
- A before-and-after diff showing exactly what changed.
- A note if the break suggests a deeper structural issue.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Fix the break. Do not redesign. Do not "take the opportunity to clean up."
- If the damage is too extensive for a targeted repair, say so and recommend a larger intervention.
- Preserve the artifact's original design, style, and structure.
- Do not use for: "Diagnose why production is broken" → investigation spell
- Do not use for: "Clean up formatting on this file" → formatting spell
- Do not use for: "Reset this stuck flag/alert" → operational spell
- Do not use for: "Redesign this module from scratch" → refactoring spell
- Do not use for: "Clean up data integrity across all tables" → data project spell

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/mending fix this broken artifact with the smallest repair that restores it to working condition
```
