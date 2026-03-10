---
name: mass-cure-wounds
description: "In D&D, Mass Cure Wounds heals multiple creatures simultaneously. The real-world version is batch triage: the same bug in 50 repos, the same misconfiguration across a fleet, the same broken migration in every tenant database. When the same problem appears everywhere, fixing them one at a time is Cure Wounds. Fixing them all at once is Mass Cure Wounds."
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
      - repair-and-recovery
      - recovery
      - repair
      - triage
      - stabilization
---
# Mass Cure Wounds
Apply the same fix across many instances of the same problem at once.
## What This Skill Does
In D&D, Mass Cure Wounds heals multiple creatures simultaneously. The real-world version is batch triage: the same bug in 50 repos, the same misconfiguration across a fleet, the same broken migration in every tenant database. When the same problem appears everywhere, fixing them one at a time is Cure Wounds. Fixing them all at once is Mass Cure Wounds.
In this grimoire, Mass Cure Wounds is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Mass Cure Wounds (spell).
## When To Use

- The same problem exists across multiple instances, services, repos, or environments.
- A fix has been verified on one instance and needs to be rolled out to all affected targets.
- A fleet-wide issue needs coordinated remediation.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Confirm the problem is identical across all instances — not just similar, identical.
3. Verify the fix on a single instance first (this is Cure Wounds).
4. Design the batch application strategy: parallel, rolling, or staged.
5. Apply the fix across all instances with monitoring for failures.
6. Report results: how many succeeded, how many failed, and what the failures have in common.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- The batch fix strategy: how the fix will be applied across all instances.
- A results report: successes, failures, and any instances that need individual attention.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Never apply a batch fix that has not been verified on a single instance first. Mass Cure Wounds comes after Cure Wounds, not instead of it.
- Batch operations need rollback plans. If the fix causes a new problem at scale, the blast radius is the entire fleet.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/mass-cure-wounds apply this verified fix across all affected [instances/services/repos]. Design the rollout strategy and monitor for failures
```
