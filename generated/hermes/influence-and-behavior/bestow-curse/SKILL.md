---
name: bestow-curse
description: "Bestow Curse saddles a target with a lasting disadvantage. The real-world version is constraint injection: deliberately adding friction, limitations, or handicaps to see how a system, process, or team adapts. This is the skill of resilience testing through artificial adversity — bandwidth throttling, feature removal, resource reduction."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - prototype
      - metaphorical
      - influence-and-behavior
      - influence
      - behavior
      - attention
      - engagement
---
# Bestow Curse
Add persistent constraints or friction to test how a system copes.
## What This Skill Does
Bestow Curse saddles a target with a lasting disadvantage. The real-world version is constraint injection: deliberately adding friction, limitations, or handicaps to see how a system, process, or team adapts. This is the skill of resilience testing through artificial adversity — bandwidth throttling, feature removal, resource reduction.
In this grimoire, Bestow Curse is treated as a metaphorical spell with a prototype delivery profile.
Canonical reference input: Bestow Curse (spell).
## When To Use

- You want to test how a system performs under degraded conditions before those conditions occur naturally.
- A process is too dependent on ideal circumstances and you need to know its failure boundaries.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify the system or process to stress-test through constraint injection.
3. Design the curse: what specific limitation, degradation, or friction to introduce.
4. Define the measurement criteria: how will you know if the system coped well or poorly?
5. Deliver the constraint injection plan with expected outcomes and rollback procedures.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A constraint injection plan: what to degrade, by how much, for how long.
- Success and failure criteria: what coping looks like vs. what breaking looks like.

## Pitfalls / Guardrails

- Call out the glue, permissions, or missing infrastructure before you imply this is fully operational.
- Constraint injection must be reversible. The curse should reveal weaknesses, not create permanent damage.
- Do not inject constraints into production systems without authorization and rollback plans.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.
- Check that any missing glue code, permissions, or future work is labeled before the skill is treated as ready.

## Example Invocation
```text
/bestow-curse design a constraint injection test for this [system/process]. What happens when we deliberately degrade it?
```
