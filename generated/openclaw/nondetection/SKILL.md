---
name: nondetection
description: "Use this spell when a system, file, or workflow is leaking more information than it should — metadata, tracking parameters, unnecessary data collection, or identifiable fingerprints."
user-invocable: true
---

# Nondetection

Harden privacy by stripping metadata, minimizing data exposure, and removing tracking.

## Overview

Nondetection is interpreted here as a literal spell with a prototype execution model.

Canonical source: Nondetection (spell)

Provider target: OpenClaw

## When To Use

- Files contain metadata (EXIF, document properties, hidden fields) that should be stripped before sharing.
- A system collects or exposes more data than necessary and needs privacy hardening.
- URLs, logs, or outputs contain tracking parameters or identifiable information that should be removed.

## Workflow

1. Identify the detection surface: what information is being leaked, to whom, and through what channel.
2. Choose the appropriate countermeasure: metadata stripping, data minimization, anonymization, or configuration hardening.
3. Apply the privacy hardening and verify the information is no longer detectable from the outside.
4. Document what was removed, what remains, and the privacy boundary that now exists.

## Deliverables

- A privacy-hardened artifact, configuration, or workflow.
- A report of what information was removed or suppressed.
- A residual exposure assessment — what can still be detected after hardening.

## Guardrails

- Do not use privacy hardening to evade legitimate regulatory compliance, law enforcement, or audit requirements.
- Distinguish privacy from concealment of wrongdoing — make the boundary explicit.

## Default Invocation

Use $nondetection to strip unnecessary metadata and tracking from this and tell me what exposure remains.

