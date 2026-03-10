---
name: silent-image
description: "In D&D, Silent Image creates a purely visual illusion — no sound, no smell, no substance. It looks real but falls apart if you interact with it. The real-world version is the static design comp: a high-fidelity visual mockup that shows exactly what something will look like but does nothing when you click it. Figma frames without prototyping links, screenshot mockups, rendered previews, static architecture diagrams. Silent Image is faster than Major Image because it skips interactivity. Use it when the only question is what does it look like."
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
      - simulation-and-staging
      - simulation
      - staging
      - mockup
      - testing
---
# Silent Image
Create a static visual mockup — no interaction, no sound, just the picture.
## What This Skill Does
In D&D, Silent Image creates a purely visual illusion — no sound, no smell, no substance. It looks real but falls apart if you interact with it. The real-world version is the static design comp: a high-fidelity visual mockup that shows exactly what something will look like but does nothing when you click it. Figma frames without prototyping links, screenshot mockups, rendered previews, static architecture diagrams. Silent Image is faster than Major Image because it skips interactivity. Use it when the only question is what does it look like.
In this grimoire, Silent Image is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Silent Image (spell).
## When To Use

- The question is purely visual: what will it look like, how will it be laid out, what is the aesthetic?
- A static mockup or design comp is sufficient and interactivity would be over-investment.
- You need to communicate a visual design direction quickly without building a working prototype.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Clarify the visual question: layout, styling, content hierarchy, or aesthetic direction.
3. Create a static visual artifact: design comp, rendered mockup, annotated screenshot, or diagram.
4. Present it as a visual reference, not a functional prototype.
5. Gather visual feedback and iterate on the design before investing in interactivity.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A static visual artifact: design comp, mockup, or rendered preview.
- Annotations explaining any visual decisions that are not self-evident.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Do not present static mockups as interactive prototypes. If stakeholders will try to click, use Major Image instead.
- Static visuals that represent real data must be clearly marked as illustrations, not live dashboards.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/silent-image create a static visual mockup or design comp that answers the question what will this look like without investing in interactivity
```
