---
name: animal-messenger
description: "Animal Messenger is for delivery paths that are asynchronous, delayed, or a little scruffy. It fits webhook queues, batch email, pub/sub topics, and other channels where you launch the payload and trust the route more than the timing. The real craft is designing for eventual arrival without panic."
user-invocable: true
---

# Animal Messenger

Release the packet and trust the trail, not the clock.

## Overview

Animal Messenger is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Animal Messenger (spell)

Provider target: OpenClaw

## When To Use

- The message is moving through a queue, bus, webhook chain, or other non-immediate route.
- You need fire-and-forget behavior with retries instead of synchronous confirmation.
- The receiver can tolerate delay but not duplication, corruption, or ambiguity.

## Workflow

1. Shape the payload for the carrier: compact, authenticated, and safe to retry.
2. Define delivery assumptions such as idempotency, retry policy, and dead-letter handling.
3. Return the message contract plus the signs that it arrived, stalled, or was mishandled.

## Deliverables

- An async-safe payload or message template.
- Retry and idempotency guidance for the chosen channel.
- A failure map covering delay, duplication, and silent loss.

## Guardrails

- Do not design async delivery as if it were instant or guaranteed.
- Use authentication, signatures, or integrity checks when the channel crosses trust boundaries.

## Default Invocation

Use $animal-messenger to package this message for an async delivery path and tell me how to make it reliable enough.

