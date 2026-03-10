---
name: sleep
description: "In D&D, Sleep drops creatures into unconsciousness without violence — no save, no damage, they just stop. The real-world analog is graceful process suspension: DND mode, hibernation workflows, maintenance windows, cooldown periods. Sleep is not Kill. The target should wake up intact when the spell ends. This is the spell for when you need things to stop happening for a while without destroying state."
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
In D&D, Sleep drops creatures into unconsciousness without violence — no save, no damage, they just stop. The real-world analog is graceful process suspension: DND mode, hibernation workflows, maintenance windows, cooldown periods. Sleep is not Kill. The target should wake up intact when the spell ends. This is the spell for when you need things to stop happening for a while without destroying state.
In this grimoire, Sleep is treated as a hybrid spell with a shipping-now delivery profile.
Canonical reference input: Sleep (spell).
## When To Use

- You need to design or trigger a DND mode, maintenance window, or cooldown period.
- A noisy system — notifications, alerts, CI pipelines, chatbots — needs to be temporarily silenced without losing queued work.
- You want to draft a graceful degradation or hibernation plan for a service.

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
2. Identify what needs to sleep: the process, notification channel, service, or workflow.
3. Define the sleep boundary: what stops, what keeps running, and what queues for later.
4. Set the wake condition: timer, manual trigger, threshold, or external event.
5. Ensure state preservation — nothing should be lost during sleep, only deferred.
6. Return the sleep plan with wake conditions and a list of what remains active.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A sleep configuration: what is suspended, what stays active, and what queues.
- Wake conditions: how and when the system resumes.
- A state-preservation checklist: confirmation that no data or context is lost during suspension.

## Pitfalls / Guardrails

- Keep the theatrical framing, but name the concrete mechanism that makes the skill useful right now.
- Sleep must be reversible. If waking the target would lose state or cause corruption, this is the wrong spell — use a proper shutdown instead.
- Do not use Sleep to avoid dealing with problems. Silencing alerts is not the same as fixing the underlying issue.
- Always define a maximum sleep duration. Indefinite sleep without a wake condition is a bug, not a feature.
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
