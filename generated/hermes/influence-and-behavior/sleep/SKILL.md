---
name: sleep
description: "Sleep = temporary, reversible suspension with guaranteed state preservation. The target stops acting but wakes up intact. No data loss, no corruption, no permanent change."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - shipping-now
      - hybrid
      - influence-and-behavior
      - influence
      - behavior
      - attention
      - engagement
      - integration
      - home-assistant
---
# Sleep
Put processes, notifications, or systems into graceful suspension.
## What This Skill Does
Sleep = temporary, reversible suspension with guaranteed state preservation. The target stops acting but wakes up intact. No data loss, no corruption, no permanent change.
In this grimoire, Sleep is treated as a hybrid spell with a shipping-now delivery profile.
Canonical reference input: Sleep (spell).
## When To Use

- Keywords: pause, suspend, hibernate, DND, maintenance window, cooldown, quiet mode, silence temporarily, freeze (with resume), graceful degradation
- Patterns requiring all three:
- Something must stop acting for a defined period
- State/queue/context must be preserved during the stop
- A wake condition exists (timer, threshold, manual trigger, external event)

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
2. Identify the sleeper: What exact process, channel, service, or workflow stops?
3. Define the boundary: What stops, what keeps running, what queues for later?
4. Set the wake condition: Timer? Manual trigger? Threshold? External event? Must have one.
5. Verify state preservation: Confirm nothing is lost—only deferred. List what persists.
6. Return the plan: Sleep configuration + wake conditions + state-preservation checklist.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- Sleep configuration: what suspends, what stays active, what queues
- Wake conditions: how/when resume happens
- State-preservation checklist: confirmation nothing is lost

## Pitfalls / Guardrails

- Keep the theatrical framing, but name the concrete mechanism that makes the skill useful right now.
- Do not use for: "Permanently decommission" / "never come back" → Kill, not Sleep
- Do not use for: "Shut it down right now" / "pull offline" / "kill it" → Kill, not Sleep
- Do not use for: "Lock their credentials" / "prevent any further queries" → Access control, not Sleep
- Do not use for: "Paralyze a competing process" / "hard block" → Resource blocking, not Sleep
- Do not use for: "Team-wide agreement" / "communication norms" → Policy, not Sleep
- Do not use for: "Reduce fan noise" / "HVAC configuration" → Hardware config, not Sleep
- Do not use for: No wake condition defined → Bug, not Sleep (ask for one)
- Do not rely on a live integration until credentials, target scope, and rollback expectations are verified.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check which parts are concrete actions versus framing, so the user can tell what is real now.
- Check the required environment variables and binaries in the active Hermes runtime before trusting the procedure on a live target.

## Example Invocation
```text
/sleep design a graceful suspension plan for this [system/process/notification channel]. Define what stops, what queues, and how it wakes up
```
