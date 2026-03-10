---
name: suggestion
description: "The bard whispers a reasonable-sounding course of action and the target pursues it as if it were their own idea. In practice this is the craft of the nudge: writing the CTA that gets clicked, the notification that gets read, the microcopy that steers behavior without the user feeling steered. Suggestion is not deception — the planted idea must sound reasonable. If it does not survive the sniff test, the spell fails."
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
The bard whispers a reasonable-sounding course of action and the target pursues it as if it were their own idea. In practice this is the craft of the nudge: writing the CTA that gets clicked, the notification that gets read, the microcopy that steers behavior without the user feeling steered. Suggestion is not deception — the planted idea must sound reasonable. If it does not survive the sniff test, the spell fails.
In this grimoire, Suggestion is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Suggestion (spell).
## When To Use

- You need a CTA, notification, tooltip, or nudge that drives a specific user action.
- The goal is behavior change through a single, well-placed prompt — not a wall of argument.
- You want to draft microcopy, onboarding prompts, or opt-in flows that feel natural rather than pushy.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify the single action you want the target to take and why it is genuinely in their interest.
3. Draft the suggestion in the target's own voice, at the moment they are most receptive.
4. Stress-test: would a reasonable person feel manipulated if they learned how this was crafted?
5. If it passes the sniff test, deliver the copy. If not, revise or refuse.
6. Return the suggestion with a note on where and when to deploy it.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- The suggested microcopy, CTA, notification text, or nudge language.
- Placement and timing guidance — where in the flow this should appear.
- A brief manipulation audit: why this nudge is legitimate, or a flag if it is not.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- The suggestion must be something a reasonable person would consider beneficial or at least neutral to themselves.
- Refuse dark patterns: fake urgency, manufactured scarcity, guilt-based CTAs, or opt-out-by-default traps.
- If the nudge would not survive disclosure — if users would be angry to learn how it was designed — do not ship it.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/suggestion draft a single nudge, CTA, or notification that drives this action while passing the 'would they be angry if they knew?' test
```
