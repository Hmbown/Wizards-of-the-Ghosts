---
name: mending
description: "Use this spell when something specific is broken and needs targeted repair, not a refactor or a rebuild."
user-invocable: true
---

# Mending

Repair a single broken artifact - a config, a file, a build, a migration - without redesigning it.

## Overview

Mending is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Mending (spell)

Provider target: OpenClaw

## When To Use

- A config file, build script, migration, or data file has a specific, identifiable break.
- The fix is surgical - you need to repair the damage, not redesign the system.
- The broken artifact was working before and should work again with minimal intervention.

## Workflow

1. Identify the exact break: what is damaged, and what the artifact looked like when it was whole.
2. Determine the minimal repair that restores function without changing the artifact's design.
3. Apply the fix with a clear before-and-after comparison.
4. If the break reveals a deeper structural problem, report it rather than papering over it.

## Deliverables

- The repaired artifact in working condition.
- A before-and-after diff showing exactly what changed.
- A note if the break suggests a deeper structural issue.

## Guardrails

- Mending fixes the break; it does not redesign the object. Resist the urge to improve while repairing.
- If the damage is too extensive for a targeted repair, say so and recommend a larger intervention.

## Default Invocation

Use $mending to fix this broken artifact with the smallest repair that restores it to working condition.

