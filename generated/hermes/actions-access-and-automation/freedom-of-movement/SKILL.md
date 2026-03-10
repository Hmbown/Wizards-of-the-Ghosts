---
name: freedom-of-movement
description: "Freedom of Movement is for processes that should be moving but are caught in glue: locked files, blocked ports, circular dependencies, wedged jobs, or permissions that almost work. The skill is about diagnosing the restraint, then removing or routing around it without tearing the whole system apart. It favors unblocking over brute force."
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
      - actions-access-and-automation
      - execution
      - automation
      - access
      - actuation
---
# Freedom of Movement
Cut the nets around a stuck workflow.
## What This Skill Does
Freedom of Movement is for processes that should be moving but are caught in glue: locked files, blocked ports, circular dependencies, wedged jobs, or permissions that almost work. The skill is about diagnosing the restraint, then removing or routing around it without tearing the whole system apart. It favors unblocking over brute force.
In this grimoire, Freedom of Movement is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Freedom of Movement (spell).
## When To Use

- A pipeline, deploy, or local workflow is stalled by some specific obstruction.
- You suspect contention, locking, dependency loops, or environment constraints rather than core logic failure.
- The system might recover cleanly if the right knot is cut.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Trace the exact point of restriction and identify whether it is policy, resource contention, dependency structure, or state corruption.
3. Choose the least destructive unblock: release, reroute, defer, or re-sequence.
4. Return the unblock plan with post-clearance checks so movement resumes without hidden damage.
5. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A blocker map naming the real constraint.
- A recommended sequence for removing or bypassing it.
- A verification checklist for restored flow.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Do not remove locks, guards, or permissions until you understand who relies on them.
- Refuse shortcuts that solve the jam by bypassing legitimate security or safety controls.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/freedom-of-movement diagnose what is binding this workflow and show me the safest way to clear it
```
