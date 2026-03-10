---
name: symbol
description: "In D&D, Symbol inscribes a powerful glyph with a predefined effect — death, fear, sleep, stunning — that triggers when conditions are met. Unlike Glyph of Warding (which protects a specific place or object), Symbol marks a conceptual boundary with a named policy. The real-world version is semantic policy tagging: marking a database column as PII so access triggers audit logging, tagging a deployment as HIPAA-scoped so changes require compliance review, or labeling an API endpoint as rate-limited-aggressive so traffic spikes trigger automatic throttling. The symbol is the policy, and the policy enforces itself."
user-invocable: true
---

# Symbol

Mark a resource with a named sigil that triggers automatic policy enforcement when conditions are met.

## Overview

Symbol is interpreted here as a literal spell with a shipping-now execution model.

Canonical source: Symbol (spell)

Provider target: OpenClaw

## When To Use

- A resource, role, or state needs a machine-readable tag that carries enforcement with it wherever it appears.
- Audit logging, throttling, approval gates, or compliance review should trigger automatically from classification.
- You need a named policy marker that expresses semantic scope, not just a location-bound tripwire.

## Workflow

1. Identify the resource, role, or state to mark and the policy the symbol should represent.
2. Define the trigger conditions, enforcement actions, owner, and scope of the symbol.
3. Apply the symbol as a machine-readable tag or classification that downstream systems can detect.
4. Test visibility and precedence against existing policies so the sigil is legible and deterministic.
5. Return the symbol definition, enforcement paths, and failure modes.

## Deliverables

- A named policy symbol with scope, owner, and machine-readable definition.
- Trigger conditions and automatic enforcement actions.
- A precedence and visibility note covering conflicts, auditability, and blind spots.

## Guardrails

- Symbols must be visible to the people they constrain. Hidden policy enforcement without disclosure is a trap, not a safeguard.
- Every symbol needs a defined scope and an owner. Policy tags that outlive their original context become governance ghosts — still triggering, no longer understood.
- Do not stack conflicting symbols on the same resource without explicit precedence rules.

## Default Invocation

Use $symbol to mark this resource, role, or state with a named policy sigil that triggers automatic enforcement when conditions are met.

