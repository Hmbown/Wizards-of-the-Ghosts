---
name: hold-monster
description: "Hold Monster is Hold Person scaled to larger targets. The real-world version is the emergency circuit breaker: halting an entire service, freezing a deployment pipeline, or stopping a runaway process at the infrastructure level. This is the big red button — it stops everything, and it should only be pressed when the alternative is worse."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - prototype
      - hybrid
      - influence-and-behavior
      - influence
      - behavior
      - attention
      - engagement
---
# Hold Monster
Freeze a large-scale system or service as an emergency circuit breaker.
## What This Skill Does
Hold Monster is Hold Person scaled to larger targets. The real-world version is the emergency circuit breaker: halting an entire service, freezing a deployment pipeline, or stopping a runaway process at the infrastructure level. This is the big red button — it stops everything, and it should only be pressed when the alternative is worse.
In this grimoire, Hold Monster is treated as a hybrid spell with a prototype delivery profile.
Canonical reference input: Hold Monster (spell).
## When To Use

- A system-wide emergency requires an immediate halt: runaway costs, cascading failures, or data integrity threats.
- You need to design a circuit breaker or emergency stop mechanism for a large-scale system.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Assess the emergency: what is happening, how fast, and what is the blast radius if unchecked?
3. Determine the freeze scope: what can be stopped safely vs. what must keep running even in an emergency.
4. Activate the circuit breaker with explicit logging and notification.
5. Define the recovery plan: how to restore service safely after the emergency is resolved.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A circuit breaker specification: what stops, what stays running, and what triggers the halt.
- A recovery plan: step-by-step restoration procedure after the emergency.

## Pitfalls / Guardrails

- Call out the glue, permissions, or missing infrastructure before you imply this is fully operational.
- Circuit breakers are for genuine emergencies. Do not use system-wide halts for problems that can be solved with targeted intervention.
- Every circuit breaker must have a recovery plan. Stopping a system without knowing how to restart it is not safety — it is a different kind of failure.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check which parts are concrete actions versus framing, so the user can tell what is real now.
- Check that any missing glue code, permissions, or future work is labeled before the skill is treated as ready.

## Example Invocation
```text
/hold-monster design an emergency circuit breaker for this [system/service/pipeline] with freeze scope and recovery plan
```
