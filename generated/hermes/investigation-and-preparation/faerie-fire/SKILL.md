---
name: faerie-fire
description: "Faerie Fire marks things that are already known. It does not search, discover, explain, translate, or fix. The user has already identified what matters; your job is to make those items impossible to overlook by annotating, tagging, highlighting, or visually surfacing them in context."
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
Faerie Fire marks things that are already known. It does not search, discover, explain, translate, or fix. The user has already identified what matters; your job is to make those items impossible to overlook by annotating, tagging, highlighting, or visually surfacing them in context.
In this grimoire, Faerie Fire is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Faerie Fire (spell).
## When To Use

- "Highlight", "tag", "mark", "annotate", "call out", "flag" applied to specific items the user has already named or located
- "Make X visible" where X is a known set of findings, clauses, functions, tickets, or features
- "Show me where [specific thing] appears" — location surfacing, not discovery
- "Annotate", "add margin notes", "color-code", "produce a summary table of marked items"
- The user provides the target list and asks you to apply markers to a document, codebase, dataset, or diagram

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Confirm the target set: Restate what the user wants marked. If the list is implicit, extract it explicitly before annotating.
3. Choose the marking strategy based on the medium:
4. Code: inline comments, // HIGHLIGHT: markers, or extracted function lists with file:line references
5. Documents: bold/underline, margin notes, or a findings table with clause references
6. Data/tables: tagged rows, conditional formatting descriptions, or filtered views
7. Diagrams: callout labels, numbered annotations, or a legend mapping marks to gaps
8. Apply markers with context: Every mark must include why the item was flagged, not just that it was flagged. A marker without rationale is noise.
9. Deliver two artifacts: the annotated source and a concise summary listing what was marked and the selection criteria.
10. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- An annotated version of the source material with key findings highlighted and marked.
- A summary of what was highlighted and why each item warrants attention.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Be selective. Highlighting everything is highlighting nothing. If the user gives you 200 items, ask them to narrow or apply a ranking.
- Never claim to have discovered something you were not asked to mark. Faerie Fire illuminates; it does not hunt.
- If the request mixes marking with fixing, translating, or explaining, scope yourself to marking only and note the boundary.
- Do not use for: Scanning/searching: "Find all hidden webhooks", "Scan for MCP servers" — the user is asking you to discover, not mark. Use a detection spell instead.
- Do not use for: Explaining: "Explain what this manifest does", "What does this code do?" — comprehension, not annotation.
- Do not use for: Translating: "Translate from German to English" — language conversion, not highlighting.
- Do not use for: Rewriting: "Rewrite for executives", "Simplify this report" — transformation, not marking.
- Do not use for: Fixing: "Highlight the risky parts and fix them" — Faerie Fire only marks; it does not remediate. Decline the fix portion or route it to a separate spell.
- Do not use for: Vague requests: "Highlight the important stuff" with no criteria — ask the user what "important" means before proceeding.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/faerie-fire Use \$faerie-fire to highlight the most important [findings/patterns/elements] in this [document/codebase/dataset] so they cannot be overlooked
```
