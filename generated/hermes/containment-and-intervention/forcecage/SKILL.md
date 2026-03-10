---
name: forcecage
description: "Use this spell when you need to run something you do not fully trust — untrusted code, an experimental agent, a destructive operation — inside a containment boundary that prevents it from affecting the outside."
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
Contain untrusted code, agents, or operations inside an isolated sandbox with no escape.
## What This Skill Does
Use this spell when you need to run something you do not fully trust — untrusted code, an experimental agent, a destructive operation — inside a containment boundary that prevents it from affecting the outside.
In this grimoire, Forcecage is treated as a literal spell with a prototype delivery profile.
Canonical reference input: Forcecage (spell).
## When To Use

- You need to execute untrusted or experimental code in a sandbox before trusting it in production.
- An agent or automation needs to be constrained to a strict scope with no ability to escape.
- You want to test a destructive operation in isolation before running it for real.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Define what needs containment and what the cage must prevent: file writes, network access, process spawning, or data exfiltration.
3. Configure the isolation boundary: sandbox mode, filesystem restrictions, network policies, and execution limits.
4. Execute the contained operation and observe its behavior from outside the cage.
5. Report results, any attempted escapes or boundary violations, and whether the operation is safe to run uncontained.
6. Stop for explicit confirmation before taking a live action that changes access, triggers an alert, or touches a real system boundary.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A configured isolation environment with explicit containment boundaries.
- An execution report from inside the cage, including any attempted boundary violations.
- A safety assessment: is the contained operation safe to run in a less restricted environment.

## Pitfalls / Guardrails

- Call out the glue, permissions, or missing infrastructure before you imply this is fully operational.
- Test the cage before putting something dangerous in it. Verify isolation boundaries actually hold.
- Do not assume containment is perfect — monitor for escape attempts and unexpected behavior.
- Prefer over-constraining to under-constraining. The cost of a cage that is too tight is much lower than a cage that leaks.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the exact live target, confirmation gate, and rollback or recovery path are explicit.
- Check that any missing glue code, permissions, or future work is labeled before the skill is treated as ready.

## Example Invocation
```text
/forcecage run this in a contained sandbox and tell me whether it behaved safely before I trust it outside
```
