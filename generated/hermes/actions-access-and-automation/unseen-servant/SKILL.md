---
name: unseen-servant
description: "Use this spell when you need a tireless helper that organizes, tidies, triages, and maintains without requiring your constant attention."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - shipping-now
      - literal
      - actions-access-and-automation
      - execution
      - automation
      - access
      - actuation
---
# Unseen Servant
Run a persistent background agent that handles mundane, repeating tasks silently.
## What This Skill Does
Use this spell when you need a tireless helper that organizes, tidies, triages, and maintains without requiring your constant attention.
In this grimoire, Unseen Servant is treated as a literal spell with a shipping-now delivery profile.
Canonical reference input: Unseen Servant (spell).
## When To Use

- Routine maintenance tasks keep piling up: dependency updates, stale branch cleanup, inbox triage, log rotation.
- You want a helper that runs continuously in the background and only surfaces when something needs your attention.
- The work is important but low-priority - it should happen reliably without competing for your focus.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Define the servant's mandate: which tasks, which surfaces, and what scope boundaries.
3. Configure the cadence - continuous, periodic, or event-triggered.
4. Let the servant operate silently, logging its actions for later review.
5. Review the activity log periodically and adjust the mandate or dismiss the servant when done.
6. Stop for explicit confirmation before taking a live action that changes access, triggers an alert, or touches a real system boundary.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A running background process or agent loop with a clear task mandate.
- An activity log of everything the servant touched, with timestamps.
- A dismiss or pause mechanism so the user stays in control.

## Pitfalls / Guardrails

- Treat the live action surface as real operational work, not decorative lore.
- The servant does not expand its own mandate - it only touches what the user pre-approved.
- All actions must be logged and reviewable. Silent operation does not mean unaccountable operation.
- Provide a clear dismiss mechanism - the user must always be able to stop the servant immediately.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the exact live target, confirmation gate, and rollback or recovery path are explicit.

## Example Invocation
```text
/unseen-servant set up a background agent for this recurring task, with a clear mandate, activity log, and kill switch
```
