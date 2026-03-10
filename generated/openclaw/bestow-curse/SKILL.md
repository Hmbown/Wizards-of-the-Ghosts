---
name: bestow-curse
description: "Bestow Curse saddles a target with a lasting disadvantage. The real-world version is constraint injection: deliberately adding friction, limitations, or handicaps to see how a system, process, or team adapts. This is the skill of resilience testing through artificial adversity — bandwidth throttling, feature removal, resource reduction."
user-invocable: true
---

# Bestow Curse

Add persistent constraints or friction to test how a system copes.

## Overview

Bestow Curse is interpreted here as a metaphorical spell with a prototype execution model.

Canonical source: Bestow Curse (spell)

Provider target: OpenClaw

## When To Use

- You want to test how a system performs under degraded conditions before those conditions occur naturally.
- A process is too dependent on ideal circumstances and you need to know its failure boundaries.

## Workflow

1. Identify the system or process to stress-test through constraint injection.
2. Design the curse: what specific limitation, degradation, or friction to introduce.
3. Define the measurement criteria: how will you know if the system coped well or poorly?
4. Deliver the constraint injection plan with expected outcomes and rollback procedures.

## Deliverables

- A constraint injection plan: what to degrade, by how much, for how long.
- Success and failure criteria: what coping looks like vs. what breaking looks like.

## Guardrails

- Constraint injection must be reversible. The curse should reveal weaknesses, not create permanent damage.
- Do not inject constraints into production systems without authorization and rollback plans.

## Default Invocation

Use $bestow-curse to design a constraint injection test for this [system/process]. What happens when we deliberately degrade it?

