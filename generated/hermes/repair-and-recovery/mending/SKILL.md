---
name: mending
description: "Use this spell when something specific is broken and needs targeted repair, not a refactor or a rebuild."
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
Use this spell when something specific is broken and needs targeted repair, not a refactor or a rebuild.
In this grimoire, Mending is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Mending (spell).
## When To Use

- A config file, build script, migration, or data file has a specific, identifiable break.
- The fix is surgical - you need to repair the damage, not redesign the system.
- The broken artifact was working before and should work again with minimal intervention.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify the exact break: what is damaged, and what the artifact looked like when it was whole.
3. Determine the minimal repair that restores function without changing the artifact's design.
4. Apply the fix with a clear before-and-after comparison.
5. If the break reveals a deeper structural problem, report it rather than papering over it.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- The repaired artifact in working condition.
- A before-and-after diff showing exactly what changed.
- A note if the break suggests a deeper structural issue.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Mending fixes the break; it does not redesign the object. Resist the urge to improve while repairing.
- If the damage is too extensive for a targeted repair, say so and recommend a larger intervention.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/mending fix this broken artifact with the smallest repair that restores it to working condition
```
