---
name: legend-lore
description: "Use this spell when you need everything knowable about a person, company, library, framework, concept, or system — not a quick answer, but a deep dossier."
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
# Legend Lore
Research any named entity exhaustively across all available sources.
## What This Skill Does
Use this spell when you need everything knowable about a person, company, library, framework, concept, or system — not a quick answer, but a deep dossier.
In this grimoire, Legend Lore is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Legend Lore (spell).
## When To Use

- You have a name or identifier and need comprehensive background before making a decision.
- A quick search is insufficient — you need cross-referenced depth from docs, repos, papers, and web.
- You are entering unfamiliar territory and want the full map before acting.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Accept the named subject and any known context or constraints on scope.
3. Search exhaustively across documentation, source code, academic papers, web, and community knowledge.
4. Cross-reference findings and resolve contradictions between sources.
5. Return a structured dossier with sourced claims, confidence levels, and identified gaps.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A comprehensive, sourced research dossier on the named subject.
- A confidence-rated summary distinguishing established facts from community consensus from speculation.
- A list of known unknowns and suggested next research steps.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Cite sources for all non-trivial claims. Do not present inference as established fact.
- Respect access boundaries — do not attempt to access paywalled, private, or restricted sources without authorization.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/legend-lore build a comprehensive research dossier on this subject, with sourced claims and confidence levels
```
