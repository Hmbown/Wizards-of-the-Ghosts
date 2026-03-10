---
name: clairvoyance
description: "In D&D, Clairvoyance lets you place an invisible sensor in a location you know, seeing or hearing through it. Unlike Scrying (which follows a specific target in real time), Clairvoyance is a point-in-time snapshot of a place. The real-world version is remote system inspection: checking the state of a production environment you cannot SSH into, reading the public-facing state of a competitor's deployment, or gathering the current observable state of a system through its exposed interfaces without modifying it."
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
      - investigation-and-preparation
      - analysis
      - discovery
      - translation
      - preflight
---
# Clairvoyance
Get a snapshot of a remote system or environment you cannot directly access.
## What This Skill Does
In D&D, Clairvoyance lets you place an invisible sensor in a location you know, seeing or hearing through it. Unlike Scrying (which follows a specific target in real time), Clairvoyance is a point-in-time snapshot of a place. The real-world version is remote system inspection: checking the state of a production environment you cannot SSH into, reading the public-facing state of a competitor's deployment, or gathering the current observable state of a system through its exposed interfaces without modifying it.
In this grimoire, Clairvoyance is treated as a hybrid spell with a shipping-now delivery profile.
Canonical reference input: Clairvoyance (spell).
## When To Use

- You need to understand the current state of a system or environment you cannot directly access or modify.
- You want a snapshot assessment — not ongoing monitoring (that is Scrying) but a point-in-time read.
- You need to gather observable information about a remote service, API, or public-facing system.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify the target location or system and what specifically you want to observe.
3. Determine what is observable through legitimate interfaces: public APIs, status pages, DNS records, HTTP headers, documented endpoints.
4. Collect the snapshot: gather all available observable state at this moment.
5. Distinguish facts (what is directly observed) from inferences (what the observations suggest about internal state).
6. Deliver the snapshot with a timestamp and confidence levels for any inferences.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A point-in-time snapshot of the target's observable state.
- Inferences about internal state, clearly marked as inferences with confidence levels.
- Recommendations for what to investigate further based on what the snapshot reveals.

## Pitfalls / Guardrails

- Keep the theatrical framing, but name the concrete mechanism that makes the skill useful right now.
- Clairvoyance observes through legitimate channels only. Do not attempt to access systems beyond their public or authorized interfaces.
- A snapshot is a moment in time, not a guarantee of current state. Always timestamp observations and note that they may already be stale.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check which parts are concrete actions versus framing, so the user can tell what is real now.

## Example Invocation
```text
/clairvoyance get a snapshot of this [system/service/environment]. What can we observe right now through legitimate interfaces?
```
