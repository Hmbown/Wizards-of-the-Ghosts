---
name: faerie-fire
description: "In D&D, Faerie Fire outlines invisible creatures in light, making them visible and easier to hit. The real-world version is the highlighter spell: annotating code with markers, tagging items in a dataset for review, adding visual indicators to dashboards that surface hidden patterns, or marking elements in a document so others can see what you see. Faerie Fire does not find hidden things (that is Detect Magic or See Invisibility) — it makes already-found things impossible to overlook."
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
# Faerie Fire
Make hidden things visible by highlighting, tagging, and marking them for attention.
## What This Skill Does
In D&D, Faerie Fire outlines invisible creatures in light, making them visible and easier to hit. The real-world version is the highlighter spell: annotating code with markers, tagging items in a dataset for review, adding visual indicators to dashboards that surface hidden patterns, or marking elements in a document so others can see what you see. Faerie Fire does not find hidden things (that is Detect Magic or See Invisibility) — it makes already-found things impossible to overlook.
In this grimoire, Faerie Fire is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Faerie Fire (spell).
## When To Use

- You have identified important elements in a document, codebase, or dataset and need to highlight them for others.
- A review process needs annotations, markers, or tags so that findings are visible to the next reviewer.
- You want to create a visual overlay or summary that surfaces the most important signals from a noisy source.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify what needs highlighting: the elements, patterns, or findings that should be visible.
3. Choose the marking strategy: inline annotations, tags, color-coding, summary tables, or extracted lists.
4. Apply the markers with enough context that someone else can understand why each item is highlighted.
5. Deliver the annotated version alongside the original for comparison.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- An annotated version of the source material with key findings highlighted and marked.
- A summary of what was highlighted and why each item warrants attention.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Highlighting everything is the same as highlighting nothing. Be selective — mark only what genuinely warrants attention.
- Annotations should explain why something is highlighted, not just that it is. Context-free markers create noise.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/faerie-fire Use \$faerie-fire to highlight the most important [findings/patterns/elements] in this [document/codebase/dataset] so they cannot be overlooked
```
