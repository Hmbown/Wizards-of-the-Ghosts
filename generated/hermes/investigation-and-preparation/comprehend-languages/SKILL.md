---
name: comprehend-languages
description: "Use this skill when the words are legible but the meaning is trapped inside an unfamiliar dialect, format, or community."
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
      - investigation-and-preparation
      - analysis
      - discovery
      - translation
      - preflight
---
# Comprehend Languages
Translate code, jargon, protocol surfaces, or human language into operational meaning.
## What This Skill Does
Use this skill when the words are legible but the meaning is trapped inside an unfamiliar dialect, format, or community.
In this grimoire, Comprehend Languages is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Comprehend Languages (spell).
## When To Use

- You are reading unfamiliar jargon, logs, schemas, or domain-specific shorthand.
- You need translation plus interpretation, not literal word substitution.
- A team or toolchain uses language that blocks progress.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify the source dialect, format, or jargon domain.
3. Translate the surface text into plain language while preserving technical meaning.
4. Explain domain-specific assumptions, idioms, and missing context.
5. Return the translated content with terms of art preserved where necessary.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A plain-language translation.
- A glossary of non-obvious terms.
- Notes on ambiguity or lost nuance.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Do not flatten away important technical distinctions.
- Flag ambiguity when a term has multiple plausible meanings.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/comprehend-languages translate this code, jargon, or protocol into clear operational English
```
