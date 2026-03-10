---
name: insight
description: "In D&D, Insight detects lies and reads true intentions. The real-world version is subtext analysis: figuring out what an email actually means, what a stakeholder's real objection is, what a user's bug report is actually describing, or what the unsaid concern is behind a seemingly simple question. Insight does not read minds — it reads signals that are present but not foregrounded."
user-invocable: true
---

# Insight

Read between the lines to surface what someone means but is not saying.

## Overview

Insight is interpreted here as a metaphorical skill with a shipping-now execution model.

Canonical source: Insight (skill)

Provider target: OpenClaw

## When To Use

- A message, request, or conversation has an obvious surface meaning and a likely different real meaning.
- You need to understand what someone actually wants rather than what they literally asked for.
- A stakeholder's stated objection does not match their behavior, and you need to identify the real blocker.

## Workflow

1. Read the surface communication: what is being explicitly said or asked.
2. Identify the signals that do not fit the surface reading: tone shifts, conspicuous omissions, hedging language, over-specificity.
3. Generate the most likely subtext: what is the real concern, objection, or request?
4. Present both readings — surface and subtext — with confidence levels. Never claim the subtext is certain.
5. Suggest a response that addresses the subtext without calling it out aggressively.

## Deliverables

- The surface reading: what was literally said.
- The subtext reading: what is likely meant, with evidence from the signals.
- A suggested response that addresses the real concern diplomatically.

## Guardrails

- Subtext analysis is inference, not mind-reading. Always present it as a hypothesis with supporting evidence, never as certainty.
- Do not project malicious intent without strong signal. Most communication gaps are confusion, not manipulation.

## Default Invocation

Use $insight to read between the lines of this [message/conversation/request]. What is the surface meaning, what is the likely subtext, and how should I respond to the real concern?

