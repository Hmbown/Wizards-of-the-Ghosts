---
name: hallucinatory-terrain
description: "In D&D, Hallucinatory Terrain makes natural terrain look like a different kind of terrain — a field appears as a forest, a hill appears as a valley. The underlying terrain is unchanged; only the perception shifts. The real-world version is environment staging: test environments styled to look like production, sandbox databases seeded with realistic data, training simulations that overlay a learning scenario onto real infrastructure. Hallucinatory Terrain does not change the real system. It changes how the system appears so you can test, train, or demo safely."
user-invocable: true
---

# Hallucinatory Terrain

Overlay a different reality onto an existing environment for testing or training.

## Overview

Hallucinatory Terrain is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Hallucinatory Terrain (spell)

Provider target: OpenClaw

## When To Use

- You need a test environment that looks and behaves like production without touching real data.
- Training scenarios require realistic context overlaid onto safe infrastructure.
- A demo or presentation needs to show a real-looking environment without exposing actual systems.

## Workflow

1. Identify the real environment to overlay and the illusory version you need it to resemble.
2. Build the overlay: seed synthetic data, configure staging environments, or create training scenarios.
3. Verify the illusion is convincing enough for its purpose.
4. Ensure clear separation between the overlay and the real environment.
5. Document which parts are real and which are illusory.

## Deliverables

- A staged environment overlaying the real one with synthetic or simulated content.
- Clear documentation of what is real infrastructure vs. illusory overlay.
- Separation guarantees: evidence that the overlay cannot contaminate the real environment.

## Guardrails

- Never let hallucinatory environments contaminate production. The overlay must be fully isolated.
- Synthetic data in staged environments must not contain real personal information.
- Always label staged environments clearly — engineers who mistake staging for production cause real incidents.

## Default Invocation

Use $hallucinatory-terrain to create a staged environment that overlays realistic synthetic content onto safe infrastructure for testing, training, or demo purposes.

