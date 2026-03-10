---
name: programmed-illusion
description: "In D&D, Programmed Illusion creates an illusion that lies dormant until a specific trigger condition is met, then plays out its scene automatically. The real-world version is the conditional demo, automated preview, or triggered walkthrough: onboarding flows that appear when a user first visits, contextual tooltips that activate on hover, preview environments that spin up on pull request, automated scenario presentations that play when specific data conditions are detected. Programmed Illusion is the illusion that does not need a wizard present to cast it."
user-invocable: true
---

# Programmed Illusion

Set up an illusion that activates automatically when conditions are met.

## Overview

Programmed Illusion is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Programmed Illusion (spell)

Provider target: OpenClaw

## When To Use

- A demo, tutorial, or preview should activate automatically based on user behavior or system state.
- Onboarding flows, contextual help, or guided walkthroughs need to trigger on specific conditions.
- Preview environments or scenario simulations should spin up automatically in response to events.

## Workflow

1. Define the trigger condition: what event, state, or behavior should activate the illusion.
2. Design the illusion sequence: what plays out when the trigger fires.
3. Implement the trigger mechanism and the illusion payload.
4. Test that the illusion activates correctly and does not fire on false conditions.
5. Set an expiry or review cycle — programmed illusions should not persist forever without review.

## Deliverables

- A triggered illusion or automated demo with clear activation conditions.
- Documentation of the trigger condition and the illusion sequence.
- A review schedule to assess whether the programmed illusion is still relevant.

## Guardrails

- Programmed illusions that trigger on user behavior must be disclosed — surprise popups and unsolicited walkthroughs are a dark pattern if hidden.
- Triggered demos must not impersonate real system state. If a preview environment looks like production, label it.
- Set expiry dates. Forgotten programmed illusions that fire on outdated conditions create confusion.

## Default Invocation

Use $programmed-illusion to create an automated demo, triggered walkthrough, or conditional preview that activates when specific conditions are met — without requiring someone to run it manually.

