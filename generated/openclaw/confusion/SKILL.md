---
name: confusion
description: "Confusion makes targets act randomly and unpredictably. The real-world version is chaos engineering: injecting controlled randomness, unexpected inputs, and edge cases to discover how systems behave when things go wrong. This is fuzzing, monkey testing, and the art of breaking things on purpose so they do not break by accident."
user-invocable: true
---

# Confusion

Generate controlled chaos to stress-test a system's resilience.

## Overview

Confusion is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Confusion (spell)

Provider target: OpenClaw

## When To Use

- You want to stress-test a system, API, or workflow with unexpected inputs and edge cases.
- A process works perfectly under ideal conditions and you need to know how it fails under chaos.
- You need to generate adversarial test cases, random inputs, or edge-case scenarios.

## Workflow

1. Identify the system, API, workflow, or process to stress-test.
2. Generate a set of chaotic inputs: edge cases, malformed data, race conditions, unexpected sequences.
3. Predict how each chaotic input should be handled (graceful degradation, error, recovery).
4. Deliver the chaos test suite with expected vs. worst-case outcomes for each scenario.

## Deliverables

- A chaos test suite: specific adversarial inputs, edge cases, and unexpected scenarios.
- Expected behavior for each scenario: how the system should handle it vs. how it might fail.

## Guardrails

- Chaos must be controlled. Always define blast radius and rollback procedures before injecting randomness.
- Do not generate chaos for production systems without explicit safety gates and authorization.

## Default Invocation

Use $confusion to generate a chaos test suite for this [system/API/workflow]. Give me the edge cases that will break it.

