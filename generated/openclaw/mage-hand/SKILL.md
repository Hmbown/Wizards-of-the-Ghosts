---
name: mage-hand
description: "Use this skill for small, careful remote manipulations where dexterity matters more than force."
user-invocable: true
---

# Mage Hand

Manipulate files, records, and lightweight system state with precision and minimal blast radius.

## Overview

Mage Hand is interpreted here as a hybrid spell with a shipping-now execution model.

Canonical source: Mage Hand (spell)

Provider target: OpenClaw

## When To Use

- You need narrow edits across files, tickets, docs, or structured records.
- You want a delicate helper rather than a broad refactor.
- A task should feel like reaching for an object, not rebuilding the room.

## Workflow

1. Define the exact object to move, change, or inspect.
2. Prefer the smallest tool or edit surface that can complete the task safely.
3. Apply the change with a clear before-and-after diff or state transition.
4. Report what moved, what stayed untouched, and any nearby constraints.

## Deliverables

- A minimal, well-scoped change.
- A short audit trail of touched surfaces.
- A note on adjacent objects that were intentionally left alone.

## Guardrails

- Avoid broad destructive actions when a surgical edit is sufficient.
- Preserve user work and unrelated state.

## Default Invocation

Use $mage-hand to make the smallest safe change needed here and show exactly what you touched.

