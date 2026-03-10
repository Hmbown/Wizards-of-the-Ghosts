---
name: programmed-illusion
description: "In D&D, Programmed Illusion creates an illusion that lies dormant until a specific trigger condition is met, then plays out its scene automatically. The real-world version is the conditional demo, automated preview, or triggered walkthrough: onboarding flows that appear when a user first visits, contextual tooltips that activate on hover, preview environments that spin up on pull request, automated scenario presentations that play when specific data conditions are detected. Programmed Illusion is the illusion that does not need a wizard present to cast it."
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
# Programmed Illusion
Set up an illusion that activates automatically when conditions are met.
## What This Skill Does
In D&D, Programmed Illusion creates an illusion that lies dormant until a specific trigger condition is met, then plays out its scene automatically. The real-world version is the conditional demo, automated preview, or triggered walkthrough: onboarding flows that appear when a user first visits, contextual tooltips that activate on hover, preview environments that spin up on pull request, automated scenario presentations that play when specific data conditions are detected. Programmed Illusion is the illusion that does not need a wizard present to cast it.
In this grimoire, Programmed Illusion is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Programmed Illusion (spell).
## When To Use

- A demo, tutorial, or preview should activate automatically based on user behavior or system state.
- Onboarding flows, contextual help, or guided walkthroughs need to trigger on specific conditions.
- Preview environments or scenario simulations should spin up automatically in response to events.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Define the trigger condition: what event, state, or behavior should activate the illusion.
3. Design the illusion sequence: what plays out when the trigger fires.
4. Implement the trigger mechanism and the illusion payload.
5. Test that the illusion activates correctly and does not fire on false conditions.
6. Set an expiry or review cycle — programmed illusions should not persist forever without review.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A triggered illusion or automated demo with clear activation conditions.
- Documentation of the trigger condition and the illusion sequence.
- A review schedule to assess whether the programmed illusion is still relevant.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Programmed illusions that trigger on user behavior must be disclosed — surprise popups and unsolicited walkthroughs are a dark pattern if hidden.
- Triggered demos must not impersonate real system state. If a preview environment looks like production, label it.
- Set expiry dates. Forgotten programmed illusions that fire on outdated conditions create confusion.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/programmed-illusion create an automated demo, triggered walkthrough, or conditional preview that activates when specific conditions are met — without requiring someone to run it manually
```
