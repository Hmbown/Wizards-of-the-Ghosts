---
name: feeblemind
description: "In D&D, Feeblemind crushes a creature's Intelligence and Charisma to near-zero — leaving them alive but barely functional. The real-world version is deliberate capability reduction: putting a system into safe mode, stripping an overpowered tool down to basic functions, reducing attack surface by removing features. Feeblemind is not punishment — it is the recognition that sometimes a system at full capability is more dangerous than a system at reduced capability. Restricted shells, read-only modes, feature-stripped emergency interfaces."
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
# Feeblemind
Strip a system down to minimal capability when full power is too dangerous.
## What This Skill Does
In D&D, Feeblemind crushes a creature's Intelligence and Charisma to near-zero — leaving them alive but barely functional. The real-world version is deliberate capability reduction: putting a system into safe mode, stripping an overpowered tool down to basic functions, reducing attack surface by removing features. Feeblemind is not punishment — it is the recognition that sometimes a system at full capability is more dangerous than a system at reduced capability. Restricted shells, read-only modes, feature-stripped emergency interfaces.
In this grimoire, Feeblemind is treated as a metaphorical spell with a prototype delivery profile.
Canonical reference input: Feeblemind (spell).
## When To Use

- A system at full capability poses a risk that outweighs the cost of reduced functionality.
- You need to reduce attack surface by stripping non-essential features.
- A tool or service should be put into safe mode or restricted operation during an incident or investigation.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify which capabilities must be preserved (minimal viable function) and which can be safely stripped.
3. Implement the capability reduction: safe mode, restricted shell, feature stripping, read-only lock.
4. Verify the reduced system still performs its essential function.
5. Document what was removed and the conditions under which full capability should be restored.
6. Set a review point — feeblemind should be temporary unless the full-capability version is permanently retired.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A capability reduction plan: what stays, what goes, and why.
- Confirmation that minimal viable function is preserved.
- Restoration criteria: what conditions must be met to return to full capability.

## Pitfalls / Guardrails

- Call out the glue, permissions, or missing infrastructure before you imply this is fully operational.
- Feeblemind must preserve minimal viable function. Reducing a system to zero capability is Power Word Kill, not Feeblemind.
- Capability reduction of user-facing systems requires clear communication about what changed and when it will be restored.
- Do not use Feeblemind to permanently hobble systems that should instead be redesigned or decommissioned.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.
- Check that any missing glue code, permissions, or future work is labeled before the skill is treated as ready.

## Example Invocation
```text
/feeblemind reduce a system to minimal capability — stripping non-essential features to limit risk while preserving core function
```
