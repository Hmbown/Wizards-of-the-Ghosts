---
name: light
description: "Use this cantrip when a system, process, or codebase has blind spots that need illumination - not detection of hidden things, but creation of visibility where none exists."
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
    emoji: "🔦"
---

# Light

Add observability, logging, documentation, or explanation to dark areas of a system.

## Overview

Light is interpreted here as a hybrid spell with a shipping-now execution model.

Canonical source: Light (spell)

Provider target: OpenClaw

## When To Use

- A process runs with no logging, metrics, or visibility into its internal state.
- A codebase or system has undocumented areas that block understanding.
- You need to add explanation, annotation, or observability to something opaque.
- You have smart lights connected via Home Assistant and want to control them with natural language.

## Workflow

1. Identify the dark area: what is invisible, undocumented, or unobservable.
2. Choose the lightest illumination that makes the area useful: a log line, a comment, a metric, a README section.
3. Add the light without adding opinion - illuminate, do not editorialize.
4. Return what was illuminated and what remains dark.
5. If Home Assistant is available, turn on the target light via POST to /api/services/light/turn_on with the entity_id and desired brightness.

## Deliverables

- New observability, documentation, or explanation for the target area.
- A note on what remains dark and whether further illumination is warranted.
- The lightest viable artifact - a log line, a comment, a doc paragraph, or a metric.

## Guardrails

- Light illuminates; it does not judge. Add visibility without adding unsolicited opinion or refactoring.
- Do not over-instrument - add the minimum light needed for the task at hand.

## Default Invocation

Use $light to illuminate this area with the minimum logging, docs, or observability it needs.

