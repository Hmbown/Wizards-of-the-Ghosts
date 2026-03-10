---
name: faerie-fire
description: "In D&D, Faerie Fire outlines invisible creatures in light, making them visible and easier to hit. The real-world version is the highlighter spell: annotating code with markers, tagging items in a dataset for review, adding visual indicators to dashboards that surface hidden patterns, or marking elements in a document so others can see what you see. Faerie Fire does not find hidden things (that is Detect Magic or See Invisibility) — it makes already-found things impossible to overlook."
user-invocable: true
---

# Faerie Fire

Make hidden things visible by highlighting, tagging, and marking them for attention.

## Overview

Faerie Fire is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Faerie Fire (spell)

Provider target: OpenClaw

## When To Use

- You have identified important elements in a document, codebase, or dataset and need to highlight them for others.
- A review process needs annotations, markers, or tags so that findings are visible to the next reviewer.
- You want to create a visual overlay or summary that surfaces the most important signals from a noisy source.

## Workflow

1. Identify what needs highlighting: the elements, patterns, or findings that should be visible.
2. Choose the marking strategy: inline annotations, tags, color-coding, summary tables, or extracted lists.
3. Apply the markers with enough context that someone else can understand why each item is highlighted.
4. Deliver the annotated version alongside the original for comparison.

## Deliverables

- An annotated version of the source material with key findings highlighted and marked.
- A summary of what was highlighted and why each item warrants attention.

## Guardrails

- Highlighting everything is the same as highlighting nothing. Be selective — mark only what genuinely warrants attention.
- Annotations should explain why something is highlighted, not just that it is. Context-free markers create noise.

## Default Invocation

Use \$faerie-fire to highlight the most important [findings/patterns/elements] in this [document/codebase/dataset] so they cannot be overlooked.

