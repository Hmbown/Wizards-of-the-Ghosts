---
name: mage-hand
description: "Use this skill for small, careful remote manipulations where dexterity matters more than force."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - shipping-now
      - hybrid
      - actions-access-and-automation
      - execution
      - automation
      - access
      - actuation
---
# Mage Hand
Manipulate files, records, and lightweight system state with precision and minimal blast radius.
## Sigil

```text
     __
  .-'  `-.
 /  .--.  \\
|  / /\\ \\ |
|  | \\/ | |
 \\  `--'  /
  `-.__.-'
```

## What This Skill Does
Use this skill for small, careful remote manipulations where dexterity matters more than force.
In this grimoire, Mage Hand is treated as a hybrid spell with a shipping-now delivery profile.
Canonical reference input: Mage Hand (spell).
## When To Use

- You need narrow edits across files, tickets, docs, or structured records.
- You want a delicate helper rather than a broad refactor.
- A task should feel like reaching for an object, not rebuilding the room.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Define the exact object to move, change, or inspect.
3. Prefer the smallest tool or edit surface that can complete the task safely.
4. Apply the change with a clear before-and-after diff or state transition.
5. Report what moved, what stayed untouched, and any nearby constraints.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A minimal, well-scoped change.
- A short audit trail of touched surfaces.
- A note on adjacent objects that were intentionally left alone.

## Pitfalls / Guardrails

- Keep the theatrical framing, but name the concrete mechanism that makes the skill useful right now.
- Avoid broad destructive actions when a surgical edit is sufficient.
- Preserve user work and unrelated state.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check which parts are concrete actions versus framing, so the user can tell what is real now.

## Example Invocation
```text
/mage-hand make the smallest safe change needed here and show exactly what you touched
```
