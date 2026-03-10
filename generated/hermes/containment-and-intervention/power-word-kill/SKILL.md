---
name: power-word-kill
description: "In D&D, Power Word Kill instantly destroys any creature below a hit-point threshold — no saving throw, no resistance, just death. The real-world version is kill -9: the unconditional termination signal. Emergency circuit breakers. Hard account terminations. The nuclear option that exists because sometimes graceful shutdown is not available and the cost of continuing is worse than the cost of data loss. Power Word Kill is not elegant. It is not kind. It is the thing you reach for when everything else has already failed."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - shipping-now
      - hybrid
      - containment-and-intervention
      - containment
      - intervention
      - disruption
      - safety
---
# Power Word Kill
End a process instantly. No negotiation, no cleanup, no save state.
## What This Skill Does
In D&D, Power Word Kill instantly destroys any creature below a hit-point threshold — no saving throw, no resistance, just death. The real-world version is kill -9: the unconditional termination signal. Emergency circuit breakers. Hard account terminations. The nuclear option that exists because sometimes graceful shutdown is not available and the cost of continuing is worse than the cost of data loss. Power Word Kill is not elegant. It is not kind. It is the thing you reach for when everything else has already failed.
In this grimoire, Power Word Kill is treated as a hybrid spell with a shipping-now delivery profile.
Canonical reference input: Power Word Kill (spell).
## When To Use

- A process, service, or system must stop immediately and graceful shutdown is not available or has already failed.
- The cost of the system continuing to run exceeds the cost of abrupt termination and potential data loss.
- An emergency requires instant action — a runaway process, a security breach in progress, a cascading failure.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Confirm the target is correct. Power Word Kill has no undo.
3. Verify that graceful alternatives (SIGTERM, drain, decommission) have been attempted or are not viable.
4. Execute the hard kill: process termination, circuit breaker trip, account lock, or emergency shutdown.
5. Immediately assess blast radius: what downstream systems were affected, what state was lost, what needs recovery.
6. Document what happened and why the hard kill was necessary — this is your incident report seed.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- Confirmation that the target has been terminated.
- A blast-radius assessment: what was lost, what was affected, what needs recovery.
- An incident seed documenting the kill decision and its justification.

## Pitfalls / Guardrails

- Keep the theatrical framing, but name the concrete mechanism that makes the skill useful right now.
- Power Word Kill is for emergencies. If you have time to do a graceful shutdown, you have time to use a different spell.
- Never kill a process you do not own or have explicit authorization to terminate.
- Always document the kill. Unexplained hard terminations are how organizations lose trust in their own systems.
- If the target is a person's account or access, this requires human authorization — an AI should never unilaterally terminate a human's access.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check which parts are concrete actions versus framing, so the user can tell what is real now.

## Example Invocation
```text
/power-word-kill immediately terminate a process or system that cannot be shut down gracefully. Confirm the target, verify alternatives are exhausted, execute, and assess blast radius
```
