---
name: silence
description: "Use this spell when you are drowning in notifications, verbose logs, irrelevant alerts, or context that does not serve the current task."
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
      - monitoring-and-protection
      - observability
      - monitoring
      - guardrails
      - privacy
      - integration
      - slack
---
# Silence
Suppress noise, filter irrelevant signals, and create focused working environments.
## What This Skill Does
Use this spell when you are drowning in notifications, verbose logs, irrelevant alerts, or context that does not serve the current task.
In this grimoire, Silence is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Silence (spell).
## When To Use

- Log output, notifications, or alerts are too noisy to find the signal.
- You need a focused environment where only relevant information gets through.
- A process or channel is generating volume that obscures what actually matters.
- You want to actually mute Slack channels or set DND mode, not just plan a noise-reduction strategy.

## Prerequisites

- Environment variables available to Hermes: `SLACK_TOKEN`.
- Primary credential or token: `SLACK_TOKEN`.
- Binaries on PATH: `curl`.

## Setup

1. Confirm the required environment variables are available inside the active Hermes runtime, not just in a shell profile.
2. Verify the required binaries resolve on PATH before you rely on them in a procedure.
3. Choose a non-production or low-risk target first if the skill can page, unlock, alert, or touch a live integration.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify the noise source and the signal you need to preserve.
3. Define the filter criteria: what gets silenced and what passes through.
4. Apply the silence with clear documentation of what is being suppressed.
5. Provide a way to lift the silence and restore full output when needed.
6. If Slack is available, use the Slack API to set DND (dnd.setSnooze), mute channels, or update notification preferences directly.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A filter or suppression configuration that reduces noise to signal.
- Clear documentation of what is silenced and what passes through.
- A restore mechanism to lift the silence when the focused session ends.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Silence suppresses noise, not signal. Never silence errors, critical alerts, or security warnings.
- Make the filter criteria explicit so important signals are not accidentally muted.
- Do not rely on a live integration until credentials, target scope, and rollback expectations are verified.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.
- Check the required environment variables and binaries in the active Hermes runtime before trusting the procedure on a live target.

## Example Invocation
```text
/silence filter the noise here down to what actually matters, and tell me what you are suppressing
```
