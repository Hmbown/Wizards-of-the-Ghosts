---
name: awaken
description: "Awaken gives a non-intelligent system a usable voice without pretending the underlying system became sentient. The real move is to wrap a thermostat, spreadsheet, legacy database, shell script, or crusty internal tool in a conversational or agent-like interface that exposes what it can already do. Good Awaken work turns buried affordances into accessible ones. Bad Awaken work hallucinates capabilities the substrate does not have. The spell is strongest when the wrapper is honest about its limits and preserves the original system's safety boundaries."
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
      - actions-access-and-automation
      - execution
      - automation
      - access
      - actuation
      - integration
      - home-assistant
---
# Awaken
Teach an old machine to answer back.
## What This Skill Does
Awaken gives a non-intelligent system a usable voice without pretending the underlying system became sentient. The real move is to wrap a thermostat, spreadsheet, legacy database, shell script, or crusty internal tool in a conversational or agent-like interface that exposes what it can already do. Good Awaken work turns buried affordances into accessible ones. Bad Awaken work hallucinates capabilities the substrate does not have. The spell is strongest when the wrapper is honest about its limits and preserves the original system's safety boundaries.
In this grimoire, Awaken is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Awaken (spell).
## When To Use

- A useful system exists already, but only through brittle commands, forms, or legacy interfaces.
- You want to add natural-language access, summarization, or guided actions on top of a dumb substrate.
- The real value is interface uplift, not rebuilding the underlying system from scratch.
- Your Home Assistant setup has devices that should activate together as a morning routine — lights, coffee maker, blinds, thermostat.

## Prerequisites

- Environment variables available to Hermes: `HA_URL`, `HA_TOKEN`.
- Primary credential or token: `HA_TOKEN`.
- Binaries on PATH: `curl`.

## Setup

1. Confirm the required environment variables are available inside the active Hermes runtime, not just in a shell profile.
2. Verify the required binaries resolve on PATH before you rely on them in a procedure.
3. Choose a non-production or low-risk target first if the skill can page, unlock, alert, or touch a live integration.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Inventory the system's real capabilities, constraints, and permissions before adding any language layer.
3. Design the conversational surface around concrete intents, mapped actions, and explicit fallbacks when the wrapper cannot comply.
4. Define how the wrapper reads state, executes approved actions, and explains failures in plain language.
5. Return an awakening plan with interface examples, backend bindings, and the limits that must stay visible to the user.
6. If Home Assistant is available, trigger a wake scene or automation via POST to /api/services/scene/turn_on or /api/services/automation/trigger with the appropriate entity_id.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- An interface-wrapping plan for the existing system.
- An intent-to-action map covering supported requests and fallback paths.
- A risk note describing what the wrapper must never imply or automate.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Do not present the wrapped system as more capable, autonomous, or reliable than it really is.
- Preserve the source system's permissions, approval steps, and failure semantics instead of bypassing them.
- Do not rely on a live integration until credentials, target scope, and rollback expectations are verified.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.
- Check the required environment variables and binaries in the active Hermes runtime before trusting the procedure on a live target.

## Example Invocation
```text
/awaken design a conversational or intelligent wrapper around this dumb system without pretending the underlying machine became smarter than it is
```
