---
name: find-the-path
description: "In D&D, Find the Path reveals the shortest route to a destination, even through mazes and across planes. The real-world version is wayfinding through complexity: navigating a sprawling codebase to find where a change should go, plotting the fastest path through a bureaucratic process, mapping the decision tree to get from current state to desired state, or finding the critical path through a project dependency graph."
user-invocable: true
---

# Find the Path

Find the shortest, safest route to a destination through a complex space.

## Overview

Find the Path is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Find the Path (spell)

Provider target: OpenClaw

## When To Use

- You know where you want to end up but the path through the system, process, or codebase is unclear.
- A project has tangled dependencies and you need to find the critical path or the right order of operations.
- You need to navigate a complex process — regulatory, bureaucratic, or organizational — and want the most direct route.

## Workflow

1. Define the destination: what does 'done' look like? Be specific.
2. Map the terrain: what are the major obstacles, dependencies, and decision points between here and there?
3. Find the shortest viable path: not the most thorough, not the most cautious — the shortest one that actually works.
4. Identify the single biggest risk on the path and a fallback if it is blocked.
5. Deliver turn-by-turn directions: the ordered sequence of steps from here to the destination.

## Deliverables

- A step-by-step path from current state to destination, in execution order.
- The critical dependency or risk on the path — the one thing most likely to block progress.
- An alternate route if the primary path is blocked.

## Guardrails

- The shortest path is not always the best path. Flag when a faster route has significantly higher risk than a slightly longer one.
- Do not confuse the path with the destination. Find the Path gives directions, not guarantees of arrival.

## Default Invocation

Use $find-the-path to map the route from where I am now to this [goal/destination/state]. Give me turn-by-turn steps and flag the biggest risk.

