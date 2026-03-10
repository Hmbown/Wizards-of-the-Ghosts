---
name: greater-invisibility
description: "Greater Invisibility covers live work performed with reduced observability: silent deploys, zero-downtime migrations, background reindexing, and backfills that avoid user-facing turbulence. The distinction from ordinary Invisibility is that action continues while the footprint stays deliberately subdued. That makes it useful and easy to misuse, so the operator view has to remain explicit even when the audience view stays calm."
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
      - monitoring-and-protection
      - observability
      - monitoring
      - guardrails
      - privacy
---
# Greater Invisibility
Keep moving while the audience barely notices the stagehands.
## What This Skill Does
Greater Invisibility covers live work performed with reduced observability: silent deploys, zero-downtime migrations, background reindexing, and backfills that avoid user-facing turbulence. The distinction from ordinary Invisibility is that action continues while the footprint stays deliberately subdued. That makes it useful and easy to misuse, so the operator view has to remain explicit even when the audience view stays calm.
In this grimoire, Greater Invisibility is treated as a metaphorical spell with a prototype delivery profile.
Canonical reference input: Greater Invisibility (spell).
## When To Use

- You need to make live changes while minimizing user-visible noise or metric spikes.
- The work can be sequenced behind feature flags, background jobs, shadow writes, or progressive rollout techniques.
- You still need trusted operator visibility even if the broader surface stays quiet.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Define which observers should notice the work, which should not, and what counts as acceptable visibility.
3. Choose the live-change pattern that keeps user impact low while preserving operator feedback.
4. Return the execution sequence, rollback triggers, and the monitoring surfaces that stay intentionally visible.
5. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A low-observability live-change plan.
- A list of operator-visible signals and user-visible signals.
- Rollback conditions for when the stealth stops being safe.

## Pitfalls / Guardrails

- Call out the glue, permissions, or missing infrastructure before you imply this is fully operational.
- Do not use reduced observability to hide policy-relevant changes from required reviewers.
- If user-impacting work is happening, retain enough telemetry to prove whether the spell is working or failing.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.
- Check that any missing glue code, permissions, or future work is labeled before the skill is treated as ready.

## Example Invocation
```text
/greater-invisibility plan a live change that stays quiet to users while preserving the operator signals we still need
```
