---
name: resurrection
description: "Use this spell when a system has truly died — crashed, deleted, corrupted beyond repair — and needs to be rebuilt from whatever remains. Distinct from Speak with Dead, which queries dead systems for knowledge; Resurrection actually revives them."
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
      - repair-and-recovery
      - recovery
      - repair
      - triage
      - stabilization
---
# Resurrection
Bring a dead system, service, or environment back to full operation from backups and artifacts.
## What This Skill Does
Use this spell when a system has truly died — crashed, deleted, corrupted beyond repair — and needs to be rebuilt from whatever remains. Distinct from Speak with Dead, which queries dead systems for knowledge; Resurrection actually revives them.
In this grimoire, Resurrection is treated as a literal spell with a prototype delivery profile.
Canonical reference input: Resurrection (spell).
## When To Use

- A production system has crashed or been destroyed and needs to be restored from backups or artifacts.
- A deleted repository, database, or environment needs to be rebuilt from available evidence.
- The system was alive, it died, and the goal is to bring it back — not to understand it, but to restore it.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Assess what remains: backups, artifacts, logs, snapshots, cached copies, and configuration fragments.
3. Determine the most complete and recent restoration path from available materials.
4. Execute the resurrection step by step, verifying each restored component before proceeding.
5. Confirm the system is alive and functional, and report any components that could not be restored.
6. Stop for explicit confirmation before taking a live action that changes access, triggers an alert, or touches a real system boundary.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A restored and functional system, or the closest achievable approximation.
- A detailed log of every restoration step taken.
- A list of components that could not be recovered and their impact on system function.

## Pitfalls / Guardrails

- Call out the glue, permissions, or missing infrastructure before you imply this is fully operational.
- Verify backup integrity before attempting restoration — do not restore from corrupted sources.
- Never overwrite live data with restoration data without explicit user confirmation.
- Log every step. Resurrection is high-stakes surgery and must be fully auditable.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the exact live target, confirmation gate, and rollback or recovery path are explicit.
- Check that any missing glue code, permissions, or future work is labeled before the skill is treated as ready.

## Example Invocation
```text
/resurrection bring this dead system back from whatever backups and artifacts remain, verifying each step
```
