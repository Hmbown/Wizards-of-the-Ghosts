---
name: foresight
description: "Foresight produces bounded forecasts with explicit uncertainty to guide decisions. It is NOT:\n- Preflight checks: Verifying prerequisites before executing a known action (disk space, backups, connection strings). Those are safety gates, not forecasts.\n- Diagnosis/Debugging: Finding what's broken right now (null pointers, deprecated APIs). Those are root-cause analyses, not predictions.\n- Monitoring: Watching real-time metrics or alerting on thresholds. Those are observability tasks, not forward-looking estimates.\n- Reconnaissance: Gathering facts about competitors or systems. Intelligence gathering feeds foresight but isn't foresight itself. Key distinction: If the user wants to know \"what will likely happen if we choose X,\" use Foresight. If they want to know \"is it safe to run X now,\" \"what's broken,\" or \"what are they doing,\" use a different spell."
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
      - investigation-and-preparation
      - analysis
      - discovery
      - translation
      - preflight
---
# Foresight
Estimate likely outcomes before committing to a plan, change, or launch.
## What This Skill Does
Foresight produces bounded forecasts with explicit uncertainty to guide decisions. It is NOT:
- Preflight checks: Verifying prerequisites before executing a known action (disk space, backups, connection strings). Those are safety gates, not forecasts.
- Diagnosis/Debugging: Finding what's broken right now (null pointers, deprecated APIs). Those are root-cause analyses, not predictions.
- Monitoring: Watching real-time metrics or alerting on thresholds. Those are observability tasks, not forward-looking estimates.
- Reconnaissance: Gathering facts about competitors or systems. Intelligence gathering feeds foresight but isn't foresight itself. Key distinction: If the user wants to know "what will likely happen if we choose X," use Foresight. If they want to know "is it safe to run X now," "what's broken," or "what are they doing," use a different spell.
In this grimoire, Foresight is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Foresight (spell).
## When To Use

- Activate this spell when the user asks for a forward-looking, probability-weighted forecast to inform a decision. Look for:
- Explicit choice between options ("should we X or Y?", "migrate vs stay", "build vs buy")
- Time-bounded outcome requests ("over the next 12 months", "by Q3", "18-month trajectory")
- Risk/uncertainty language ("risk-weighted", "confidence level", "probability", "best case/worst case", "weal or woe")
- Decision frameworks with explicit unknowns ("what would change your recommendation?", "decisive unknowns")

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Scope the decision: Restate the choice, the time horizon, and what success/failure looks like.
3. Map the paths: List the strongest upside and downside scenarios for each option.
4. Estimate from evidence: Assign likelihoods based on current data, not vibes. State your assumptions explicitly.
5. Return the forecast: Deliver (a) a recommendation with confidence level, (b) a short risk matrix, and (c) the decisive unknowns that would change the call.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- Recommendation: [clear choice] (Confidence: X%) Assumptions: [what you're basing this on]
- | Path | Upside | Downside | Likelihood |
- Decisive Unknowns: [1-3 things that would change this call] ```

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Do not use for: "Check if the backup completed before I run this" → Preflight
- Do not use for: "Find all deprecated API calls in our codebase" → Scan/Diagnosis
- Do not use for: "Alert me if error rates exceed 2% this hour" → Monitoring
- Do not use for: "What features is our competitor shipping?" → Reconnaissance
- Do not use for: "Why is this function throwing a null pointer?" → Diagnosis
- Do not use for: Activate only when the core request is forecasting outcomes to inform a choice under uncertainty.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/foresight evaluate this decision, give me the likely upside and downside, and tell me what would change your call
```
