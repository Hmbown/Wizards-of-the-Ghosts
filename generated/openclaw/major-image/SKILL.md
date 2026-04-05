---
name: major-image
description: "In D&D, Major Image creates a multi-sensory illusion — visual, auditory, thermal, even olfactory — that persists and can be animated. It is convincing enough that creatures must actively investigate to see through it. The real-world version is the interactive prototype: the demo that makes stakeholders ask 'wait, is this real?' The answer is no, but the conviction is the point. Clickable Figma prototypes, scenario simulations, pitch decks with working demos, preview environments with synthetic data. Major Image is the spell that sells a future state before it is built."
user-invocable: true
---

# Major Image

Build a full interactive simulation that looks and feels real — but is not.

## Overview

Major Image is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Major Image (spell)

Provider target: OpenClaw

## When To Use

- Stakeholders need to experience a proposed feature, product, or workflow before committing to build it.
- A pitch, demo, or presentation needs a working simulation rather than slides.
- Scenario planning requires a realistic preview of how a system would behave under specific conditions.

## Workflow

1. Define what the illusion needs to demonstrate — the core experience, not every edge case.
2. Choose the simulation medium: interactive prototype, synthetic demo environment, scenario walkthrough, or animated preview.
3. Build the simulation with enough fidelity to be convincing but do not over-engineer the scaffolding.
4. Present the illusion with clear framing: this is a simulation of how it would work, not a working system.
5. Capture decisions made based on the simulation and translate them into real implementation requirements.

## Deliverables

- An interactive simulation or prototype that demonstrates the proposed experience.
- Clear documentation of what is real and what is simulated.
- A decision log: what the simulation revealed and what was decided based on it.

## Guardrails

- Always disclose that a simulation is a simulation. Passing off a prototype as a working product is fraud, not magic.
- Do not simulate outcomes you cannot actually deliver. If the demo promises capabilities the real system will not have, the illusion is a lie.
- Simulations with synthetic user data must be clearly marked — never mix synthetic data with real data.

## Default Invocation

Use $major-image to build an interactive simulation, clickable prototype, or scenario preview that demonstrates a proposed experience convincingly enough to drive real decisions.

