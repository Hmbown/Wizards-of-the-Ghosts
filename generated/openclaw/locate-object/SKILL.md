---
name: locate-object
description: "In D&D, Locate Object senses the direction to a specific object within range. The real-world version is artifact search: finding that config file you know exists somewhere, locating a document someone mentioned but did not link, tracking down the source of a data value through a pipeline, or finding where a specific resource is defined in a sprawling repository."
user-invocable: true
---

# Locate Object

Find a specific file, artifact, or resource you know exists but cannot locate.

## Overview

Locate Object is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Locate Object (spell)

Provider target: OpenClaw

## When To Use

- You know something exists but cannot find it: a file, document, config value, or resource.
- A data value appears in output and you need to trace it back to its source or definition.
- Someone referenced an artifact without providing a link or path, and you need to locate it.

## Workflow

1. Define the target artifact: what is it, what would it look like, and what context do you have?
2. Determine the search strategy: file name patterns, content search, reference tracing, or dependency analysis.
3. Search systematically, narrowing scope with each round.
4. Deliver the located artifact with its path, context, and any related artifacts discovered along the way.

## Deliverables

- The located artifact: path, location, or reference.
- Context: what the artifact is, why it matters, and any related artifacts found during the search.

## Guardrails

- Locate Object finds things through search and deduction, not through unauthorized access. Respect access boundaries.
- If the artifact cannot be found, say so clearly rather than returning a near-miss as if it were the target.

## Default Invocation

Use \$locate-object to find this [file/document/config/resource]. I know it exists but cannot locate it.

