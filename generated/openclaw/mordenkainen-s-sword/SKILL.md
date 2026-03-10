---
name: mordenkainen-s-sword
description: "Use this spell when you need an autonomous tool with a narrow mandate: a daemon, scheduled worker, watcher, or persistent background agent that repeatedly executes one precise task. It is prototype territory because the hard part is lifecycle control, observability, and safe cancellation, not the single action itself."
user-invocable: true
---

# Mordenkainen’s Sword

Summon a standing process that keeps cutting through one job until dismissed.

## Overview

Mordenkainen’s Sword is interpreted here as a metaphorical spell with a prototype execution model.

Canonical source: Mordenkainen’s Sword (spell)

Provider target: OpenClaw

## When To Use

- You need a long-running background process, scheduled task, or watcher with a single clear mandate.
- A recurring precise action should persist without manual babysitting once it is safely launched.
- The right abstraction is a narrow autonomous worker, not a broad orchestration system.

## Workflow

1. Define the worker's single mandate, cadence, start conditions, and stop conditions.
2. Design the loop for idempotence, observability, safe retries, and deliberate dismissal.
3. Return a runnable spec with lifecycle hooks, failure handling, and operator controls.

## Deliverables

- A daemon, cron, or persistent worker design for the task.
- Lifecycle and cancellation rules for starting, monitoring, and stopping it safely.
- Monitoring, error-recovery, and escalation notes for ongoing operation.

## Guardrails

- Do not give the process broader authority than the single job requires.
- Ensure repeated actions are idempotent or explicitly bounded so persistence does not accumulate damage.

## Default Invocation

Use $mordenkainen-s-sword to design a persistent worker for this single job, including how it starts, reports, and stops.

