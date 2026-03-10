---
name: dispel-magic
description: "Use this spell when you need to cleanly shut down, disable, or remove active AI tooling — the reverse of Detect Magic."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - shipping-now
      - literal
      - monitoring-and-protection
      - observability
      - monitoring
      - guardrails
      - privacy
---
# Dispel Magic
Safely decommission active automations, agents, monitors, and integrations.
## What This Skill Does
Use this spell when you need to cleanly shut down, disable, or remove active AI tooling — the reverse of Detect Magic.
In this grimoire, Dispel Magic is treated as a literal spell with a shipping-now delivery profile.
Canonical reference input: Dispel Magic (spell).
## When To Use

- An active automation, cron job, webhook, or agent loop needs to be turned off cleanly.
- You are decommissioning a system and need to ensure no orphaned automations keep running.
- A monitor or integration is misfiring and needs to be disabled before it causes more damage.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify the active magic to dispel — use Detect Magic first if the landscape is unclear.
3. Assess dependencies: what else relies on this automation, and what breaks if it stops.
4. Execute a graceful shutdown, preserving configuration for potential re-enable.
5. Verify the automation is fully stopped and report any residual effects or orphaned state.
6. Stop for explicit confirmation before taking a live action that changes access, triggers an alert, or touches a real system boundary.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- Confirmation that the target automation is fully stopped.
- A preserved copy of the configuration for potential re-enable.
- A list of downstream effects and any orphaned state that needs cleanup.

## Pitfalls / Guardrails

- Treat the live action surface as real operational work, not decorative lore.
- Always confirm with the user before disabling production-connected automations.
- Prefer graceful shutdown over hard kill — preserve state for recovery.
- Never dispel something you do not understand. Use Detect Magic first if uncertain.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the exact live target, confirmation gate, and rollback or recovery path are explicit.

## Example Invocation
```text
/dispel-magic safely shut down this automation and confirm nothing is left running that shouldn't be
```
