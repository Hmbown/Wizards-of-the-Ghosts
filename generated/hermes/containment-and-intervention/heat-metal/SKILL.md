---
name: heat-metal
description: "In D&D, Heat Metal makes a metal object painfully hot — the creature holding it must either endure the pain or drop it. The real-world version is deliberate friction injection: making a deprecated API progressively slower, adding escalating CAPTCHAs to suspicious traffic, increasing the cost of a bad behavior path until the actor self-selects out. Heat Metal does not break the tool. It makes continuing to use it more painful than switching to the alternative. This is the spell behind deprecation-by-discomfort, progressive rate limiting, and sunset friction curves."
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
      - containment-and-intervention
      - containment
      - intervention
      - disruption
      - safety
---
# Heat Metal
Make a tool or process increasingly uncomfortable to use until it is abandoned.
## What This Skill Does
In D&D, Heat Metal makes a metal object painfully hot — the creature holding it must either endure the pain or drop it. The real-world version is deliberate friction injection: making a deprecated API progressively slower, adding escalating CAPTCHAs to suspicious traffic, increasing the cost of a bad behavior path until the actor self-selects out. Heat Metal does not break the tool. It makes continuing to use it more painful than switching to the alternative. This is the spell behind deprecation-by-discomfort, progressive rate limiting, and sunset friction curves.
In this grimoire, Heat Metal is treated as a hybrid spell with a prototype delivery profile.
Canonical reference input: Heat Metal (spell).
## When To Use

- You want to drive migration away from a deprecated tool, API, or workflow without hard-cutting access.
- Suspicious or abusive behavior should be progressively penalized without outright blocking.
- A gradual escalation of friction is more appropriate than an immediate ban or shutdown.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify the tool, path, or behavior you want to discourage.
3. Design the friction curve: what discomfort increases over time and at what rate.
4. Implement the progressive friction: latency injection, CAPTCHA escalation, cost increases, warning banners.
5. Monitor adoption of the preferred alternative to confirm the friction is driving the intended migration.
6. Set a sunset date: Heat Metal should eventually end in either full migration or hard deprecation.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A friction curve specification: what changes, how fast, and what the escalation stages are.
- Migration metrics: how many users/systems have moved to the preferred alternative.
- A sunset timeline with hard cutoff criteria.

## Pitfalls / Guardrails

- Call out the glue, permissions, or missing infrastructure before you imply this is fully operational.
- Friction injection must be disclosed. Secretly making tools worse without explanation is a dark pattern.
- Heat Metal targets behavior, not people. Progressive friction applied to specific users as punishment crosses into harassment.
- Always provide a visible alternative. Making something painful to use without offering a better path is cruelty, not engineering.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check which parts are concrete actions versus framing, so the user can tell what is real now.
- Check that any missing glue code, permissions, or future work is labeled before the skill is treated as ready.

## Example Invocation
```text
/heat-metal design a progressive friction strategy that makes a deprecated tool, abusive pattern, or unwanted behavior increasingly uncomfortable until users migrate to the better alternative
```
