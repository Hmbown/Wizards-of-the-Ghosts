---
name: identify
description: "Use this skill when the object is in front of you but its function, constraints, or provenance are unclear."
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
# Identify
Explain what a mysterious file, service, workflow, or artifact actually does.
## What This Skill Does
Use this skill when the object is in front of you but its function, constraints, or provenance are unclear.
In this grimoire, Identify is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Identify (spell).
## When To Use

- A script, config file, model, or service exists but its purpose is opaque.
- You need the contract of an artifact before you rely on it.
- You want the shortest path from mystery to operational understanding.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Inspect the artifact directly before speculating.
3. Infer purpose from structure, dependencies, naming, and runtime touchpoints.
4. Separate confirmed behavior, likely behavior, and unknowns.
5. Return usage notes, hazards, and the safest next validation step.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A plain-English explanation of the artifact.
- Inputs, outputs, dependencies, and side effects when known.
- A confidence-rated list of unknowns.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Do not overstate certainty when the object cannot be fully validated.
- Prefer source-backed explanation over lore.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/identify Use $identify on this file, tool, or service and tell me what it does, what it touches, and what we still do not know
```
