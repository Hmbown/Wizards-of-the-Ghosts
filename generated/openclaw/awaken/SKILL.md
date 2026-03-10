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

- A useful system exists already, but only through brittle commands, forms, or legacy interfaces.
- You want to add natural-language access, summarization, or guided actions on top of a dumb substrate.
- The real value is interface uplift, not rebuilding the underlying system from scratch.
- Your Home Assistant setup has devices that should activate together as a morning routine — lights, coffee maker, blinds, thermostat.

## Workflow

1. Inventory the system's real capabilities, constraints, and permissions before adding any language layer.
2. Design the conversational surface around concrete intents, mapped actions, and explicit fallbacks when the wrapper cannot comply.
3. Define how the wrapper reads state, executes approved actions, and explains failures in plain language.
4. Return an awakening plan with interface examples, backend bindings, and the limits that must stay visible to the user.
5. If Home Assistant is available, trigger a wake scene or automation via POST to /api/services/scene/turn_on or /api/services/automation/trigger with the appropriate entity_id.

## Deliverables

- An interface-wrapping plan for the existing system.
- An intent-to-action map covering supported requests and fallback paths.
- A risk note describing what the wrapper must never imply or automate.

## Guardrails

- Do not present the wrapped system as more capable, autonomous, or reliable than it really is.
- Preserve the source system's permissions, approval steps, and failure semantics instead of bypassing them.

## Default Invocation

Use $awaken to design a conversational or intelligent wrapper around this dumb system without pretending the underlying machine became smarter than it is.

