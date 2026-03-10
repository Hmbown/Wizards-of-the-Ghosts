---
name: unseen-servant
description: "Use this spell when you need a tireless helper that organizes, tidies, triages, and maintains without requiring your constant attention."
user-invocable: true
---

# Unseen Servant

Run a persistent background agent that handles mundane, repeating tasks silently.

## Overview

Unseen Servant is interpreted here as a literal spell with a shipping-now execution model.

Canonical source: Unseen Servant (spell)

Provider target: OpenClaw

## When To Use

- Routine maintenance tasks keep piling up: dependency updates, stale branch cleanup, inbox triage, log rotation.
- You want a helper that runs continuously in the background and only surfaces when something needs your attention.
- The work is important but low-priority - it should happen reliably without competing for your focus.

## Workflow

1. Define the servant's mandate: which tasks, which surfaces, and what scope boundaries.
2. Configure the cadence - continuous, periodic, or event-triggered.
3. Let the servant operate silently, logging its actions for later review.
4. Review the activity log periodically and adjust the mandate or dismiss the servant when done.

## Deliverables

- A running background process or agent loop with a clear task mandate.
- An activity log of everything the servant touched, with timestamps.
- A dismiss or pause mechanism so the user stays in control.

## Guardrails

- The servant does not expand its own mandate - it only touches what the user pre-approved.
- All actions must be logged and reviewable. Silent operation does not mean unaccountable operation.
- Provide a clear dismiss mechanism - the user must always be able to stop the servant immediately.

## Default Invocation

Use $unseen-servant to set up a background agent for this recurring task, with a clear mandate, activity log, and kill switch.

