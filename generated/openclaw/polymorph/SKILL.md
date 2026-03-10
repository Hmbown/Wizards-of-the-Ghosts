---
name: polymorph
description: "Use this spell when you need a full transformation: CSV to JSON, Python to JavaScript, REST to GraphQL, monolith spec to microservices spec, or any structural conversion between representations."
user-invocable: true
---

# Polymorph

Transform one representation into another entirely — formats, schemas, protocols, or interfaces.

## Overview

Polymorph is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Polymorph (spell)

Provider target: OpenClaw

## When To Use

- Data, code, or a specification needs to change form entirely — not a tweak, but a full transformation.
- You are migrating between formats, protocols, schemas, or interface paradigms.
- The source and target representations have different structures, and the conversion requires real mapping, not just renaming.

## Workflow

1. Identify the source representation and the target representation.
2. Map the structural correspondences and identify what cannot translate losslessly.
3. Execute the transformation, preserving semantics where possible and flagging losses.
4. Validate the output in the target format and report what was preserved, approximated, or lost.

## Deliverables

- The transformed artifact in the target representation.
- A mapping report showing what was preserved, approximated, and lost in translation.
- Validation that the output is well-formed in the target format.

## Guardrails

- Transformation can lose information. Explicitly identify what is lost and what is preserved.
- Do not claim lossless conversion when the source and target formats have different expressive power.

## Default Invocation

Use $polymorph to transform this from its current form into the target format, and tell me what survived the conversion and what did not.

