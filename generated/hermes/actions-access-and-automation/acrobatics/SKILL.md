---
name: acrobatics
description: "Use this skill when the work is a choreography problem: brittle sequencing, async handoffs, or constrained flows that must stay upright end to end. It shines on API dances, dependency ordering, and recovery logic where grace matters more than brute force."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - skill
      - shipping-now
      - metaphorical
      - actions-access-and-automation
      - execution
      - automation
      - access
      - actuation
---
# Acrobatics
Thread complex systems without tripping rate limits, retries, or state.
## What This Skill Does
Use this skill when the work is a choreography problem: brittle sequencing, async handoffs, or constrained flows that must stay upright end to end. It shines on API dances, dependency ordering, and recovery logic where grace matters more than brute force.
In this grimoire, Acrobatics is treated as a metaphorical skill with a shipping-now delivery profile.
Canonical reference input: Acrobatics (skill).
## When To Use

- An integration requires a precise sequence of calls, callbacks, or tokens.
- Concurrency, pagination, or retries can topple the flow if handled clumsily.
- You need a nimble route through constraints rather than more compute.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Map the sequence, tight constraints, and recovery points before moving.
3. Reorder or simplify the path to reduce wasted calls, unstable state, and timing risk.
4. Return the stepwise route with checkpoints, balance points, and fallback moves.
5. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A sequenced execution plan for the constrained flow.
- A list of state, timing, and rate-limit risks.
- A compact recovery playbook for dropped or misordered steps.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Do not mistake unnecessary cleverness for agility; the cleanest path wins.
- Surface hidden coupling and time-sensitive assumptions instead of relying on luck.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/acrobatics thread this workflow cleanly through its sequencing constraints and show me the balance points
```
