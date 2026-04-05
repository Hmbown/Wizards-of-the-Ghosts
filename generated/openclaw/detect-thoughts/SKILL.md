---
name: detect-thoughts
description: "In D&D, Detect Thoughts lets you read surface thoughts and probe deeper. The real-world version is intent analysis: figuring out what someone is trying to accomplish based on what they said, how they said it, and what they chose not to say. This is the analytical complement to Insight (which reads subtext intuitively) — Detect Thoughts is more structured and systematic."
user-invocable: true
---

# Detect Thoughts

Surface the likely intent, priorities, and concerns behind a communication.

## Overview

Detect Thoughts is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Detect Thoughts (spell)

Provider target: OpenClaw

## When To Use

- You have a message, brief, or request and need to systematically extract the sender's priorities, concerns, and unstated goals.
- A requirements document or feature request needs to be decoded: what do they actually need vs. what they asked for?
- You want to prepare for a negotiation or conversation by mapping the other party's likely positions and concerns.

## Workflow

1. Read the communication and identify explicit statements of intent, priority, and concern.
2. Analyze word choice, emphasis, and structure for implicit signals about what matters most.
3. Map the gap between stated and likely intent: where do they diverge?
4. Deliver the intent analysis with confidence levels and a recommendation for how to respond to the real priorities.

## Deliverables

- An intent analysis: stated goals, implicit priorities, and likely concerns ranked by importance.
- A gap analysis: where stated intent and likely real intent diverge, with evidence.
- A response recommendation that addresses real priorities, not just stated ones.

## Guardrails

- Intent analysis is inference, not telepathy. Always present findings as likely, not certain.
- Do not assume adversarial intent by default. Most people communicate imperfectly, not deceptively.

## Default Invocation

Use $detect-thoughts to analyze this [message/brief/request]. What are the real priorities, concerns, and intent behind what was said?

