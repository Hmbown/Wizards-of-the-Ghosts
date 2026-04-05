---
name: etherealness
description: "Etherealness is observational only. It answers \"what is happening?\" or \"what would happen?\" without changing anything. The system under study continues normally; you add a ghost layer that watches, mirrors, or dry-runs without becoming part of the live mutation path."
user-invocable: true
---

# Etherealness

Walk through the walls of a system without leaving fingerprints.

## Overview

Etherealness is interpreted here as a metaphorical spell with a prototype execution model.

Canonical source: Etherealness (spell)

Provider target: OpenClaw

## When To Use

- You need to observe production-like behavior without writing to the live system.
- A dry run, shadow deployment, or mirrored environment would answer the question more safely than direct experimentation.
- You want to inspect effects first and decide later whether crossing fully into action is justified.

## Workflow

1. Identify the least invasive observation surface that still answers the question. Prefer: existing metrics/logs → read replicas → shadow deployments → mirrored traffic. Escalate invasiveness only when necessary.
2. Define the trust boundary. Explicitly state what the ghost view can prove and what it cannot. Dry runs don't capture live contention. Read replicas may lag. Mirrored traffic at 1% doesn't prove behavior at 100%.
3. Return three deliverables:
4. The observation setup plan (what to deploy, where, how to connect)
5. Findings you can safely gather before acting
6. A caveat list: what ghost mode cannot prove and what requires real execution to validate

## Deliverables

- A read-only or shadow-observation setup plan.
- A list of findings you can gather safely before acting.
- A caveat list for what ghost mode cannot prove.

## Guardrails

- The observation itself must not become the problem. If your ghost layer adds measurable latency, consumes significant resources, or creates a new data liability, you've violated the spell. Design for lightweight passivity.
- Do not use for: Permanent logging/auditing — storing request bodies, headers, auth tokens for compliance. Etherealness is ephemeral; permanent storage is a different concern.
- Do not use for: Active interception/modification — rewriting responses, hotfix proxies, real-time traffic manipulation. Etherealness never modifies.
- Do not use for: External monitoring/scrying — watching competitor websites, market prices, third-party systems you don't control.
- Do not use for: Prediction/forecasting — crystal ball dashboards, failure prediction, trend extrapolation. Etherealness observes what is or what would be, not what will be.
- Do not use for: Concealment/invisibility — hiding services from discovery, making things undetectable. Etherealness is about seeing, not being unseen.
- Do not use for: Human surveillance — watching coworkers' screens, monitoring people. Etherealness is for systems, not people.

## Default Invocation

Use $etherealness to show me how to inspect this system in read-only ghost mode and tell me what that view can and cannot prove.

