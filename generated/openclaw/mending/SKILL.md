---
name: mending
description: "Mending is surgical repair of a known-working artifact that has a specific, identifiable break. It is NOT:\n- Triage/diagnosis: If the problem is \"API is throwing 500s, figure out why\" — that's investigation, not mending. Mending requires the break to already be identified.\n- Formatting/cleanup: If the data is correct but looks messy (sort keys, normalize indentation) — that's formatting, not repair.\n- State reset: If a flag is stuck or an alert needs clearing — that's an operational toggle, not a file repair.\n- Refactoring/redesign: If the system is \"fundamentally flawed\" and needs redesign — that's rebuilding, not mending.\n- Comprehensive cleanup: If there are \"years of orphaned records\" across tables — that's a data integrity project, not a surgical fix."
user-invocable: true
---

# Mending

Repair a single broken artifact - a config, a file, a build, a migration - without redesigning it.

## Overview

Mending is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Mending (spell)

Provider target: OpenClaw

## When To Use

- Trigger this spell when the request contains:
- A specific file or artifact named (e.g., .gitignore, docker-compose.yml, Makefile, package.json, migration script, manifest)
- A localized break: syntax error, typo, missing character, wrong reference, indentation issue, unclosed bracket, trailing comma, misspelled key
- Evidence the artifact was working before ("broke yesterday", "was fine last week", "worked before the merge")
- Language like: "just fix", "repair", "fix the typo", "missing semicolon", "broken reference", "indentation error", "without changing"

## Workflow

1. Confirm the break is specific and localized — name the exact file, the exact error, and what "working" looked like before.
2. Apply the minimal change that restores the original behavior — fix the typo, add the missing character, correct the reference, move the misplaced directive. Do not improve, modernize, or restructure.
3. Show a before/after diff so the repair is auditable and reversible.
4. If the break reveals a deeper structural problem (e.g., the same typo appears in 12 files, or the config format is fundamentally unsound), report it — do not paper over it with repeated patches.

## Deliverables

- The repaired artifact in working condition.
- A before-and-after diff showing exactly what changed.
- A note if the break suggests a deeper structural issue.

## Guardrails

- Fix the break. Do not redesign. Do not "take the opportunity to clean up."
- If the damage is too extensive for a targeted repair, say so and recommend a larger intervention.
- Preserve the artifact's original design, style, and structure.
- Do not use for: "Diagnose why production is broken" → investigation spell
- Do not use for: "Clean up formatting on this file" → formatting spell
- Do not use for: "Reset this stuck flag/alert" → operational spell
- Do not use for: "Redesign this module from scratch" → refactoring spell
- Do not use for: "Clean up data integrity across all tables" → data project spell

## Default Invocation

Use $mending to fix this broken artifact with the smallest repair that restores it to working condition.

