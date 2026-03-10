---
name: deception
description: "Use this skill to generate believable synthetic artifacts for testing, demos, adversarial exercises, or rehearsal environments. The goal is plausibility under inspection by software and operators, not manipulation of real users or fabrication of evidence."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - skill
      - shipping-now
      - metaphorical
      - simulation-and-staging
      - simulation
      - staging
      - mockup
      - testing
---
# Deception
Forge realistic stand-ins for systems, traffic, and data without misleading actual people.
## What This Skill Does
Use this skill to generate believable synthetic artifacts for testing, demos, adversarial exercises, or rehearsal environments. The goal is plausibility under inspection by software and operators, not manipulation of real users or fabrication of evidence.
In this grimoire, Deception is treated as a metaphorical skill with a shipping-now delivery profile.
Canonical reference input: Deception (skill).
## When To Use

- You need fake data, demo traffic, or a mock environment that feels operationally real.
- Testing requires a plausible cover story, persona, or artifact without touching production.
- Smoke tests or drills work better when the synthetic inputs resemble actual conditions.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify which signals must look authentic and which markers must remain clearly synthetic.
3. Generate the stand-in artifacts and validate them against the target format, workflow, or constraint.
4. Return the synthetic set with labeling, isolation rules, and notes on what realism it is simulating.
5. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A realistic synthetic dataset, script, or demo environment brief.
- Notes on the realism targets and what was intentionally faked.
- Isolation and labeling guidance so the artifacts cannot be mistaken for real records.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Never create content meant to impersonate real people, mislead customers, or support fraud.
- Clearly label synthetic artifacts in docs, headers, or test context even when the payload looks real.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/deception create a plausible synthetic version of this scenario for testing or demo use, and label the lines I must not cross
```
