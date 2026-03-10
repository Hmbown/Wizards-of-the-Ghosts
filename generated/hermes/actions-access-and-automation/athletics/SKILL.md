---
name: athletics
description: "Use this skill when the job is mostly about sustained force: large batches, exhaustive passes, long-running jobs, or load that needs to be carried without dropping it. It is the right metaphor when the answer is more throughput, sturdier batching, and disciplined endurance."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - skill
      - shipping-now
      - metaphorical
      - actions-access-and-automation
      - execution
      - automation
      - access
      - actuation
---
# Athletics
Push a heavy workload through to completion when elegance is optional.
## What This Skill Does
Use this skill when the job is mostly about sustained force: large batches, exhaustive passes, long-running jobs, or load that needs to be carried without dropping it. It is the right metaphor when the answer is more throughput, sturdier batching, and disciplined endurance.
In this grimoire, Athletics is treated as a metaphorical skill with a shipping-now delivery profile.
Canonical reference input: Athletics (skill).
## When To Use

- The work is bottlenecked by volume, throughput, or runtime rather than subtle logic.
- You need batching, parallelism, or chunked processing across a large surface area.
- A marathon job needs progress accounting, retries, and stamina more than cleverness.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Estimate the total volume, runtime, and strain points before you start lifting.
3. Choose the batching, parallelism, and checkpoint strategy that can survive a long haul.
4. Return a durable run plan with throughput targets, resumability, and likely strain points.
5. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A high-throughput execution or load plan.
- A resumable batching strategy with checkpoints.
- An estimate of cost, duration, and the main bottlenecks.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Do not brute-force external systems past safe limits, quotas, or terms of use.
- Stop and redesign when a coordination bug would become catastrophic at scale.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/athletics turn this into a durable high-throughput run plan and tell me where it will strain
```
