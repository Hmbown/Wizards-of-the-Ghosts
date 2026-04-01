---
name: polymorph
description: "This spell is about representation change, not:\n- Naming changes (same structure, different identifiers)\n- Execution changes (same code, different runtime)\n- Architecture changes (new system design)\n- Duplication (same thing, different place) The key test: Can you point to a source artifact and a target artifact where the same information is expressed in structurally different ways? If yes → Polymorph."
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
      - actions-access-and-automation
      - execution
      - automation
      - access
      - actuation
---
# Polymorph
Transform one representation into another entirely — formats, schemas, protocols, or interfaces.
## What This Skill Does
This spell is about representation change, not:
- Naming changes (same structure, different identifiers)
- Execution changes (same code, different runtime)
- Architecture changes (new system design)
- Duplication (same thing, different place) The key test: Can you point to a source artifact and a target artifact where the same information is expressed in structurally different ways? If yes → Polymorph.
In this grimoire, Polymorph is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Polymorph (spell).
## When To Use

- Activate this spell when the user asks to convert, transform, or migrate data, code, or specifications from one representation format to another where the source and target have different structures and require real semantic mapping.
- Verbs: "convert", "transform", "translate", "migrate" (between formats)
- Explicit format pairs: "CSV to JSON", "Python to JavaScript", "REST to GraphQL", "YAML to HCL", "Swagger to OpenAPI", "Avro to JSON Schema"
- Phrases: "preserve the structure but change the format", "map X concepts to Y", "flag what doesn't translate", "equivalent in [target format]"
- Scope indicators: "150 test files", "50 components", "entire test suite" (still this spell if it's format conversion at scale)

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify source and target representations — name both formats explicitly
3. Map structural correspondences — list what maps to what; identify what has no equivalent
4. Execute transformation — convert preserving semantics; flag losses immediately
5. Validate and report — confirm output is well-formed; document preserved, approximated, and lost elements
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- The transformed artifact in the target representation.
- A mapping report showing what was preserved, approximated, and lost in translation.
- Validation that the output is well-formed in the target format.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Always report losses — never claim lossless conversion when formats differ in expressive power
- Flag ambiguous mappings — when source concept has no clean target equivalent, say so
- Validate output format — the result must be syntactically valid in the target representation
- Do NOT activate this spell for:
- Do not use for: Global rename/refactor: "rename module X to Y across the codebase" — same structure, different names
- Do not use for: Disguise/wrapper layers: "make JSON look like XML without changing backend" — not actual transformation
- Do not use for: Workflow orchestration: "chain these scripts into a pipeline", "create a DAG" — about execution order, not representation
- Do not use for: Worker pools/parallelism: "spawn background workers for each record" — about concurrency, not format
- Do not use for: Full redesign from scratch: "rewrite as blockchain-based system" — new architecture, not mapping
- Do not use for: Cloning/duplicating: "make staging look like production" — copying, not transforming

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/polymorph transform this from its current form into the target format, and tell me what survived the conversion and what did not
```
