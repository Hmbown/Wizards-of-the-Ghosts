---
name: teleport
description: "Teleport is FULL-CONTEXT migration, not partial transformation. The defining characteristic is that EVERYTHING must move together and keep working: data, dependencies, auth, traffic routing, background jobs, secrets, and human workflows. The old system must remain recoverable until the new one is proven. This spell IS: Database migrations (RDS→Cloud SQL, self-managed→Atlas), cloud provider moves (on-prem→AWS, Heroku→K8s), environment promotions (staging→prod), account/tenant consolidations, platform migrations (Jenkins→GitHub Actions, SendGrid→SES), identity migrations (AD→Azure AD), cluster upgrades with relocation"
user-invocable: false
disable-model-invocation: true
---

# Teleport

Move an entire world without leaving its people stranded.

## Overview

Teleport is interpreted here as a hybrid spell with a prototype execution model.

Canonical source: Teleport (spell)

Provider target: OpenClaw

## When To Use

- Trigger this spell when the user describes moving an ENTIRE system, service, or environment from one place to another while PRESERVING state and continuity. Look for these patterns:

## Workflow

1. Define boundaries: Identify source world, destination world, and the 5 invariants that must survive: data integrity, authentication, latency/SLA, dependency graph, rollback viability. If any invariant is undefined, stop and ask.
2. Inventory everything: List every stateful surface and dependency that must travel or reconnect: databases, caches, queues, background jobs, secrets, DNS records, storage volumes, CI/CD pipelines, monitoring/alerting, human operator workflows, third-party integrations.
3. Design the safety net FIRST: Before any movement plan, specify: rehearsal strategy (dry run in staging), cutover window (when, how long, who approves), rollback path (exact steps to reverse), validation checks (how to prove arrival succeeded), and failure gates (conditions that abort the migration mid-flight).
4. Sequence the move: Order operations to minimize risk. Typically: replicate data → verify consistency → switch read traffic → switch write traffic → decommission old (after observation period). Return a runbook with explicit timestamps, owners, and go/no-go checkpoints.

## Deliverables

- Always produce: (1) Migration runbook with sequencing, (2) Rollback plan with decision thresholds, (3) Post-arrival validation checklist covering data, traffic, permissions, and dependencies.

## Guardrails

- If the request lacks a rollback path OR a way to validate successful arrival, output ONLY the planning phase. Do not proceed to execution steps. Never claim the move is safe without rehearsals, backups, and integrity verification steps.
- Do not use for: Simple data copies (one table, one file) → use data extraction spells
- Do not use for: Format transformations (OpenAPI 2→3, Python→TypeScript) → use translation spells
- Do not use for: Branch switching or git operations → use version control spells
- Do not use for: Setting up permanent connections (VPN, tunnels) → use infrastructure spells
- Do not use for: Multi-environment deployments from same config → use deployment spells
- Do not use for: Feature toggles or A/B testing → use experimentation spells

## Default Invocation

Use $teleport to plan a full system migration from this source environment to that destination, including cutover, rollback, and post-arrival verification.

