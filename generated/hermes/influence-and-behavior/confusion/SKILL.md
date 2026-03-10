---
name: confusion
description: "Confusion makes targets act randomly and unpredictably. The real-world version is chaos engineering: injecting controlled randomness, unexpected inputs, and edge cases to discover how systems behave when things go wrong. This is fuzzing, monkey testing, and the art of breaking things on purpose so they do not break by accident."
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
      - influence-and-behavior
      - influence
      - behavior
      - attention
      - engagement
---
# Confusion
Generate controlled chaos to stress-test a system's resilience.
## What This Skill Does
Confusion makes targets act randomly and unpredictably. The real-world version is chaos engineering: injecting controlled randomness, unexpected inputs, and edge cases to discover how systems behave when things go wrong. This is fuzzing, monkey testing, and the art of breaking things on purpose so they do not break by accident.
In this grimoire, Confusion is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Confusion (spell).
## When To Use

- You want to stress-test a system, API, or workflow with unexpected inputs and edge cases.
- A process works perfectly under ideal conditions and you need to know how it fails under chaos.
- You need to generate adversarial test cases, random inputs, or edge-case scenarios.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify the system, API, workflow, or process to stress-test.
3. Generate a set of chaotic inputs: edge cases, malformed data, race conditions, unexpected sequences.
4. Predict how each chaotic input should be handled (graceful degradation, error, recovery).
5. Deliver the chaos test suite with expected vs. worst-case outcomes for each scenario.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A chaos test suite: specific adversarial inputs, edge cases, and unexpected scenarios.
- Expected behavior for each scenario: how the system should handle it vs. how it might fail.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Chaos must be controlled. Always define blast radius and rollback procedures before injecting randomness.
- Do not generate chaos for production systems without explicit safety gates and authorization.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/confusion generate a chaos test suite for this [system/API/workflow]. Give me the edge cases that will break it
```
