---
name: glyph-of-warding
description: "Use this skill when you need a watchful boundary around files, systems, metrics, queues, or workflows."
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
    emoji: "🛡️"
---

# Glyph of Warding

Set monitors, watches, or trigger conditions that alert when a boundary is crossed.

## Overview

Glyph of Warding is interpreted here as a literal spell with a shipping-now execution model.

Canonical source: Glyph of Warding (spell)

Provider target: OpenClaw

## When To Use

- A repo, service, or process needs a tripwire.
- You want notification when a threshold, change, or policy breach occurs.
- A quiet monitor is safer than constant manual checking.
- You want to set up a Home Assistant automation that alerts you when a sensor crosses a threshold — motion detected, door opened, temperature spike.

## Workflow

1. Define the boundary, signal, or threshold to watch.
2. Choose the lightest viable monitoring mechanism.
3. Specify trigger behavior, recipient, and escalation path.
4. Return the alarm definition plus test instructions.
5. If Home Assistant is available, create or update an automation via the HA REST API that watches the specified entity and triggers an alert action (notification, light flash, webhook) when conditions are met.

## Deliverables

- A concrete monitor or alert configuration.
- A test plan for verifying the trigger.
- A note on false-positive and false-negative risk.

## Guardrails

- Avoid noisy alerts with no clear owner or threshold.
- Do not silently create monitors that page humans without explicit intent.

## Default Invocation

Use $glyph-of-warding to define a watch or alert around this workflow and make the trigger conditions explicit.

