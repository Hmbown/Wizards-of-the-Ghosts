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

- You suspect there are MCP servers, agents, webhooks, cron jobs, or hidden automations.
- You are entering an unfamiliar codebase and want the weird parts before making changes.
- You need a capability map, not just a file listing.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Inventory obvious entrypoints such as docs, scripts, config, package manifests, and agent folders.
3. Trace outward to hidden capability surfaces like MCP configuration, background jobs, webhooks, queues, and device bridges.
4. Call out surprising affordances, dangerous edges, and missing observability.
5. Return a compact map of where automation, model behavior, and side effects actually live.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A concise capability inventory.
- A risk list covering hidden side effects or untrusted execution paths.
- A shortlist of follow-up skills or next actions.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Do not claim magic where there is only speculation; separate confirmed mechanisms from inference.
- Do not execute risky hooks or automations just to prove they exist.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/detect-magic scan this repo for hidden AI tooling, agents, MCP servers, and automation hooks before we change anything
```
