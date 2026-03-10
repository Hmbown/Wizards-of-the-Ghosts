---
name: knock
description: "Use this spell when a locked door - a stuck process, an expired token, a permission gap, or a locked file - stands between you and progress, and you need the legitimate path through."
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
# Knock
Bypass access friction through legitimate unlock paths: key rotation, permission requests, and recovery workflows.
## What This Skill Does
Use this spell when a locked door - a stuck process, an expired token, a permission gap, or a locked file - stands between you and progress, and you need the legitimate path through.
In this grimoire, Knock is treated as a literal spell with a prototype delivery profile.
Canonical reference input: Knock (spell).
## When To Use

- An expired API key, locked file, or revoked permission is blocking a workflow.
- You need to request elevated access or rotate credentials through the proper channel.
- A process is stuck behind an authentication or authorization barrier that has a legitimate resolution.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify the lock: what is blocked, what kind of access is needed, and who owns the key.
3. Determine the legitimate unlock path - key rotation, permission request, recovery workflow, or escalation.
4. Execute the unlock through the narrowest authorized channel, logging every step.
5. Confirm the door is open and report what access was granted and for how long.
6. Stop for explicit confirmation before taking a live action that changes access, triggers an alert, or touches a real system boundary.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A clear identification of the lock and its legitimate unlock path.
- An execution log of the unlock steps taken.
- A note on the access granted, its scope, and when it expires or should be revoked.

## Pitfalls / Guardrails

- Call out the glue, permissions, or missing infrastructure before you imply this is fully operational.
- Never attempt to bypass security controls the user does not own or is not authorized to unlock.
- Refuse to crack, brute-force, or exploit - always prefer the legitimate recovery path.
- Log every unlock attempt. Transparency is non-negotiable for access-related operations.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the exact live target, confirmation gate, and rollback or recovery path are explicit.
- Check that any missing glue code, permissions, or future work is labeled before the skill is treated as ready.

## Example Invocation
```text
/knock find the legitimate way through this access barrier and open it cleanly, with a full audit trail
```
