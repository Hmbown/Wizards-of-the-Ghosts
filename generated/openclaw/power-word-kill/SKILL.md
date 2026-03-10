---
name: power-word-kill
description: "In D&D, Power Word Kill instantly destroys any creature below a hit-point threshold — no saving throw, no resistance, just death. The real-world version is kill -9: the unconditional termination signal. Emergency circuit breakers. Hard account terminations. The nuclear option that exists because sometimes graceful shutdown is not available and the cost of continuing is worse than the cost of data loss. Power Word Kill is not elegant. It is not kind. It is the thing you reach for when everything else has already failed."
user-invocable: true
---

# Power Word Kill

End a process instantly. No negotiation, no cleanup, no save state.

## Overview

Power Word Kill is interpreted here as a hybrid spell with a shipping-now execution model.

Canonical source: Power Word Kill (spell)

Provider target: OpenClaw

## When To Use

- A process, service, or system must stop immediately and graceful shutdown is not available or has already failed.
- The cost of the system continuing to run exceeds the cost of abrupt termination and potential data loss.
- An emergency requires instant action — a runaway process, a security breach in progress, a cascading failure.

## Workflow

1. Confirm the target is correct. Power Word Kill has no undo.
2. Verify that graceful alternatives (SIGTERM, drain, decommission) have been attempted or are not viable.
3. Execute the hard kill: process termination, circuit breaker trip, account lock, or emergency shutdown.
4. Immediately assess blast radius: what downstream systems were affected, what state was lost, what needs recovery.
5. Document what happened and why the hard kill was necessary — this is your incident report seed.

## Deliverables

- Confirmation that the target has been terminated.
- A blast-radius assessment: what was lost, what was affected, what needs recovery.
- An incident seed documenting the kill decision and its justification.

## Guardrails

- Power Word Kill is for emergencies. If you have time to do a graceful shutdown, you have time to use a different spell.
- Never kill a process you do not own or have explicit authorization to terminate.
- Always document the kill. Unexplained hard terminations are how organizations lose trust in their own systems.
- If the target is a person's account or access, this requires human authorization — an AI should never unilaterally terminate a human's access.

## Default Invocation

Use $power-word-kill to immediately terminate a process or system that cannot be shut down gracefully. Confirm the target, verify alternatives are exhausted, execute, and assess blast radius.

