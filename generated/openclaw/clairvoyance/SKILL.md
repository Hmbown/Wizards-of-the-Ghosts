---
name: clairvoyance
description: "In D&D, Clairvoyance lets you place an invisible sensor in a location you know, seeing or hearing through it. Unlike Scrying (which follows a specific target in real time), Clairvoyance is a point-in-time snapshot of a place. The real-world version is remote system inspection: checking the state of a production environment you cannot SSH into, reading the public-facing state of a competitor's deployment, or gathering the current observable state of a system through its exposed interfaces without modifying it."
user-invocable: true
---

# Clairvoyance

Get a snapshot of a remote system or environment you cannot directly access.

## Overview

Clairvoyance is interpreted here as a hybrid spell with a shipping-now execution model.

Canonical source: Clairvoyance (spell)

Provider target: OpenClaw

## When To Use

- You need to understand the current state of a system or environment you cannot directly access or modify.
- You want a snapshot assessment — not ongoing monitoring (that is Scrying) but a point-in-time read.
- You need to gather observable information about a remote service, API, or public-facing system.

## Workflow

1. Identify the target location or system and what specifically you want to observe.
2. Determine what is observable through legitimate interfaces: public APIs, status pages, DNS records, HTTP headers, documented endpoints.
3. Collect the snapshot: gather all available observable state at this moment.
4. Distinguish facts (what is directly observed) from inferences (what the observations suggest about internal state).
5. Deliver the snapshot with a timestamp and confidence levels for any inferences.

## Deliverables

- A point-in-time snapshot of the target's observable state.
- Inferences about internal state, clearly marked as inferences with confidence levels.
- Recommendations for what to investigate further based on what the snapshot reveals.

## Guardrails

- Clairvoyance observes through legitimate channels only. Do not attempt to access systems beyond their public or authorized interfaces.
- A snapshot is a moment in time, not a guarantee of current state. Always timestamp observations and note that they may already be stale.

## Default Invocation

Use $clairvoyance to get a snapshot of this [system/service/environment]. What can we observe right now through legitimate interfaces?

