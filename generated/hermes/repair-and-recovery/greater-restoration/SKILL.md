---
name: greater-restoration
description: "In D&D, Greater Restoration ends charm, petrification, curses, ability score reductions, and hit point maximum reductions — the serious, long-term ailments. The real-world version is deep system recovery: unfucking a database that has been gradually corrupted, restoring a codebase that has accumulated technical debt to the point of dysfunction, or recovering from a long-running misconfiguration that has silently degraded performance."
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
# Greater Restoration
Undo deep corruption and restore a system degraded by accumulated damage.
## What This Skill Does
In D&D, Greater Restoration ends charm, petrification, curses, ability score reductions, and hit point maximum reductions — the serious, long-term ailments. The real-world version is deep system recovery: unfucking a database that has been gradually corrupted, restoring a codebase that has accumulated technical debt to the point of dysfunction, or recovering from a long-running misconfiguration that has silently degraded performance.
In this grimoire, Greater Restoration is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Greater Restoration (spell).
## When To Use

- A system has been gradually degraded by accumulated problems and no single fix will restore it.
- Corruption, misconfiguration, or technical debt has built up to the point where triage is insufficient.
- The system needs a comprehensive restoration plan, not a hotfix.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Assess the scope of degradation: how many subsystems are affected, and how deep does the damage go?
3. Identify the root causes: what introduced the corruption and is it still active?
4. Design the restoration plan: the ordered sequence of fixes, migrations, or rebuilds needed.
5. Execute restoration with verification at each stage — do not batch this without checkpoints.
6. Deliver the restored system with a post-restoration health check.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A restoration plan: ordered steps to undo accumulated damage.
- Root-cause identification: what caused the degradation and how to prevent recurrence.
- A post-restoration health check confirming the system is back to full function.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Greater Restoration is expensive and disruptive. Verify that Lesser Restoration or Cure Wounds cannot solve the problem first.
- Do not restore to a previous known-good state without checking whether that state had its own problems. Rolling back is not the same as restoring.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/greater-restoration assess this [system/codebase/database] for accumulated damage and design a comprehensive restoration plan
```
