---
name: disguise-self
description: "Disguise Self changes how something is said, never what is said. The input content is already correct — only the delivery surface needs adjustment. If the user wants to change facts, add new information, transform code implementations, or produce multiple versions at once, this is NOT this spell."
user-invocable: true
---

# Disguise Self

Adapt voice, tone, or presentation for a specific audience without changing the underlying substance.

## Overview

Disguise Self is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Disguise Self (spell)

Provider target: OpenClaw

## When To Use

- Trigger this spell when the user asks to rewrite, adapt, repackage, or convert existing content for a different audience, tone, format, or medium while keeping all facts, meaning, and requirements intact.

## Workflow

1. Lock the substance. Read the source content and extract all facts, requirements, decisions, and constraints. These are immutable.
2. Profile the target. Identify the audience's reading level, expectations, preferred structure, and what jargon they know or don't know.
3. Apply the disguise. Rewrite using the target's vocabulary, sentence length, formality, and structure. Map every original point to a corresponding point in the output — nothing drops, nothing invents.
4. Report the changes. Return the adapted content plus a short note: what presentation choices were made and which facts were deliberately preserved unchanged.

## Deliverables

- The content re-presented for the target audience or medium.
- A brief note on the presentation changes made.
- Confirmation that no factual content or critical nuance was altered.

## Guardrails

- Never alter facts, omit requirements, or soften warnings to suit the audience.
- Adaptation serves comprehension, not deception. The reader should understand the same thing the original reader understood, just in their own language.
- If the source content is ambiguous or incomplete, flag it — do not invent clarity that isn't there.
- Do not use for: Multi-audience generation ("write versions for engineering, sales, and legal") — that's a batch/orchestration spell, not a single disguise.
- Do not use for: Code refactoring ("rewrite this Python in Go", "switch to the new ORM") — implementation changes, not presentation changes.
- Do not use for: Rebranding ("change the name, logo, branding") — identity work, not content adaptation.
- Do not use for: Anonymization/redaction ("strip PII", "remove sensitive data") — that removes substance; disguise preserves everything.
- Do not use for: Monitoring/visibility changes ("hide this service from dashboards") — literal invisibility, not metaphorical disguise.
- Do not use for: Adding or removing content ("summarize by cutting details", "expand with examples") — substance changes, not presentation changes.

## Default Invocation

Use $disguise-self to rewrite this for the target audience without changing what it actually says.

