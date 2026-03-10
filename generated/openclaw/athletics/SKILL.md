---
name: athletics
description: "Use this skill when the job is mostly about sustained force: large batches, exhaustive passes, long-running jobs, or load that needs to be carried without dropping it. It is the right metaphor when the answer is more throughput, sturdier batching, and disciplined endurance."
user-invocable: true
---

# Athletics

Push a heavy workload through to completion when elegance is optional.

## Overview

Athletics is interpreted here as a metaphorical skill with a shipping-now execution model.

Canonical source: Athletics (skill)

Provider target: OpenClaw

## When To Use

- The work is bottlenecked by volume, throughput, or runtime rather than subtle logic.
- You need batching, parallelism, or chunked processing across a large surface area.
- A marathon job needs progress accounting, retries, and stamina more than cleverness.

## Workflow

1. Estimate the total volume, runtime, and strain points before you start lifting.
2. Choose the batching, parallelism, and checkpoint strategy that can survive a long haul.
3. Return a durable run plan with throughput targets, resumability, and likely strain points.

## Deliverables

- A high-throughput execution or load plan.
- A resumable batching strategy with checkpoints.
- An estimate of cost, duration, and the main bottlenecks.

## Guardrails

- Do not brute-force external systems past safe limits, quotas, or terms of use.
- Stop and redesign when a coordination bug would become catastrophic at scale.

## Default Invocation

Use $athletics to turn this into a durable high-throughput run plan and tell me where it will strain.

