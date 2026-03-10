---
name: locate-creature
description: "In D&D, Locate Creature points you toward a specific creature within range. The real-world version is entity search: finding a specific person in an organization, locating a running service in a distributed system, tracking down who owns a particular piece of code, or identifying which team is responsible for a specific decision. The target is alive or active — for static artifacts, use Locate Object."
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
# Locate Creature
Find a specific person, service, or active process in a large system.
## What This Skill Does
In D&D, Locate Creature points you toward a specific creature within range. The real-world version is entity search: finding a specific person in an organization, locating a running service in a distributed system, tracking down who owns a particular piece of code, or identifying which team is responsible for a specific decision. The target is alive or active — for static artifacts, use Locate Object.
In this grimoire, Locate Creature is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Locate Creature (spell).
## When To Use

- You need to find who is responsible for a specific system, decision, or process.
- A running service or active process needs to be located in a complex distributed environment.
- You need to track down the right person to talk to about a specific topic in a large organization.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Define the target: who or what are you looking for, and what characteristics identify them?
3. Determine the search space: where could this entity be? Narrow the scope before searching broadly.
4. Search using available signals: ownership records, commit history, org charts, service registries, process lists.
5. Deliver the location with a confidence level and verification suggestion.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- The located entity: who/what it is and where it was found.
- The evidence trail: how we found it and how confident we are in the identification.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Locate Creature finds entities through legitimate, observable channels. Do not attempt to track people through unauthorized surveillance.
- Clearly state confidence level. A likely match is not a confirmed identification.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/locate-creature Use \$locate-creature to find this [person/service/process] in [the organization/system/environment]. Who owns it and where is it?
```
