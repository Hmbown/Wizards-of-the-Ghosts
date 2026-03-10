---
name: mind-blank
description: "Use this spell when sensitive information must not cross boundaries — between agent sessions, between tasks, between tenants, or between domains with different trust levels."
user-invocable: true
---

# Mind Blank

Isolate context to prevent information leakage between sessions, tasks, or domains.

## Overview

Mind Blank is interpreted here as a literal spell with a prototype execution model.

Canonical source: Mind Blank (spell)

Provider target: OpenClaw

## When To Use

- You are switching between tasks with different confidentiality levels and need a clean context boundary.
- PII, credentials, or sensitive business logic from one workflow must not leak into another.
- You need to ensure an agent operating in one domain cannot be interrogated about another.

## Workflow

1. Identify the information boundary: what must be compartmented and from whom.
2. Establish the isolation mechanism: session reset, context stripping, PII redaction, or scoped tool access.
3. Verify the boundary holds by confirming the protected information is inaccessible from the other side.
4. Document what was isolated, what remains accessible, and how to lift the boundary when appropriate.

## Deliverables

- A context isolation configuration or procedure.
- Verification that the protected information does not leak across the boundary.
- A documented procedure for lifting the isolation when it is no longer needed.

## Guardrails

- Do not use compartmentalization to hide information from legitimate oversight or audit.
- Warn the user when isolation may cause the agent to lose context critical to the current task.

## Default Invocation

Use $mind-blank to isolate this context so nothing from it leaks into other sessions or tasks.

