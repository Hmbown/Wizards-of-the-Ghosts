---
name: hold-person
description: "Hold Person = hard freeze. Nothing moves. In-flight operations stop. Requires authority. Used for security incidents, fraud, compliance holds, misbehaving systems. Sleep = graceful suspension. State is preserved and queued. Operations resume automatically. Used for maintenance windows, temporary pauses, planned downtime."
user-invocable: true
---

# Hold Person

Freeze a process, account, or workflow in place with administrative authority.

## Overview

Hold Person is interpreted here as a hybrid spell with a prototype execution model.

Canonical source: Hold Person (spell)

Provider target: OpenClaw

## When To Use

- Activate Hold Person when the user needs to hard-freeze an account, process, workflow, or system pending investigation, review, or resolution, with these conditions:
- Something must stop immediately and completely — no partial operation
- The frozen state must be preserved intact (not deleted, not terminated)
- The freeze is temporary and reversible — release conditions matter
- Administrative authority is required — someone must be authorized to impose and lift the hold
- The freeze is targeted — specific accounts, pipelines, endpoints, or jobs, not mass org-wide changes

## Workflow

1. Verify authority: Who can impose this hold? Is the requester authorized? Document the authorization chain. If authority is unclear, flag it before proceeding.
2. Define freeze scope: What exactly stops? What continues? What happens to in-flight operations? Be specific: which accounts, which pipelines, which endpoints. Preserve all state — nothing is deleted.
3. Set release conditions: Who can unfreeze? Under what circumstances? What audit trail is required? What happens if the hold exceeds a time threshold (e.g., auto-escalate after 48 hours)? A hold without release criteria is a permanent lockout — that's a different and more dangerous action.
4. Deliver the hold plan: Provide the hold specification (what is frozen, by whose authority, under what conditions) and release procedures (how to unfreeze, who authorizes it, what audit trail is required).

## Deliverables

- Hold specification: frozen scope, authority chain, conditions
- Release procedures: unfreeze steps, authorization requirements, audit trail
- Guardrails: never impose without authority, always define release conditions, preserve state

## Guardrails

- Do NOT use Hold Person for:
- Do not use for: Graceful pause with queuing (use Sleep): "pause during maintenance", "queue and deliver later", "no state lost"
- Do not use for: OS-level process control (use Stun): "SIGSTOP/SIGCONT", "stun for diagnostic", "quick memory check"
- Do not use for: Mass/organization-wide freezes: "all 500 users", "entire role", "every account"
- Do not use for: Permanent termination or deletion: "revoke permanently", "delete access", "shut down for good"
- Do not use for: Simple scheduling delays: "run two hours later", "shift the cron", "delay until upstream is ready"
- Do not use for: Stop restarting without preservation: "just stop the restart loop", "keep it down until I say"

## Default Invocation

Use $hold-person to design an administrative hold for this [account/process/workflow] with proper authorization and release conditions.

