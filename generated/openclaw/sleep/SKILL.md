---
name: sleep
description: "Sleep = temporary, reversible suspension with guaranteed state preservation. The target stops acting but wakes up intact. No data loss, no corruption, no permanent change."
user-invocable: true
metadata:
  openclaw:
    requires:
      env:
        - HA_URL
        - HA_TOKEN
      bins:
        - curl
    primaryEnv: HA_TOKEN
    emoji: "😴"
---

# Sleep

Put processes, notifications, or systems into graceful suspension.

## Overview

Sleep is interpreted here as a hybrid spell with a shipping-now execution model.

Canonical source: Sleep (spell)

Provider target: OpenClaw

## When To Use

- Keywords: pause, suspend, hibernate, DND, maintenance window, cooldown, quiet mode, silence temporarily, freeze (with resume), graceful degradation
- Patterns requiring all three:
- Something must stop acting for a defined period
- State/queue/context must be preserved during the stop
- A wake condition exists (timer, threshold, manual trigger, external event)

## Workflow

1. Identify the sleeper: What exact process, channel, service, or workflow stops?
2. Define the boundary: What stops, what keeps running, what queues for later?
3. Set the wake condition: Timer? Manual trigger? Threshold? External event? Must have one.
4. Verify state preservation: Confirm nothing is lost—only deferred. List what persists.
5. Return the plan: Sleep configuration + wake conditions + state-preservation checklist.

## Deliverables

- Sleep configuration: what suspends, what stays active, what queues
- Wake conditions: how/when resume happens
- State-preservation checklist: confirmation nothing is lost

## Guardrails

- Do not use for: "Permanently decommission" / "never come back" → Kill, not Sleep
- Do not use for: "Shut it down right now" / "pull offline" / "kill it" → Kill, not Sleep
- Do not use for: "Lock their credentials" / "prevent any further queries" → Access control, not Sleep
- Do not use for: "Paralyze a competing process" / "hard block" → Resource blocking, not Sleep
- Do not use for: "Team-wide agreement" / "communication norms" → Policy, not Sleep
- Do not use for: "Reduce fan noise" / "HVAC configuration" → Hardware config, not Sleep
- Do not use for: No wake condition defined → Bug, not Sleep (ask for one)

## Default Invocation

Use $sleep to design a graceful suspension plan for this [system/process/notification channel]. Define what stops, what queues, and how it wakes up.

