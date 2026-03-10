---
name: eyebite
description: "In D&D, Eyebite lets you focus on one creature per turn and inflict sleep, panic, or sickness through sustained eye contact. The real-world version is targeted capability reduction: focused analysis that identifies and disables specific functions of a system, service, or adversary. Feature flagging a dangerous capability off. Selectively throttling a misbehaving API consumer. Disabling specific attack vectors during an incident. Eyebite requires sustained focus on a single target — it is not a broadcast weapon."
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
      - containment-and-intervention
      - containment
      - intervention
      - disruption
      - safety
---
# Eyebite
Fix your attention on a target and selectively degrade its capabilities.
## What This Skill Does
In D&D, Eyebite lets you focus on one creature per turn and inflict sleep, panic, or sickness through sustained eye contact. The real-world version is targeted capability reduction: focused analysis that identifies and disables specific functions of a system, service, or adversary. Feature flagging a dangerous capability off. Selectively throttling a misbehaving API consumer. Disabling specific attack vectors during an incident. Eyebite requires sustained focus on a single target — it is not a broadcast weapon.
In this grimoire, Eyebite is treated as a metaphorical spell with a prototype delivery profile.
Canonical reference input: Eyebite (spell).
## When To Use

- A specific system, service, or feature needs to be selectively degraded rather than fully shut down.
- You are responding to an incident and need to disable specific capabilities while keeping the rest operational.
- Targeted throttling or feature disabling is more appropriate than a full kill or freeze.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify the specific target and the capability you want to degrade or disable.
3. Assess dependencies — what else relies on the capability you are about to remove?
4. Execute the selective degradation: feature flag, targeted throttle, capability restriction.
5. Monitor the target to confirm the degradation is working as intended without cascading side effects.
6. Document the intervention and set a review point for restoration.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- Confirmation of which capabilities were degraded and how.
- A dependency impact assessment.
- A restoration plan for when the degradation should be reversed.

## Pitfalls / Guardrails

- Call out the glue, permissions, or missing infrastructure before you imply this is fully operational.
- Eyebite is surgical, not punitive. Degrade only what is necessary to address the specific problem.
- Selective degradation of user-facing features requires clear communication to affected users.
- Do not use targeted degradation as a substitute for fixing the underlying issue.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.
- Check that any missing glue code, permissions, or future work is labeled before the skill is treated as ready.

## Example Invocation
```text
/eyebite selectively degrade a specific capability of a system or service while keeping the rest operational
```
