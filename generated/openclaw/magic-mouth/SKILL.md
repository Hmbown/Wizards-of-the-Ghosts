---
name: magic-mouth
description: "Use this spell for event-driven responses: autoresponders, webhook messages, alert text, or chatbot replies that fire when a known condition is met. The craft lies in defining the trigger boundary and the exact message that should emerge when it trips."
user-invocable: true
metadata:
  openclaw:
    requires:
      env:
        - SLACK_TOKEN
      bins:
        - curl
    primaryEnv: SLACK_TOKEN
    emoji: "🗣️"
---

# Magic Mouth

Bind a message to a trigger so the system speaks exactly when it should.

## Overview

Magic Mouth is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Magic Mouth (spell)

Provider target: OpenClaw

## When To Use

- When X happens, you need the system to send or say Y without manual intervention.
- A recurring operational message, chatbot reply, or alert should be driven by a known event.
- The main work is specifying the trigger, payload, and suppression rules clearly.
- You want to set up an autoresponder or event-triggered message in Slack — out-of-office replies, deploy notifications, or welcome messages.

## Workflow

1. Define the trigger condition, delivery channel, recipient context, and no-fire cases.
2. Write the response template with variables, suppression rules, and escalation behavior.
3. Return the automation spec with test cases for fire, no-fire, and repeated-trigger scenarios.
4. If Slack is available, use the Slack API to set up scheduled messages, channel topic updates, or workflow-triggered responses.

## Deliverables

- A trigger-response specification or message template.
- Example payloads covering nominal and edge-case inputs.
- Notes on rate limits, suppression, escalation, and logging.

## Guardrails

- Do not automate messages that require human judgment, empathy, or legal review.
- Protect against loops, spam, and trigger conditions that can be spoofed too easily.

## Default Invocation

Use $magic-mouth to turn this trigger into a reliable automated response and show me the exact fire conditions.

