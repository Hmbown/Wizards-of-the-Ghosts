---
name: eyebite
description: "In D&D, Eyebite lets you focus on one creature per turn and inflict sleep, panic, or sickness through sustained eye contact. The real-world version is targeted capability reduction: focused analysis that identifies and disables specific functions of a system, service, or adversary. Feature flagging a dangerous capability off. Selectively throttling a misbehaving API consumer. Disabling specific attack vectors during an incident. Eyebite requires sustained focus on a single target — it is not a broadcast weapon."
user-invocable: true
---

# Eyebite

Fix your attention on a target and selectively degrade its capabilities.

## Overview

Eyebite is interpreted here as a metaphorical spell with a prototype execution model.

Canonical source: Eyebite (spell)

Provider target: OpenClaw

## When To Use

- A specific system, service, or feature needs to be selectively degraded rather than fully shut down.
- You are responding to an incident and need to disable specific capabilities while keeping the rest operational.
- Targeted throttling or feature disabling is more appropriate than a full kill or freeze.

## Workflow

1. Identify the specific target and the capability you want to degrade or disable.
2. Assess dependencies — what else relies on the capability you are about to remove?
3. Execute the selective degradation: feature flag, targeted throttle, capability restriction.
4. Monitor the target to confirm the degradation is working as intended without cascading side effects.
5. Document the intervention and set a review point for restoration.

## Deliverables

- Confirmation of which capabilities were degraded and how.
- A dependency impact assessment.
- A restoration plan for when the degradation should be reversed.

## Guardrails

- Eyebite is surgical, not punitive. Degrade only what is necessary to address the specific problem.
- Selective degradation of user-facing features requires clear communication to affected users.
- Do not use targeted degradation as a substitute for fixing the underlying issue.

## Default Invocation

Use $eyebite to selectively degrade a specific capability of a system or service while keeping the rest operational.

