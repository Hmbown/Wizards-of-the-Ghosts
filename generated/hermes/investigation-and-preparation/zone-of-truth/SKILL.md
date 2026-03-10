---
name: zone-of-truth
description: "Use this spell to enter a mode where every assertion is backed by evidence, confidence is calibrated, speculation is flagged, and hallucination is actively resisted."
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
# Zone of Truth
Establish a high-integrity epistemic environment where claims must be sourced and uncertainty labeled.
## What This Skill Does
Use this spell to enter a mode where every assertion is backed by evidence, confidence is calibrated, speculation is flagged, and hallucination is actively resisted.
In this grimoire, Zone of Truth is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Zone of Truth (spell).
## When To Use

- You are making a high-stakes decision and need maximum epistemic rigor from the agent.
- A previous conversation has drifted into speculation and you want to reset to verified ground.
- You want the agent to clearly separate what it knows, what it infers, and what it is guessing.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Activate truth-zone discipline: all claims require sources or explicit confidence labels.
3. Re-examine any prior assertions in the conversation and flag unsupported ones.
4. For each new claim, provide the evidence basis or clearly mark it as inference, estimation, or speculation.
5. Maintain the zone until the user explicitly dismisses it or the conversation ends.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A conversation mode where every claim is sourced or confidence-labeled.
- A re-audit of prior unsupported assertions if the zone is activated mid-conversation.
- Clear visual markers distinguishing fact, inference, and speculation.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Do not claim this mode eliminates all error — it reduces unsourced assertions, not all mistakes.
- Do not use the zone framing to imply that the agent's normal mode is dishonest.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/zone-of-truth switch into high-integrity mode: source every claim, label every uncertainty, and flag anything speculative
```
