---
name: teleportation-circle
description: "Use this spell when you need a permanent, reliable portal between two environments — a CI/CD pipeline, a standing data sync, a repeatable deployment, or a migration path you will use more than once."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - prototype
      - literal
      - actions-access-and-automation
      - execution
      - automation
      - access
      - actuation
---
# Teleportation Circle
Establish reusable deployment pipelines, standing sync routes, and repeatable migration paths.
## What This Skill Does
Use this spell when you need a permanent, reliable portal between two environments — a CI/CD pipeline, a standing data sync, a repeatable deployment, or a migration path you will use more than once.
In this grimoire, Teleportation Circle is treated as a literal spell with a prototype delivery profile.
Canonical reference input: Teleportation Circle (spell).
## When To Use

- You are setting up a CI/CD pipeline or deployment workflow that will be used repeatedly.
- Two systems need a standing sync route that runs reliably without manual intervention.
- A migration path needs to be codified so it can be re-run, tested, and trusted.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Define the source, destination, and what travels through the circle: code, data, configuration, or artifacts.
3. Build the pipeline or sync route with explicit triggers, validation steps, and failure handling.
4. Test the circle end-to-end before relying on it for production traffic.
5. Document the circle's configuration, monitoring, and maintenance requirements.
6. Stop for explicit confirmation before taking a live action that changes access, triggers an alert, or touches a real system boundary.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A configured, tested pipeline or sync route between source and destination.
- Documentation of triggers, validation steps, failure modes, and rollback procedures.
- A monitoring and maintenance plan — permanent portals need ongoing attention.

## Pitfalls / Guardrails

- Call out the glue, permissions, or missing infrastructure before you imply this is fully operational.
- Do not create a circle and forget about it. Permanent portals need health checks, alerting, and maintenance.
- Test the circle in a non-production environment before routing real traffic through it.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the exact live target, confirmation gate, and rollback or recovery path are explicit.
- Check that any missing glue code, permissions, or future work is labeled before the skill is treated as ready.

## Example Invocation
```text
/teleportation-circle establish a reusable pipeline between these environments, with testing and monitoring built in
```
