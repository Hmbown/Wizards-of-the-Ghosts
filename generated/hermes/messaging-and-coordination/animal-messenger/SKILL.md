---
name: animal-messenger
description: "Animal Messenger is for delivery paths that are asynchronous, delayed, or a little scruffy. It fits webhook queues, batch email, pub/sub topics, and other channels where you launch the payload and trust the route more than the timing. The real craft is designing for eventual arrival without panic."
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
---
# Animal Messenger
Release the packet and trust the trail, not the clock.
## What This Skill Does
Animal Messenger is for delivery paths that are asynchronous, delayed, or a little scruffy. It fits webhook queues, batch email, pub/sub topics, and other channels where you launch the payload and trust the route more than the timing. The real craft is designing for eventual arrival without panic.
In this grimoire, Animal Messenger is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Animal Messenger (spell).
## When To Use

- The message is moving through a queue, bus, webhook chain, or other non-immediate route.
- You need fire-and-forget behavior with retries instead of synchronous confirmation.
- The receiver can tolerate delay but not duplication, corruption, or ambiguity.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Shape the payload for the carrier: compact, authenticated, and safe to retry.
3. Define delivery assumptions such as idempotency, retry policy, and dead-letter handling.
4. Return the message contract plus the signs that it arrived, stalled, or was mishandled.
5. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- An async-safe payload or message template.
- Retry and idempotency guidance for the chosen channel.
- A failure map covering delay, duplication, and silent loss.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Do not design async delivery as if it were instant or guaranteed.
- Use authentication, signatures, or integrity checks when the channel crosses trust boundaries.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/animal-messenger package this message for an async delivery path and tell me how to make it reliable enough
```
