---
name: hallucinatory-terrain
description: "In D&D, Hallucinatory Terrain makes natural terrain look like a different kind of terrain — a field appears as a forest, a hill appears as a valley. The underlying terrain is unchanged; only the perception shifts. The real-world version is environment staging: test environments styled to look like production, sandbox databases seeded with realistic data, training simulations that overlay a learning scenario onto real infrastructure. Hallucinatory Terrain does not change the real system. It changes how the system appears so you can test, train, or demo safely."
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
# Hallucinatory Terrain
Overlay a different reality onto an existing environment for testing or training.
## What This Skill Does
In D&D, Hallucinatory Terrain makes natural terrain look like a different kind of terrain — a field appears as a forest, a hill appears as a valley. The underlying terrain is unchanged; only the perception shifts. The real-world version is environment staging: test environments styled to look like production, sandbox databases seeded with realistic data, training simulations that overlay a learning scenario onto real infrastructure. Hallucinatory Terrain does not change the real system. It changes how the system appears so you can test, train, or demo safely.
In this grimoire, Hallucinatory Terrain is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Hallucinatory Terrain (spell).
## When To Use

- You need a test environment that looks and behaves like production without touching real data.
- Training scenarios require realistic context overlaid onto safe infrastructure.
- A demo or presentation needs to show a real-looking environment without exposing actual systems.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify the real environment to overlay and the illusory version you need it to resemble.
3. Build the overlay: seed synthetic data, configure staging environments, or create training scenarios.
4. Verify the illusion is convincing enough for its purpose.
5. Ensure clear separation between the overlay and the real environment.
6. Document which parts are real and which are illusory.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A staged environment overlaying the real one with synthetic or simulated content.
- Clear documentation of what is real infrastructure vs. illusory overlay.
- Separation guarantees: evidence that the overlay cannot contaminate the real environment.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Never let hallucinatory environments contaminate production. The overlay must be fully isolated.
- Synthetic data in staged environments must not contain real personal information.
- Always label staged environments clearly — engineers who mistake staging for production cause real incidents.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/hallucinatory-terrain create a staged environment that overlays realistic synthetic content onto safe infrastructure for testing, training, or demo purposes
```
