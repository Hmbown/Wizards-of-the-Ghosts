---
name: freedom-of-movement
description: "Freedom of Movement is for processes that should be moving but are caught in glue: locked files, blocked ports, circular dependencies, wedged jobs, or permissions that almost work. The skill is about diagnosing the restraint, then removing or routing around it without tearing the whole system apart. It favors unblocking over brute force."
user-invocable: true
---

# Freedom of Movement

Cut the nets around a stuck workflow.

## Overview

Freedom of Movement is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Freedom of Movement (spell)

Provider target: OpenClaw

## When To Use

- A pipeline, deploy, or local workflow is stalled by some specific obstruction.
- You suspect contention, locking, dependency loops, or environment constraints rather than core logic failure.
- The system might recover cleanly if the right knot is cut.

## Workflow

1. Trace the exact point of restriction and identify whether it is policy, resource contention, dependency structure, or state corruption.
2. Choose the least destructive unblock: release, reroute, defer, or re-sequence.
3. Return the unblock plan with post-clearance checks so movement resumes without hidden damage.

## Deliverables

- A blocker map naming the real constraint.
- A recommended sequence for removing or bypassing it.
- A verification checklist for restored flow.

## Guardrails

- Do not remove locks, guards, or permissions until you understand who relies on them.
- Refuse shortcuts that solve the jam by bypassing legitimate security or safety controls.

## Default Invocation

Use $freedom-of-movement to diagnose what is binding this workflow and show me the safest way to clear it.

