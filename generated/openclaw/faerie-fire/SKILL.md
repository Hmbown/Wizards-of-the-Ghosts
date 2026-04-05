---
name: faerie-fire
description: "Faerie Fire marks things that are already known. It does not search, discover, explain, translate, or fix. The user has already identified what matters; your job is to make those items impossible to overlook by annotating, tagging, highlighting, or visually surfacing them in context."
user-invocable: true
---

# Faerie Fire

Make hidden things visible by highlighting, tagging, and marking them for attention.

## Overview

Faerie Fire is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Faerie Fire (spell)

Provider target: OpenClaw

## When To Use

- "Highlight", "tag", "mark", "annotate", "call out", "flag" applied to specific items the user has already named or located
- "Make X visible" where X is a known set of findings, clauses, functions, tickets, or features
- "Show me where [specific thing] appears" — location surfacing, not discovery
- "Annotate", "add margin notes", "color-code", "produce a summary table of marked items"
- The user provides the target list and asks you to apply markers to a document, codebase, dataset, or diagram

## Workflow

1. Confirm the target set: Restate what the user wants marked. If the list is implicit, extract it explicitly before annotating.
2. Choose the marking strategy based on the medium:
3. Code: inline comments, // HIGHLIGHT: markers, or extracted function lists with file:line references
4. Documents: bold/underline, margin notes, or a findings table with clause references
5. Data/tables: tagged rows, conditional formatting descriptions, or filtered views
6. Diagrams: callout labels, numbered annotations, or a legend mapping marks to gaps
7. Apply markers with context: Every mark must include why the item was flagged, not just that it was flagged. A marker without rationale is noise.
8. Deliver two artifacts: the annotated source and a concise summary listing what was marked and the selection criteria.

## Deliverables

- An annotated version of the source material with key findings highlighted and marked.
- A summary of what was highlighted and why each item warrants attention.

## Guardrails

- Be selective. Highlighting everything is highlighting nothing. If the user gives you 200 items, ask them to narrow or apply a ranking.
- Never claim to have discovered something you were not asked to mark. Faerie Fire illuminates; it does not hunt.
- If the request mixes marking with fixing, translating, or explaining, scope yourself to marking only and note the boundary.
- Do not use for: Scanning/searching: "Find all hidden webhooks", "Scan for MCP servers" — the user is asking you to discover, not mark. Use a detection spell instead.
- Do not use for: Explaining: "Explain what this manifest does", "What does this code do?" — comprehension, not annotation.
- Do not use for: Translating: "Translate from German to English" — language conversion, not highlighting.
- Do not use for: Rewriting: "Rewrite for executives", "Simplify this report" — transformation, not marking.
- Do not use for: Fixing: "Highlight the risky parts and fix them" — Faerie Fire only marks; it does not remediate. Decline the fix portion or route it to a separate spell.
- Do not use for: Vague requests: "Highlight the important stuff" with no criteria — ask the user what "important" means before proceeding.

## Default Invocation

Use \$faerie-fire to highlight the most important [findings/patterns/elements] in this [document/codebase/dataset] so they cannot be overlooked.

