---
name: teleport
description: "Teleport is FULL-CONTEXT migration, not partial transformation. The defining characteristic is that EVERYTHING must move together and keep working: data, dependencies, auth, traffic routing, background jobs, secrets, and human workflows. The old system must remain recoverable until the new one is proven. This spell IS: Database migrations (RDS→Cloud SQL, self-managed→Atlas), cloud provider moves (on-prem→AWS, Heroku→K8s), environment promotions (staging→prod), account/tenant consolidations, platform migrations (Jenkins→GitHub Actions, SendGrid→SES), identity migrations (AD→Azure AD), cluster upgrades with relocation"
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - prototype
      - hybrid
      - actions-access-and-automation
      - execution
      - automation
      - access
      - actuation
---
# Teleport
Move an entire world without leaving its people stranded.
## What This Skill Does
Teleport is FULL-CONTEXT migration, not partial transformation. The defining characteristic is that EVERYTHING must move together and keep working: data, dependencies, auth, traffic routing, background jobs, secrets, and human workflows. The old system must remain recoverable until the new one is proven. This spell IS: Database migrations (RDS→Cloud SQL, self-managed→Atlas), cloud provider moves (on-prem→AWS, Heroku→K8s), environment promotions (staging→prod), account/tenant consolidations, platform migrations (Jenkins→GitHub Actions, SendGrid→SES), identity migrations (AD→Azure AD), cluster upgrades with relocation
In this grimoire, Teleport is treated as a hybrid spell with a prototype delivery profile.
Canonical reference input: Teleport (spell).
## When To Use

- Trigger this spell when the user describes moving an ENTIRE system, service, or environment from one place to another while PRESERVING state and continuity. Look for these patterns:

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Define boundaries: Identify source world, destination world, and the 5 invariants that must survive: data integrity, authentication, latency/SLA, dependency graph, rollback viability. If any invariant is undefined, stop and ask.
3. Inventory everything: List every stateful surface and dependency that must travel or reconnect: databases, caches, queues, background jobs, secrets, DNS records, storage volumes, CI/CD pipelines, monitoring/alerting, human operator workflows, third-party integrations.
4. Design the safety net FIRST: Before any movement plan, specify: rehearsal strategy (dry run in staging), cutover window (when, how long, who approves), rollback path (exact steps to reverse), validation checks (how to prove arrival succeeded), and failure gates (conditions that abort the migration mid-flight).
5. Sequence the move: Order operations to minimize risk. Typically: replicate data → verify consistency → switch read traffic → switch write traffic → decommission old (after observation period). Return a runbook with explicit timestamps, owners, and go/no-go checkpoints.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- Always produce: (1) Migration runbook with sequencing, (2) Rollback plan with decision thresholds, (3) Post-arrival validation checklist covering data, traffic, permissions, and dependencies.

## Pitfalls / Guardrails

- Call out the glue, permissions, or missing infrastructure before you imply this is fully operational.
- If the request lacks a rollback path OR a way to validate successful arrival, output ONLY the planning phase. Do not proceed to execution steps. Never claim the move is safe without rehearsals, backups, and integrity verification steps.
- Do not use for: Simple data copies (one table, one file) → use data extraction spells
- Do not use for: Format transformations (OpenAPI 2→3, Python→TypeScript) → use translation spells
- Do not use for: Branch switching or git operations → use version control spells
- Do not use for: Setting up permanent connections (VPN, tunnels) → use infrastructure spells
- Do not use for: Multi-environment deployments from same config → use deployment spells
- Do not use for: Feature toggles or A/B testing → use experimentation spells

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check which parts are concrete actions versus framing, so the user can tell what is real now.
- Check that any missing glue code, permissions, or future work is labeled before the skill is treated as ready.

## Example Invocation
```text
/teleport plan a full system migration from this source environment to that destination, including cutover, rollback, and post-arrival verification
```
