---
name: forcecage
description: "Use this spell when you need to run untrusted code, an experimental agent, or a destructive operation inside a tested containment boundary, observe it from outside, and define the release condition before anything descends into a looser environment."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - prototype
      - literal
      - containment-and-intervention
      - containment
      - intervention
      - disruption
      - safety
---
# Forcecage
Contain untrusted code, agents, or operations inside a tested cage before anything leaves it.
## Sigil

```text
+-------------+
|  x     x    |
|    .-.      |
|   (###)     |
|    `-'      |
|  x     x    |
+-------------+
```

## What This Skill Does
Use this spell when you need to run untrusted code, an experimental agent, or a destructive operation inside a tested containment boundary, observe it from outside, and define the release condition before anything descends into a looser environment.
In this grimoire, Forcecage is treated as a literal spell with a prototype delivery profile.
Canonical reference input: Forcecage (spell).
## When To Use

- You need to execute untrusted or experimental code in a synthetic or replay environment before trusting it anywhere near production.
- An agent, parser, extension, or refactor tool needs explicit filesystem, network, process, and credential boundaries while it is observed from outside the cage.
- A destructive or mutating operation should prove itself in containment before any human authorizes a step-down into a less restricted environment.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Define the containment boundary: allowed files, network policy, process spawning, credential access, and resource limits.
3. Build the cage in a synthetic environment or copied workspace, then self-test the bars before introducing the subject.
4. Run the subject inside the cage and observe it from outside with audit logs, denied-action telemetry, and other operator signals.
5. Set a release condition, authorization check, and descent mechanism before any step-down into a looser environment.
6. Stop for explicit confirmation before taking a live action that changes access, triggers an alert, or touches a real system boundary.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A configured containment boundary with explicit blocked surfaces and operator visibility.
- An execution report that includes attempted boundary violations, denied actions, and other outside-the-cage observations.
- A safety assessment that states the release condition and whether the subject should stay cage-only or descend one layer.

## Pitfalls / Guardrails

- Call out the glue, permissions, or missing infrastructure before you imply this is fully operational.
- Test the cage before use; a sandbox that has not been challenged is not yet trusted.
- Do not assume containment is perfect; keep operator visibility active and treat denied actions as findings.
- Prefer synthetic environments, copied workspaces, and egress-blocked defaults over exposing real production systems, secrets, or customer data.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the exact live target, confirmation gate, and rollback or recovery path are explicit.
- Check that any missing glue code, permissions, or future work is labeled before the skill is treated as ready.

## Example Invocation
```text
/forcecage run this inside a tested containment boundary, keep the dangerous parts sealed, and tell me the release condition before anything leaves the cage
```
