---
name: mass-cure-wounds
description: "In D&D, Mass Cure Wounds heals multiple creatures simultaneously. The real-world version is batch triage: the same bug in 50 repos, the same misconfiguration across a fleet, the same broken migration in every tenant database. When the same problem appears everywhere, fixing them one at a time is Cure Wounds. Fixing them all at once is Mass Cure Wounds."
user-invocable: true
---

# Mass Cure Wounds

Apply the same fix across many instances of the same problem at once.

## Overview

Mass Cure Wounds is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Mass Cure Wounds (spell)

Provider target: OpenClaw

## When To Use

- The same problem exists across multiple instances, services, repos, or environments.
- A fix has been verified on one instance and needs to be rolled out to all affected targets.
- A fleet-wide issue needs coordinated remediation.

## Workflow

1. Confirm the problem is identical across all instances — not just similar, identical.
2. Verify the fix on a single instance first (this is Cure Wounds).
3. Design the batch application strategy: parallel, rolling, or staged.
4. Apply the fix across all instances with monitoring for failures.
5. Report results: how many succeeded, how many failed, and what the failures have in common.

## Deliverables

- The batch fix strategy: how the fix will be applied across all instances.
- A results report: successes, failures, and any instances that need individual attention.

## Guardrails

- Never apply a batch fix that has not been verified on a single instance first. Mass Cure Wounds comes after Cure Wounds, not instead of it.
- Batch operations need rollback plans. If the fix causes a new problem at scale, the blast radius is the entire fleet.

## Default Invocation

Use $mass-cure-wounds to apply this verified fix across all affected [instances/services/repos]. Design the rollout strategy and monitor for failures.

