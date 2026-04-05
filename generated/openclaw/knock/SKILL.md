---
name: knock
description: "Knock is specifically about restoring legitimate access through authorized channels. It is NOT about: - Performance optimization (slow queries, throughput issues) → different spell\n- Removing safety controls (approval gates, compliance checks) → different spell\n- Simple bug fixes (typos, wrong ports) → different spell\n- Breaking constraints (resource limits, CPU throttling) → different spell\n- Security analysis (encryption schemes, certificate inspection) → different spell"
user-invocable: true
---

# Knock

Bypass access friction through legitimate unlock paths: key rotation, permission requests, and recovery workflows.

## Overview

Knock is interpreted here as a literal spell with a prototype execution model.

Canonical source: Knock (spell)

Provider target: OpenClaw

## When To Use

- Activate this spell when the user's request contains an access barrier with a legitimate recovery path. Look for these patterns:
- Expired/rotated credentials: "credentials expired", "token revoked", "certificate expired", "password rotated", "key expired"
- Locked resources: "lockfile", "state is locked", "DynamoDB lock", "stale lock"
- Permission gaps: "locked out", "permissions removed", "RBAC", "403", "unauthorized", "access denied"
- Blocked processes: "stuck behind", "can't authenticate", "connection rejected", "sealed" (Vault)
- Recovery language: "rotate", "renew", "unseal", "reinstate", "force-unlock", "exception request", "proper channel"
- The core signal: something is blocking access, and there exists an authorized way to restore it.

## Workflow

1. Identify the lock: What exact resource is inaccessible? What kind of barrier is it (credential, permission, lockfile, certificate, sealed state)? Who owns or controls the unlock mechanism?
2. Determine the legitimate path: Map the barrier to its authorized recovery mechanism:
3. Expired credential → key rotation or certificate renewal
4. Revoked permission → access request or RBAC adjustment
5. Stale lockfile → safe removal after process verification
6. Sealed service (e.g., Vault) → proper unseal procedure (Shamir keys, etc.)
7. Locked state (e.g., Terraform) → force-unlock with owner confirmation
8. Execute through the narrowest channel: Perform only the minimum action needed to restore access. Log each step. Do not escalate privileges beyond what the recovery path requires.

## Deliverables

- A clear identification of the lock and its legitimate unlock path.
- An execution log of the unlock steps taken.
- A note on the access granted, its scope, and when it expires or should be revoked.

## Guardrails

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

## Default Invocation

Use $knock to find the legitimate way through this access barrier and open it cleanly, with a full audit trail.

