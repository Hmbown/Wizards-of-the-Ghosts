---
name: illusory-script
description: "Illusory Script is for audience-gated or self-expiring content: burn-after-reading notes, scoped links, ephemeral secrets, and documents that should only mean something to the right reader in the right window. The spell is partly social pattern and partly security mechanism. It is useful, but it is not a substitute for mature secrets management or compliance records."
user-invocable: false
disable-model-invocation: true
---

# Illusory Script

Let the secret appear only to the intended eyes, then fade.

## Overview

Illusory Script is interpreted here as a hybrid spell with a prototype execution model.

Canonical source: Illusory Script (spell)

Provider target: OpenClaw

## When To Use

- A message or credential should have limited audience, limited lifetime, or both.
- You need temporary visibility rather than permanent shared documentation.
- The content is sensitive enough that broad or durable circulation creates needless risk.

## Workflow

1. Define who may see the content, under what conditions, and when it must disappear or be revoked.
2. Choose the delivery and expiry mechanism that best fits the sensitivity and audit needs.
3. Return the audience, lifetime, and residual-risk model for the message.

## Deliverables

- A scoped-delivery plan for the content or secret.
- Expiry, revocation, or burn-after-read rules.
- A note on what must still be tracked outside the ephemeral channel.

## Guardrails

- Do not confuse expiring visibility with actual deletion from logs, inboxes, screenshots, or downstream systems.
- Do not use ephemeral channels where policy, legal, or operational requirements demand durable records.

## Default Invocation

Use $illusory-script to design a message or secret-sharing flow that only the right audience can read, for only as long as it should exist.

