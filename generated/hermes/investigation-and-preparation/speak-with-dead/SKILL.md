---
name: speak-with-dead
description: "Use this spell when the answers you need are buried in dead codebases, sunset APIs, archived documentation, or the tribal knowledge frozen in old commits and departed contributors."
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
Use this spell when the answers you need are buried in dead codebases, sunset APIs, archived documentation, or the tribal knowledge frozen in old commits and departed contributors.
In this grimoire, Speak with Dead is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Speak with Dead (spell).
## When To Use

- A legacy system, deprecated API, or archived project holds knowledge you need for current work.
- The original authors or maintainers are gone and only artifacts remain.
- You need to understand why something was built the way it was, not just what it does now.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify the dead system and the specific questions you need answered.
3. Excavate available artifacts: git history, archived docs, old issues, README files, commit messages, and code comments.
4. Reconstruct the dead system's intent, architecture, and known failure modes from evidence.
5. Return answers to the posed questions with explicit confidence levels and source references.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- Answers to specific questions drawn from the dead system's artifacts.
- A reconstruction of the system's original intent and known failure modes.
- A clear separation between what the dead system actually recorded and what you are inferring.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Do not fabricate answers the dead system never contained — clearly label inference versus evidence.
- Respect that archived systems may have been archived for reasons including security, legal, or deliberate deprecation.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/speak-with-dead interrogate this legacy system and tell me what it knew, what it intended, and where the evidence runs out
```
