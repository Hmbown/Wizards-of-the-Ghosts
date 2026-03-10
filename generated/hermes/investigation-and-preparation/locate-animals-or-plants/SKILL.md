---
name: locate-animals-or-plants
description: "Locate Animals or Plants is service discovery with ecological instincts. It helps you find running services, background jobs, data stores, dependency roots, and other living things in an environment before you touch them. The point is not just location, but context: what is active, who depends on it, and what keeps it alive."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - shipping-now
      - metaphorical
      - investigation-and-preparation
      - analysis
      - discovery
      - translation
      - preflight
---
# Locate Animals or Plants
Find what is alive, where it lives, and what it is feeding on.
## What This Skill Does
Locate Animals or Plants is service discovery with ecological instincts. It helps you find running services, background jobs, data stores, dependency roots, and other living things in an environment before you touch them. The point is not just location, but context: what is active, who depends on it, and what keeps it alive.
In this grimoire, Locate Animals or Plants is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Locate Animals or Plants (spell).
## When To Use

- You need an inventory of active services, dependencies, or data flows in an unfamiliar environment.
- The problem involves discovering what is running rather than debugging one known component.
- You suspect there are hidden dependencies or stale registrations mixed in with live systems.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Sweep the environment for active services, scheduled jobs, stores, queues, and known dependency markers.
3. Trace the discovered components to the systems they depend on or feed.
4. Return a live-system map with confidence levels and any blind spots in the survey.
5. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A discovery map of live services and dependencies.
- A shortlist of the most likely roots, leaves, and chokepoints.
- A confidence note on stale entries, missing telemetry, or unobservable zones.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Do not mistake stale config, dead DNS, or abandoned containers for living systems without corroborating signals.
- Stay within authorized discovery boundaries when scanning networks or environments.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/locate-animals-or-plants discover what services and dependencies are alive in this environment and how they connect
```
