---
name: foresight
description: "Foresight produces bounded forecasts with explicit uncertainty to guide decisions. It is NOT:\n- Preflight checks: Verifying prerequisites before executing a known action (disk space, backups, connection strings). Those are safety gates, not forecasts.\n- Diagnosis/Debugging: Finding what's broken right now (null pointers, deprecated APIs). Those are root-cause analyses, not predictions.\n- Monitoring: Watching real-time metrics or alerting on thresholds. Those are observability tasks, not forward-looking estimates.\n- Reconnaissance: Gathering facts about competitors or systems. Intelligence gathering feeds foresight but isn't foresight itself. Key distinction: If the user wants to know \"what will likely happen if we choose X,\" use Foresight. If they want to know \"is it safe to run X now,\" \"what's broken,\" or \"what are they doing,\" use a different spell."
user-invocable: true
---

# Foresight

Estimate likely outcomes before committing to a plan, change, or launch.

## Overview

Foresight is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Foresight (spell)

Provider target: OpenClaw

## When To Use

- Activate this spell when the user asks for a forward-looking, probability-weighted forecast to inform a decision. Look for:
- Explicit choice between options ("should we X or Y?", "migrate vs stay", "build vs buy")
- Time-bounded outcome requests ("over the next 12 months", "by Q3", "18-month trajectory")
- Risk/uncertainty language ("risk-weighted", "confidence level", "probability", "best case/worst case", "weal or woe")
- Decision frameworks with explicit unknowns ("what would change your recommendation?", "decisive unknowns")

## Workflow

1. Scope the decision: Restate the choice, the time horizon, and what success/failure looks like.
2. Map the paths: List the strongest upside and downside scenarios for each option.
3. Estimate from evidence: Assign likelihoods based on current data, not vibes. State your assumptions explicitly.
4. Return the forecast: Deliver (a) a recommendation with confidence level, (b) a short risk matrix, and (c) the decisive unknowns that would change the call.

## Deliverables

- Recommendation: [clear choice] (Confidence: X%) Assumptions: [what you're basing this on]
- | Path | Upside | Downside | Likelihood |
- Decisive Unknowns: [1-3 things that would change this call] ```

## Guardrails

- Do not use for: "Check if the backup completed before I run this" → Preflight
- Do not use for: "Find all deprecated API calls in our codebase" → Scan/Diagnosis
- Do not use for: "Alert me if error rates exceed 2% this hour" → Monitoring
- Do not use for: "What features is our competitor shipping?" → Reconnaissance
- Do not use for: "Why is this function throwing a null pointer?" → Diagnosis
- Do not use for: Activate only when the core request is forecasting outcomes to inform a choice under uncertainty.

## Default Invocation

Use $foresight to evaluate this decision, give me the likely upside and downside, and tell me what would change your call.

