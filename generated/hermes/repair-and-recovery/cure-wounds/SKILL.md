---
name: cure-wounds
description: "In D&D, Cure Wounds heals damage through touch — direct, immediate, hands-on. The real-world version is the hotfix: diagnosing the immediate problem and applying the minimum viable fix to restore function. Not a redesign, not a refactor, not a root-cause analysis — just stop the bleeding right now."
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
In D&D, Cure Wounds heals damage through touch — direct, immediate, hands-on. The real-world version is the hotfix: diagnosing the immediate problem and applying the minimum viable fix to restore function. Not a redesign, not a refactor, not a root-cause analysis — just stop the bleeding right now.
In this grimoire, Cure Wounds is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Cure Wounds (spell).
## When To Use

- Something is broken right now and needs a fix before further damage occurs.
- The priority is restoring function, not understanding root cause (that comes after).
- A production issue, broken build, or failing pipeline needs immediate hands-on intervention.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify the immediate symptom: what exactly is broken?
3. Diagnose the proximate cause: what changed or failed to cause this specific breakage?
4. Apply the minimum fix that restores function without introducing new risks.
5. Verify the fix works and document it for follow-up root-cause analysis.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- The fix: the specific change that stops the bleeding.
- A brief note on what caused the breakage and whether deeper investigation is needed.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Cure Wounds is triage, not treatment. Always note whether root-cause analysis is still needed after the immediate fix.
- The minimum fix should not make the underlying problem harder to diagnose. Preserve evidence.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/cure-wounds diagnose and fix this [broken build/failing service/production issue] with the minimum change needed to restore function
```
