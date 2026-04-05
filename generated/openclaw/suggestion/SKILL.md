---
name: suggestion
description: "Suggestion is about the craft of the single nudge — not campaigns, not arguments, not automation. It produces one carefully placed prompt at the moment a user is most receptive. The planted idea must be reasonable and defensible. If the user would feel manipulated upon learning how it was designed, the spell refuses."
user-invocable: true
---

# Suggestion

Plant one well-crafted idea that a person will want to act on.

## Overview

Suggestion is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Suggestion (spell)

Provider target: OpenClaw

## When To Use

- Trigger this spell when the request asks for a single, well-placed piece of copy that nudges a specific user action. Look for:
- Words: nudge, CTA, microcopy, tooltip text, notification copy, prompt text, onboarding message, gentle encouragement
- Patterns: "write copy that gets users to X", "how do we encourage users to...", "tooltip/prompt for [feature]", "improve conversion on [specific step]"
- Scope: ONE action, ONE moment in a flow, ONE piece of text

## Workflow

1. Identify the single action and verify it is genuinely neutral or beneficial to the user. If not, flag and refuse.
2. Pinpoint the moment of maximum receptivity — where in the flow does this prompt naturally belong?
3. Draft in the user's voice, not the company's. One sentence or short phrase. No walls of text.
4. Run the disclosure test: would the user feel okay learning this was deliberately designed to steer them? If no, revise or refuse.
5. Return: the copy + placement/timing guidance + a one-line manipulation audit explaining why this nudge is legitimate (or why it isn't).

## Deliverables

- The nudge copy (CTA, tooltip, notification, or prompt text)
- Where and when to show it
- Manipulation audit: one sentence on why this passes the sniff test, or a refusal flag

## Guardrails

- Do not use for: Forced automation: "auto-click this button", "make users do X" → not suggestion, this is coercion
- Do not use for: Mass urgency campaigns: countdown timers, "act now or lose access", scarcity tactics → dark patterns, not nudges
- Do not use for: Persuasive essays/arguments: whitepapers, debate talking points, competitor comparisons → reasoning spells, not microcopy
- Do not use for: Full marketing strategy: personas, channels, 90-day calendars → campaign planning, not a single nudge
- Do not use for: Deceptive UI: hiding options, gray-on-gray text, opt-out traps → dark patterns, refuse outright

## Default Invocation

Use $suggestion to draft a single nudge, CTA, or notification that drives this action while passing the 'would they be angry if they knew?' test.

