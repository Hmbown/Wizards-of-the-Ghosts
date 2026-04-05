---
name: animate-objects
description: "This spell transforms inert → reactive. It does NOT create new tools, train models, run one-off fixes, or build physical systems. The key pattern: existing artifact + trigger/watcher + bounded autonomy."
user-invocable: true
---

# Animate Objects

Give agency to passive data by attaching triggers, watchers, and autonomous update logic.

## Overview

Animate Objects is interpreted here as a literal spell with a prototype execution model.

Canonical source: Animate Objects (spell)

Provider target: OpenClaw

## When To Use

- Trigger this spell when a user asks to make an existing static artifact self-updating, reactive, or autonomous. Look for:
- "make it alive", "living document", "self-updating", "auto-refresh"
- References to existing files: CSV, YAML, JSON, README, config, spreadsheet, dashboard, spec, diagram
- Phrases like "pulls from [source]", "watches for changes", "reconciles differences", "flags when stale"
- Desire for ongoing automation attached to a specific existing artifact

## Workflow

1. Identify the inert artifact — name the exact file, dataset, or document. Confirm it exists and is currently static.
2. Define the trigger — what event, schedule, or change should wake it up? (cron, file watch, API poll, git hook, webhook)
3. Specify the autonomous action — what exactly should it do when triggered? Keep scope narrow: update itself, flag discrepancies, regenerate derived output.
4. Set boundaries and kill switch — what must it NOT do? How do you revert it to passive state? Document both before implementing.
5. Implement minimal agency — attach the simplest trigger + action loop that satisfies the request. Prefer existing tooling (watchexec, cron, GitHub Actions, simple scripts) over custom daemons.
6. Verify containment — confirm the artifact only acts within its granted scope and the kill switch works.

## Deliverables

- A previously static artifact with autonomous update or reaction logic attached.
- A clear definition of the object's granted agency and its boundaries.
- A kill switch or revert path that returns the object to its inert state.

## Guardrails

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

## Default Invocation

Use $animate-objects to make this artifact self-updating, with clear agency boundaries and a kill switch.

