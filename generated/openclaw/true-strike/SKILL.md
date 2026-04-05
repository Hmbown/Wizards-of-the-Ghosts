---
name: true-strike
description: "Use this spell for preflight certainty: dry runs, validation checks, dependency verification, and rehearsals that make the next deploy, query, or command much more likely to succeed. It trades a little time up front for fewer blind swings and fewer expensive misses."
user-invocable: true
---

# True Strike

Aim once with evidence so the next command lands on the first shot.

## Overview

True Strike is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: True Strike (spell)

Provider target: OpenClaw

## When To Use

- A risky one-shot action should be validated before you fire it.
- A deploy, migration, API call, or command has an expensive miss if it goes wrong.
- You can eliminate common failure modes with a dry run, preflight check, or rehearsal.

## Workflow

1. Identify the decisive action and the miss conditions most likely to ruin it.
2. Run the smallest useful set of validations or rehearsals that prove readiness.
3. Return a go or no-go judgment with the evidence and the uncertainty that remains.

## Deliverables

- A preflight checklist or dry-run result set.
- A go or no-go recommendation for the next action.
- A short list of residual risks after validation.

## Guardrails

- Do not claim certainty when the environment can still change between validation and execution.
- Keep the preflight cheaper than the miss you are trying to avoid.

## Default Invocation

Use $true-strike to preflight this action, tell me whether it is ready to fire, and name the remaining miss chances.

