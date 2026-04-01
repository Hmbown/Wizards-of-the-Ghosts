---
name: light
description: "Use this cantrip when a system, process, or codebase has blind spots that need illumination - not detection of hidden things, but creation of visibility where none exists."
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
# Light
Add observability, logging, documentation, or explanation to dark areas of a system.
## What This Skill Does
Use this cantrip when a system, process, or codebase has blind spots that need illumination - not detection of hidden things, but creation of visibility where none exists.
In this grimoire, Light is treated as a hybrid spell with a shipping-now delivery profile.
Canonical reference input: Light (spell).
## When To Use

- A process runs with no logging, metrics, or visibility into its internal state.
- A codebase or system has undocumented areas that block understanding.
- You need to add explanation, annotation, or observability to something opaque.
- You have smart lights connected via Home Assistant and want to control them with natural language.

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
2. Give 3 to 6 steps.
3. the dark area
4. the chosen artifact
5. where it should live
6. how to read it
7. freshness qualification if relevant
8. If relevant, include an exact artifact example:
9. a structured log line
10. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- List the concrete artifact(s) created.
- Name where operators check them.
- Include what remains dark exactly.
- For logging tasks, say structured log line explicitly.
- For documentation tasks, say runbook note, README paragraph, or stdout line explicitly.
- For status tasks, say status note, heartbeat, or metric explicitly.

## Pitfalls / Guardrails

- Keep the theatrical framing, but name the concrete mechanism that makes the skill useful right now.
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
- Do not rely on a live integration until credentials, target scope, and rollback expectations are verified.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check which parts are concrete actions versus framing, so the user can tell what is real now.
- Check the required environment variables and binaries in the active Hermes runtime before trusting the procedure on a live target.

## Example Invocation
```text
/light illuminate this area with the minimum logging, docs, or observability it needs
```
