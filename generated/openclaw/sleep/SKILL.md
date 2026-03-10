---
name: sleep
description: "In D&D, Sleep drops creatures into unconsciousness without violence — no save, no damage, they just stop. The real-world analog is graceful process suspension: DND mode, hibernation workflows, maintenance windows, cooldown periods. Sleep is not Kill. The target should wake up intact when the spell ends. This is the spell for when you need things to stop happening for a while without destroying state."
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

- You need to design or trigger a DND mode, maintenance window, or cooldown period.
- A noisy system — notifications, alerts, CI pipelines, chatbots — needs to be temporarily silenced without losing queued work.
- You want to draft a graceful degradation or hibernation plan for a service.

## Workflow

1. Identify what needs to sleep: the process, notification channel, service, or workflow.
2. Define the sleep boundary: what stops, what keeps running, and what queues for later.
3. Set the wake condition: timer, manual trigger, threshold, or external event.
4. Ensure state preservation — nothing should be lost during sleep, only deferred.
5. Return the sleep plan with wake conditions and a list of what remains active.

## Deliverables

- A sleep configuration: what is suspended, what stays active, and what queues.
- Wake conditions: how and when the system resumes.
- A state-preservation checklist: confirmation that no data or context is lost during suspension.

## Guardrails

- Sleep must be reversible. If waking the target would lose state or cause corruption, this is the wrong spell — use a proper shutdown instead.
- Do not use Sleep to avoid dealing with problems. Silencing alerts is not the same as fixing the underlying issue.
- Always define a maximum sleep duration. Indefinite sleep without a wake condition is a bug, not a feature.

## Default Invocation

Use $sleep to design a graceful suspension plan for this [system/process/notification channel]. Define what stops, what queues, and how it wakes up.

