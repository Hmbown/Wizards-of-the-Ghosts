---
name: nondetection
description: "Use this spell when a system, file, or workflow is leaking more information than it should — metadata, tracking parameters, unnecessary data collection, or identifiable fingerprints."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - prototype
      - literal
      - monitoring-and-protection
      - observability
      - monitoring
      - guardrails
      - privacy
---
# Nondetection
Harden privacy by stripping metadata, minimizing data exposure, and removing tracking.
## What This Skill Does
Use this spell when a system, file, or workflow is leaking more information than it should — metadata, tracking parameters, unnecessary data collection, or identifiable fingerprints.
In this grimoire, Nondetection is treated as a literal spell with a prototype delivery profile.
Canonical reference input: Nondetection (spell).
## When To Use

- Files contain metadata (EXIF, document properties, hidden fields) that should be stripped before sharing.
- A system collects or exposes more data than necessary and needs privacy hardening.
- URLs, logs, or outputs contain tracking parameters or identifiable information that should be removed.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify the detection surface: what information is being leaked, to whom, and through what channel.
3. Choose the appropriate countermeasure: metadata stripping, data minimization, anonymization, or configuration hardening.
4. Apply the privacy hardening and verify the information is no longer detectable from the outside.
5. Document what was removed, what remains, and the privacy boundary that now exists.
6. Stop for explicit confirmation before taking a live action that changes access, triggers an alert, or touches a real system boundary.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A privacy-hardened artifact, configuration, or workflow.
- A report of what information was removed or suppressed.
- A residual exposure assessment — what can still be detected after hardening.

## Pitfalls / Guardrails

- Call out the glue, permissions, or missing infrastructure before you imply this is fully operational.
- Do not use privacy hardening to evade legitimate regulatory compliance, law enforcement, or audit requirements.
- Distinguish privacy from concealment of wrongdoing — make the boundary explicit.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the exact live target, confirmation gate, and rollback or recovery path are explicit.
- Check that any missing glue code, permissions, or future work is labeled before the skill is treated as ready.

## Example Invocation
```text
/nondetection strip unnecessary metadata and tracking from this and tell me what exposure remains
```
