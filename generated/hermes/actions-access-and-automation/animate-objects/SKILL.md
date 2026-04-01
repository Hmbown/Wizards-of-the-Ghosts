---
name: animate-objects
description: "This spell transforms inert → reactive. It does NOT create new tools, train models, run one-off fixes, or build physical systems. The key pattern: existing artifact + trigger/watcher + bounded autonomy."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - prototype
      - literal
      - actions-access-and-automation
      - execution
      - automation
      - access
      - actuation
---
# Animate Objects
Give agency to passive data by attaching triggers, watchers, and autonomous update logic.
## What This Skill Does
This spell transforms inert → reactive. It does NOT create new tools, train models, run one-off fixes, or build physical systems. The key pattern: existing artifact + trigger/watcher + bounded autonomy.
In this grimoire, Animate Objects is treated as a literal spell with a prototype delivery profile.
Canonical reference input: Animate Objects (spell).
## When To Use

- Trigger this spell when a user asks to make an existing static artifact self-updating, reactive, or autonomous. Look for:
- "make it alive", "living document", "self-updating", "auto-refresh"
- References to existing files: CSV, YAML, JSON, README, config, spreadsheet, dashboard, spec, diagram
- Phrases like "pulls from [source]", "watches for changes", "reconciles differences", "flags when stale"
- Desire for ongoing automation attached to a specific existing artifact

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify the inert artifact — name the exact file, dataset, or document. Confirm it exists and is currently static.
3. Define the trigger — what event, schedule, or change should wake it up? (cron, file watch, API poll, git hook, webhook)
4. Specify the autonomous action — what exactly should it do when triggered? Keep scope narrow: update itself, flag discrepancies, regenerate derived output.
5. Set boundaries and kill switch — what must it NOT do? How do you revert it to passive state? Document both before implementing.
6. Implement minimal agency — attach the simplest trigger + action loop that satisfies the request. Prefer existing tooling (watchexec, cron, GitHub Actions, simple scripts) over custom daemons.
7. Verify containment — confirm the artifact only acts within its granted scope and the kill switch works.
8. Stop for explicit confirmation before taking a live action that changes access, triggers an alert, or touches a real system boundary.
9. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A previously static artifact with autonomous update or reaction logic attached.
- A clear definition of the object's granted agency and its boundaries.
- A kill switch or revert path that returns the object to its inert state.

## Pitfalls / Guardrails

- Call out the glue, permissions, or missing infrastructure before you imply this is fully operational.
- Scope must be explicit: a self-updating spreadsheet does not start sending emails unless approved
- Always provide a documented kill switch or revert path
- No write access to downstream systems without explicit user approval
- Prefer read-only or self-modifying behavior over cross-system actuation
- Do not use for: Training AI on data — "teach this dataset to understand queries" → ML/NLP spell
- Do not use for: One-off cleanup scripts — "run once to fix stale entries" → simple scripting, no ongoing agency
- Do not use for: Building new tools — "create a CLI tool" → software development, not animating existing artifact
- Do not use for: Physical automation — "robot that moves objects" → hardware/IoT, out of scope
- Do not use for: Syntax repair — "fix broken JSON" → data repair, no autonomy added
- Do not use for: Autonomous agents — "virtual assistant that makes decisions" → agent design, not artifact animation

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the exact live target, confirmation gate, and rollback or recovery path are explicit.
- Check that any missing glue code, permissions, or future work is labeled before the skill is treated as ready.

## Example Invocation
```text
/animate-objects make this artifact self-updating, with clear agency boundaries and a kill switch
```
