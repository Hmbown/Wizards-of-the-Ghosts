---
name: see-invisibility
description: "In D&D, See Invisibility lets you see creatures and objects that have been made invisible. The real-world version is revealing deliberate obscurity: finding the hidden costs in a pricing page, uncovering the actual terms buried in a EULA, identifying the obfuscated tracking in a codebase, or surfacing the real behavior behind a misleading UI. Unlike Perception (which notices what is overlooked) or True Seeing (which pierces all illusion), See Invisibility specifically targets things that were hidden on purpose."
user-invocable: true
---

# See Invisibility

Reveal what has been deliberately hidden, obscured, or made hard to find.

## Overview

See Invisibility is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: See Invisibility (spell)

Provider target: OpenClaw

## When To Use

- You suspect something is being deliberately hidden or obscured: hidden fees, buried terms, obfuscated code, or misleading UI.
- A system or document seems designed to make certain information hard to find.
- You want to audit a product, contract, or codebase for deliberately obscured behavior.

## Workflow

1. Identify the context where something might be deliberately hidden.
2. Look for the signs of intentional obscurity: complexity that serves no user, deep nesting, misleading labels, dark patterns.
3. Extract and surface what was hidden, with evidence of the obscuring mechanism.
4. Deliver the findings with a clear distinction between confirmed hidden elements and suspicious-but-unconfirmed patterns.

## Deliverables

- A list of deliberately hidden or obscured elements, with the mechanism used to hide each one.
- Evidence for each finding: why this appears intentionally hidden rather than merely overlooked.

## Guardrails

- Distinguish between intentional obscurity and accidental complexity. Not everything hard to find was hidden on purpose.
- Do not assume malice without evidence. Surface the hidden elements and let the user judge intent.

## Default Invocation

Use \$see-invisibility to audit this [product/contract/codebase/page] for deliberately hidden or obscured elements. What has been made hard to find on purpose?

