---
name: animate-objects
description: "Use this spell when a static file, dataset, or configuration should become a living artifact that reacts to changes, heals itself, or updates autonomously."
user-invocable: true
---

# Animate Objects

Give agency to passive data by attaching triggers, watchers, and autonomous update logic.

## Overview

Animate Objects is interpreted here as a literal spell with a prototype execution model.

Canonical source: Animate Objects (spell)

Provider target: OpenClaw

## When To Use

- A spreadsheet, dashboard, or config file should stay current without manual intervention.
- You want a document or dataset to react when its inputs change.
- A passive artifact would be more useful if it could monitor its own health and act on drift.

## Workflow

1. Identify the inert object and the behavior it should gain.
2. Attach the minimal trigger, watcher, or update loop that gives it the desired agency.
3. Define the object's scope of autonomous action and its kill switch.
4. Test the animated behavior and confirm the object stays within its granted agency.

## Deliverables

- A previously static artifact with autonomous update or reaction logic attached.
- A clear definition of the object's granted agency and its boundaries.
- A kill switch or revert path that returns the object to its inert state.

## Guardrails

- Animated objects must have explicit scope limits - a self-updating spreadsheet should not start sending emails.
- Always provide a kill switch that returns the object to a passive state.
- Do not grant write access to downstream systems the user has not explicitly approved.

## Default Invocation

Use $animate-objects to make this artifact self-updating, with clear agency boundaries and a kill switch.

