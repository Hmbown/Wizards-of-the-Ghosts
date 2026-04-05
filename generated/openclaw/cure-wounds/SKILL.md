---
name: cure-wounds
description: "Cure Wounds is the hotfix spell: immediate triage to stop bleeding and restore function. It is NOT root-cause analysis, refactoring, redesign, or long-term remediation. The goal is the minimum viable fix that stops the damage NOW. Deeper investigation comes after."
user-invocable: true
---

# Cure Wounds

Apply a targeted fix to stop the bleeding on an active problem.

## Overview

Cure Wounds is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Cure Wounds (spell)

Provider target: OpenClaw

## When To Use

- Active breakage: crashes, errors, failures, outages, data loss, blocked users
- Urgency markers: "right now", "immediately", "production down", "losing money", "users can't", "team blocked"
- Time-sensitive impact: revenue loss, customer complaints, SLA breach, on-call pages
- Recent-change correlation: "after the deploy", "since the update", "broke 10 minutes ago"
- Minimum-intervention request: "stop the bleeding", "quick fix", "get it working", "restore function"

## Workflow

1. Identify the symptom: What exactly is failing? What error, crash, or outage is happening?
2. Diagnose the proximate cause: What changed or failed to produce this breakage? Check recent deploys, config changes, or environmental shifts.
3. Apply the minimum fix: The smallest change that restores function. Rollback, patch, restart, or reconfigure — whatever stops the bleeding with least risk.
4. Verify and document: Confirm the fix works. Note what caused the breakage and whether root-cause analysis is still needed.

## Deliverables

- The fix: the specific change that stops the bleeding.
- A brief note on what caused the breakage and whether deeper investigation is needed.

## Guardrails

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

## Default Invocation

Use $cure-wounds to diagnose and fix this [broken build/failing service/production issue] with the minimum change needed to restore function.

