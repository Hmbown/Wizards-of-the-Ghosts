---
name: magic-mouth
description: "Use this spell for event-driven responses: autoresponders, webhook messages, alert text, or chatbot replies that fire when a known condition is met. The craft lies in defining the trigger boundary and the exact message that should emerge when it trips."
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
Use this spell for event-driven responses: autoresponders, webhook messages, alert text, or chatbot replies that fire when a known condition is met. The craft lies in defining the trigger boundary and the exact message that should emerge when it trips.
In this grimoire, Magic Mouth is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Magic Mouth (spell).
## When To Use

- When X happens, you need the system to send or say Y without manual intervention.
- A recurring operational message, chatbot reply, or alert should be driven by a known event.
- The main work is specifying the trigger, payload, and suppression rules clearly.
- You want to set up an autoresponder or event-triggered message in Slack — out-of-office replies, deploy notifications, or welcome messages.

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
2. Define the trigger condition, delivery channel, recipient context, and no-fire cases.
3. Write the response template with variables, suppression rules, and escalation behavior.
4. Return the automation spec with test cases for fire, no-fire, and repeated-trigger scenarios.
5. If Slack is available, use the Slack API to set up scheduled messages, channel topic updates, or workflow-triggered responses.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A trigger-response specification or message template.
- Example payloads covering nominal and edge-case inputs.
- Notes on rate limits, suppression, escalation, and logging.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Do not automate messages that require human judgment, empathy, or legal review.
- Protect against loops, spam, and trigger conditions that can be spoofed too easily.
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
