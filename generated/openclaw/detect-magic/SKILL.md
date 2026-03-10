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

- You suspect there are MCP servers, agents, webhooks, cron jobs, or hidden automations.
- You are entering an unfamiliar codebase and want the weird parts before making changes.
- You need a capability map, not just a file listing.

## Workflow

1. Inventory obvious entrypoints such as docs, scripts, config, package manifests, and agent folders.
2. Trace outward to hidden capability surfaces like MCP configuration, background jobs, webhooks, queues, and device bridges.
3. Call out surprising affordances, dangerous edges, and missing observability.
4. Return a compact map of where automation, model behavior, and side effects actually live.

## Deliverables

- A concise capability inventory.
- A risk list covering hidden side effects or untrusted execution paths.
- A shortlist of follow-up skills or next actions.

## Guardrails

- Do not claim magic where there is only speculation; separate confirmed mechanisms from inference.
- Do not execute risky hooks or automations just to prove they exist.

## Default Invocation

Use $detect-magic to scan this repo for hidden AI tooling, agents, MCP servers, and automation hooks before we change anything.

