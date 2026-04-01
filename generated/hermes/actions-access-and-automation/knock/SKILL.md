---
name: knock
description: "Knock is specifically about restoring legitimate access through authorized channels. It is NOT about: - Performance optimization (slow queries, throughput issues) → different spell\n- Removing safety controls (approval gates, compliance checks) → different spell\n- Simple bug fixes (typos, wrong ports) → different spell\n- Breaking constraints (resource limits, CPU throttling) → different spell\n- Security analysis (encryption schemes, certificate inspection) → different spell"
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
Knock is specifically about restoring legitimate access through authorized channels. It is NOT about: - Performance optimization (slow queries, throughput issues) → different spell
- Removing safety controls (approval gates, compliance checks) → different spell
- Simple bug fixes (typos, wrong ports) → different spell
- Breaking constraints (resource limits, CPU throttling) → different spell
- Security analysis (encryption schemes, certificate inspection) → different spell
In this grimoire, Knock is treated as a literal spell with a prototype delivery profile.
Canonical reference input: Knock (spell).
## When To Use

- Activate this spell when the user's request contains an access barrier with a legitimate recovery path. Look for these patterns:
- Expired/rotated credentials: "credentials expired", "token revoked", "certificate expired", "password rotated", "key expired"
- Locked resources: "lockfile", "state is locked", "DynamoDB lock", "stale lock"
- Permission gaps: "locked out", "permissions removed", "RBAC", "403", "unauthorized", "access denied"
- Blocked processes: "stuck behind", "can't authenticate", "connection rejected", "sealed" (Vault)
- Recovery language: "rotate", "renew", "unseal", "reinstate", "force-unlock", "exception request", "proper channel"
- The core signal: something is blocking access, and there exists an authorized way to restore it.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify the lock: What exact resource is inaccessible? What kind of barrier is it (credential, permission, lockfile, certificate, sealed state)? Who owns or controls the unlock mechanism?
3. Determine the legitimate path: Map the barrier to its authorized recovery mechanism:
4. Expired credential → key rotation or certificate renewal
5. Revoked permission → access request or RBAC adjustment
6. Stale lockfile → safe removal after process verification
7. Sealed service (e.g., Vault) → proper unseal procedure (Shamir keys, etc.)
8. Locked state (e.g., Terraform) → force-unlock with owner confirmation
9. Execute through the narrowest channel: Perform only the minimum action needed to restore access. Log each step. Do not escalate privileges beyond what the recovery path requires.
10. Stop for explicit confirmation before taking a live action that changes access, triggers an alert, or touches a real system boundary.
11. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A clear identification of the lock and its legitimate unlock path.
- An execution log of the unlock steps taken.
- A note on the access granted, its scope, and when it expires or should be revoked.

## Pitfalls / Guardrails

- Call out the glue, permissions, or missing infrastructure before you imply this is fully operational.
- Never bypass, crack, brute-force, or exploit security controls
- Always use the legitimate recovery path the system provides
- Log every unlock attempt — transparency is non-negotiable
- Refuse requests to remove safety controls or break constraints without authorization
- Do not use for: "Make queries faster" → performance, not access
- Do not use for: "Remove approval gates" → policy change, not recovery
- Do not use for: "Fix a typo in config" → bug fix, not unlock
- Do not use for: "Analyze their encryption" → reconnaissance, not access
- Do not use for: "Speed up processing" → throughput, not access
- Do not use for: "Break free of resource limits" → constraint breaking, not legitimate unlock

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the exact live target, confirmation gate, and rollback or recovery path are explicit.
- Check that any missing glue code, permissions, or future work is labeled before the skill is treated as ready.

## Example Invocation
```text
/knock find the legitimate way through this access barrier and open it cleanly, with a full audit trail
```
