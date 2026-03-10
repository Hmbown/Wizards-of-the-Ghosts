---
name: sleight-of-hand
description: "Use this skill for surgical edits: a one-line patch, a targeted regex, a delicate config tweak, or a precise text substitution with low blast radius. The emphasis is finesse under magnification, where touching one wrong character can create a new incident."
user-invocable: true
---

# Sleight of Hand

Make the tiny exact change that fixes the problem without disturbing the room.

## Overview

Sleight of Hand is interpreted here as a metaphorical skill with a shipping-now execution model.

Canonical source: Sleight of Hand (skill)

Provider target: OpenClaw

## When To Use

- A hotfix needs to touch the minimum possible surface area.
- A refactor is too risky, but an exact micro-edit can solve the immediate problem.
- The change depends on exact matching, previewing, and rollback discipline.

## Workflow

1. Isolate the smallest safe surface that can carry the fix.
2. Stage the edit with exact-match checks and a before-and-after verification pass.
3. Return the minimal diff, the confidence check, and the rollback cue.

## Deliverables

- A targeted patch, replacement pattern, or edit instruction.
- Proof of what changed and what was intentionally left alone.
- A rollback note in case the tiny move still misfires.

## Guardrails

- Never run blind global replacements when the match surface is ambiguous.
- Preserve neighboring behavior and formatting unless the fix explicitly requires otherwise.

## Default Invocation

Use $sleight-of-hand to make the smallest safe edit here and show me exactly what moved.

