---
name: lesser-restoration
description: "In D&D, Lesser Restoration ends a specific condition: blinded, deafened, paralyzed, or poisoned. The real-world version is clearing a stuck state: a feature flag that should have been toggled, a queue that is stuck, a lock that was not released, a status field that is wrong, or a circuit breaker that is still tripped after the emergency passed. The system is not fundamentally broken — it has a specific condition that needs to be cleared."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - shipping-now
      - metaphorical
      - repair-and-recovery
      - recovery
      - repair
      - triage
      - stabilization
---
# Lesser Restoration
Clear a specific stuck state, flag, or condition that is blocking normal operation.
## What This Skill Does
In D&D, Lesser Restoration ends a specific condition: blinded, deafened, paralyzed, or poisoned. The real-world version is clearing a stuck state: a feature flag that should have been toggled, a queue that is stuck, a lock that was not released, a status field that is wrong, or a circuit breaker that is still tripped after the emergency passed. The system is not fundamentally broken — it has a specific condition that needs to be cleared.
In this grimoire, Lesser Restoration is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Lesser Restoration (spell).
## When To Use

- A system is stuck in a specific state that prevents normal operation: a lock, flag, queue, or status.
- The fix is not a code change but a state change: toggling, clearing, resetting, or releasing.
- Normal operation would resume immediately if this one condition were cleared.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify the specific condition: what state is the system stuck in?
3. Verify this is a condition problem, not a deeper issue masquerading as a stuck state.
4. Clear the condition with the appropriate mechanism: toggle, reset, release, or flush.
5. Verify normal operation resumes and the condition does not immediately recur.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- The identified stuck condition and the mechanism to clear it.
- Verification that normal operation resumed after clearing.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Clearing a condition that keeps recurring is not a fix — it is symptom suppression. If the condition comes back, escalate to Greater Restoration.
- Verify the stuck state is actually stuck and not intentionally set. Some conditions are there for a reason.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/lesser-restoration identify and clear the stuck state that is blocking this [system/process/workflow] from operating normally
```
