---
name: perception
description: "In D&D, Perception is the raw ability to notice things: the hidden door, the faint sound, the detail that does not belong. Unlike Investigation (which follows evidence methodically) or Insight (which reads subtext), Perception is about the initial act of noticing. The real-world version is detail-catching: spotting the typo in the contract, the anomaly in the dashboard, the one metric that moved when it should not have, the thing that is present but no one is looking at."
user-invocable: true
---

# Perception

Notice what is actually there, especially the details everyone else missed.

## Overview

Perception is interpreted here as a metaphorical skill with a shipping-now execution model.

Canonical source: Perception (skill)

Provider target: OpenClaw

## When To Use

- You need a fresh pair of eyes on something — a document, dashboard, codebase, or design — to catch what is being overlooked.
- Something feels off but you cannot articulate what. You need systematic observation to find the anomaly.
- A review or audit needs to prioritize what to look at: where are the details most likely to matter?

## Workflow

1. Scan the full surface: read the whole thing, not just the parts that seem important.
2. Flag anomalies: anything that does not pattern-match with its surroundings. Typos, inconsistencies, outlier values, broken symmetries.
3. Rank by consequence: which noticed details actually matter vs. which are cosmetic?
4. Deliver the perception report: what was noticed, why it stands out, and whether it warrants action.

## Deliverables

- A list of noticed anomalies, inconsistencies, or overlooked details ranked by likely consequence.
- For each finding: why it stands out and whether it requires action or is merely notable.

## Guardrails

- Perception reports what is there, not what it means. Interpretation is a different skill (Insight, Investigation). Do not over-interpret raw observations.
- Do not generate false positives for thoroughness. If nothing is wrong, saying so is the correct perception check.

## Default Invocation

Use $perception to scan this [document/dashboard/codebase/design] with fresh eyes. What details are being overlooked? What does not belong?

