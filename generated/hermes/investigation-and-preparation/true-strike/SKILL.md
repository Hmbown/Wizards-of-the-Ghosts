---
name: true-strike
description: "Use this spell for preflight certainty: dry runs, validation checks, dependency verification, and rehearsals that make the next deploy, query, or command much more likely to succeed. It trades a little time up front for fewer blind swings and fewer expensive misses."
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
# True Strike
Aim once with evidence so the next command lands on the first shot.
## What This Skill Does
Use this spell for preflight certainty: dry runs, validation checks, dependency verification, and rehearsals that make the next deploy, query, or command much more likely to succeed. It trades a little time up front for fewer blind swings and fewer expensive misses.
In this grimoire, True Strike is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: True Strike (spell).
## When To Use

- A risky one-shot action should be validated before you fire it.
- A deploy, migration, API call, or command has an expensive miss if it goes wrong.
- You can eliminate common failure modes with a dry run, preflight check, or rehearsal.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify the decisive action and the miss conditions most likely to ruin it.
3. Run the smallest useful set of validations or rehearsals that prove readiness.
4. Return a go or no-go judgment with the evidence and the uncertainty that remains.
5. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A preflight checklist or dry-run result set.
- A go or no-go recommendation for the next action.
- A short list of residual risks after validation.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Do not claim certainty when the environment can still change between validation and execution.
- Keep the preflight cheaper than the miss you are trying to avoid.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/true-strike preflight this action, tell me whether it is ready to fire, and name the remaining miss chances
```
