---
name: speak-with-dead
description: "This spell is archaeology, not history research. It operates on specific artifacts from a specific dead system to answer specific questions. It is NOT general tech history, NOT interviewing living people, and NOT monitoring live systems."
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
# Speak with Dead
Extract knowledge from abandoned, deprecated, or legacy systems.
## What This Skill Does
This spell is archaeology, not history research. It operates on specific artifacts from a specific dead system to answer specific questions. It is NOT general tech history, NOT interviewing living people, and NOT monitoring live systems.
In this grimoire, Speak with Dead is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Speak with Dead (spell).
## When To Use

- Route to this spell when the user asks to extract knowledge from systems that are dead, abandoned, deprecated, or archived AND the people who built or maintained them are no longer available. The knowledge must be recoverable from existing artifacts (code, commits, docs, configs, databases, state files) rather than from living people or live systems.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Scope the dead system: Name the specific system, confirm it is actually dead/archived, and list the user's concrete questions.
3. Inventory artifacts: Identify what remains — git history, commit messages, PR descriptions, README files, archived docs, config files, database schemas, state files, packet captures, ADRs. Note what is missing.
4. Reconstruct from evidence: Trace intent through commit messages, code structure, config values, and data schemas. Separate what the artifacts directly state from what you are inferring.
5. Return with confidence labels: For each answer, cite the specific artifact (file, commit hash, line, config key) and label it as evidence (directly stated) or inference (reasoned from patterns). Flag any gaps where the trail goes cold.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- Answers to specific questions drawn from the dead system's artifacts.
- A reconstruction of the system's original intent and known failure modes.
- A clear separation between what the dead system actually recorded and what you are inferring.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Never fabricate answers the artifacts do not support. Label inferences explicitly.
- Note if the system may have been archived for security, legal, or compliance reasons — flag this to the user.
- If artifacts are insufficient to answer the question, say so rather than guessing.
- Do not use for: General tech history ("history of JavaScript frameworks," "evolution of REST APIs") → route to research/knowledge spells
- Do not use for: Company lore from living people ("ask the team why we chose Postgres") → route to collaboration/survey spells
- Do not use for: Live system observation ("what's happening on staging right now") → route to monitoring/observability spells
- Do not use for: Competitor watching ("monitor their API for changes") → route to monitoring/automation spells
- Do not use for: Active system debugging ("why is this production service failing") → route to debugging/troubleshooting spells
- Do not use for: Generic code explanation ("explain what this function does") → route to code-understanding spells

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/speak-with-dead interrogate this legacy system and tell me what it knew, what it intended, and where the evidence runs out
```
