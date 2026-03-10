---
name: history
description: "In D&D, History recalls significant past events, legendary figures, and ancient knowledge. The real-world version is temporal investigation: git blame across the entire project, reading changelogs to understand why a decision was made, reconstructing the sequence of events that led to a production incident, or understanding organizational context that explains why the code looks the way it does."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - skill
      - shipping-now
      - metaphorical
      - investigation-and-preparation
      - analysis
      - discovery
      - translation
      - preflight
---
# History
Trace how a system, decision, or codebase arrived at its current state.
## What This Skill Does
In D&D, History recalls significant past events, legendary figures, and ancient knowledge. The real-world version is temporal investigation: git blame across the entire project, reading changelogs to understand why a decision was made, reconstructing the sequence of events that led to a production incident, or understanding organizational context that explains why the code looks the way it does.
In this grimoire, History is treated as a metaphorical skill with a shipping-now delivery profile.
Canonical reference input: History (skill).
## When To Use

- You need to understand why something is the way it is — not just what it does, but how it got here.
- A post-mortem or root-cause analysis needs the timeline of events reconstructed.
- Legacy code or legacy decisions need context before you can safely change them.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify what you need the history of: a codebase, a decision, an incident, or an organizational pattern.
3. Reconstruct the timeline: what happened, in what order, and what caused each transition.
4. Identify the key decision points: where could things have gone differently, and why did they go this way?
5. Deliver the historical narrative with a note on which parts are documented and which are reconstructed.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A timeline of the relevant history: events, decisions, and transitions in order.
- Key decision points identified: what was decided, why, and what the alternatives were.
- Context that explains the current state and constrains future changes.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- History is reconstruction, not certainty. Always note where the record is incomplete or ambiguous.
- Do not assume past decisions were wrong just because the current state is problematic. Context matters.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/history trace how this [system/decision/codebase] arrived at its current state. What happened, in what order, and why?
```
