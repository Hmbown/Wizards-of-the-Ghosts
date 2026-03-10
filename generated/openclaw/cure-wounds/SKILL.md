---
name: cure-wounds
description: "In D&D, Cure Wounds heals damage through touch — direct, immediate, hands-on. The real-world version is the hotfix: diagnosing the immediate problem and applying the minimum viable fix to restore function. Not a redesign, not a refactor, not a root-cause analysis — just stop the bleeding right now."
user-invocable: true
---

# Cure Wounds

Apply a targeted fix to stop the bleeding on an active problem.

## Overview

Cure Wounds is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Cure Wounds (spell)

Provider target: OpenClaw

## When To Use

- Something is broken right now and needs a fix before further damage occurs.
- The priority is restoring function, not understanding root cause (that comes after).
- A production issue, broken build, or failing pipeline needs immediate hands-on intervention.

## Workflow

1. Identify the immediate symptom: what exactly is broken?
2. Diagnose the proximate cause: what changed or failed to cause this specific breakage?
3. Apply the minimum fix that restores function without introducing new risks.
4. Verify the fix works and document it for follow-up root-cause analysis.

## Deliverables

- The fix: the specific change that stops the bleeding.
- A brief note on what caused the breakage and whether deeper investigation is needed.

## Guardrails

- Cure Wounds is triage, not treatment. Always note whether root-cause analysis is still needed after the immediate fix.
- The minimum fix should not make the underlying problem harder to diagnose. Preserve evidence.

## Default Invocation

Use $cure-wounds to diagnose and fix this [broken build/failing service/production issue] with the minimum change needed to restore function.

