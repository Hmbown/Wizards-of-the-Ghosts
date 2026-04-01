---
name: greater-restoration
description: "Lesser Restoration = one thing is wrong, fix it directly (reset a flag, clear a cache, remove a curse).\nGreater Restoration = many things are wrong because they decayed together over time, and fixing one thing without fixing the others will fail."
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
Lesser Restoration = one thing is wrong, fix it directly (reset a flag, clear a cache, remove a curse).
Greater Restoration = many things are wrong because they decayed together over time, and fixing one thing without fixing the others will fail.
In this grimoire, Greater Restoration is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Greater Restoration (spell).
## When To Use

- Activate Greater Restoration when the user describes systemic degradation that accumulated over time and requires a comprehensive, multi-step restoration plan — not a hotfix.
- Time + decay: "over N months/years", "accumulated", "gradually degraded", "drift", "bloat", "sprawl"
- Multiplicity: multiple related problems listed (inconsistent configs, orphaned resources, stale artifacts)
- Scope words: "comprehensive", "systematic", "full audit", "restore to health", "clean and restore"
- Failure of incremental fixes: "no single fix will work", "triage is insufficient", "band-aids made it worse"
- Domains: schema drift, tech debt, IaC drift, alert fatigue, bloated images, tangled dependencies, stale flags, decayed docs, corrupted data pipelines

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Scope the degradation: Inventory all affected subsystems. How many? How interconnected? What does "healthy" look like?
3. Find the root cause(s): What introduced the decay? Is the cause still active (e.g., a broken CI step still running, a misconfig still applied)?
4. Design the restoration plan: Ordered steps with dependencies. What must be fixed first? What can be parallelized? Include verification checkpoints between stages.
5. Execute with checkpoints: Do NOT batch all changes without verification. Each stage must confirm improvement before proceeding.
6. Post-restoration health check: Confirm the system is back to full function. Document what changed and how to prevent recurrence.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A restoration plan: ordered steps to undo accumulated damage.
- Root-cause identification: what caused the degradation and how to prevent recurrence.
- A post-restoration health check confirming the system is back to full function.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Do not use for: Single incident/hotfix: "API crashing after deploy", "null pointer exception" → route to Cure Wounds or Lesser Restoration
- Do not use for: Simple toggle/reset: "circuit breaker tripped", "flag stuck enabled" → Lesser Restoration
- Do not use for: Resurrection from backup: "deleted account, restore from backup" → different spell (resurrection/backup-restore)
- Do not use for: Migration/relocation: "move from Heroku to AWS" → not restoration, it's relocation
- Do not use for: Self-healing/continuous: "auto-restart pods, maintain 99.99% uptime" → ongoing automation, not one-time restoration
- Do not use for: Preventive maintenance: "add monitoring", "set up linting" → proactive, not restorative

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/greater-restoration assess this [system/codebase/database] for accumulated damage and design a comprehensive restoration plan
```
