---
name: locate-animals-or-plants
description: "Locate Animals or Plants is service discovery with ecological instincts. It helps you find running services, background jobs, data stores, dependency roots, and other living things in an environment before you touch them. The point is not just location, but context: what is active, who depends on it, and what keeps it alive."
user-invocable: true
---

# Locate Animals or Plants

Find what is alive, where it lives, and what it is feeding on.

## Overview

Locate Animals or Plants is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Locate Animals or Plants (spell)

Provider target: OpenClaw

## When To Use

- You need an inventory of active services, dependencies, or data flows in an unfamiliar environment.
- The problem involves discovering what is running rather than debugging one known component.
- You suspect there are hidden dependencies or stale registrations mixed in with live systems.

## Workflow

1. Sweep the environment for active services, scheduled jobs, stores, queues, and known dependency markers.
2. Trace the discovered components to the systems they depend on or feed.
3. Return a live-system map with confidence levels and any blind spots in the survey.

## Deliverables

- A discovery map of live services and dependencies.
- A shortlist of the most likely roots, leaves, and chokepoints.
- A confidence note on stale entries, missing telemetry, or unobservable zones.

## Guardrails

- Do not mistake stale config, dead DNS, or abandoned containers for living systems without corroborating signals.
- Stay within authorized discovery boundaries when scanning networks or environments.

## Default Invocation

Use $locate-animals-or-plants to discover what services and dependencies are alive in this environment and how they connect.

