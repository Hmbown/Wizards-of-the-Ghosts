---
name: investigation
description: "Use this skill when a problem has clues, but they need to be connected into a causal explanation."
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
# Investigation
Follow evidence through a system until the hidden mechanism becomes legible.
## What This Skill Does
Use this skill when a problem has clues, but they need to be connected into a causal explanation.
In this grimoire, Investigation is treated as a metaphorical skill with a shipping-now delivery profile.
Canonical reference input: Investigation (skill).
## When To Use

- You are debugging a failure, regression, or strange behavior.
- There are logs, traces, docs, or code clues that need synthesis.
- You need the why, not just the what.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Collect the strongest observable clues first.
3. Test causal hypotheses against code, data, logs, or configuration.
4. Eliminate weak explanations and keep the chain of reasoning tight.
5. Return the most defensible explanation plus the next decisive check.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A ranked set of causes with evidence.
- The most likely root cause.
- A next-step validation or fix path.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Do not confuse correlation with cause.
- Keep evidence and inference visibly separate.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/investigation follow the clues here and tell me the most likely root cause with evidence
```
