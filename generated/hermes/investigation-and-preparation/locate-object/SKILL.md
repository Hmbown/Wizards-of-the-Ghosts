---
name: locate-object
description: "In D&D, Locate Object senses the direction to a specific object within range. The real-world version is artifact search: finding that config file you know exists somewhere, locating a document someone mentioned but did not link, tracking down the source of a data value through a pipeline, or finding where a specific resource is defined in a sprawling repository."
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
# Locate Object
Find a specific file, artifact, or resource you know exists but cannot locate.
## What This Skill Does
In D&D, Locate Object senses the direction to a specific object within range. The real-world version is artifact search: finding that config file you know exists somewhere, locating a document someone mentioned but did not link, tracking down the source of a data value through a pipeline, or finding where a specific resource is defined in a sprawling repository.
In this grimoire, Locate Object is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Locate Object (spell).
## When To Use

- You know something exists but cannot find it: a file, document, config value, or resource.
- A data value appears in output and you need to trace it back to its source or definition.
- Someone referenced an artifact without providing a link or path, and you need to locate it.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Define the target artifact: what is it, what would it look like, and what context do you have?
3. Determine the search strategy: file name patterns, content search, reference tracing, or dependency analysis.
4. Search systematically, narrowing scope with each round.
5. Deliver the located artifact with its path, context, and any related artifacts discovered along the way.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- The located artifact: path, location, or reference.
- Context: what the artifact is, why it matters, and any related artifacts found during the search.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Locate Object finds things through search and deduction, not through unauthorized access. Respect access boundaries.
- If the artifact cannot be found, say so clearly rather than returning a near-miss as if it were the target.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/locate-object Use \$locate-object to find this [file/document/config/resource]. I know it exists but cannot locate it
```
