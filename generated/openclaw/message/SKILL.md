---
name: message
description: "Message is the cantrip of communication: a Slack ping, webhook event, push notification, terse status note, or tiny machine-to-machine update. It is for fast, targeted transfer with almost no ceremony. The skill is less about eloquence than precision under tight payload and attention budgets."
user-invocable: true
metadata:
  openclaw:
    requires:
      env:
        - SLACK_TOKEN
      bins:
        - curl
    primaryEnv: SLACK_TOKEN
    emoji: "💬"
---

# Message

Send one small signal to the right place right now.

## Overview

Message is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Message (spell)

Provider target: OpenClaw

## When To Use

- You need a low-ceremony status update, alert, or machine-readable signal.
- The receiver only needs one action, one fact, or one nudge right now.
- A longer artifact would slow the handoff instead of improving it.
- You need to actually send a quick Slack message right now, not just draft one.

## Workflow

1. Reduce the communication to the one fact, action, or state change that matters.
2. Choose the lightest channel that reliably reaches the target.
3. Return the message copy or payload with any needed action window.
4. If Slack is available, use chat.postMessage to deliver the message to the specified channel or user immediately.

## Deliverables

- A concise message or event payload.
- A recommended delivery channel.
- An acknowledgement or timeout expectation.

## Guardrails

- Do not bury critical nuance in a channel too small to carry it safely.
- Avoid sending secrets or sensitive context through lightweight channels without appropriate protection.

## Default Invocation

Use $message to turn this into the smallest effective real-time update and choose the right channel for it.

