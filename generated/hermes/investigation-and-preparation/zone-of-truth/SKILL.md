---
name: zone-of-truth
description: "Enter a mode where every assertion is backed by evidence, confidence is calibrated, speculation is flagged, and hallucination is actively resisted."
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
Enter a mode where every assertion is backed by evidence, confidence is calibrated, speculation is flagged, and hallucination is actively resisted.
In this grimoire, Zone of Truth is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Zone of Truth (spell).
## When To Use

- Use $zone-of-truth ACTIVATED to signal the zone is active
- Include the custom phrase: "Switching into high-integrity mode: source every claim, label every uncertainty, flag anything speculative"
- High-stakes decisions requiring maximum epistemic rigor
- Conversation has drifted into speculation and needs reset to verified ground
- Need to clearly separate what is known, inferred, and guessed
- Roadmap debates, compliance verification, vendor claims, customer demand validation

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
- Error disclaimer: "This zone does not eliminate all error — it reduces unsourced assertions, not all mistakes."
- Normal mode defense: "Normal mode is not dishonest — this is about rigor, not trustworthiness."
- Absence of evidence caveat: "Absence of evidence ≠ evidence of absence — limited findings reflect documentation gaps, not necessarily reality."
- Include a two-part boundary:

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/zone-of-truth switch into high-integrity mode: source every claim, label every uncertainty, and flag anything speculative
```
