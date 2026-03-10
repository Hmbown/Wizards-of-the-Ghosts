---
name: regenerate
description: "In D&D, Regenerate regrows lost limbs. The real-world version is reconstruction: rebuilding lost data from backups and surrounding context, regenerating a deleted component from its tests and documentation, or reconstructing a corrupted file from its known structure and partial content. Unlike Resurrection (which brings back a fully dead system from artifacts), Regenerate is for systems that are alive but missing pieces."
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
      - repair-and-recovery
      - recovery
      - repair
      - triage
      - stabilization
---
# Regenerate
Reconstruct missing components or lost data from surrounding context.
## What This Skill Does
In D&D, Regenerate regrows lost limbs. The real-world version is reconstruction: rebuilding lost data from backups and surrounding context, regenerating a deleted component from its tests and documentation, or reconstructing a corrupted file from its known structure and partial content. Unlike Resurrection (which brings back a fully dead system from artifacts), Regenerate is for systems that are alive but missing pieces.
In this grimoire, Regenerate is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Regenerate (spell).
## When To Use

- Data, code, or components have been lost or deleted but surrounding context survives.
- A file is corrupted but its structure and partial content provide enough signal to reconstruct it.
- A component needs to be rebuilt from its tests, documentation, or integration points.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Inventory what is missing and what context survives: tests, docs, logs, backups, related code.
3. Assess reconstruction feasibility: is there enough context to rebuild accurately?
4. Reconstruct the missing component using the best available evidence.
5. Verify the reconstruction against whatever validation is available: tests, checksums, expected behavior.
6. Mark the reconstruction as reconstructed, not original — provenance matters.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- The reconstructed component with a provenance note on what sources informed the reconstruction.
- A confidence assessment: how accurate is the reconstruction and what might be wrong?

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Clearly mark reconstructed data as reconstructed. Never present regenerated content as if it were the original.
- If there is not enough context for accurate reconstruction, say so rather than generating plausible but potentially wrong content.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/regenerate reconstruct this [lost file/deleted component/corrupted data] from surviving context, tests, and documentation
```
