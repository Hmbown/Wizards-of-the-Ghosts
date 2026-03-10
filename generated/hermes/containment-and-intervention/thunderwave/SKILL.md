---
name: thunderwave
description: "Use this skill for intentionally theatrical or forceful actions, but only behind explicit confirmation and a hard safety boundary."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - prototype
      - literal
      - containment-and-intervention
      - containment
      - intervention
      - disruption
      - safety
---
# Thunderwave
Trigger a dramatic, high-impact action through a tightly gated device, webhook, or automation.
## What This Skill Does
Use this skill for intentionally theatrical or forceful actions, but only behind explicit confirmation and a hard safety boundary.
In this grimoire, Thunderwave is treated as a literal spell with a prototype delivery profile.
Canonical reference input: Thunderwave (spell).
## When To Use

- You want a visible real-world effect such as lights, sounds, signage, or a controlled automation burst.
- A dramatic action is part of the experience, demo, or ritual.
- The blast radius is known and the target surface is intentionally prepared.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify the target device, webhook, or effect surface.
3. Require explicit confirmation of the payload, boundary, and rollback plan.
4. Trigger the effect through the narrowest possible integration.
5. Report exactly what fired and whether rollback is available.
6. Stop for explicit confirmation before taking a live action that changes access, triggers an alert, or touches a real system boundary.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A precise execution plan or payload.
- A clear confirmation checkpoint.
- A rollback or shutdown path when one exists.

## Pitfalls / Guardrails

- Call out the glue, permissions, or missing infrastructure before you imply this is fully operational.
- Never improvise on unverified device integrations or dangerous automations.
- Refuse actions that create real-world safety hazards or uncontrolled side effects.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the exact live target, confirmation gate, and rollback or recovery path are explicit.
- Check that any missing glue code, permissions, or future work is labeled before the skill is treated as ready.

## Example Invocation
```text
/thunderwave design or trigger a tightly scoped dramatic effect, but stop for confirmation before any irreversible action
```
