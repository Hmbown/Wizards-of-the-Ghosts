---
name: symbol
description: "In D&D, Symbol inscribes a powerful glyph with a predefined effect — death, fear, sleep, stunning — that triggers when conditions are met. Unlike Glyph of Warding (which protects a specific place or object), Symbol marks a conceptual boundary with a named policy. The real-world version is semantic policy tagging: marking a database column as PII so access triggers audit logging, tagging a deployment as HIPAA-scoped so changes require compliance review, or labeling an API endpoint as rate-limited-aggressive so traffic spikes trigger automatic throttling. The symbol is the policy, and the policy enforces itself."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - shipping-now
      - literal
      - monitoring-and-protection
      - observability
      - monitoring
      - guardrails
      - privacy
---
# Symbol
Mark a resource with a named sigil that triggers automatic policy enforcement when conditions are met.
## What This Skill Does
In D&D, Symbol inscribes a powerful glyph with a predefined effect — death, fear, sleep, stunning — that triggers when conditions are met. Unlike Glyph of Warding (which protects a specific place or object), Symbol marks a conceptual boundary with a named policy. The real-world version is semantic policy tagging: marking a database column as PII so access triggers audit logging, tagging a deployment as HIPAA-scoped so changes require compliance review, or labeling an API endpoint as rate-limited-aggressive so traffic spikes trigger automatic throttling. The symbol is the policy, and the policy enforces itself.
In this grimoire, Symbol is treated as a literal spell with a shipping-now delivery profile.
Canonical reference input: Symbol (spell).
## When To Use

- A resource, role, or state needs a machine-readable tag that carries enforcement with it wherever it appears.
- Audit logging, throttling, approval gates, or compliance review should trigger automatically from classification.
- You need a named policy marker that expresses semantic scope, not just a location-bound tripwire.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify the resource, role, or state to mark and the policy the symbol should represent.
3. Define the trigger conditions, enforcement actions, owner, and scope of the symbol.
4. Apply the symbol as a machine-readable tag or classification that downstream systems can detect.
5. Test visibility and precedence against existing policies so the sigil is legible and deterministic.
6. Return the symbol definition, enforcement paths, and failure modes.
7. Stop for explicit confirmation before taking a live action that changes access, triggers an alert, or touches a real system boundary.
8. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A named policy symbol with scope, owner, and machine-readable definition.
- Trigger conditions and automatic enforcement actions.
- A precedence and visibility note covering conflicts, auditability, and blind spots.

## Pitfalls / Guardrails

- Treat the live action surface as real operational work, not decorative lore.
- Symbols must be visible to the people they constrain. Hidden policy enforcement without disclosure is a trap, not a safeguard.
- Every symbol needs a defined scope and an owner. Policy tags that outlive their original context become governance ghosts — still triggering, no longer understood.
- Do not stack conflicting symbols on the same resource without explicit precedence rules.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the exact live target, confirmation gate, and rollback or recovery path are explicit.

## Example Invocation
```text
/symbol mark this resource, role, or state with a named policy sigil that triggers automatic enforcement when conditions are met
```
