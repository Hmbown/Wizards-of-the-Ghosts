---
name: hold-monster
description: "Hold Monster is Hold Person scaled to larger targets. The real-world version is the emergency circuit breaker: halting an entire service, freezing a deployment pipeline, or stopping a runaway process at the infrastructure level. This is the big red button — it stops everything, and it should only be pressed when the alternative is worse."
user-invocable: true
---

# Hold Monster

Freeze a large-scale system or service as an emergency circuit breaker.

## Overview

Hold Monster is interpreted here as a hybrid spell with a prototype execution model.

Canonical source: Hold Monster (spell)

Provider target: OpenClaw

## When To Use

- A system-wide emergency requires an immediate halt: runaway costs, cascading failures, or data integrity threats.
- You need to design a circuit breaker or emergency stop mechanism for a large-scale system.

## Workflow

1. Assess the emergency: what is happening, how fast, and what is the blast radius if unchecked?
2. Determine the freeze scope: what can be stopped safely vs. what must keep running even in an emergency.
3. Activate the circuit breaker with explicit logging and notification.
4. Define the recovery plan: how to restore service safely after the emergency is resolved.

## Deliverables

- A circuit breaker specification: what stops, what stays running, and what triggers the halt.
- A recovery plan: step-by-step restoration procedure after the emergency.

## Guardrails

- Circuit breakers are for genuine emergencies. Do not use system-wide halts for problems that can be solved with targeted intervention.
- Every circuit breaker must have a recovery plan. Stopping a system without knowing how to restart it is not safety — it is a different kind of failure.

## Default Invocation

Use $hold-monster to design an emergency circuit breaker for this [system/service/pipeline] with freeze scope and recovery plan.

