---
name: arcana
description: "In D&D, Arcana is knowledge of magic, its traditions, symbols, and mechanisms. The real-world version is deep technical literacy: understanding how software architectures work, what protocols do at the wire level, how APIs behave beyond their documentation, and what the actual mechanisms are behind the abstractions everyone else takes on faith."
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
      - investigation-and-preparation
      - analysis
      - discovery
      - translation
      - preflight
---
# Arcana
Apply deep technical knowledge to understand how systems work under the hood.
## What This Skill Does
In D&D, Arcana is knowledge of magic, its traditions, symbols, and mechanisms. The real-world version is deep technical literacy: understanding how software architectures work, what protocols do at the wire level, how APIs behave beyond their documentation, and what the actual mechanisms are behind the abstractions everyone else takes on faith.
In this grimoire, Arcana is treated as a metaphorical skill with a shipping-now delivery profile.
Canonical reference input: Arcana (skill).
## When To Use

- A technical system needs to be understood at a level deeper than its documentation provides.
- You need to explain how something actually works — not what it claims to do, but what it does.
- A debugging or architecture question requires knowledge of underlying mechanisms, not just surface APIs.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify the system, protocol, or technology to analyze.
3. Explain the mechanism at the appropriate depth: not the marketing version, but how it actually works.
4. Surface non-obvious implications, edge cases, or failure modes that follow from the mechanism.
5. Deliver the explanation with a clear note on what is documented fact vs. observed behavior vs. inference.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A mechanistic explanation of how the system actually works under the hood.
- Non-obvious implications or edge cases that follow from the mechanism.
- A confidence note: what is documented, what is observed, and what is inferred.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Do not confuse documentation with behavior. The docs say what it should do; arcana reveals what it does.
- Clearly separate established knowledge from speculation when reasoning about undocumented behavior.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/arcana explain how this [system/protocol/technology] actually works under the hood, beyond what the documentation says
```
