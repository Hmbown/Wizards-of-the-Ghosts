---
name: see-invisibility
description: "In D&D, See Invisibility lets you see creatures and objects that have been made invisible. The real-world version is revealing deliberate obscurity: finding the hidden costs in a pricing page, uncovering the actual terms buried in a EULA, identifying the obfuscated tracking in a codebase, or surfacing the real behavior behind a misleading UI. Unlike Perception (which notices what is overlooked) or True Seeing (which pierces all illusion), See Invisibility specifically targets things that were hidden on purpose."
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
# See Invisibility
Reveal what has been deliberately hidden, obscured, or made hard to find.
## What This Skill Does
In D&D, See Invisibility lets you see creatures and objects that have been made invisible. The real-world version is revealing deliberate obscurity: finding the hidden costs in a pricing page, uncovering the actual terms buried in a EULA, identifying the obfuscated tracking in a codebase, or surfacing the real behavior behind a misleading UI. Unlike Perception (which notices what is overlooked) or True Seeing (which pierces all illusion), See Invisibility specifically targets things that were hidden on purpose.
In this grimoire, See Invisibility is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: See Invisibility (spell).
## When To Use

- You suspect something is being deliberately hidden or obscured: hidden fees, buried terms, obfuscated code, or misleading UI.
- A system or document seems designed to make certain information hard to find.
- You want to audit a product, contract, or codebase for deliberately obscured behavior.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify the context where something might be deliberately hidden.
3. Look for the signs of intentional obscurity: complexity that serves no user, deep nesting, misleading labels, dark patterns.
4. Extract and surface what was hidden, with evidence of the obscuring mechanism.
5. Deliver the findings with a clear distinction between confirmed hidden elements and suspicious-but-unconfirmed patterns.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A list of deliberately hidden or obscured elements, with the mechanism used to hide each one.
- Evidence for each finding: why this appears intentionally hidden rather than merely overlooked.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Distinguish between intentional obscurity and accidental complexity. Not everything hard to find was hidden on purpose.
- Do not assume malice without evidence. Surface the hidden elements and let the user judge intent.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/see-invisibility Use \$see-invisibility to audit this [product/contract/codebase/page] for deliberately hidden or obscured elements. What has been made hard to find on purpose?
```
