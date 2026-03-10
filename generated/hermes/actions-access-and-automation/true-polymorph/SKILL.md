---
name: true-polymorph
description: "In D&D, True Polymorph is the permanent transformation — the target becomes something fundamentally different, and if held long enough, the change is irreversible. Unlike Polymorph (temporary disguise or adaptation), True Polymorph means the old identity is gone. The real-world version is irreversible system transformation: rewriting a service from Python to Rust so thoroughly the Python version cannot be recovered, migrating from SQL to a graph database with no backward-compatible schema, or restructuring an organization so completely that the old org chart is not just outdated but nonsensical. True Polymorph is the point of no return."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - prototype
      - hybrid
      - actions-access-and-automation
      - execution
      - automation
      - access
      - actuation
---
# True Polymorph
Transform a system so completely that the original form is gone — no rollback, no undo.
## What This Skill Does
In D&D, True Polymorph is the permanent transformation — the target becomes something fundamentally different, and if held long enough, the change is irreversible. Unlike Polymorph (temporary disguise or adaptation), True Polymorph means the old identity is gone. The real-world version is irreversible system transformation: rewriting a service from Python to Rust so thoroughly the Python version cannot be recovered, migrating from SQL to a graph database with no backward-compatible schema, or restructuring an organization so completely that the old org chart is not just outdated but nonsensical. True Polymorph is the point of no return.
In this grimoire, True Polymorph is treated as a hybrid spell with a prototype delivery profile.
Canonical reference input: True Polymorph (spell).
## When To Use

- A system, stack, or organization must become something fundamentally different and the old form will not be maintained.
- Backward compatibility or rollback is no longer a real requirement.
- The transformation changes identity, interfaces, or structure so completely that dependents must migrate too.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Define the current form, target form, and what exactly makes the transformation irreversible.
3. Run or review a reversible trial transformation first to surface hidden failure modes.
4. Inventory every dependent system, contract, and operator workflow that assumes the old form.
5. Plan the cutover so dependents migrate before the original interface disappears.
6. Return the irreversible transformation plan with go or no-go criteria and explicit point-of-no-return conditions.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- An irreversible transformation plan with explicit point-of-no-return criteria.
- A dependency migration map covering systems that assume the old form.
- A preflight checklist showing the reversible trial and why rollback is no longer required.

## Pitfalls / Guardrails

- Call out the glue, permissions, or missing infrastructure before you imply this is fully operational.
- Irreversibility is the defining feature and the primary risk. Before casting, verify that rollback to the original form is genuinely unnecessary — not just inconvenient.
- True Polymorph should be preceded by regular Polymorph (a reversible trial run). If the trial fails, the permanent version would be catastrophic.
- Do not True Polymorph a system that other systems depend on without migrating all dependents first. The old interface will not exist.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check which parts are concrete actions versus framing, so the user can tell what is real now.
- Check that any missing glue code, permissions, or future work is labeled before the skill is treated as ready.

## Example Invocation
```text
/true-polymorph evaluate and plan an irreversible transformation of this system into a fundamentally different form, including the point of no return and all dependent migrations
```
