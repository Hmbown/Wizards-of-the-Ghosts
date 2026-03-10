---
name: dancing-lights
description: "Use this spell for lightweight indicators: status pips, progress markers, heartbeat widgets, and ambient observability that help humans orient quickly. It is not a full dashboard strategy; it is the small visual cue that says where to look next."
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
      - monitoring-and-protection
      - observability
      - monitoring
      - guardrails
      - privacy
      - integration
      - home-assistant
---
# Dancing Lights
Hang small moving signals in the dark so people can tell what the system is doing.
## What This Skill Does
Use this spell for lightweight indicators: status pips, progress markers, heartbeat widgets, and ambient observability that help humans orient quickly. It is not a full dashboard strategy; it is the small visual cue that says where to look next.
In this grimoire, Dancing Lights is treated as a hybrid spell with a shipping-now delivery profile.
Canonical reference input: Dancing Lights (spell).
## When To Use

- You need a lightweight status or progress display rather than a full observability buildout.
- A small ambient indicator would help people see health, motion, or blockage at a glance.
- The goal is orientation and reassurance, not deep analysis in a heavy dashboard.
- Your Home Assistant setup has Philips Hue or other smart lights that can serve as ambient status indicators.

## Prerequisites

- Environment variables available to Hermes: `HA_URL`, `HA_TOKEN`.
- Primary credential or token: `HA_TOKEN`.
- Binaries on PATH: `curl`.

## Setup

1. Confirm the required environment variables are available inside the active Hermes runtime, not just in a shell profile.
2. Verify the required binaries resolve on PATH before you rely on them in a procedure.
3. Choose a non-production or low-risk target first if the skill can page, unlock, alert, or touch a live integration.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Choose the minimum set of signals that actually matter at a glance.
3. Map those signals to simple visuals, placement, and refresh behavior that stay legible under stress.
4. Return the indicator spec with data sources, stale-state handling, and error states.
5. If Home Assistant is available, use the HA REST API to set light states directly — POST to /api/services/light/turn_on with entity_id, brightness, and rgb_color.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A compact status display concept or implementation brief.
- A signal-to-visual mapping for healthy, stale, and failing states.
- Notes on refresh cadence, placement, and what the indicator does not claim.

## Pitfalls / Guardrails

- Keep the theatrical framing, but name the concrete mechanism that makes the skill useful right now.
- Do not imply precision or freshness the underlying data cannot support.
- Make stale, unknown, or disconnected states visibly different from healthy ones.
- Do not rely on a live integration until credentials, target scope, and rollback expectations are verified.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check which parts are concrete actions versus framing, so the user can tell what is real now.
- Check the required environment variables and binaries in the active Hermes runtime before trusting the procedure on a live target.

## Example Invocation
```text
/dancing-lights design a small status display for this workflow and make the signal states unambiguous
```
