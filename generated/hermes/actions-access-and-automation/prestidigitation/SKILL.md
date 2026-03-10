---
name: prestidigitation
description: "Use this cantrip for small acts of practical magic: reformat some text, clean a small dataset, generate a quick chart, convert a unit, tidy a file, or produce a one-off artifact."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - shipping-now
      - hybrid
      - actions-access-and-automation
      - execution
      - automation
      - access
      - actuation
---
# Prestidigitation
Handle quick, low-stakes utility tasks that do not deserve a full spell.
## What This Skill Does
Use this cantrip for small acts of practical magic: reformat some text, clean a small dataset, generate a quick chart, convert a unit, tidy a file, or produce a one-off artifact.
In this grimoire, Prestidigitation is treated as a hybrid spell with a shipping-now delivery profile.
Canonical reference input: Prestidigitation (spell).
## When To Use

- The task is small, self-contained, and not worth a dedicated workflow.
- You need a quick formatting fix, unit conversion, data cleanup, or throwaway generation.
- The ask is closer to a party trick than a serious project - and that is fine.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Accept the small task and confirm it is actually cantrip-scale.
3. Perform the trick directly, without over-engineering scaffolding or process.
4. Return the result immediately with a brief note on what was done.
5. If the task turns out to be larger than cantrip-scale, say so and recommend the appropriate spell.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- The completed small artifact, fix, or transformation.
- A one-line note on what was done.
- A flag if the task was actually bigger than it looked.

## Pitfalls / Guardrails

- Keep the theatrical framing, but name the concrete mechanism that makes the skill useful right now.
- Do not let prestidigitation scope-creep into a full project. If the task needs real work, name the right spell instead.
- Quick does not mean careless - even small tricks should be correct.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check which parts are concrete actions versus framing, so the user can tell what is real now.

## Example Invocation
```text
/prestidigitation handle this quick task cleanly, without over-engineering it
```
