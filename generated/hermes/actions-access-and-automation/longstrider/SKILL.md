---
name: longstrider
description: "Longstrider is the optimization spell for systems that already work. It makes the path shorter without changing the destination. It cares about sustained pace, not flashy one-off benchmarks."
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
      - actions-access-and-automation
      - execution
      - automation
      - access
      - actuation
---
# Longstrider
Make the path shorter without changing the destination.
## What This Skill Does
Longstrider is the optimization spell for systems that already work. It makes the path shorter without changing the destination. It cares about sustained pace, not flashy one-off benchmarks.
In this grimoire, Longstrider is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Longstrider (spell).
## When To Use

- Trigger Longstrider when the user describes a working system that is slower than it should be and asks for speed improvements. Look for:
- Time complaints with metrics: "takes 22 minutes", "4.2 seconds to load", "p95 is 800ms", "cold start is 8 seconds"
- Optimization keywords: "bottleneck", "speed up", "optimize", "faster", "profiling", "cache", "parallelize", "batch"
- Constraint phrases: "without rewriting", "without skipping tests", "without schema changes", "quick wins", "don't want to change the product"
- Evidence of friction: "most of that is...", "the largest contentful paint is...", "single-threaded Python reading line by line"
- Measurement mindset: "before/after", "measurement plan", "profile", "identify what's happening"

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Profile first: Identify where time, waiting, or repeated work is actually being spent. Never optimize based on vibes—demand or propose measurement of the real bottleneck.
3. Smallest effective change: Choose the minimal optimization that attacks the highest-friction segment. Prefer caching, batching, parallelism, or path simplification over rewrites.
4. Return the speed plan: Deliver a prioritized optimization plan with expected gains, a before-and-after measurement strategy, and a watchlist for correctness, cost, or cache-invalidation regressions.
5. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A prioritized optimization plan.
- A before-and-after measurement strategy.
- A watchlist for correctness, cost, or cache-invalidation regressions.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Protect correctness and maintainability over raw speed
- Identify the real bottleneck before proposing solutions
- Flag regression risks explicitly (cache invalidation, race conditions, test integrity)
- Do not use for: Rewrites or migrations: "rewrite from Node.js to Go" → different spell
- Do not use for: Bug fixes: "deploy keeps failing due to permissions" → fix spell, not optimization
- Do not use for: Resilience patterns: "add retry logic and circuit breakers" → reliability spell
- Do not use for: Concept teaching: "explain generators and async/await" → education spell
- Do not use for: Team scaling: "write a hiring plan" → org spell
- Do not use for: Personal fitness: "optimize my training schedule" → literal misinterpretation

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/longstrider show me how to make this workflow meaningfully faster without changing what it is supposed to accomplish
```
