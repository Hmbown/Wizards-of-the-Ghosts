---
name: detect-thoughts
description: "In D&D, Detect Thoughts lets you read surface thoughts and probe deeper. The real-world version is intent analysis: figuring out what someone is trying to accomplish based on what they said, how they said it, and what they chose not to say. This is the analytical complement to Insight (which reads subtext intuitively) — Detect Thoughts is more structured and systematic."
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
      - investigation-and-preparation
      - analysis
      - discovery
      - translation
      - preflight
---
# Detect Thoughts
Surface the likely intent, priorities, and concerns behind a communication.
## What This Skill Does
In D&D, Detect Thoughts lets you read surface thoughts and probe deeper. The real-world version is intent analysis: figuring out what someone is trying to accomplish based on what they said, how they said it, and what they chose not to say. This is the analytical complement to Insight (which reads subtext intuitively) — Detect Thoughts is more structured and systematic.
In this grimoire, Detect Thoughts is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Detect Thoughts (spell).
## When To Use

- You have a message, brief, or request and need to systematically extract the sender's priorities, concerns, and unstated goals.
- A requirements document or feature request needs to be decoded: what do they actually need vs. what they asked for?
- You want to prepare for a negotiation or conversation by mapping the other party's likely positions and concerns.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Read the communication and identify explicit statements of intent, priority, and concern.
3. Analyze word choice, emphasis, and structure for implicit signals about what matters most.
4. Map the gap between stated and likely intent: where do they diverge?
5. Deliver the intent analysis with confidence levels and a recommendation for how to respond to the real priorities.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- An intent analysis: stated goals, implicit priorities, and likely concerns ranked by importance.
- A gap analysis: where stated intent and likely real intent diverge, with evidence.
- A response recommendation that addresses real priorities, not just stated ones.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Intent analysis is inference, not telepathy. Always present findings as likely, not certain.
- Do not assume adversarial intent by default. Most people communicate imperfectly, not deceptively.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/detect-thoughts analyze this [message/brief/request]. What are the real priorities, concerns, and intent behind what was said?
```
