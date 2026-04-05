---
name: detect-magic
description: "Use this skill when you need a fast, structured scan for where the real magic is hiding in a repo, workflow, or system."
user-invocable: true
---

# Detect Magic

Surface hidden AI affordances, agents, automations, and tool hooks before acting.

## Overview

Detect Magic is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Detect Magic (spell)

Provider target: OpenClaw

## When To Use

- You need a preflight scan of a repo or system before making any changes.
- You need to map where automation, model behavior, and side effects actually live.
- You want to inventory hidden capability surfaces: model providers, tool registries, shell bridges, webhooks, schedulers.
- You need to identify surprising affordances, dangerous edges, or missing observability.
- The request involves AI tooling, agents, starter kits, or model behavior scanning.

## Workflow

1. Inventory obvious entrypoints: README, package manifests, setup docs, scripts/, CI/CD folders, env templates.
2. Trace outward to hidden capability surfaces: model providers, tool registries, function-calling schemas, MCP config, plugin loaders, shell bridges.
3. Identify background jobs, cron, schedulers, queues, workers, webhooks, event consumers, notification hooks.
4. Call out surprising affordances, dangerous edges, missing observability, and fan-out points.
5. Return a compact map of confirmed mechanisms, inferred mechanisms, and unknowns needing follow-up.
6. Separate confirmed findings from inference every time — use explicit uncertainty language.

## Deliverables

- A concise capability inventory mapping all discovered execution surfaces.
- A risk list covering hidden side effects or untrusted execution paths.
- A shortlist of follow-up skills or next actions (e.g. $identify, $zone-of-truth, $glyph-of-warding).

## Guardrails

- Do not claim magic where there is only speculation — separate proof from suspicion.
- Do not execute risky hooks, automations, deploys, rollbacks, webhooks, or billing mutations just to prove they exist.
- Treat dependency or environment artifacts carefully — a binary suggests tooling is installed but does not prove the repo ships that capability.
- Use explicit uncertainty language: Confirmed, Inferred not confirmed, Unknown from repo evidence.
- Do not drift into generic security-review prose — sound like a structured capability-scan ritual.

## Default Invocation

Use $detect-magic to scan this repo for hidden AI tooling, agents, MCP servers, and automation hooks before we change anything.

