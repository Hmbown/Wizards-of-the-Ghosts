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
2. Identify the dark area: what is invisible, undocumented, or unobservable.
3. Choose the lightest illumination that makes the area useful: a log line, a comment, a metric, a README section.
4. Add the light without adding opinion - illuminate, do not editorialize.
5. Return what was illuminated and what remains dark.
6. If Home Assistant is available, turn on the target light via POST to /api/services/light/turn_on with the entity_id and desired brightness.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- New observability, documentation, or explanation for the target area.
- A note on what remains dark and whether further illumination is warranted.
- The lightest viable artifact - a log line, a comment, a doc paragraph, or a metric.

## Pitfalls / Guardrails

- Keep the theatrical framing, but name the concrete mechanism that makes the skill useful right now.
- Light illuminates; it does not judge. Add visibility without adding unsolicited opinion or refactoring.
- Do not over-instrument - add the minimum light needed for the task at hand.
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
