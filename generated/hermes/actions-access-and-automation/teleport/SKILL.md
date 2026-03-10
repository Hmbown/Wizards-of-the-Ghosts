---
name: teleport
description: "Teleport is full-context migration: an application, environment, dataset, or service estate moves from one place to another in a way that tries to feel instantaneous to everyone depending on it. In reality, there is always preparation behind the magic. Data has to stay consistent, dependencies have to reattach, traffic has to cut over, and the old world has to remain recoverable long enough to trust the new one. The spell is powerful because it compresses a terrifying amount of movement into one decisive act. It is dangerous for exactly the same reason."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - prototype
      - hybrid
      - actions-access-and-automation
      - execution
      - automation
      - access
      - actuation
---
# Teleport
Move an entire world without leaving its people stranded.
## What This Skill Does
Teleport is full-context migration: an application, environment, dataset, or service estate moves from one place to another in a way that tries to feel instantaneous to everyone depending on it. In reality, there is always preparation behind the magic. Data has to stay consistent, dependencies have to reattach, traffic has to cut over, and the old world has to remain recoverable long enough to trust the new one. The spell is powerful because it compresses a terrifying amount of movement into one decisive act. It is dangerous for exactly the same reason.
In this grimoire, Teleport is treated as a hybrid spell with a prototype delivery profile.
Canonical reference input: Teleport (spell).
## When To Use

- You are planning a database migration, environment promotion, cloud move, or major system relocation.
- The core challenge is preserving state, continuity, and user trust across a high-stakes move.
- A reversible cutover plan matters as much as the destination architecture.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Define the source world, destination world, and the invariants that must survive the jump: data integrity, auth, latency, dependencies, and rollback viability.
3. Inventory every dependency and stateful surface that must travel or reconnect, including background jobs, secrets, DNS, storage, and human operator workflows.
4. Design the rehearsal, cutover window, rollback path, and validation checks before any live movement begins.
5. Return the migration plan with sequencing, integrity checks, and explicit failure gates that stop the spell if confidence drops.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A migration or cutover runbook.
- A rollback and recovery plan with decision thresholds.
- A validation checklist for data, traffic, permissions, and dependent systems after arrival.

## Pitfalls / Guardrails

- Call out the glue, permissions, or missing infrastructure before you imply this is fully operational.
- Do not claim this move is safe without rehearsals, backups, and integrity verification.
- If the request lacks a rollback path or a way to validate arrival, the spell should stop at planning.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check which parts are concrete actions versus framing, so the user can tell what is real now.
- Check that any missing glue code, permissions, or future work is labeled before the skill is treated as ready.

## Example Invocation
```text
/teleport plan a full system migration from this source environment to that destination, including cutover, rollback, and post-arrival verification
```
