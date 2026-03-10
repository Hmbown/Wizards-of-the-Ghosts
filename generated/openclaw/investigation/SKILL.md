---
name: investigation
description: "Use this skill when a problem has clues, but they need to be connected into a causal explanation."
user-invocable: true
---

# Investigation

Follow evidence through a system until the hidden mechanism becomes legible.

## Overview

Investigation is interpreted here as a metaphorical skill with a shipping-now execution model.

Canonical source: Investigation (skill)

Provider target: OpenClaw

## When To Use

- You are debugging a failure, regression, or strange behavior.
- There are logs, traces, docs, or code clues that need synthesis.
- You need the why, not just the what.

## Workflow

1. Collect the strongest observable clues first.
2. Test causal hypotheses against code, data, logs, or configuration.
3. Eliminate weak explanations and keep the chain of reasoning tight.
4. Return the most defensible explanation plus the next decisive check.

## Deliverables

- A ranked set of causes with evidence.
- The most likely root cause.
- A next-step validation or fix path.

## Guardrails

- Do not confuse correlation with cause.
- Keep evidence and inference visibly separate.

## Default Invocation

Use $investigation to follow the clues here and tell me the most likely root cause with evidence.

