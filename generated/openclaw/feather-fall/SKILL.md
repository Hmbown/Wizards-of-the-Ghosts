---
name: feather-fall
description: "Feather Fall is the spell for bad situations that are already in motion. A deploy is going sideways, a service is thrashing, a queue is backing up, or an integration is failing faster than the humans can think. Instead of pretending you can teleport back to normal instantly, you slow the fall: circuit breakers, degraded modes, load shedding, safe defaults, and graceful shutdown paths. The point is not elegance. The point is buying time without multiplying damage. A good Feather Fall plan makes failure survivable and visible enough to recover from."
user-invocable: true
---

# Feather Fall

Turn a hard crash into a controlled descent.

## Overview

Feather Fall is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Feather Fall (spell)

Provider target: OpenClaw

## When To Use

- A live service, deploy, or workflow is failing and needs a safer landing path immediately.
- The right answer is graceful degradation, fallback behavior, or controlled shutdown rather than business-as-usual.
- You need to define what stays up, what gets dropped, and how to keep users from falling with the system.

## Workflow

1. Identify the failure that is already underway, including the blast radius if nothing changes.
2. Choose the descent mechanisms that reduce harm fastest: feature flags, circuit breakers, throttles, queue draining, or static fallbacks.
3. Define the minimal safe experience during the fall, along with the signals that prove the descent is stabilizing.
4. Return the emergency sequence, operator checks, and the criteria for either recovery or a full shutdown.

## Deliverables

- A graceful-degradation or safe-landing sequence.
- Trigger thresholds and operator signals for entering and exiting fallback mode.
- A note on what user experience, data guarantees, or capacity are intentionally reduced during the descent.

## Guardrails

- Do not use graceful degradation to hide the incident from operators who need to respond.
- Fallback modes must protect data integrity and user safety before they protect polish or convenience.

## Default Invocation

Use $feather-fall to design the fastest safe descent for this failing deploy, service, or workflow, including what should degrade first.

