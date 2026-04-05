---
name: history
description: "In D&D, History recalls significant past events, legendary figures, and ancient knowledge. The real-world version is temporal investigation: git blame across the entire project, reading changelogs to understand why a decision was made, reconstructing the sequence of events that led to a production incident, or understanding organizational context that explains why the code looks the way it does."
user-invocable: true
---

# History

Trace how a system, decision, or codebase arrived at its current state.

## Overview

History is interpreted here as a metaphorical skill with a shipping-now execution model.

Canonical source: History (skill)

Provider target: OpenClaw

## When To Use

- You need to understand why something is the way it is — not just what it does, but how it got here.
- A post-mortem or root-cause analysis needs the timeline of events reconstructed.
- Legacy code or legacy decisions need context before you can safely change them.

## Workflow

1. Identify what you need the history of: a codebase, a decision, an incident, or an organizational pattern.
2. Reconstruct the timeline: what happened, in what order, and what caused each transition.
3. Identify the key decision points: where could things have gone differently, and why did they go this way?
4. Deliver the historical narrative with a note on which parts are documented and which are reconstructed.

## Deliverables

- A timeline of the relevant history: events, decisions, and transitions in order.
- Key decision points identified: what was decided, why, and what the alternatives were.
- Context that explains the current state and constrains future changes.

## Guardrails

- History is reconstruction, not certainty. Always note where the record is incomplete or ambiguous.
- Do not assume past decisions were wrong just because the current state is problematic. Context matters.

## Default Invocation

Use $history to trace how this [system/decision/codebase] arrived at its current state. What happened, in what order, and why?

