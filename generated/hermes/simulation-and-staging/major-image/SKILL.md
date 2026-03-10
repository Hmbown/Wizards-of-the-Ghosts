---
name: major-image
description: "In D&D, Major Image creates a multi-sensory illusion — visual, auditory, thermal, even olfactory — that persists and can be animated. It is convincing enough that creatures must actively investigate to see through it. The real-world version is the interactive prototype: the demo that makes stakeholders ask 'wait, is this real?' The answer is no, but the conviction is the point. Clickable Figma prototypes, scenario simulations, pitch decks with working demos, preview environments with synthetic data. Major Image is the spell that sells a future state before it is built."
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
# Major Image
Build a full interactive simulation that looks and feels real — but is not.
## What This Skill Does
In D&D, Major Image creates a multi-sensory illusion — visual, auditory, thermal, even olfactory — that persists and can be animated. It is convincing enough that creatures must actively investigate to see through it. The real-world version is the interactive prototype: the demo that makes stakeholders ask 'wait, is this real?' The answer is no, but the conviction is the point. Clickable Figma prototypes, scenario simulations, pitch decks with working demos, preview environments with synthetic data. Major Image is the spell that sells a future state before it is built.
In this grimoire, Major Image is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Major Image (spell).
## When To Use

- Stakeholders need to experience a proposed feature, product, or workflow before committing to build it.
- A pitch, demo, or presentation needs a working simulation rather than slides.
- Scenario planning requires a realistic preview of how a system would behave under specific conditions.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Define what the illusion needs to demonstrate — the core experience, not every edge case.
3. Choose the simulation medium: interactive prototype, synthetic demo environment, scenario walkthrough, or animated preview.
4. Build the simulation with enough fidelity to be convincing but do not over-engineer the scaffolding.
5. Present the illusion with clear framing: this is a simulation of how it would work, not a working system.
6. Capture decisions made based on the simulation and translate them into real implementation requirements.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- An interactive simulation or prototype that demonstrates the proposed experience.
- Clear documentation of what is real and what is simulated.
- A decision log: what the simulation revealed and what was decided based on it.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Always disclose that a simulation is a simulation. Passing off a prototype as a working product is fraud, not magic.
- Do not simulate outcomes you cannot actually deliver. If the demo promises capabilities the real system will not have, the illusion is a lie.
- Simulations with synthetic user data must be clearly marked — never mix synthetic data with real data.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/major-image build an interactive simulation, clickable prototype, or scenario preview that demonstrates a proposed experience convincingly enough to drive real decisions
```
