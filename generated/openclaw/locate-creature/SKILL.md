---
name: locate-creature
description: "In D&D, Locate Creature points you toward a specific creature within range. The real-world version is entity search: finding a specific person in an organization, locating a running service in a distributed system, tracking down who owns a particular piece of code, or identifying which team is responsible for a specific decision. The target is alive or active — for static artifacts, use Locate Object."
user-invocable: true
---

# Locate Creature

Find a specific person, service, or active process in a large system.

## Overview

Locate Creature is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Locate Creature (spell)

Provider target: OpenClaw

## When To Use

- You need to find who is responsible for a specific system, decision, or process.
- A running service or active process needs to be located in a complex distributed environment.
- You need to track down the right person to talk to about a specific topic in a large organization.

## Workflow

1. Define the target: who or what are you looking for, and what characteristics identify them?
2. Determine the search space: where could this entity be? Narrow the scope before searching broadly.
3. Search using available signals: ownership records, commit history, org charts, service registries, process lists.
4. Deliver the location with a confidence level and verification suggestion.

## Deliverables

- The located entity: who/what it is and where it was found.
- The evidence trail: how we found it and how confident we are in the identification.

## Guardrails

- Locate Creature finds entities through legitimate, observable channels. Do not attempt to track people through unauthorized surveillance.
- Clearly state confidence level. A likely match is not a confirmed identification.

## Default Invocation

Use \$locate-creature to find this [person/service/process] in [the organization/system/environment]. Who owns it and where is it?

