---
name: dream
description: "Dream is asynchronous insight delivery timed to the receiver's readiness rather than the sender's convenience. It covers overnight reports, pre-meeting briefings, dawn digests, and other messages that should arrive as ambient context before work begins. The spell's magic is timing plus framing: the receiver wakes up to the answer, not a pile of raw events. It works best when the message feels prepared, quiet, and exactly on time. It fails when it becomes another noisy alert stream wearing a moonlit costume."
user-invocable: true
metadata:
  openclaw:
    requires:
      env:
        - SLACK_TOKEN
      bins:
        - curl
    primaryEnv: SLACK_TOKEN
    emoji: "🌙"
---

# Dream

Deliver the briefing before the recipient wakes up needing it.

## Overview

Dream is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Dream (spell)

Provider target: OpenClaw

## When To Use

- You need a scheduled report, wake-up memo, morning brief, or overnight analysis drop.
- The value comes from arriving before a decision window opens, not from immediate back-and-forth.
- A recipient needs distilled signal from work that happened while they were offline.
- You want to schedule a Slack message or digest that arrives before your team's morning standup.

## Workflow

1. Identify the receiver, the wake moment, and the decision or action the briefing should support.
2. Gather the overnight inputs, compress them into signal, and separate stable conclusions from still-moving facts.
3. Choose the delivery form and schedule that best fits the receiver: email digest, Slack summary, dashboard snapshot, or calendar-attached note.
4. Return the Dream package with the briefing itself, the send window, and the escalation rules for anything too urgent to wait.
5. If Slack is available, use chat.scheduleMessage to time the briefing delivery to the target channel before the recipient's work begins.

## Deliverables

- A scheduled briefing or digest template.
- A timing rule that says when it should land and why.
- A source list with freshness notes and any escalation exceptions.

## Guardrails

- Do not turn Dream into stealth paging; urgent incidents still need the right real-time channel.
- Label confidence and staleness so a polished morning brief does not masquerade as omniscience.

## Default Invocation

Use $dream to create an async briefing that arrives at the right future moment, already distilled for the person who will wake up to it.

