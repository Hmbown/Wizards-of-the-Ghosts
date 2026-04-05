---
name: magic-mouth
description: "Magic Mouth is trigger → message. The entire craft is specifying the trigger boundary, the message payload, and the suppression/escalation rules. It is NOT: - One-time messages: \"Send a Slack message now saying X\" (no trigger, no automation)\n- Full chatbots: \"Build a conversational AI that understands context and handles open-ended questions\" (requires NLU, dialogue management)\n- Monitoring dashboards: \"Set up Grafana with real-time graphs and trend analysis\" (visualization, not message routing)\n- Silent traps/wards: \"Revert changes silently and log who tried\" (defensive code manipulation, not messaging)\n- Encryption: \"Encrypt a message so only the recipient can read it\" (cryptography, not event-driven delivery)\n- Multimedia presentations: \"Play a 20-slide deck with animations and narration\" (media playback, not conditional messaging)"
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

- Use this spell when the user describes an event-driven message automation: a specific trigger condition (X) should cause a specific message or notification (Y) to be sent without manual intervention.
- Look for these patterns in the request:
- "When [condition], send/post/notify [message/recipient]"
- "Set up an autoresponder for [scenario]"
- "Create an alert rule for [metric/event]"
- "Design a webhook handler that posts to [channel] when [event]"
- Mentions of triggers, fire conditions, suppression rules, rate limits, or escalation stages
- Explicit no-fire cases ("don't fire if...", "suppress duplicates for...", "only once per...")

## Workflow

1. Extract the trigger: Identify the exact condition that fires the message (metric threshold, event type, time window, keyword match). Note any compound conditions or timing delays ("wait 5 minutes before firing").
2. Specify the payload: List every variable in the message (who, what, where, severity, links). Write the response template with placeholders.
3. Define boundaries: Document no-fire cases, rate limits, suppression windows, and escalation stages. Explicitly state what happens on repeated triggers.
4. Return the spec: Produce a trigger-response specification with test cases covering: nominal fire, no-fire, repeated-trigger suppression, and escalation progression. If Slack or a messaging API is available, include the concrete API call or workflow configuration.

## Deliverables

- A trigger-response specification or message template.
- Example payloads covering nominal and edge-case inputs.
- Notes on rate limits, suppression, escalation, and logging.

## Guardrails

- Do not automate messages requiring human judgment, empathy, or legal review
- Protect against loops, spam, and easily-spoofed trigger conditions
- Always include a suppression mechanism for repeated triggers

## Default Invocation

Use $magic-mouth to turn this trigger into a reliable automated response and show me the exact fire conditions.

