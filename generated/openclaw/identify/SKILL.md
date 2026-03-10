---
name: identify
description: "Use this skill when the object is in front of you but its function, constraints, or provenance are unclear."
user-invocable: true
---

# Identify

Explain what a mysterious file, service, workflow, or artifact actually does.

## Overview

Identify is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Identify (spell)

Provider target: OpenClaw

## When To Use

- A script, config file, model, or service exists but its purpose is opaque.
- You need the contract of an artifact before you rely on it.
- You want the shortest path from mystery to operational understanding.

## Workflow

1. Inspect the artifact directly before speculating.
2. Infer purpose from structure, dependencies, naming, and runtime touchpoints.
3. Separate confirmed behavior, likely behavior, and unknowns.
4. Return usage notes, hazards, and the safest next validation step.

## Deliverables

- A plain-English explanation of the artifact.
- Inputs, outputs, dependencies, and side effects when known.
- A confidence-rated list of unknowns.

## Guardrails

- Do not overstate certainty when the object cannot be fully validated.
- Prefer source-backed explanation over lore.

## Default Invocation

Use $identify on this file, tool, or service and tell me what it does, what it touches, and what we still do not know.

