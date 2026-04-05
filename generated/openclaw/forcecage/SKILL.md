---
name: forcecage
description: "Forcecage creates a pre-tested containment boundary around a subject that has not yet run. It is not about stopping, pausing, or muting something already in motion. The cage is built first, self-tested, then the subject enters. The operator watches from outside and decides whether to release."
user-invocable: true
---

# Forcecage

Contain untrusted code, agents, or operations inside a tested cage before anything leaves it.

## Overview

Forcecage is interpreted here as a literal spell with a prototype execution model.

Canonical source: Forcecage (spell)

Provider target: OpenClaw

## When To Use

- Trigger this spell when the user asks to contain, cage, sandbox, isolate, or box untrusted/experimental/dangerous code, agents, tools, or operations before they run. Look for:
- Explicit boundary requests: "only inside", "cannot reach", "blocked from", "disposable", "throwaway"
- Subject types: untrusted code, third-party binaries, experimental agents, red-team samples, vendor scripts, refactor tools
- Observation intent: "watch what it does", "log denied actions", "see what it reaches for", "observe from outside"
- Release conditions: "before we trust it", "prove itself first", "step-down after", "authorize descent"

## Workflow

1. Define the boundary: List exactly what the subject CAN access (specific files, URLs, namespaces) and what is BLOCKED (network egress, credential stores, process spawning, writes outside a target directory). Default to deny-all.
2. Build and self-test the cage: Create the containment environment (disposable workspace, copied repo, fake namespace, egress-blocked container). Run probes to confirm blocked surfaces actually block. A cage that hasn't been challenged is not trusted.
3. Run the subject inside, observe from outside: Execute the subject within the boundary. Collect audit logs of denied actions, attempted escapes, and resource access patterns. The operator stays outside the cage.
4. Set release condition before descent: Define what must be true for the subject to leave the cage (e.g., zero unauthorized writes, specific test pass, operator sign-off). If the condition is not met, the subject stays cage-only. If met, authorize a single step-down to a less restricted environment.

## Deliverables

- Containment boundary spec: allowed surfaces, blocked surfaces, resource limits
- Execution report: attempted violations, denied actions, escape telemetry
- Safety assessment: release condition stated, recommendation (stay caged vs. descend one layer)

## Guardrails

- Do not use for: Freezing/pausing a running workflow → use a halt/interrupt spell
- Do not use for: Muting a specific stream or endpoint → use a filter/silence spell
- Do not use for: Editing CI/config to restrict a job → use a policy/config spell
- Do not use for: Inspecting existing sandbox logs → use an audit/inspect spell
- Do not use for: Disabling a feature temporarily → use a toggle/disable spell
- Do not use for: Forcecage is the only spell that combines: (1) pre-run boundary definition, (2) cage self-test, (3) outside observation with violation logging, and (4) explicit release authorization.

## Default Invocation

Use $forcecage to run this inside a tested containment boundary, keep the dangerous parts sealed, and tell me the release condition before anything leaves the cage.

