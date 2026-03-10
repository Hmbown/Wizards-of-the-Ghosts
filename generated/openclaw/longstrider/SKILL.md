---
name: longstrider
description: "Longstrider is optimization for systems that already work. It focuses on build speed, cache design, parallelization, query tuning, shortcut discovery, and other ways to cover the same ground faster. The spell cares about sustained pace, not flashy one-off benchmarks."
user-invocable: true
---

# Longstrider

Make the path shorter without changing the destination.

## Overview

Longstrider is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Longstrider (spell)

Provider target: OpenClaw

## When To Use

- A workflow is correct but slower, heavier, or more repetitive than it should be.
- You have evidence of friction and want speed gains without changing the product outcome.
- Caching, batching, parallelism, or path simplification look more promising than a rewrite.

## Workflow

1. Profile where time, waiting, or repeated work is actually being spent.
2. Choose the smallest optimization that attacks the highest-friction segment first.
3. Return the speed plan with expected gains, measurement method, and regression risks.

## Deliverables

- A prioritized optimization plan.
- A before-and-after measurement strategy.
- A watchlist for correctness, cost, or cache-invalidation regressions.

## Guardrails

- Do not optimize based on vibes; identify the real bottleneck first.
- Protect correctness and maintainability instead of chasing speed at any price.

## Default Invocation

Use $longstrider to show me how to make this workflow meaningfully faster without changing what it is supposed to accomplish.

