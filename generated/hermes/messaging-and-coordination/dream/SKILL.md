---
name: dream
description: "Dream is asynchronous insight delivery timed to the receiver's readiness rather than the sender's convenience. It covers overnight reports, pre-meeting briefings, dawn digests, and other messages that should arrive as ambient context before work begins. The spell's magic is timing plus framing: the receiver wakes up to the answer, not a pile of raw events. It works best when the message feels prepared, quiet, and exactly on time. It fails when it becomes another noisy alert stream wearing a moonlit costume."
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
# Dream
Deliver the briefing before the recipient wakes up needing it.
## What This Skill Does
Dream is asynchronous insight delivery timed to the receiver's readiness rather than the sender's convenience. It covers overnight reports, pre-meeting briefings, dawn digests, and other messages that should arrive as ambient context before work begins. The spell's magic is timing plus framing: the receiver wakes up to the answer, not a pile of raw events. It works best when the message feels prepared, quiet, and exactly on time. It fails when it becomes another noisy alert stream wearing a moonlit costume.
In this grimoire, Dream is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Dream (spell).
## When To Use

- You need a scheduled report, wake-up memo, morning brief, or overnight analysis drop.
- The value comes from arriving before a decision window opens, not from immediate back-and-forth.
- A recipient needs distilled signal from work that happened while they were offline.
- You want to schedule a Slack message or digest that arrives before your team's morning standup.

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
2. Identify the receiver, the wake moment, and the decision or action the briefing should support.
3. Gather the overnight inputs, compress them into signal, and separate stable conclusions from still-moving facts.
4. Choose the delivery form and schedule that best fits the receiver: email digest, Slack summary, dashboard snapshot, or calendar-attached note.
5. Return the Dream package with the briefing itself, the send window, and the escalation rules for anything too urgent to wait.
6. If Slack is available, use chat.scheduleMessage to time the briefing delivery to the target channel before the recipient's work begins.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A scheduled briefing or digest template.
- A timing rule that says when it should land and why.
- A source list with freshness notes and any escalation exceptions.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Do not turn Dream into stealth paging; urgent incidents still need the right real-time channel.
- Label confidence and staleness so a polished morning brief does not masquerade as omniscience.
- Do not rely on a live integration until credentials, target scope, and rollback expectations are verified.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.
- Check the required environment variables and binaries in the active Hermes runtime before trusting the procedure on a live target.

## Example Invocation
```text
/dream create an async briefing that arrives at the right future moment, already distilled for the person who will wake up to it
```
