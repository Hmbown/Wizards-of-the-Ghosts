---
name: forcecage
description: "Forcecage creates a pre-tested containment boundary around a subject that has not yet run. It is not about stopping, pausing, or muting something already in motion. The cage is built first, self-tested, then the subject enters. The operator watches from outside and decides whether to release."
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
Forcecage creates a pre-tested containment boundary around a subject that has not yet run. It is not about stopping, pausing, or muting something already in motion. The cage is built first, self-tested, then the subject enters. The operator watches from outside and decides whether to release.
In this grimoire, Forcecage is treated as a literal spell with a prototype delivery profile.
Canonical reference input: Forcecage (spell).
## When To Use

- Trigger this spell when the user asks to contain, cage, sandbox, isolate, or box untrusted/experimental/dangerous code, agents, tools, or operations before they run. Look for:
- Explicit boundary requests: "only inside", "cannot reach", "blocked from", "disposable", "throwaway"
- Subject types: untrusted code, third-party binaries, experimental agents, red-team samples, vendor scripts, refactor tools
- Observation intent: "watch what it does", "log denied actions", "see what it reaches for", "observe from outside"
- Release conditions: "before we trust it", "prove itself first", "step-down after", "authorize descent"

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Define the boundary: List exactly what the subject CAN access (specific files, URLs, namespaces) and what is BLOCKED (network egress, credential stores, process spawning, writes outside a target directory). Default to deny-all.
3. Build and self-test the cage: Create the containment environment (disposable workspace, copied repo, fake namespace, egress-blocked container). Run probes to confirm blocked surfaces actually block. A cage that hasn't been challenged is not trusted.
4. Run the subject inside, observe from outside: Execute the subject within the boundary. Collect audit logs of denied actions, attempted escapes, and resource access patterns. The operator stays outside the cage.
5. Set release condition before descent: Define what must be true for the subject to leave the cage (e.g., zero unauthorized writes, specific test pass, operator sign-off). If the condition is not met, the subject stays cage-only. If met, authorize a single step-down to a less restricted environment.
6. Stop for explicit confirmation before taking a live action that changes access, triggers an alert, or touches a real system boundary.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- Containment boundary spec: allowed surfaces, blocked surfaces, resource limits
- Execution report: attempted violations, denied actions, escape telemetry
- Safety assessment: release condition stated, recommendation (stay caged vs. descend one layer)

## Pitfalls / Guardrails

- Call out the glue, permissions, or missing infrastructure before you imply this is fully operational.
- Do not use for: Freezing/pausing a running workflow → use a halt/interrupt spell
- Do not use for: Muting a specific stream or endpoint → use a filter/silence spell
- Do not use for: Editing CI/config to restrict a job → use a policy/config spell
- Do not use for: Inspecting existing sandbox logs → use an audit/inspect spell
- Do not use for: Disabling a feature temporarily → use a toggle/disable spell
- Do not use for: Forcecage is the only spell that combines: (1) pre-run boundary definition, (2) cage self-test, (3) outside observation with violation logging, and (4) explicit release authorization.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the exact live target, confirmation gate, and rollback or recovery path are explicit.
- Check that any missing glue code, permissions, or future work is labeled before the skill is treated as ready.

## Example Invocation
```text
/forcecage run this inside a tested containment boundary, keep the dangerous parts sealed, and tell me the release condition before anything leaves the cage
```
