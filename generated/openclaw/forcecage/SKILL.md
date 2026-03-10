---
name: forcecage
description: "Use this spell when you need to run something you do not fully trust — untrusted code, an experimental agent, a destructive operation — inside a containment boundary that prevents it from affecting the outside."
user-invocable: true
---

# Forcecage

Contain untrusted code, agents, or operations inside an isolated sandbox with no escape.

## Overview

Forcecage is interpreted here as a literal spell with a prototype execution model.

Canonical source: Forcecage (spell)

Provider target: OpenClaw

## When To Use

- You need to execute untrusted or experimental code in a sandbox before trusting it in production.
- An agent or automation needs to be constrained to a strict scope with no ability to escape.
- You want to test a destructive operation in isolation before running it for real.

## Workflow

1. Define what needs containment and what the cage must prevent: file writes, network access, process spawning, or data exfiltration.
2. Configure the isolation boundary: sandbox mode, filesystem restrictions, network policies, and execution limits.
3. Execute the contained operation and observe its behavior from outside the cage.
4. Report results, any attempted escapes or boundary violations, and whether the operation is safe to run uncontained.

## Deliverables

- A configured isolation environment with explicit containment boundaries.
- An execution report from inside the cage, including any attempted boundary violations.
- A safety assessment: is the contained operation safe to run in a less restricted environment.

## Guardrails

- Test the cage before putting something dangerous in it. Verify isolation boundaries actually hold.
- Do not assume containment is perfect — monitor for escape attempts and unexpected behavior.
- Prefer over-constraining to under-constraining. The cost of a cage that is too tight is much lower than a cage that leaks.

## Default Invocation

Use $forcecage to run this in a contained sandbox and tell me whether it behaved safely before I trust it outside.

