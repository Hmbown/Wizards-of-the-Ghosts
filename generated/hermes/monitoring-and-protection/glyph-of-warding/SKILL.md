---
name: glyph-of-warding
description: "Use this skill when you need a watchful boundary around files, systems, metrics, queues, or workflows."
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
      - integration
      - home-assistant
---
# Glyph of Warding
Set monitors, watches, or trigger conditions that alert when a boundary is crossed.
## What This Skill Does
Use this skill when you need a watchful boundary around files, systems, metrics, queues, or workflows.
In this grimoire, Glyph of Warding is treated as a literal spell with a shipping-now delivery profile.
Canonical reference input: Glyph of Warding (spell).
## When To Use

- A repo, service, or process needs a tripwire.
- You want notification when a threshold, change, or policy breach occurs.
- A quiet monitor is safer than constant manual checking.
- You want to set up a Home Assistant automation that alerts you when a sensor crosses a threshold — motion detected, door opened, temperature spike.

## Prerequisites

- Environment variables available to Hermes: `HA_URL`, `HA_TOKEN`.
- Primary credential or token: `HA_TOKEN`.
- Binaries on PATH: `curl`.

## Setup

1. Confirm the required environment variables are available inside the active Hermes runtime, not just in a shell profile.
2. Verify the required binaries resolve on PATH before you rely on them in a procedure.
3. Choose a non-production or low-risk target first if the skill can page, unlock, alert, or touch a live integration.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Define the boundary, signal, or threshold to watch.
3. Choose the lightest viable monitoring mechanism.
4. Specify trigger behavior, recipient, and escalation path.
5. Return the alarm definition plus test instructions.
6. If Home Assistant is available, create or update an automation via the HA REST API that watches the specified entity and triggers an alert action (notification, light flash, webhook) when conditions are met.
7. Stop for explicit confirmation before taking a live action that changes access, triggers an alert, or touches a real system boundary.
8. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A concrete monitor or alert configuration.
- A test plan for verifying the trigger.
- A note on false-positive and false-negative risk.

## Pitfalls / Guardrails

- Treat the live action surface as real operational work, not decorative lore.
- Avoid noisy alerts with no clear owner or threshold.
- Do not silently create monitors that page humans without explicit intent.
- Do not rely on a live integration until credentials, target scope, and rollback expectations are verified.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the exact live target, confirmation gate, and rollback or recovery path are explicit.
- Check the required environment variables and binaries in the active Hermes runtime before trusting the procedure on a live target.

## Example Invocation
```text
/glyph-of-warding define a watch or alert around this workflow and make the trigger conditions explicit
```
