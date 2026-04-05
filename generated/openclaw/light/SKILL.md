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

1. Give 3 to 6 steps.
2. the dark area
3. the chosen artifact
4. where it should live
5. how to read it
6. freshness qualification if relevant
7. If relevant, include an exact artifact example:
8. a structured log line

## Deliverables

- List the concrete artifact(s) created.
- Name where operators check them.
- Include what remains dark exactly.
- For logging tasks, say structured log line explicitly.
- For documentation tasks, say runbook note, README paragraph, or stdout line explicitly.
- For status tasks, say status note, heartbeat, or metric explicitly.

## Guardrails

- Keep this section visible and explicit.
- It must say that Light illuminates and does not judge.
- It must say observation must stay within authorized surfaces.
- It must include one sentence about false positive.
- It must include one sentence about false negative.
- It must include one sentence about stale, timestamp, last seen, or privacy.
- It must reject over-instrumentation, unsolicited refactors, covert monitoring, and root-cause overclaiming.
- Useful guardrail patterns:
- A false positive here would be...
- A false negative remains possible if...

## Default Invocation

Use $light to illuminate this area with the minimum logging, docs, or observability it needs.

