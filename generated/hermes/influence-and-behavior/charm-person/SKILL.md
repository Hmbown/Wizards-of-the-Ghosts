---
name: charm-person
description: "Charm Person is about ONE-TO-ONE interpersonal communication where warmth, honesty, and respect for autonomy are the primary constraints. It is not about persuasion tactics, conversion rates, conflict mediation, public performance, or operational coordination. The spell succeeds when the recipient feels respected even if they say no."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - shipping-now
      - hybrid
      - influence-and-behavior
      - influence
      - behavior
      - attention
      - engagement
---
# Charm Person
Draft warm, trust-building communication that navigates social dynamics with ethical care.
## What This Skill Does
Charm Person is about ONE-TO-ONE interpersonal communication where warmth, honesty, and respect for autonomy are the primary constraints. It is not about persuasion tactics, conversion rates, conflict mediation, public performance, or operational coordination. The spell succeeds when the recipient feels respected even if they say no.
In this grimoire, Charm Person is treated as a hybrid spell with a shipping-now delivery profile.
Canonical reference input: Charm Person (spell).
## When To Use

- Activate this spell when the user asks you to draft a message, note, email, or DM where:
- The primary goal is building or maintaining genuine rapport with a specific recipient
- The situation is socially sensitive and tone matters (rejection, delay, favor, invitation, difficult news)
- The user explicitly wants warmth, compassion, or honesty alongside a request
- The draft should give the recipient a clear, comfortable way to decline or opt out

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Extract context: Identify the recipient, the existing relationship depth, the actual ask, and any boundaries the user has stated.
3. Match tone to reality: Calibrate warmth to the actual relationship. Do not manufacture intimacy. Distant relationships get warm professionalism; close relationships get genuine warmth.
4. Draft with honest structure: State the real reason for the message. Do not obscure the ask. Include a visible, frictionless way to decline or opt out.
5. Check the line: Flag any sentence where persuasion could read as manipulation, guilt, or pressure. Present the tension to the user and let them decide before finalizing.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- The drafted message
- A brief note on tone choices and why they fit the relationship
- Any flagged tension points where transparency and persuasion conflict

## Pitfalls / Guardrails

- Keep the theatrical framing, but name the concrete mechanism that makes the skill useful right now.
- Do NOT use this spell for:
- Do not use for: Conflict de-escalation between third parties in public channels (use conflict-resolution)
- Do not use for: Public speaking, keynote, or presentation copy (use stage-presence)
- Do not use for: Crisp status updates or project coordination messages (use status-report)
- Do not use for: UX copy, opt-in flows, or conversion optimization (use behavioral-design)
- Do not use for: Automated email sequences or campaign routing (use outreach-automation)
- Do not use for: Tool building, chat interfaces, or workflow glue (use tool-builder)
- Do not use for: Manufacture false urgency or lie about deadlines
- Do not use for: Make the recipient feel guilty for setting boundaries
- Do not use for: Fake intimacy or pretend a closer relationship than exists

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check which parts are concrete actions versus framing, so the user can tell what is real now.

## Example Invocation
```text
/charm-person draft this message with warmth and care, and flag anything that crosses from persuasion into manipulation
```
