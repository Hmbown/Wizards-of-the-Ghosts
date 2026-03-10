---
name: sending
description: "Use this spell when you need to dispatch a message — the agent determines the right channel, formats for that medium, and sends with the user's approval."
user-invocable: true
metadata:
  openclaw:
    requires:
      env:
        - SLACK_TOKEN
      bins:
        - curl
    primaryEnv: SLACK_TOKEN
    emoji: "📨"
---

# Sending

Deliver a precisely crafted message to a specific recipient through the optimal channel.

## Overview

Sending is interpreted here as a literal spell with a shipping-now execution model.

Canonical source: Sending (spell)

Provider target: OpenClaw

## When To Use

- You need to notify a specific person or system and want the agent to pick the right channel: Slack, email, SMS, webhook, or GitHub.
- A message needs to be brief, high-signal, and formatted for its destination medium.
- You want the agent to draft and route a message but not send until you confirm.
- You need to actually send a Slack message or notification, not just draft one.

## Workflow

1. Identify the recipient and the core message to deliver.
2. Select the optimal delivery channel based on urgency, recipient preferences, and available integrations.
3. Draft the message formatted for the target medium — brief, high-signal, and channel-appropriate.
4. Present the draft for user approval, then dispatch through the chosen channel and confirm delivery.
5. If Slack is available, use the Slack API (chat.postMessage) to send the message to the target channel or user directly.

## Deliverables

- A channel-appropriate draft message for user approval.
- Dispatch confirmation with timestamp and delivery status.
- A record of what was sent, to whom, and through which channel.

## Guardrails

- Never send without explicit user approval of both the content and the recipient.
- Never impersonate the user or misrepresent the sender. The message must be honest about its origin.
- Respect channel rate limits and norms — do not spam.

## Default Invocation

Use $sending to draft and deliver this message through the best available channel, but show me the draft before it goes out.

