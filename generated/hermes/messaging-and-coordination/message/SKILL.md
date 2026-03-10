---
name: message
description: "Message is the cantrip of communication: a Slack ping, webhook event, push notification, terse status note, or tiny machine-to-machine update. It is for fast, targeted transfer with almost no ceremony. The skill is less about eloquence than precision under tight payload and attention budgets."
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
      - messaging-and-coordination
      - messaging
      - coordination
      - handoffs
      - rhetoric
      - integration
      - slack
---
# Message
Send one small signal to the right place right now.
## What This Skill Does
Message is the cantrip of communication: a Slack ping, webhook event, push notification, terse status note, or tiny machine-to-machine update. It is for fast, targeted transfer with almost no ceremony. The skill is less about eloquence than precision under tight payload and attention budgets.
In this grimoire, Message is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Message (spell).
## When To Use

- You need a low-ceremony status update, alert, or machine-readable signal.
- The receiver only needs one action, one fact, or one nudge right now.
- A longer artifact would slow the handoff instead of improving it.
- You need to actually send a quick Slack message right now, not just draft one.

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
2. Reduce the communication to the one fact, action, or state change that matters.
3. Choose the lightest channel that reliably reaches the target.
4. Return the message copy or payload with any needed action window.
5. If Slack is available, use chat.postMessage to deliver the message to the specified channel or user immediately.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A concise message or event payload.
- A recommended delivery channel.
- An acknowledgement or timeout expectation.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Do not bury critical nuance in a channel too small to carry it safely.
- Avoid sending secrets or sensitive context through lightweight channels without appropriate protection.
- Do not rely on a live integration until credentials, target scope, and rollback expectations are verified.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.
- Check the required environment variables and binaries in the active Hermes runtime before trusting the procedure on a live target.

## Example Invocation
```text
/message turn this into the smallest effective real-time update and choose the right channel for it
```
