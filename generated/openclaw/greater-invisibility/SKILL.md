---
name: greater-invisibility
description: "Greater Invisibility covers live work performed with reduced observability: silent deploys, zero-downtime migrations, background reindexing, and backfills that avoid user-facing turbulence. The distinction from ordinary Invisibility is that action continues while the footprint stays deliberately subdued. That makes it useful and easy to misuse, so the operator view has to remain explicit even when the audience view stays calm."
user-invocable: true
---

# Greater Invisibility

Keep moving while the audience barely notices the stagehands.

## Overview

Greater Invisibility is interpreted here as a metaphorical spell with a prototype execution model.

Canonical source: Greater Invisibility (spell)

Provider target: OpenClaw

## When To Use

- You need to make live changes while minimizing user-visible noise or metric spikes.
- The work can be sequenced behind feature flags, background jobs, shadow writes, or progressive rollout techniques.
- You still need trusted operator visibility even if the broader surface stays quiet.

## Workflow

1. Define which observers should notice the work, which should not, and what counts as acceptable visibility.
2. Choose the live-change pattern that keeps user impact low while preserving operator feedback.
3. Return the execution sequence, rollback triggers, and the monitoring surfaces that stay intentionally visible.

## Deliverables

- A low-observability live-change plan.
- A list of operator-visible signals and user-visible signals.
- Rollback conditions for when the stealth stops being safe.

## Guardrails

- Do not use reduced observability to hide policy-relevant changes from required reviewers.
- If user-impacting work is happening, retain enough telemetry to prove whether the spell is working or failing.

## Default Invocation

Use $greater-invisibility to plan a live change that stays quiet to users while preserving the operator signals we still need.

