---
name: forcecage
description: "Use this spell when you need to run untrusted code, an experimental agent, or a destructive operation inside a tested containment boundary, observe it from outside, and define the release condition before anything descends into a looser environment."
user-invocable: true
---

# Forcecage

Contain untrusted code, agents, or operations inside a tested cage before anything leaves it.

## Overview

Forcecage is interpreted here as a literal spell with a prototype execution model.

Canonical source: Forcecage (spell)

Provider target: OpenClaw

## When To Use

- You need to execute untrusted or experimental code in a synthetic or replay environment before trusting it anywhere near production.
- An agent, parser, extension, or refactor tool needs explicit filesystem, network, process, and credential boundaries while it is observed from outside the cage.
- A destructive or mutating operation should prove itself in containment before any human authorizes a step-down into a less restricted environment.

## Workflow

1. Define the containment boundary: allowed files, network policy, process spawning, credential access, and resource limits.
2. Build the cage in a synthetic environment or copied workspace, then self-test the bars before introducing the subject.
3. Run the subject inside the cage and observe it from outside with audit logs, denied-action telemetry, and other operator signals.
4. Set a release condition, authorization check, and descent mechanism before any step-down into a looser environment.

## Deliverables

- A configured containment boundary with explicit blocked surfaces and operator visibility.
- An execution report that includes attempted boundary violations, denied actions, and other outside-the-cage observations.
- A safety assessment that states the release condition and whether the subject should stay cage-only or descend one layer.

## Guardrails

- Test the cage before use; a sandbox that has not been challenged is not yet trusted.
- Do not assume containment is perfect; keep operator visibility active and treat denied actions as findings.
- Prefer synthetic environments, copied workspaces, and egress-blocked defaults over exposing real production systems, secrets, or customer data.

## Default Invocation

Use $forcecage to run this inside a tested containment boundary, keep the dangerous parts sealed, and tell me the release condition before anything leaves the cage.

