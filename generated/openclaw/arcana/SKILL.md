---
name: arcana
description: "In D&D, Arcana is knowledge of magic, its traditions, symbols, and mechanisms. The real-world version is deep technical literacy: understanding how software architectures work, what protocols do at the wire level, how APIs behave beyond their documentation, and what the actual mechanisms are behind the abstractions everyone else takes on faith."
user-invocable: true
---

# Arcana

Apply deep technical knowledge to understand how systems work under the hood.

## Overview

Arcana is interpreted here as a metaphorical skill with a shipping-now execution model.

Canonical source: Arcana (skill)

Provider target: OpenClaw

## When To Use

- A technical system needs to be understood at a level deeper than its documentation provides.
- You need to explain how something actually works — not what it claims to do, but what it does.
- A debugging or architecture question requires knowledge of underlying mechanisms, not just surface APIs.

## Workflow

1. Identify the system, protocol, or technology to analyze.
2. Explain the mechanism at the appropriate depth: not the marketing version, but how it actually works.
3. Surface non-obvious implications, edge cases, or failure modes that follow from the mechanism.
4. Deliver the explanation with a clear note on what is documented fact vs. observed behavior vs. inference.

## Deliverables

- A mechanistic explanation of how the system actually works under the hood.
- Non-obvious implications or edge cases that follow from the mechanism.
- A confidence note: what is documented, what is observed, and what is inferred.

## Guardrails

- Do not confuse documentation with behavior. The docs say what it should do; arcana reveals what it does.
- Clearly separate established knowledge from speculation when reasoning about undocumented behavior.

## Default Invocation

Use $arcana to explain how this [system/protocol/technology] actually works under the hood, beyond what the documentation says.

