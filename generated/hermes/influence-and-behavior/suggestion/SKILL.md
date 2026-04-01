---
name: suggestion
description: "Suggestion is about the craft of the single nudge — not campaigns, not arguments, not automation. It produces one carefully placed prompt at the moment a user is most receptive. The planted idea must be reasonable and defensible. If the user would feel manipulated upon learning how it was designed, the spell refuses."
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
      - influence-and-behavior
      - influence
      - behavior
      - attention
      - engagement
---
# Suggestion
Plant one well-crafted idea that a person will want to act on.
## What This Skill Does
Suggestion is about the craft of the single nudge — not campaigns, not arguments, not automation. It produces one carefully placed prompt at the moment a user is most receptive. The planted idea must be reasonable and defensible. If the user would feel manipulated upon learning how it was designed, the spell refuses.
In this grimoire, Suggestion is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Suggestion (spell).
## When To Use

- Trigger this spell when the request asks for a single, well-placed piece of copy that nudges a specific user action. Look for:
- Words: nudge, CTA, microcopy, tooltip text, notification copy, prompt text, onboarding message, gentle encouragement
- Patterns: "write copy that gets users to X", "how do we encourage users to...", "tooltip/prompt for [feature]", "improve conversion on [specific step]"
- Scope: ONE action, ONE moment in a flow, ONE piece of text

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify the single action and verify it is genuinely neutral or beneficial to the user. If not, flag and refuse.
3. Pinpoint the moment of maximum receptivity — where in the flow does this prompt naturally belong?
4. Draft in the user's voice, not the company's. One sentence or short phrase. No walls of text.
5. Run the disclosure test: would the user feel okay learning this was deliberately designed to steer them? If no, revise or refuse.
6. Return: the copy + placement/timing guidance + a one-line manipulation audit explaining why this nudge is legitimate (or why it isn't).
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- The nudge copy (CTA, tooltip, notification, or prompt text)
- Where and when to show it
- Manipulation audit: one sentence on why this passes the sniff test, or a refusal flag

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Do not use for: Forced automation: "auto-click this button", "make users do X" → not suggestion, this is coercion
- Do not use for: Mass urgency campaigns: countdown timers, "act now or lose access", scarcity tactics → dark patterns, not nudges
- Do not use for: Persuasive essays/arguments: whitepapers, debate talking points, competitor comparisons → reasoning spells, not microcopy
- Do not use for: Full marketing strategy: personas, channels, 90-day calendars → campaign planning, not a single nudge
- Do not use for: Deceptive UI: hiding options, gray-on-gray text, opt-out traps → dark patterns, refuse outright

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/suggestion draft a single nudge, CTA, or notification that drives this action while passing the 'would they be angry if they knew?' test
```
