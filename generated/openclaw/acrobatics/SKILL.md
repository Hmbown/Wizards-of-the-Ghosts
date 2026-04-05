---
name: acrobatics
description: "Use this skill when the work is a choreography problem: brittle sequencing, async handoffs, or constrained flows that must stay upright end to end. It shines on API dances, dependency ordering, and recovery logic where grace matters more than brute force."
user-invocable: true
---

# Acrobatics

Thread complex systems without tripping rate limits, retries, or state.

## Overview

Acrobatics is interpreted here as a metaphorical skill with a shipping-now execution model.

Canonical source: Acrobatics (skill)

Provider target: OpenClaw

## When To Use

- An integration requires a precise sequence of calls, callbacks, or tokens.
- Concurrency, pagination, or retries can topple the flow if handled clumsily.
- You need a nimble route through constraints rather than more compute.

## Workflow

1. Map the sequence, tight constraints, and recovery points before moving.
2. Reorder or simplify the path to reduce wasted calls, unstable state, and timing risk.
3. Return the stepwise route with checkpoints, balance points, and fallback moves.

## Deliverables

- A sequenced execution plan for the constrained flow.
- A list of state, timing, and rate-limit risks.
- A compact recovery playbook for dropped or misordered steps.

## Guardrails

- Do not mistake unnecessary cleverness for agility; the cleanest path wins.
- Surface hidden coupling and time-sensitive assumptions instead of relying on luck.

## Default Invocation

Use $acrobatics to thread this workflow cleanly through its sequencing constraints and show me the balance points.

