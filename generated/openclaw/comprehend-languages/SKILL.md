---
name: comprehend-languages
description: "Use this skill when the words are legible but the meaning is trapped inside an unfamiliar dialect, format, or community."
user-invocable: true
---

# Comprehend Languages

Translate code, jargon, protocol surfaces, or human language into operational meaning.

## Overview

Comprehend Languages is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Comprehend Languages (spell)

Provider target: OpenClaw

## When To Use

- You are reading unfamiliar jargon, logs, schemas, or domain-specific shorthand.
- You need translation plus interpretation, not literal word substitution.
- A team or toolchain uses language that blocks progress.

## Workflow

1. Identify the source dialect, format, or jargon domain.
2. Translate the surface text into plain language while preserving technical meaning.
3. Explain domain-specific assumptions, idioms, and missing context.
4. Return the translated content with terms of art preserved where necessary.

## Deliverables

- A plain-language translation.
- A glossary of non-obvious terms.
- Notes on ambiguity or lost nuance.

## Guardrails

- Do not flatten away important technical distinctions.
- Flag ambiguity when a term has multiple plausible meanings.

## Default Invocation

Use $comprehend-languages to translate this code, jargon, or protocol into clear operational English.

