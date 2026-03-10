---
name: knock
description: "Use this spell when a locked door - a stuck process, an expired token, a permission gap, or a locked file - stands between you and progress, and you need the legitimate path through."
user-invocable: true
---

# Knock

Bypass access friction through legitimate unlock paths: key rotation, permission requests, and recovery workflows.

## Overview

Knock is interpreted here as a literal spell with a prototype execution model.

Canonical source: Knock (spell)

Provider target: OpenClaw

## When To Use

- An expired API key, locked file, or revoked permission is blocking a workflow.
- You need to request elevated access or rotate credentials through the proper channel.
- A process is stuck behind an authentication or authorization barrier that has a legitimate resolution.

## Workflow

1. Identify the lock: what is blocked, what kind of access is needed, and who owns the key.
2. Determine the legitimate unlock path - key rotation, permission request, recovery workflow, or escalation.
3. Execute the unlock through the narrowest authorized channel, logging every step.
4. Confirm the door is open and report what access was granted and for how long.

## Deliverables

- A clear identification of the lock and its legitimate unlock path.
- An execution log of the unlock steps taken.
- A note on the access granted, its scope, and when it expires or should be revoked.

## Guardrails

- Never attempt to bypass security controls the user does not own or is not authorized to unlock.
- Refuse to crack, brute-force, or exploit - always prefer the legitimate recovery path.
- Log every unlock attempt. Transparency is non-negotiable for access-related operations.

## Default Invocation

Use $knock to find the legitimate way through this access barrier and open it cleanly, with a full audit trail.

