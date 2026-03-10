---
name: scrying
description: "Use this spell when you need to see what is happening right now on a distant system rather than reading stale logs or cached reports."
user-invocable: true
metadata:
  openclaw:
    requires:
      env:
        - HA_URL
        - HA_TOKEN
      bins:
        - curl
    primaryEnv: HA_TOKEN
    emoji: "🔭"
---

# Scrying

Observe a live remote system, service, or deployment in real time.

## Overview

Scrying is interpreted here as a literal spell with a prototype execution model.

Canonical source: Scrying (spell)

Provider target: OpenClaw

## When To Use

- You need live status from a remote service, server, or deployment.
- Cached dashboards or old logs are not trustworthy enough for the decision at hand.
- You want continuous observation of a system you cannot directly access.
- You want to pull a live snapshot of your Home Assistant device states — all lights, sensors, locks, and climate status in one view.

## Workflow

1. Identify the target system, service, or resource to observe.
2. Establish the best available live data channel: API polling, log streaming, health endpoints, or dashboard scraping.
3. Present the current state with explicit timestamps and staleness indicators.
4. Maintain the scrying session with periodic refresh and alert on state changes.
5. If Home Assistant is available, GET /api/states to retrieve all entity states and present a human-readable summary of the current home status.

## Deliverables

- A live or near-live status view of the target system.
- Timestamps and refresh intervals so the user knows how stale each datum is.
- Alerts or callouts for state changes detected during the session.

## Guardrails

- Do not access systems without the user's authorization and credentials.
- Never conflate cached or stale data with live state — always label the observation time.
- Prefer read-only observation channels; do not mutate the target to observe it.

## Default Invocation

Use $scrying to show me the live state of this system right now, with timestamps and staleness clearly labeled.

