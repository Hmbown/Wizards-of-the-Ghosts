---
name: dancing-lights
description: "Use this spell for lightweight indicators: status pips, progress markers, heartbeat widgets, and ambient observability that help humans orient quickly. It is not a full dashboard strategy; it is the small visual cue that says where to look next."
user-invocable: true
metadata:
  openclaw:
    requires:
      env:
        - HA_URL
        - HA_TOKEN
      bins:
        - curl
    primaryEnv: HA_TOKEN
    emoji: "💡"
---

# Dancing Lights

Hang small moving signals in the dark so people can tell what the system is doing.

## Overview

Dancing Lights is interpreted here as a hybrid spell with a shipping-now execution model.

Canonical source: Dancing Lights (spell)

Provider target: OpenClaw

## When To Use

- You need a lightweight status or progress display rather than a full observability buildout.
- A small ambient indicator would help people see health, motion, or blockage at a glance.
- The goal is orientation and reassurance, not deep analysis in a heavy dashboard.
- Your Home Assistant setup has Philips Hue or other smart lights that can serve as ambient status indicators.

## Workflow

1. Choose the minimum set of signals that actually matter at a glance.
2. Map those signals to simple visuals, placement, and refresh behavior that stay legible under stress.
3. Return the indicator spec with data sources, stale-state handling, and error states.
4. If Home Assistant is available, use the HA REST API to set light states directly — POST to /api/services/light/turn_on with entity_id, brightness, and rgb_color.

## Deliverables

- A compact status display concept or implementation brief.
- A signal-to-visual mapping for healthy, stale, and failing states.
- Notes on refresh cadence, placement, and what the indicator does not claim.

## Guardrails

- Do not imply precision or freshness the underlying data cannot support.
- Make stale, unknown, or disconnected states visibly different from healthy ones.

## Default Invocation

Use $dancing-lights to design a small status display for this workflow and make the signal states unambiguous.

