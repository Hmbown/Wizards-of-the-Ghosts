---
name: heat-metal
description: "In D&D, Heat Metal makes a metal object painfully hot — the creature holding it must either endure the pain or drop it. The real-world version is deliberate friction injection: making a deprecated API progressively slower, adding escalating CAPTCHAs to suspicious traffic, increasing the cost of a bad behavior path until the actor self-selects out. Heat Metal does not break the tool. It makes continuing to use it more painful than switching to the alternative. This is the spell behind deprecation-by-discomfort, progressive rate limiting, and sunset friction curves."
user-invocable: true
---

# Heat Metal

Make a tool or process increasingly uncomfortable to use until it is abandoned.

## Overview

Heat Metal is interpreted here as a hybrid spell with a prototype execution model.

Canonical source: Heat Metal (spell)

Provider target: OpenClaw

## When To Use

- You want to drive migration away from a deprecated tool, API, or workflow without hard-cutting access.
- Suspicious or abusive behavior should be progressively penalized without outright blocking.
- A gradual escalation of friction is more appropriate than an immediate ban or shutdown.

## Workflow

1. Identify the tool, path, or behavior you want to discourage.
2. Design the friction curve: what discomfort increases over time and at what rate.
3. Implement the progressive friction: latency injection, CAPTCHA escalation, cost increases, warning banners.
4. Monitor adoption of the preferred alternative to confirm the friction is driving the intended migration.
5. Set a sunset date: Heat Metal should eventually end in either full migration or hard deprecation.

## Deliverables

- A friction curve specification: what changes, how fast, and what the escalation stages are.
- Migration metrics: how many users/systems have moved to the preferred alternative.
- A sunset timeline with hard cutoff criteria.

## Guardrails

- Friction injection must be disclosed. Secretly making tools worse without explanation is a dark pattern.
- Heat Metal targets behavior, not people. Progressive friction applied to specific users as punishment crosses into harassment.
- Always provide a visible alternative. Making something painful to use without offering a better path is cruelty, not engineering.

## Default Invocation

Use $heat-metal to design a progressive friction strategy that makes a deprecated tool, abusive pattern, or unwanted behavior increasingly uncomfortable until users migrate to the better alternative.

