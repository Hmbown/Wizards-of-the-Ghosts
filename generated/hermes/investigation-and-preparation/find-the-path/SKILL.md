---
name: find-the-path
description: "In D&D, Find the Path reveals the shortest route to a destination, even through mazes and across planes. The real-world version is wayfinding through complexity: navigating a sprawling codebase to find where a change should go, plotting the fastest path through a bureaucratic process, mapping the decision tree to get from current state to desired state, or finding the critical path through a project dependency graph."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - shipping-now
      - metaphorical
      - investigation-and-preparation
      - analysis
      - discovery
      - translation
      - preflight
---
# Find the Path
Find the shortest, safest route to a destination through a complex space.
## What This Skill Does
In D&D, Find the Path reveals the shortest route to a destination, even through mazes and across planes. The real-world version is wayfinding through complexity: navigating a sprawling codebase to find where a change should go, plotting the fastest path through a bureaucratic process, mapping the decision tree to get from current state to desired state, or finding the critical path through a project dependency graph.
In this grimoire, Find the Path is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Find the Path (spell).
## When To Use

- You know where you want to end up but the path through the system, process, or codebase is unclear.
- A project has tangled dependencies and you need to find the critical path or the right order of operations.
- You need to navigate a complex process — regulatory, bureaucratic, or organizational — and want the most direct route.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Define the destination: what does 'done' look like? Be specific.
3. Map the terrain: what are the major obstacles, dependencies, and decision points between here and there?
4. Find the shortest viable path: not the most thorough, not the most cautious — the shortest one that actually works.
5. Identify the single biggest risk on the path and a fallback if it is blocked.
6. Deliver turn-by-turn directions: the ordered sequence of steps from here to the destination.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A step-by-step path from current state to destination, in execution order.
- The critical dependency or risk on the path — the one thing most likely to block progress.
- An alternate route if the primary path is blocked.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- The shortest path is not always the best path. Flag when a faster route has significantly higher risk than a slightly longer one.
- Do not confuse the path with the destination. Find the Path gives directions, not guarantees of arrival.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/find-the-path map the route from where I am now to this [goal/destination/state]. Give me turn-by-turn steps and flag the biggest risk
```
