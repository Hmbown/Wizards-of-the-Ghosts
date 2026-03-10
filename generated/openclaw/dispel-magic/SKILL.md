---
name: dispel-magic
description: "Use this spell when you need to cleanly shut down, disable, or remove active AI tooling — the reverse of Detect Magic."
user-invocable: true
---

# Dispel Magic

Safely decommission active automations, agents, monitors, and integrations.

## Overview

Dispel Magic is interpreted here as a literal spell with a shipping-now execution model.

Canonical source: Dispel Magic (spell)

Provider target: OpenClaw

## When To Use

- An active automation, cron job, webhook, or agent loop needs to be turned off cleanly.
- You are decommissioning a system and need to ensure no orphaned automations keep running.
- A monitor or integration is misfiring and needs to be disabled before it causes more damage.

## Workflow

1. Identify the active magic to dispel — use Detect Magic first if the landscape is unclear.
2. Assess dependencies: what else relies on this automation, and what breaks if it stops.
3. Execute a graceful shutdown, preserving configuration for potential re-enable.
4. Verify the automation is fully stopped and report any residual effects or orphaned state.

## Deliverables

- Confirmation that the target automation is fully stopped.
- A preserved copy of the configuration for potential re-enable.
- A list of downstream effects and any orphaned state that needs cleanup.

## Guardrails

- Always confirm with the user before disabling production-connected automations.
- Prefer graceful shutdown over hard kill — preserve state for recovery.
- Never dispel something you do not understand. Use Detect Magic first if uncertain.

## Default Invocation

Use $dispel-magic to safely shut down this automation and confirm nothing is left running that shouldn't be.

