---
name: hold-person
description: "Hold Person paralyzes a creature in place. The real-world version is administrative lockout: freezing an account, suspending a process, or putting a workflow on hold. Unlike Sleep (which is graceful suspension with state preservation), Hold Person is a hard freeze — nothing moves until explicitly released. This requires legitimate authority."
user-invocable: true
---

# Hold Person

Freeze a process, account, or workflow in place with administrative authority.

## Overview

Hold Person is interpreted here as a hybrid spell with a prototype execution model.

Canonical source: Hold Person (spell)

Provider target: OpenClaw

## When To Use

- An account, process, or workflow needs to be frozen pending investigation or review.
- You need to design an administrative hold or suspension mechanism with proper authorization.

## Workflow

1. Verify authorization: who has the authority to freeze this target, and is this invocation legitimate?
2. Define the freeze scope: what stops, what continues, and what happens to in-flight operations.
3. Set release conditions: who can unfreeze, under what circumstances, and with what audit trail.
4. Deliver the hold plan with authorization chain and release procedures.

## Deliverables

- A hold specification: what is frozen, by whose authority, and under what conditions.
- Release procedures: how to unfreeze, who can authorize it, and what audit trail is required.

## Guardrails

- Hold requires legitimate administrative authority. This is not a tool for unauthorized denial of service.
- Always define release conditions. A hold without release criteria is a permanent lockout, which is a different and more dangerous action.

## Default Invocation

Use $hold-person to design an administrative hold for this [account/process/workflow] with proper authorization and release conditions.

