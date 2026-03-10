---
name: scrying
description: "Use this spell when you need to see what is happening right now on a distant system rather than reading stale logs or cached reports."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - prototype
      - literal
      - monitoring-and-protection
      - observability
      - monitoring
      - guardrails
      - privacy
      - integration
      - home-assistant
---
# Scrying
Observe a live remote system, service, or deployment in real time.
## What This Skill Does
Use this spell when you need to see what is happening right now on a distant system rather than reading stale logs or cached reports.
In this grimoire, Scrying is treated as a literal spell with a prototype delivery profile.
Canonical reference input: Scrying (spell).
## When To Use

- You need live status from a remote service, server, or deployment.
- Cached dashboards or old logs are not trustworthy enough for the decision at hand.
- You want continuous observation of a system you cannot directly access.
- You want to pull a live snapshot of your Home Assistant device states — all lights, sensors, locks, and climate status in one view.

## Prerequisites

- Environment variables available to Hermes: `HA_URL`, `HA_TOKEN`.
- Primary credential or token: `HA_TOKEN`.
- Binaries on PATH: `curl`.

## Setup

1. Confirm the required environment variables are available inside the active Hermes runtime, not just in a shell profile.
2. Verify the required binaries resolve on PATH before you rely on them in a procedure.
3. Choose a non-production or low-risk target first if the skill can page, unlock, alert, or touch a live integration.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify the target system, service, or resource to observe.
3. Establish the best available live data channel: API polling, log streaming, health endpoints, or dashboard scraping.
4. Present the current state with explicit timestamps and staleness indicators.
5. Maintain the scrying session with periodic refresh and alert on state changes.
6. If Home Assistant is available, GET /api/states to retrieve all entity states and present a human-readable summary of the current home status.
7. Stop for explicit confirmation before taking a live action that changes access, triggers an alert, or touches a real system boundary.
8. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A live or near-live status view of the target system.
- Timestamps and refresh intervals so the user knows how stale each datum is.
- Alerts or callouts for state changes detected during the session.

## Pitfalls / Guardrails

- Call out the glue, permissions, or missing infrastructure before you imply this is fully operational.
- Do not access systems without the user's authorization and credentials.
- Never conflate cached or stale data with live state — always label the observation time.
- Prefer read-only observation channels; do not mutate the target to observe it.
- Do not rely on a live integration until credentials, target scope, and rollback expectations are verified.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the exact live target, confirmation gate, and rollback or recovery path are explicit.
- Check that any missing glue code, permissions, or future work is labeled before the skill is treated as ready.
- Check the required environment variables and binaries in the active Hermes runtime before trusting the procedure on a live target.

## Example Invocation
```text
/scrying show me the live state of this system right now, with timestamps and staleness clearly labeled
```
