---
name: silence
description: "Use this spell when you are drowning in notifications, verbose logs, irrelevant alerts, or context that does not serve the current task."
user-invocable: true
metadata:
  openclaw:
    requires:
      env:
        - SLACK_TOKEN
      bins:
        - curl
    primaryEnv: SLACK_TOKEN
    emoji: "🤫"
---

# Silence

Suppress noise, filter irrelevant signals, and create focused working environments.

## Overview

Silence is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Silence (spell)

Provider target: OpenClaw

## When To Use

- Log output, notifications, or alerts are too noisy to find the signal.
- You need a focused environment where only relevant information gets through.
- A process or channel is generating volume that obscures what actually matters.
- You want to actually mute Slack channels or set DND mode, not just plan a noise-reduction strategy.

## Workflow

1. Identify the noise source and the signal you need to preserve.
2. Define the filter criteria: what gets silenced and what passes through.
3. Apply the silence with clear documentation of what is being suppressed.
4. Provide a way to lift the silence and restore full output when needed.
5. If Slack is available, use the Slack API to set DND (dnd.setSnooze), mute channels, or update notification preferences directly.

## Deliverables

- A filter or suppression configuration that reduces noise to signal.
- Clear documentation of what is silenced and what passes through.
- A restore mechanism to lift the silence when the focused session ends.

## Guardrails

- Silence suppresses noise, not signal. Never silence errors, critical alerts, or security warnings.
- Make the filter criteria explicit so important signals are not accidentally muted.

## Default Invocation

Use $silence to filter the noise here down to what actually matters, and tell me what you are suppressing.

