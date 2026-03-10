---
name: perception
description: "In D&D, Perception is the raw ability to notice things: the hidden door, the faint sound, the detail that does not belong. Unlike Investigation (which follows evidence methodically) or Insight (which reads subtext), Perception is about the initial act of noticing. The real-world version is detail-catching: spotting the typo in the contract, the anomaly in the dashboard, the one metric that moved when it should not have, the thing that is present but no one is looking at."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - skill
      - shipping-now
      - metaphorical
      - investigation-and-preparation
      - analysis
      - discovery
      - translation
      - preflight
---
# Perception
Notice what is actually there, especially the details everyone else missed.
## What This Skill Does
In D&D, Perception is the raw ability to notice things: the hidden door, the faint sound, the detail that does not belong. Unlike Investigation (which follows evidence methodically) or Insight (which reads subtext), Perception is about the initial act of noticing. The real-world version is detail-catching: spotting the typo in the contract, the anomaly in the dashboard, the one metric that moved when it should not have, the thing that is present but no one is looking at.
In this grimoire, Perception is treated as a metaphorical skill with a shipping-now delivery profile.
Canonical reference input: Perception (skill).
## When To Use

- You need a fresh pair of eyes on something — a document, dashboard, codebase, or design — to catch what is being overlooked.
- Something feels off but you cannot articulate what. You need systematic observation to find the anomaly.
- A review or audit needs to prioritize what to look at: where are the details most likely to matter?

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Scan the full surface: read the whole thing, not just the parts that seem important.
3. Flag anomalies: anything that does not pattern-match with its surroundings. Typos, inconsistencies, outlier values, broken symmetries.
4. Rank by consequence: which noticed details actually matter vs. which are cosmetic?
5. Deliver the perception report: what was noticed, why it stands out, and whether it warrants action.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A list of noticed anomalies, inconsistencies, or overlooked details ranked by likely consequence.
- For each finding: why it stands out and whether it requires action or is merely notable.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Perception reports what is there, not what it means. Interpretation is a different skill (Insight, Investigation). Do not over-interpret raw observations.
- Do not generate false positives for thoroughness. If nothing is wrong, saying so is the correct perception check.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/perception scan this [document/dashboard/codebase/design] with fresh eyes. What details are being overlooked? What does not belong?
```
