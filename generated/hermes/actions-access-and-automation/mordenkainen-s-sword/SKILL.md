---
name: mordenkainen-s-sword
description: "Use this spell when you need an autonomous tool with a narrow mandate: a daemon, scheduled worker, watcher, or persistent background agent that repeatedly executes one precise task. It is prototype territory because the hard part is lifecycle control, observability, and safe cancellation, not the single action itself."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - prototype
      - metaphorical
      - actions-access-and-automation
      - execution
      - automation
      - access
      - actuation
---
# Mordenkainen’s Sword
Summon a standing process that keeps cutting through one job until dismissed.
## What This Skill Does
Use this spell when you need an autonomous tool with a narrow mandate: a daemon, scheduled worker, watcher, or persistent background agent that repeatedly executes one precise task. It is prototype territory because the hard part is lifecycle control, observability, and safe cancellation, not the single action itself.
In this grimoire, Mordenkainen’s Sword is treated as a metaphorical spell with a prototype delivery profile.
Canonical reference input: Mordenkainen’s Sword (spell).
## When To Use

- You need a long-running background process, scheduled task, or watcher with a single clear mandate.
- A recurring precise action should persist without manual babysitting once it is safely launched.
- The right abstraction is a narrow autonomous worker, not a broad orchestration system.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Define the worker's single mandate, cadence, start conditions, and stop conditions.
3. Design the loop for idempotence, observability, safe retries, and deliberate dismissal.
4. Return a runnable spec with lifecycle hooks, failure handling, and operator controls.
5. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A daemon, cron, or persistent worker design for the task.
- Lifecycle and cancellation rules for starting, monitoring, and stopping it safely.
- Monitoring, error-recovery, and escalation notes for ongoing operation.

## Pitfalls / Guardrails

- Call out the glue, permissions, or missing infrastructure before you imply this is fully operational.
- Do not give the process broader authority than the single job requires.
- Ensure repeated actions are idempotent or explicitly bounded so persistence does not accumulate damage.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.
- Check that any missing glue code, permissions, or future work is labeled before the skill is treated as ready.

## Example Invocation
```text
/mordenkainen-s-sword design a persistent worker for this single job, including how it starts, reports, and stops
```
