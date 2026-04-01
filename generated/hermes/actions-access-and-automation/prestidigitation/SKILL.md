---
name: prestidigitation
description: "Prestidigitation transforms. It does not fix, build, scaffold, migrate, or actuate. If the user says \"make this look better\" or \"convert this to that format\" — use prestidigitation. If the user says \"make this work\" or \"set this up\" or \"build this system\" — use something else."
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
Prestidigitation transforms. It does not fix, build, scaffold, migrate, or actuate. If the user says "make this look better" or "convert this to that format" — use prestidigitation. If the user says "make this work" or "set this up" or "build this system" — use something else.
In this grimoire, Prestidigitation is treated as a hybrid spell with a shipping-now delivery profile.
Canonical reference input: Prestidigitation (spell).
## When To Use

- Trigger this spell when the request contains:
- Format/transform verbs: reformat, convert, sort, strip, encode, decode, tidy, clean, pretty-print
- Scale qualifiers: quick, just, small, one-off, throwaway, simple, nothing fancy, straightforward
- Artifact types: a table, a list, a single file, a string, a UUID, a snippet, a blob
- Bounded counts: "about 20", "10 rows", "5 columns", "one line", "a few"
- The task is cantrip-scale when all three are true:
- The input fits in a single message or small file
- The output is a single artifact (text, table, string, file)

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Scope check: Confirm the task is single-input → single-output. If it spans multiple files or needs external services, stop and recommend the correct spell.
3. Execute directly: Perform the transformation in-session. Do not create scaffolding, config files, or helper scripts. Do the work, do not build the tool to do the work.
4. Return result: Output the artifact immediately. Add one sentence explaining what was done.
5. Escalate if needed: If mid-execution the task reveals hidden complexity (nested edge cases, data too large, ambiguous requirements), stop and name the appropriate full spell.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- The completed small artifact, fix, or transformation.
- A one-line note on what was done.
- A flag if the task was actually bigger than it looked.

## Pitfalls / Guardrails

- Keep the theatrical framing, but name the concrete mechanism that makes the skill useful right now.
- Do not use for: These look similar but belong to other spells:
- Do not use for: | Looks like prestidigitation | Actually is | Why | |---|---|---| | "Fix the broken nginx config" | Debug/repair spell | Something is broken and needs diagnosis, not just reformatted | | "Set up Prettier + ESLint + pre-commit hooks" | Scaffolding spell | Multi-tool infrastructure setup, not a one-off transform | | "Convert our entire codebase from Python 2 to 3" | Migration spell | Hundreds of files, structural change, not a quick trick | | "Build a data visualization dashboard" | Build spell | Multi-component system with interactivity, not a single artifact | | "Create a fake dashboard that looks real" | Illusion/deception spell | Intent is to deceive, not to transform | | "Turn on the lights, set thermostat" | Device actuation spell | Physical world control, not text/data manipulation |
- Do not use for: Rule of thumb: if the task requires reading multiple files, writing to multiple locations, installing dependencies, or touching infrastructure — it is not prestidigitation.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check which parts are concrete actions versus framing, so the user can tell what is real now.

## Example Invocation
```text
/prestidigitation handle this quick task cleanly, without over-engineering it
```
