---
name: lesser-restoration
description: "In D&D, Lesser Restoration ends a specific condition: blinded, deafened, paralyzed, or poisoned. The real-world version is clearing a stuck state: a feature flag that should have been toggled, a queue that is stuck, a lock that was not released, a status field that is wrong, or a circuit breaker that is still tripped after the emergency passed. The system is not fundamentally broken — it has a specific condition that needs to be cleared."
user-invocable: true
---

# Lesser Restoration

Clear a specific stuck state, flag, or condition that is blocking normal operation.

## Overview

Lesser Restoration is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Lesser Restoration (spell)

Provider target: OpenClaw

## When To Use

- A system is stuck in a specific state that prevents normal operation: a lock, flag, queue, or status.
- The fix is not a code change but a state change: toggling, clearing, resetting, or releasing.
- Normal operation would resume immediately if this one condition were cleared.

## Workflow

1. Identify the specific condition: what state is the system stuck in?
2. Verify this is a condition problem, not a deeper issue masquerading as a stuck state.
3. Clear the condition with the appropriate mechanism: toggle, reset, release, or flush.
4. Verify normal operation resumes and the condition does not immediately recur.

## Deliverables

- The identified stuck condition and the mechanism to clear it.
- Verification that normal operation resumed after clearing.

## Guardrails

- Clearing a condition that keeps recurring is not a fix — it is symptom suppression. If the condition comes back, escalate to Greater Restoration.
- Verify the stuck state is actually stuck and not intentionally set. Some conditions are there for a reason.

## Default Invocation

Use $lesser-restoration to identify and clear the stuck state that is blocking this [system/process/workflow] from operating normally.

