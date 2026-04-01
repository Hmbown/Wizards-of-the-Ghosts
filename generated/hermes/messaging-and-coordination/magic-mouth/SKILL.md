---
name: magic-mouth
description: "Magic Mouth is trigger → message. The entire craft is specifying the trigger boundary, the message payload, and the suppression/escalation rules. It is NOT: - One-time messages: \"Send a Slack message now saying X\" (no trigger, no automation)\n- Full chatbots: \"Build a conversational AI that understands context and handles open-ended questions\" (requires NLU, dialogue management)\n- Monitoring dashboards: \"Set up Grafana with real-time graphs and trend analysis\" (visualization, not message routing)\n- Silent traps/wards: \"Revert changes silently and log who tried\" (defensive code manipulation, not messaging)\n- Encryption: \"Encrypt a message so only the recipient can read it\" (cryptography, not event-driven delivery)\n- Multimedia presentations: \"Play a 20-slide deck with animations and narration\" (media playback, not conditional messaging)"
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
# Magic Mouth
Bind a message to a trigger so the system speaks exactly when it should.
## What This Skill Does
Magic Mouth is trigger → message. The entire craft is specifying the trigger boundary, the message payload, and the suppression/escalation rules. It is NOT: - One-time messages: "Send a Slack message now saying X" (no trigger, no automation)
- Full chatbots: "Build a conversational AI that understands context and handles open-ended questions" (requires NLU, dialogue management)
- Monitoring dashboards: "Set up Grafana with real-time graphs and trend analysis" (visualization, not message routing)
- Silent traps/wards: "Revert changes silently and log who tried" (defensive code manipulation, not messaging)
- Encryption: "Encrypt a message so only the recipient can read it" (cryptography, not event-driven delivery)
- Multimedia presentations: "Play a 20-slide deck with animations and narration" (media playback, not conditional messaging)
In this grimoire, Magic Mouth is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Magic Mouth (spell).
## When To Use

- Use this spell when the user describes an event-driven message automation: a specific trigger condition (X) should cause a specific message or notification (Y) to be sent without manual intervention.
- Look for these patterns in the request:
- "When [condition], send/post/notify [message/recipient]"
- "Set up an autoresponder for [scenario]"
- "Create an alert rule for [metric/event]"
- "Design a webhook handler that posts to [channel] when [event]"
- Mentions of triggers, fire conditions, suppression rules, rate limits, or escalation stages
- Explicit no-fire cases ("don't fire if...", "suppress duplicates for...", "only once per...")

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
2. Extract the trigger: Identify the exact condition that fires the message (metric threshold, event type, time window, keyword match). Note any compound conditions or timing delays ("wait 5 minutes before firing").
3. Specify the payload: List every variable in the message (who, what, where, severity, links). Write the response template with placeholders.
4. Define boundaries: Document no-fire cases, rate limits, suppression windows, and escalation stages. Explicitly state what happens on repeated triggers.
5. Return the spec: Produce a trigger-response specification with test cases covering: nominal fire, no-fire, repeated-trigger suppression, and escalation progression. If Slack or a messaging API is available, include the concrete API call or workflow configuration.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A trigger-response specification or message template.
- Example payloads covering nominal and edge-case inputs.
- Notes on rate limits, suppression, escalation, and logging.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Do not automate messages requiring human judgment, empathy, or legal review
- Protect against loops, spam, and easily-spoofed trigger conditions
- Always include a suppression mechanism for repeated triggers
- Do not rely on a live integration until credentials, target scope, and rollback expectations are verified.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.
- Check the required environment variables and binaries in the active Hermes runtime before trusting the procedure on a live target.

## Example Invocation
```text
/magic-mouth turn this trigger into a reliable automated response and show me the exact fire conditions
```
