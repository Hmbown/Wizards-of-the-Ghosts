---
name: awaken
description: "Awaken gives a non-intelligent system a usable voice without pretending the underlying system became sentient. The real move is to wrap a thermostat, spreadsheet, legacy database, shell script, or crusty internal tool in a conversational or agent-like interface that exposes what it can already do. Good Awaken work turns buried affordances into accessible ones. Bad Awaken work hallucinates capabilities the substrate does not have. The spell is strongest when the wrapper is honest about its limits and preserves the original system's safety boundaries."
user-invocable: true
metadata:
  openclaw:
    requires:
      env:
        - HA_URL
        - HA_TOKEN
      bins:
        - curl
    primaryEnv: HA_TOKEN
    emoji: "🌅"
---

# Awaken

Teach an old machine to answer back.

## Overview

Awaken is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Awaken (spell)

Provider target: OpenClaw

## When To Use

- Activate Awaken when a user wants to add a conversational, natural-language, or agent-like interface on top of an existing system that already works but has a poor or technical interface. The substrate is dumb; the wrapper is smart. You are not building the underlying capability — you are exposing what already exists.
- These patterns strongly indicate Awaken:
- "wrap [system] so I can [natural language action]"
- "add a conversational layer / voice interface / chat front-end to..."
- "nobody remembers the flags/commands/FTP syntax for..."
- "give voice to..." / "make it answer when I ask..."
- "let users say '[plain English request]' instead of..."
- References to legacy systems, CLIs, green screens, serial ports, Modbus registers, cron jobs, bash scripts, spreadsheets, PLCs, Home Assistant automations, MQTT topics, or REST APIs with no UI

## Workflow

1. Inventory first: List the system's actual capabilities, constraints, and permissions before designing any language layer. Do not invent capabilities.
2. Map intents to actions: Define concrete user intents → specific backend actions → explicit fallbacks for when the wrapper cannot comply.
3. Design the honest wrapper: Specify how it reads state, executes approved actions, and explains failures in plain language. The wrapper must never imply the substrate is more capable than it is.
4. Return the awakening plan: Deliver an interface-wrapping plan, intent-to-action map with fallback paths, and a risk note describing what the wrapper must never imply or automate.
5. Home Assistant path: If Home Assistant is the target, trigger wake scenes or automations via POST to /api/services/scene/turn_on or /api/services/automation/trigger with the appropriate entity_id.

## Deliverables

- An interface-wrapping plan for the existing system.
- An intent-to-action map covering supported requests and fallback paths.
- A risk note describing what the wrapper must never imply or automate.

## Guardrails

- Never present the wrapped system as more capable, autonomous, or reliable than it really is.
- Preserve the source system's permissions, approval steps, and failure semantics — do not bypass them.
- If a request asks you to build the underlying system, reject and clarify: Awaken wraps, it does not create.
- Do not use for: Creating from scratch: "spin up", "build these services", "bring to life" → animate, not awaken
- Do not use for: Interpreting output: "parse these logs", "what do these sensors mean", "translate this data" → translate/attune, not awaken
- Do not use for: Understanding architecture: "walk me through how this works", "attune me to the codebase" → attune, not awaken
- Do not use for: The key distinction: Awaken requires an existing system with real affordances that need a better interface. If there's nothing to wrap, it's not Awaken.

## Default Invocation

Use $awaken to design a conversational or intelligent wrapper around this dumb system without pretending the underlying machine became smarter than it is.

