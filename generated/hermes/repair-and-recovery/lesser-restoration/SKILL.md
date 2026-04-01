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

- Words: stuck, won't reset, not clearing, stale, orphaned, lingering, trapped, hung, frozen, deadlocked
- Patterns: "X is stuck in Y state", "need to clear/reset/flush/release X", "Z was never released/cleaned up", "flag/toggle/switch won't change"
- Context: The underlying system works fine; one specific condition is preventing it from proceeding

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify the specific stuck condition: what exact state, flag, lock, or queue is blocking progress?
3. Verify it's truly stuck (not intentionally set or actively protecting against a real problem)
4. Clear the condition using the minimal mechanism: toggle off, reset to default, release lock, flush cache, replay queue, remove finalizer
5. Confirm normal operation resumes and the condition does not immediately recur — if it recurs, the root cause is deeper; escalate to greater-restoration
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- The identified stuck condition and the mechanism to clear it.
- Verification that normal operation resumed after clearing.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Do not use for: Fixing code bugs, syntax errors, or null pointer exceptions → use mending or hotfix patterns
- Do not use for: Cleaning up widespread data corruption or orphaned records across tables → use greater-restoration
- Do not use for: Rebuilding or redesigning a system → use rebuild or refactor patterns
- Do not use for: Debugging unknown root causes → use diagnose or identify patterns
- Do not use for: Adding missing features or configuration → use create or configure patterns
- Do not use for: "Fix the bug that causes X to get stuck" → code fix, not state clear
- Do not use for: "Clean up all the corrupted data" → widespread damage, not single condition
- Do not use for: "Why is X happening?" → diagnosis needed first
- Do not use for: "X keeps coming back after I clear it" → symptom suppression; find root cause instead

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/lesser-restoration identify and clear the stuck state that is blocking this [system/process/workflow] from operating normally
```
