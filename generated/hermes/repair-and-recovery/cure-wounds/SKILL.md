---
name: cure-wounds
description: "Cure Wounds is the hotfix spell: immediate triage to stop bleeding and restore function. It is NOT root-cause analysis, refactoring, redesign, or long-term remediation. The goal is the minimum viable fix that stops the damage NOW. Deeper investigation comes after."
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
# Cure Wounds
Apply a targeted fix to stop the bleeding on an active problem.
## What This Skill Does
Cure Wounds is the hotfix spell: immediate triage to stop bleeding and restore function. It is NOT root-cause analysis, refactoring, redesign, or long-term remediation. The goal is the minimum viable fix that stops the damage NOW. Deeper investigation comes after.
In this grimoire, Cure Wounds is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Cure Wounds (spell).
## When To Use

- Active breakage: crashes, errors, failures, outages, data loss, blocked users
- Urgency markers: "right now", "immediately", "production down", "losing money", "users can't", "team blocked"
- Time-sensitive impact: revenue loss, customer complaints, SLA breach, on-call pages
- Recent-change correlation: "after the deploy", "since the update", "broke 10 minutes ago"
- Minimum-intervention request: "stop the bleeding", "quick fix", "get it working", "restore function"

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify the symptom: What exactly is failing? What error, crash, or outage is happening?
3. Diagnose the proximate cause: What changed or failed to produce this breakage? Check recent deploys, config changes, or environmental shifts.
4. Apply the minimum fix: The smallest change that restores function. Rollback, patch, restart, or reconfigure — whatever stops the bleeding with least risk.
5. Verify and document: Confirm the fix works. Note what caused the breakage and whether root-cause analysis is still needed.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- The fix: the specific change that stops the bleeding.
- A brief note on what caused the breakage and whether deeper investigation is needed.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Cure Wounds is triage, not treatment. Always flag whether deeper investigation is needed after the fix.
- Preserve evidence: the minimum fix must not make the underlying problem harder to diagnose.
- If the fix requires significant redesign or architectural change, this is the wrong spell.
- Do not use for: Planned work: migrations, refactors, feature development, schema redesigns
- Do not use for: Long-term degradation: "slowly getting worse", "needs comprehensive plan", "technical debt"
- Do not use for: Presentation/formatting: reformatting logs, cleaning output, improving readability
- Do not use for: Trivial typos: single-character corrections in config (use basic editing, not triage)
- Do not use for: Communication only: "send a message", "notify the team", "update status"
- Do not use for: Feature flag state issues: configuration toggles without active breakage
- Do not use for: Root-cause analysis requests: "why did this happen", "investigate the underlying issue"

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/cure-wounds diagnose and fix this [broken build/failing service/production issue] with the minimum change needed to restore function
```
