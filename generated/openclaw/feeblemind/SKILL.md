---
name: feeblemind
description: "In D&D, Feeblemind crushes a creature's Intelligence and Charisma to near-zero — leaving them alive but barely functional. The real-world version is deliberate capability reduction: putting a system into safe mode, stripping an overpowered tool down to basic functions, reducing attack surface by removing features. Feeblemind is not punishment — it is the recognition that sometimes a system at full capability is more dangerous than a system at reduced capability. Restricted shells, read-only modes, feature-stripped emergency interfaces."
user-invocable: true
---

# Feeblemind

Strip a system down to minimal capability when full power is too dangerous.

## Overview

Feeblemind is interpreted here as a metaphorical spell with a prototype execution model.

Canonical source: Feeblemind (spell)

Provider target: OpenClaw

## When To Use

- A system at full capability poses a risk that outweighs the cost of reduced functionality.
- You need to reduce attack surface by stripping non-essential features.
- A tool or service should be put into safe mode or restricted operation during an incident or investigation.

## Workflow

1. Identify which capabilities must be preserved (minimal viable function) and which can be safely stripped.
2. Implement the capability reduction: safe mode, restricted shell, feature stripping, read-only lock.
3. Verify the reduced system still performs its essential function.
4. Document what was removed and the conditions under which full capability should be restored.
5. Set a review point — feeblemind should be temporary unless the full-capability version is permanently retired.

## Deliverables

- A capability reduction plan: what stays, what goes, and why.
- Confirmation that minimal viable function is preserved.
- Restoration criteria: what conditions must be met to return to full capability.

## Guardrails

- Feeblemind must preserve minimal viable function. Reducing a system to zero capability is Power Word Kill, not Feeblemind.
- Capability reduction of user-facing systems requires clear communication about what changed and when it will be restored.
- Do not use Feeblemind to permanently hobble systems that should instead be redesigned or decommissioned.

## Default Invocation

Use $feeblemind to reduce a system to minimal capability — stripping non-essential features to limit risk while preserving core function.

