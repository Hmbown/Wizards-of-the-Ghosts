---
name: foresight
description: "Use this skill when you need a bounded forecast with explicit uncertainty, not mystical certainty."
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
      - investigation-and-preparation
      - analysis
      - discovery
      - translation
      - preflight
---
# Foresight
Estimate likely outcomes before committing to a plan, change, or launch.
## What This Skill Does
Use this skill when you need a bounded forecast with explicit uncertainty, not mystical certainty.
In this grimoire, Foresight is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Foresight (spell).
## When To Use

- You are choosing between options and want risk-weighted guidance.
- A launch, refactor, or experiment has meaningful downside.
- You need a quick 'weal or woe' style call with evidence.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Define the decision and the time horizon that matters.
3. List the strongest upside and downside paths.
4. Estimate outcome likelihoods from current evidence rather than vibes.
5. Return the recommendation, the confidence level, and the trigger that would change the call.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A recommendation with confidence and assumptions.
- A short risk matrix.
- A set of decisive unknowns to resolve next.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Do not present forecasts as certainty.
- Do not confuse missing evidence with positive evidence.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/foresight evaluate this decision, give me the likely upside and downside, and tell me what would change your call
```
