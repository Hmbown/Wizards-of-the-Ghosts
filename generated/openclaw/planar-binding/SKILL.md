---
name: planar-binding
description: "Use this spell when you need to summon a powerful external entity - a third-party API, a cloud service, another agent - and lock it into serving your workflow under explicit terms."
user-invocable: true
---

# Planar Binding

Bind an external service, API, or agent to a contract with defined scope, duration, and failure modes.

## Overview

Planar Binding is interpreted here as a hybrid spell with a prototype execution model.

Canonical source: Planar Binding (spell)

Provider target: OpenClaw

## When To Use

- You are integrating an external API or service and need to define the contract before granting access.
- An external agent or model needs to be constrained to a specific role, scope, and duration within your workflow.
- You want explicit failure modes, cost limits, and termination conditions before binding a dependency.

## Workflow

1. Name the external entity to bind and the service it will perform.
2. Define the binding contract: scope of access, duration, rate limits, cost ceiling, and failure behavior.
3. Establish the termination conditions - when and how the binding ends.
4. Execute the binding with the user's explicit consent and credentials, then confirm the contract is active.

## Deliverables

- A binding contract specifying scope, duration, cost limits, and failure modes.
- A confirmation that the external entity is active and operating within bounds.
- A termination procedure for releasing the binding cleanly.

## Guardrails

- Never bind to an external service without the user's explicit consent and credentials.
- Make cost and rate-limit implications explicit before executing any binding.
- Include termination conditions in every binding - no open-ended commitments.

## Default Invocation

Use $planar-binding to integrate this external service with an explicit contract covering scope, cost, duration, and termination.

