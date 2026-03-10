---
name: planar-binding
description: "Use this spell when you need to summon a powerful external entity - a third-party API, a cloud service, another agent - and lock it into serving your workflow under explicit terms."
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
# Planar Binding
Bind an external service, API, or agent to a contract with defined scope, duration, and failure modes.
## What This Skill Does
Use this spell when you need to summon a powerful external entity - a third-party API, a cloud service, another agent - and lock it into serving your workflow under explicit terms.
In this grimoire, Planar Binding is treated as a hybrid spell with a prototype delivery profile.
Canonical reference input: Planar Binding (spell).
## When To Use

- You are integrating an external API or service and need to define the contract before granting access.
- An external agent or model needs to be constrained to a specific role, scope, and duration within your workflow.
- You want explicit failure modes, cost limits, and termination conditions before binding a dependency.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Name the external entity to bind and the service it will perform.
3. Define the binding contract: scope of access, duration, rate limits, cost ceiling, and failure behavior.
4. Establish the termination conditions - when and how the binding ends.
5. Execute the binding with the user's explicit consent and credentials, then confirm the contract is active.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A binding contract specifying scope, duration, cost limits, and failure modes.
- A confirmation that the external entity is active and operating within bounds.
- A termination procedure for releasing the binding cleanly.

## Pitfalls / Guardrails

- Call out the glue, permissions, or missing infrastructure before you imply this is fully operational.
- Never bind to an external service without the user's explicit consent and credentials.
- Make cost and rate-limit implications explicit before executing any binding.
- Include termination conditions in every binding - no open-ended commitments.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check which parts are concrete actions versus framing, so the user can tell what is real now.
- Check that any missing glue code, permissions, or future work is labeled before the skill is treated as ready.

## Example Invocation
```text
/planar-binding integrate this external service with an explicit contract covering scope, cost, duration, and termination
```
