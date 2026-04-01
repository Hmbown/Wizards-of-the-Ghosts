---
name: disguise-self
description: "Disguise Self changes how something is said, never what is said. The input content is already correct — only the delivery surface needs adjustment. If the user wants to change facts, add new information, transform code implementations, or produce multiple versions at once, this is NOT this spell."
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
      - monitoring-and-protection
      - observability
      - monitoring
      - guardrails
      - privacy
---
# Disguise Self
Adapt voice, tone, or presentation for a specific audience without changing the underlying substance.
## What This Skill Does
Disguise Self changes how something is said, never what is said. The input content is already correct — only the delivery surface needs adjustment. If the user wants to change facts, add new information, transform code implementations, or produce multiple versions at once, this is NOT this spell.
In this grimoire, Disguise Self is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Disguise Self (spell).
## When To Use

- Trigger this spell when the user asks to rewrite, adapt, repackage, or convert existing content for a different audience, tone, format, or medium while keeping all facts, meaning, and requirements intact.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Lock the substance. Read the source content and extract all facts, requirements, decisions, and constraints. These are immutable.
3. Profile the target. Identify the audience's reading level, expectations, preferred structure, and what jargon they know or don't know.
4. Apply the disguise. Rewrite using the target's vocabulary, sentence length, formality, and structure. Map every original point to a corresponding point in the output — nothing drops, nothing invents.
5. Report the changes. Return the adapted content plus a short note: what presentation choices were made and which facts were deliberately preserved unchanged.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- The content re-presented for the target audience or medium.
- A brief note on the presentation changes made.
- Confirmation that no factual content or critical nuance was altered.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Never alter facts, omit requirements, or soften warnings to suit the audience.
- Adaptation serves comprehension, not deception. The reader should understand the same thing the original reader understood, just in their own language.
- If the source content is ambiguous or incomplete, flag it — do not invent clarity that isn't there.
- Do not use for: Multi-audience generation ("write versions for engineering, sales, and legal") — that's a batch/orchestration spell, not a single disguise.
- Do not use for: Code refactoring ("rewrite this Python in Go", "switch to the new ORM") — implementation changes, not presentation changes.
- Do not use for: Rebranding ("change the name, logo, branding") — identity work, not content adaptation.
- Do not use for: Anonymization/redaction ("strip PII", "remove sensitive data") — that removes substance; disguise preserves everything.
- Do not use for: Monitoring/visibility changes ("hide this service from dashboards") — literal invisibility, not metaphorical disguise.
- Do not use for: Adding or removing content ("summarize by cutting details", "expand with examples") — substance changes, not presentation changes.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/disguise-self rewrite this for the target audience without changing what it actually says
```
