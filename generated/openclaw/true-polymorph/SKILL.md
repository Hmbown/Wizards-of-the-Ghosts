---
name: true-polymorph
description: "In D&D, True Polymorph is the permanent transformation — the target becomes something fundamentally different, and if held long enough, the change is irreversible. Unlike Polymorph (temporary disguise or adaptation), True Polymorph means the old identity is gone. The real-world version is irreversible system transformation: rewriting a service from Python to Rust so thoroughly the Python version cannot be recovered, migrating from SQL to a graph database with no backward-compatible schema, or restructuring an organization so completely that the old org chart is not just outdated but nonsensical. True Polymorph is the point of no return."
---

# True Polymorph

Transform a system so completely that the original form is gone — no rollback, no undo.

## Overview

True Polymorph is interpreted here as a hybrid spell with a prototype execution model.

Canonical source: True Polymorph (spell)

Provider target: OpenClaw

## When To Use

- A system, stack, or organization must become something fundamentally different and the old form will not be maintained.
- Backward compatibility or rollback is no longer a real requirement.
- The transformation changes identity, interfaces, or structure so completely that dependents must migrate too.

## Workflow

1. Define the current form, target form, and what exactly makes the transformation irreversible.
2. Run or review a reversible trial transformation first to surface hidden failure modes.
3. Inventory every dependent system, contract, and operator workflow that assumes the old form.
4. Plan the cutover so dependents migrate before the original interface disappears.
5. Return the irreversible transformation plan with go or no-go criteria and explicit point-of-no-return conditions.

## Deliverables

- An irreversible transformation plan with explicit point-of-no-return criteria.
- A dependency migration map covering systems that assume the old form.
- A preflight checklist showing the reversible trial and why rollback is no longer required.

## Guardrails

- Irreversibility is the defining feature and the primary risk. Before casting, verify that rollback to the original form is genuinely unnecessary — not just inconvenient.
- True Polymorph should be preceded by regular Polymorph (a reversible trial run). If the trial fails, the permanent version would be catastrophic.
- Do not True Polymorph a system that other systems depend on without migrating all dependents first. The old interface will not exist.

## Default Invocation

Use $true-polymorph to evaluate and plan an irreversible transformation of this system into a fundamentally different form, including the point of no return and all dependent migrations.

