---
name: hold-person
description: "Hold Person paralyzes a creature in place. The real-world version is administrative lockout: freezing an account, suspending a process, or putting a workflow on hold. Unlike Sleep (which is graceful suspension with state preservation), Hold Person is a hard freeze — nothing moves until explicitly released. This requires legitimate authority."
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
      - influence-and-behavior
      - influence
      - behavior
      - attention
      - engagement
---
# Hold Person
Freeze a process, account, or workflow in place with administrative authority.
## What This Skill Does
Hold Person paralyzes a creature in place. The real-world version is administrative lockout: freezing an account, suspending a process, or putting a workflow on hold. Unlike Sleep (which is graceful suspension with state preservation), Hold Person is a hard freeze — nothing moves until explicitly released. This requires legitimate authority.
In this grimoire, Hold Person is treated as a hybrid spell with a prototype delivery profile.
Canonical reference input: Hold Person (spell).
## When To Use

- An account, process, or workflow needs to be frozen pending investigation or review.
- You need to design an administrative hold or suspension mechanism with proper authorization.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Verify authorization: who has the authority to freeze this target, and is this invocation legitimate?
3. Define the freeze scope: what stops, what continues, and what happens to in-flight operations.
4. Set release conditions: who can unfreeze, under what circumstances, and with what audit trail.
5. Deliver the hold plan with authorization chain and release procedures.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A hold specification: what is frozen, by whose authority, and under what conditions.
- Release procedures: how to unfreeze, who can authorize it, and what audit trail is required.

## Pitfalls / Guardrails

- Call out the glue, permissions, or missing infrastructure before you imply this is fully operational.
- Hold requires legitimate administrative authority. This is not a tool for unauthorized denial of service.
- Always define release conditions. A hold without release criteria is a permanent lockout, which is a different and more dangerous action.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check which parts are concrete actions versus framing, so the user can tell what is real now.
- Check that any missing glue code, permissions, or future work is labeled before the skill is treated as ready.

## Example Invocation
```text
/hold-person design an administrative hold for this [account/process/workflow] with proper authorization and release conditions
```
