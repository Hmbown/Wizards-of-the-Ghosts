---
name: illusory-script
description: "Illusory Script is for audience-gated or self-expiring content: burn-after-reading notes, scoped links, ephemeral secrets, and documents that should only mean something to the right reader in the right window. The spell is partly social pattern and partly security mechanism. It is useful, but it is not a substitute for mature secrets management or compliance records."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - prototype
      - hybrid
      - messaging-and-coordination
      - messaging
      - coordination
      - handoffs
      - rhetoric
---
# Illusory Script
Let the secret appear only to the intended eyes, then fade.
## What This Skill Does
Illusory Script is for audience-gated or self-expiring content: burn-after-reading notes, scoped links, ephemeral secrets, and documents that should only mean something to the right reader in the right window. The spell is partly social pattern and partly security mechanism. It is useful, but it is not a substitute for mature secrets management or compliance records.
In this grimoire, Illusory Script is treated as a hybrid spell with a prototype delivery profile.
Canonical reference input: Illusory Script (spell).
## When To Use

- A message or credential should have limited audience, limited lifetime, or both.
- You need temporary visibility rather than permanent shared documentation.
- The content is sensitive enough that broad or durable circulation creates needless risk.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Define who may see the content, under what conditions, and when it must disappear or be revoked.
3. Choose the delivery and expiry mechanism that best fits the sensitivity and audit needs.
4. Return the audience, lifetime, and residual-risk model for the message.
5. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A scoped-delivery plan for the content or secret.
- Expiry, revocation, or burn-after-read rules.
- A note on what must still be tracked outside the ephemeral channel.

## Pitfalls / Guardrails

- Call out the glue, permissions, or missing infrastructure before you imply this is fully operational.
- Do not confuse expiring visibility with actual deletion from logs, inboxes, screenshots, or downstream systems.
- Do not use ephemeral channels where policy, legal, or operational requirements demand durable records.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check which parts are concrete actions versus framing, so the user can tell what is real now.
- Check that any missing glue code, permissions, or future work is labeled before the skill is treated as ready.

## Example Invocation
```text
/illusory-script design a message or secret-sharing flow that only the right audience can read, for only as long as it should exist
```
