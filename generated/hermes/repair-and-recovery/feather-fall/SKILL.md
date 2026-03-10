---
name: feather-fall
description: "Feather Fall is the spell for bad situations that are already in motion. A deploy is going sideways, a service is thrashing, a queue is backing up, or an integration is failing faster than the humans can think. Instead of pretending you can teleport back to normal instantly, you slow the fall: circuit breakers, degraded modes, load shedding, safe defaults, and graceful shutdown paths. The point is not elegance. The point is buying time without multiplying damage. A good Feather Fall plan makes failure survivable and visible enough to recover from."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - shipping-now
      - metaphorical
      - repair-and-recovery
      - recovery
      - repair
      - triage
      - stabilization
---
# Feather Fall
Turn a hard crash into a controlled descent.
## What This Skill Does
Feather Fall is the spell for bad situations that are already in motion. A deploy is going sideways, a service is thrashing, a queue is backing up, or an integration is failing faster than the humans can think. Instead of pretending you can teleport back to normal instantly, you slow the fall: circuit breakers, degraded modes, load shedding, safe defaults, and graceful shutdown paths. The point is not elegance. The point is buying time without multiplying damage. A good Feather Fall plan makes failure survivable and visible enough to recover from.
In this grimoire, Feather Fall is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Feather Fall (spell).
## When To Use

- A live service, deploy, or workflow is failing and needs a safer landing path immediately.
- The right answer is graceful degradation, fallback behavior, or controlled shutdown rather than business-as-usual.
- You need to define what stays up, what gets dropped, and how to keep users from falling with the system.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify the failure that is already underway, including the blast radius if nothing changes.
3. Choose the descent mechanisms that reduce harm fastest: feature flags, circuit breakers, throttles, queue draining, or static fallbacks.
4. Define the minimal safe experience during the fall, along with the signals that prove the descent is stabilizing.
5. Return the emergency sequence, operator checks, and the criteria for either recovery or a full shutdown.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A graceful-degradation or safe-landing sequence.
- Trigger thresholds and operator signals for entering and exiting fallback mode.
- A note on what user experience, data guarantees, or capacity are intentionally reduced during the descent.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Do not use graceful degradation to hide the incident from operators who need to respond.
- Fallback modes must protect data integrity and user safety before they protect polish or convenience.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/feather-fall design the fastest safe descent for this failing deploy, service, or workflow, including what should degrade first
```
