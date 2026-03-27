---
name: project-image
description: "Create a remote presence — bot avatar, recorded stand-in, or automated representative — that acts on your behalf in meetings, channels, or async workflows. Use when you need to be present somewhere you cannot physically attend while maintaining clear authority boundaries and escalation paths."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - shipping-now
      - hybrid
      - simulation-and-staging
      - simulation
      - staging
      - mockup
      - testing
---
# Project Image

Create a remote presence that acts on your behalf in meetings, channels, or async workflows.

## When To Use

- You need presence in a meeting, channel, or async space you cannot physically attend.
- A recorded or automated stand-in can handle routine interactions (standups, status updates, Q&A).
- You want to delegate attendance while retaining control over what the projection can commit to.

## Procedure

1. **Define the projection type.** Choose one:
   - **Live avatar**: join a video call or chat session as a bot that relays your messages in real time.
   - **Recorded stand-in**: pre-record a video or audio briefing to be played at a scheduled time.
   - **Automated representative**: deploy a bot or script that responds to known queries using pre-approved answers.

2. **Set authority boundaries.** Write an explicit scope document:
   - What the projection **can** say or commit to (e.g., "confirm attendance at next sprint review").
   - What requires **escalation** to the real person (e.g., "any budget commitment over $500").
   - What is **off-limits** (e.g., "do not agree to deadline changes").

3. **Deploy the projection.**
   - For Slack bots: configure a webhook or app with pre-approved response templates.
   - For recorded messages: schedule delivery via calendar invite or channel post.
   - For meeting bots: use a tool like Recall.ai or a custom integration to join and relay.

4. **Monitor and escalate.** Set up alerts for situations outside the projection's authority. Example: if the bot receives a question not in its approved list, it responds with "Let me check with [your name] and get back to you."

5. **Debrief.** After the session, review what the projection handled, what it escalated, and whether authority boundaries need adjustment for next time.

## Deliverables

- A deployed remote presence (bot, recording, or automated responder) with a clear mandate.
- An authority boundary document listing approved actions, escalation triggers, and off-limits topics.
- A post-session debrief noting what was handled autonomously vs. escalated.

## Pitfalls / Guardrails

- Remote projections **must be disclosed** as automated or pre-recorded. Pretending a bot is a live human is deception.
- Authority limits must be **explicit and written down** before deployment. A projection that agrees to commitments outside its scope creates real obligations.
- Do not use projected presence to avoid accountability. If a situation requires your real attention, be present.
- Always provide a way for recipients to reach the real person if the projection cannot help.

## Example

```
User: /project-image I have two meetings at the same time tomorrow — the
      sprint standup and the vendor check-in. I can attend the vendor call
      live but need a stand-in for standup.

Agent: Here is the plan for your standup projection:

       1. Projection type: Slack bot posting to #engineering-standup at 9:15 AM.
       2. Authority: report your status ("Completed auth refactor, starting
          API tests today"), confirm no blockers.
       3. Escalation: if anyone asks about timeline changes or new
          requirements, bot replies "I will loop in [you] after the vendor
          call — expect a response by 11 AM."
       4. Off-limits: do not commit to scope changes or volunteer for
          unplanned work.

       Shall I draft the bot script and schedule the post?
```
