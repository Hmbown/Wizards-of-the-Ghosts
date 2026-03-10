---
name: deception
description: "Use this skill to generate believable synthetic artifacts for testing, demos, adversarial exercises, or rehearsal environments. The goal is plausibility under inspection by software and operators, not manipulation of real users or fabrication of evidence."
---

# Deception

Forge realistic stand-ins for systems, traffic, and data without misleading actual people.

## Overview

Deception is interpreted here as a metaphorical skill with a shipping-now execution model.

Canonical source: Deception (skill)

Provider target: OpenClaw

## When To Use

- You need fake data, demo traffic, or a mock environment that feels operationally real.
- Testing requires a plausible cover story, persona, or artifact without touching production.
- Smoke tests or drills work better when the synthetic inputs resemble actual conditions.

## Workflow

1. Identify which signals must look authentic and which markers must remain clearly synthetic.
2. Generate the stand-in artifacts and validate them against the target format, workflow, or constraint.
3. Return the synthetic set with labeling, isolation rules, and notes on what realism it is simulating.

## Deliverables

- A realistic synthetic dataset, script, or demo environment brief.
- Notes on the realism targets and what was intentionally faked.
- Isolation and labeling guidance so the artifacts cannot be mistaken for real records.

## Guardrails

- Never create content meant to impersonate real people, mislead customers, or support fraud.
- Clearly label synthetic artifacts in docs, headers, or test context even when the payload looks real.

## Default Invocation

Use $deception to create a plausible synthetic version of this scenario for testing or demo use, and label the lines I must not cross.

