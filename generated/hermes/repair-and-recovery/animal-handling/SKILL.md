---
name: animal-handling
description: "Use this skill when the system is not fully broken but behaves like a skittish animal: flaky CI, fragile legacy services, or moody dependencies. It focuses on coaxing, pacing, and stable handling rather than heroic rewrites."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - skill
      - shipping-now
      - metaphorical
      - repair-and-recovery
      - recovery
      - repair
      - triage
      - stabilization
---
# Animal Handling
Calm a temperamental system long enough to get useful work out of it.
## What This Skill Does
Use this skill when the system is not fully broken but behaves like a skittish animal: flaky CI, fragile legacy services, or moody dependencies. It focuses on coaxing, pacing, and stable handling rather than heroic rewrites.
In this grimoire, Animal Handling is treated as a metaphorical skill with a shipping-now delivery profile.
Canonical reference input: Animal Handling (skill).
## When To Use

- A flaky or non-deterministic system keeps reacting badly to normal operations.
- Maintenance work depends on reading triggers, pacing changes, and not spooking the stack.
- You need a handling plan that reduces agitation before deeper repair work.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Observe the failure patterns, triggers, and safe handling rules the system seems to respond to.
3. Choose gentle interventions, sequencing, and retries that reduce instability instead of amplifying it.
4. Return a stability playbook plus the signs that the system is calming down or getting worse.
5. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A system-handling plan tuned to the temperamental behavior.
- A list of triggers, soothing interventions, and escalation signals.
- Criteria for when to continue, pause, or hand off to a deeper fix.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Do not replace diagnosis with superstition; name which patterns are evidence and which are hunches.
- Avoid making the system more dependent on manual soothing without documenting root-cause work.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/animal-handling steady this temperamental system and tell me how to work with it without provoking a failure
```
