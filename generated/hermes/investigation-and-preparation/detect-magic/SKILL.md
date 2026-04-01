---
name: detect-magic
description: "Use this skill when you need a fast, structured scan for where the real magic is hiding in a repo, workflow, or system."
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
# Detect Magic
Surface hidden AI affordances, agents, automations, and tool hooks before acting.
## What This Skill Does
Use this skill when you need a fast, structured scan for where the real magic is hiding in a repo, workflow, or system.
In this grimoire, Detect Magic is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Detect Magic (spell).
## When To Use

- You need a preflight scan of a repo or system before making any changes.
- You need to map where automation, model behavior, and side effects actually live.
- You want to inventory hidden capability surfaces: model providers, tool registries, shell bridges, webhooks, schedulers.
- You need to identify surprising affordances, dangerous edges, or missing observability.
- The request involves AI tooling, agents, starter kits, or model behavior scanning.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Inventory obvious entrypoints: README, package manifests, setup docs, scripts/, CI/CD folders, env templates.
3. Trace outward to hidden capability surfaces: model providers, tool registries, function-calling schemas, MCP config, plugin loaders, shell bridges.
4. Identify background jobs, cron, schedulers, queues, workers, webhooks, event consumers, notification hooks.
5. Call out surprising affordances, dangerous edges, missing observability, and fan-out points.
6. Return a compact map of confirmed mechanisms, inferred mechanisms, and unknowns needing follow-up.
7. Separate confirmed findings from inference every time — use explicit uncertainty language.
8. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A concise capability inventory mapping all discovered execution surfaces.
- A risk list covering hidden side effects or untrusted execution paths.
- A shortlist of follow-up skills or next actions (e.g. $identify, $zone-of-truth, $glyph-of-warding).

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Do not claim magic where there is only speculation — separate proof from suspicion.
- Do not execute risky hooks, automations, deploys, rollbacks, webhooks, or billing mutations just to prove they exist.
- Treat dependency or environment artifacts carefully — a binary suggests tooling is installed but does not prove the repo ships that capability.
- Use explicit uncertainty language: Confirmed, Inferred not confirmed, Unknown from repo evidence.
- Do not drift into generic security-review prose — sound like a structured capability-scan ritual.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/detect-magic scan this repo for hidden AI tooling, agents, MCP servers, and automation hooks before we change anything
```
