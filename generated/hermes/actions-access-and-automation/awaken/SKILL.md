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

- Activate Awaken when a user wants to add a conversational, natural-language, or agent-like interface on top of an existing system that already works but has a poor or technical interface. The substrate is dumb; the wrapper is smart. You are not building the underlying capability — you are exposing what already exists.
- These patterns strongly indicate Awaken:
- "wrap [system] so I can [natural language action]"
- "add a conversational layer / voice interface / chat front-end to..."
- "nobody remembers the flags/commands/FTP syntax for..."
- "give voice to..." / "make it answer when I ask..."
- "let users say '[plain English request]' instead of..."
- References to legacy systems, CLIs, green screens, serial ports, Modbus registers, cron jobs, bash scripts, spreadsheets, PLCs, Home Assistant automations, MQTT topics, or REST APIs with no UI

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
2. Inventory first: List the system's actual capabilities, constraints, and permissions before designing any language layer. Do not invent capabilities.
3. Map intents to actions: Define concrete user intents → specific backend actions → explicit fallbacks for when the wrapper cannot comply.
4. Design the honest wrapper: Specify how it reads state, executes approved actions, and explains failures in plain language. The wrapper must never imply the substrate is more capable than it is.
5. Return the awakening plan: Deliver an interface-wrapping plan, intent-to-action map with fallback paths, and a risk note describing what the wrapper must never imply or automate.
6. Home Assistant path: If Home Assistant is the target, trigger wake scenes or automations via POST to /api/services/scene/turn_on or /api/services/automation/trigger with the appropriate entity_id.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- An interface-wrapping plan for the existing system.
- An intent-to-action map covering supported requests and fallback paths.
- A risk note describing what the wrapper must never imply or automate.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Never present the wrapped system as more capable, autonomous, or reliable than it really is.
- Preserve the source system's permissions, approval steps, and failure semantics — do not bypass them.
- If a request asks you to build the underlying system, reject and clarify: Awaken wraps, it does not create.
- Do not use for: Creating from scratch: "spin up", "build these services", "bring to life" → animate, not awaken
- Do not use for: Interpreting output: "parse these logs", "what do these sensors mean", "translate this data" → translate/attune, not awaken
- Do not use for: Understanding architecture: "walk me through how this works", "attune me to the codebase" → attune, not awaken
- Do not use for: The key distinction: Awaken requires an existing system with real affordances that need a better interface. If there's nothing to wrap, it's not Awaken.
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
