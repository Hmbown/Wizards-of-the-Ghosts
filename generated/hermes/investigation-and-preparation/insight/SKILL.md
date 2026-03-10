---
name: insight
description: "In D&D, Insight detects lies and reads true intentions. The real-world version is subtext analysis: figuring out what an email actually means, what a stakeholder's real objection is, what a user's bug report is actually describing, or what the unsaid concern is behind a seemingly simple question. Insight does not read minds — it reads signals that are present but not foregrounded."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - skill
      - shipping-now
      - metaphorical
      - investigation-and-preparation
      - analysis
      - discovery
      - translation
      - preflight
---
# Insight
Read between the lines to surface what someone means but is not saying.
## What This Skill Does
In D&D, Insight detects lies and reads true intentions. The real-world version is subtext analysis: figuring out what an email actually means, what a stakeholder's real objection is, what a user's bug report is actually describing, or what the unsaid concern is behind a seemingly simple question. Insight does not read minds — it reads signals that are present but not foregrounded.
In this grimoire, Insight is treated as a metaphorical skill with a shipping-now delivery profile.
Canonical reference input: Insight (skill).
## When To Use

- A message, request, or conversation has an obvious surface meaning and a likely different real meaning.
- You need to understand what someone actually wants rather than what they literally asked for.
- A stakeholder's stated objection does not match their behavior, and you need to identify the real blocker.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Read the surface communication: what is being explicitly said or asked.
3. Identify the signals that do not fit the surface reading: tone shifts, conspicuous omissions, hedging language, over-specificity.
4. Generate the most likely subtext: what is the real concern, objection, or request?
5. Present both readings — surface and subtext — with confidence levels. Never claim the subtext is certain.
6. Suggest a response that addresses the subtext without calling it out aggressively.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- The surface reading: what was literally said.
- The subtext reading: what is likely meant, with evidence from the signals.
- A suggested response that addresses the real concern diplomatically.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Subtext analysis is inference, not mind-reading. Always present it as a hypothesis with supporting evidence, never as certainty.
- Do not project malicious intent without strong signal. Most communication gaps are confusion, not manipulation.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/insight read between the lines of this [message/conversation/request]. What is the surface meaning, what is the likely subtext, and how should I respond to the real concern?
```
