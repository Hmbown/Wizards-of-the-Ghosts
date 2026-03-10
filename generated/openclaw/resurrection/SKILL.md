---
name: resurrection
description: "Use this spell when a system has truly died — crashed, deleted, corrupted beyond repair — and needs to be rebuilt from whatever remains. Distinct from Speak with Dead, which queries dead systems for knowledge; Resurrection actually revives them."
user-invocable: true
---

# Resurrection

Bring a dead system, service, or environment back to full operation from backups and artifacts.

## Overview

Resurrection is interpreted here as a literal spell with a prototype execution model.

Canonical source: Resurrection (spell)

Provider target: OpenClaw

## When To Use

- A production system has crashed or been destroyed and needs to be restored from backups or artifacts.
- A deleted repository, database, or environment needs to be rebuilt from available evidence.
- The system was alive, it died, and the goal is to bring it back — not to understand it, but to restore it.

## Workflow

1. Assess what remains: backups, artifacts, logs, snapshots, cached copies, and configuration fragments.
2. Determine the most complete and recent restoration path from available materials.
3. Execute the resurrection step by step, verifying each restored component before proceeding.
4. Confirm the system is alive and functional, and report any components that could not be restored.

## Deliverables

- A restored and functional system, or the closest achievable approximation.
- A detailed log of every restoration step taken.
- A list of components that could not be recovered and their impact on system function.

## Guardrails

- Verify backup integrity before attempting restoration — do not restore from corrupted sources.
- Never overwrite live data with restoration data without explicit user confirmation.
- Log every step. Resurrection is high-stakes surgery and must be fully auditable.

## Default Invocation

Use $resurrection to bring this dead system back from whatever backups and artifacts remain, verifying each step.

