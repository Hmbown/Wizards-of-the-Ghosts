---
name: sending
description: "Use this spell when you need to dispatch a message — the agent determines the right channel, formats for that medium, and sends with the user's approval."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - shipping-now
      - literal
      - messaging-and-coordination
      - messaging
      - coordination
      - handoffs
      - rhetoric
      - integration
      - slack
---
# Sending
Deliver a precisely crafted message to a specific recipient through the optimal channel.
## What This Skill Does
Use this spell when you need to dispatch a message — the agent determines the right channel, formats for that medium, and sends with the user's approval.
In this grimoire, Sending is treated as a literal spell with a shipping-now delivery profile.
Canonical reference input: Sending (spell).
## When To Use

- You need to notify a specific person or system and want the agent to pick the right channel: Slack, email, SMS, webhook, or GitHub.
- A message needs to be brief, high-signal, and formatted for its destination medium.
- You want the agent to draft and route a message but not send until you confirm.
- You need to actually send a Slack message or notification, not just draft one.

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
2. Identify the recipient and the core message to deliver.
3. Select the optimal delivery channel based on urgency, recipient preferences, and available integrations.
4. Draft the message formatted for the target medium — brief, high-signal, and channel-appropriate.
5. Present the draft for user approval, then dispatch through the chosen channel and confirm delivery.
6. If Slack is available, use the Slack API (chat.postMessage) to send the message to the target channel or user directly.
7. Stop for explicit confirmation before taking a live action that changes access, triggers an alert, or touches a real system boundary.
8. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A channel-appropriate draft message for user approval.
- Dispatch confirmation with timestamp and delivery status.
- A record of what was sent, to whom, and through which channel.

## Pitfalls / Guardrails

- Treat the live action surface as real operational work, not decorative lore.
- Never send without explicit user approval of both the content and the recipient.
- Never impersonate the user or misrepresent the sender. The message must be honest about its origin.
- Respect channel rate limits and norms — do not spam.
- Do not rely on a live integration until credentials, target scope, and rollback expectations are verified.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the exact live target, confirmation gate, and rollback or recovery path are explicit.
- Check the required environment variables and binaries in the active Hermes runtime before trusting the procedure on a live target.

## Example Invocation
```text
/sending draft and deliver this message through the best available channel, but show me the draft before it goes out
```
