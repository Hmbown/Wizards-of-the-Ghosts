---
name: mind-blank
description: "Use this spell when sensitive information must not cross boundaries — between agent sessions, between tasks, between tenants, or between domains with different trust levels."
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
      - monitoring-and-protection
      - observability
      - monitoring
      - guardrails
      - privacy
---
# Mind Blank
Isolate context to prevent information leakage between sessions, tasks, or domains.
## What This Skill Does
Use this spell when sensitive information must not cross boundaries — between agent sessions, between tasks, between tenants, or between domains with different trust levels.
In this grimoire, Mind Blank is treated as a literal spell with a prototype delivery profile.
Canonical reference input: Mind Blank (spell).
## When To Use

- You are switching between tasks with different confidentiality levels and need a clean context boundary.
- PII, credentials, or sensitive business logic from one workflow must not leak into another.
- You need to ensure an agent operating in one domain cannot be interrogated about another.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify the information boundary: what must be compartmented and from whom.
3. Establish the isolation mechanism: session reset, context stripping, PII redaction, or scoped tool access.
4. Verify the boundary holds by confirming the protected information is inaccessible from the other side.
5. Document what was isolated, what remains accessible, and how to lift the boundary when appropriate.
6. Stop for explicit confirmation before taking a live action that changes access, triggers an alert, or touches a real system boundary.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A context isolation configuration or procedure.
- Verification that the protected information does not leak across the boundary.
- A documented procedure for lifting the isolation when it is no longer needed.

## Pitfalls / Guardrails

- Call out the glue, permissions, or missing infrastructure before you imply this is fully operational.
- Do not use compartmentalization to hide information from legitimate oversight or audit.
- Warn the user when isolation may cause the agent to lose context critical to the current task.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the exact live target, confirmation gate, and rollback or recovery path are explicit.
- Check that any missing glue code, permissions, or future work is labeled before the skill is treated as ready.

## Example Invocation
```text
/mind-blank isolate this context so nothing from it leaks into other sessions or tasks
```
