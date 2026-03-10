---
name: teleport
description: "Teleport is full-context migration: an application, environment, dataset, or service estate moves from one place to another in a way that tries to feel instantaneous to everyone depending on it. In reality, there is always preparation behind the magic. Data has to stay consistent, dependencies have to reattach, traffic has to cut over, and the old world has to remain recoverable long enough to trust the new one. The spell is powerful because it compresses a terrifying amount of movement into one decisive act. It is dangerous for exactly the same reason."
user-invocable: false
disable-model-invocation: true
---

# Teleport

Move an entire world without leaving its people stranded.

## Overview

Teleport is interpreted here as a hybrid spell with a prototype execution model.

Canonical source: Teleport (spell)

Provider target: OpenClaw

## When To Use

- You are planning a database migration, environment promotion, cloud move, or major system relocation.
- The core challenge is preserving state, continuity, and user trust across a high-stakes move.
- A reversible cutover plan matters as much as the destination architecture.

## Workflow

1. Define the source world, destination world, and the invariants that must survive the jump: data integrity, auth, latency, dependencies, and rollback viability.
2. Inventory every dependency and stateful surface that must travel or reconnect, including background jobs, secrets, DNS, storage, and human operator workflows.
3. Design the rehearsal, cutover window, rollback path, and validation checks before any live movement begins.
4. Return the migration plan with sequencing, integrity checks, and explicit failure gates that stop the spell if confidence drops.

## Deliverables

- A migration or cutover runbook.
- A rollback and recovery plan with decision thresholds.
- A validation checklist for data, traffic, permissions, and dependent systems after arrival.

## Guardrails

- Do not claim this move is safe without rehearsals, backups, and integrity verification.
- If the request lacks a rollback path or a way to validate arrival, the spell should stop at planning.

## Default Invocation

Use $teleport to plan a full system migration from this source environment to that destination, including cutover, rollback, and post-arrival verification.

