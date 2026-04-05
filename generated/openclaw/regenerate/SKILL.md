---
name: regenerate
description: "In D&D, Regenerate regrows lost limbs. The real-world version is reconstruction: rebuilding lost data from backups and surrounding context, regenerating a deleted component from its tests and documentation, or reconstructing a corrupted file from its known structure and partial content. Unlike Resurrection (which brings back a fully dead system from artifacts), Regenerate is for systems that are alive but missing pieces."
user-invocable: true
---

# Regenerate

Reconstruct missing components or lost data from surrounding context.

## Overview

Regenerate is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Regenerate (spell)

Provider target: OpenClaw

## When To Use

- Data, code, or components have been lost or deleted but surrounding context survives.
- A file is corrupted but its structure and partial content provide enough signal to reconstruct it.
- A component needs to be rebuilt from its tests, documentation, or integration points.

## Workflow

1. Inventory what is missing and what context survives: tests, docs, logs, backups, related code.
2. Assess reconstruction feasibility: is there enough context to rebuild accurately?
3. Reconstruct the missing component using the best available evidence.
4. Verify the reconstruction against whatever validation is available: tests, checksums, expected behavior.
5. Mark the reconstruction as reconstructed, not original — provenance matters.

## Deliverables

- The reconstructed component with a provenance note on what sources informed the reconstruction.
- A confidence assessment: how accurate is the reconstruction and what might be wrong?

## Guardrails

- Clearly mark reconstructed data as reconstructed. Never present regenerated content as if it were the original.
- If there is not enough context for accurate reconstruction, say so rather than generating plausible but potentially wrong content.

## Default Invocation

Use $regenerate to reconstruct this [lost file/deleted component/corrupted data] from surviving context, tests, and documentation.

