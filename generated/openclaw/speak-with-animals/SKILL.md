---
name: speak-with-animals
description: "Speak with Animals interprets non-verbal machine signals the way a skilled naturalist reads calls and tracks. It is for telemetry, dashboards, alert streams, sensor output, and odd machine behavior that clearly means something but does not yet mean anything to a human. The spell turns machine noises into operational sense-making."
user-invocable: true
---

# Speak with Animals

Translate chirps, spikes, and status lights into plain language.

## Overview

Speak with Animals is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Speak with Animals (spell)

Provider target: OpenClaw

## When To Use

- Servers, sensors, IoT devices, or dashboards are emitting signals that need interpretation.
- You have metrics, alerts, or logs but not yet a human explanation of what they imply.
- The system speaks in pulses, anomalies, and patterns rather than plain sentences.

## Workflow

1. Collect the salient signals, anomalies, and recent environmental context around them.
2. Interpret what those signals most likely indicate, separating direct evidence from informed inference.
3. Return a plain-language reading of what the machines are trying to tell you and what to check next.

## Deliverables

- A human-readable interpretation of the observed telemetry.
- A ranked list of likely machine states or emerging issues.
- A next-check recommendation grounded in the observed signals.

## Guardrails

- Do not anthropomorphize sparse telemetry into motives or certainty it cannot support.
- Mark the difference between hard signal, correlation, and intuition.

## Default Invocation

Use $speak-with-animals to translate this telemetry, dashboard noise, or sensor stream into what the machines are actually trying to tell us.

