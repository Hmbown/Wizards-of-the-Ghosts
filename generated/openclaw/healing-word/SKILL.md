---
name: healing-word
description: "In D&D, Healing Word heals at range with a bonus action — fast, remote, and efficient but less powerful than Cure Wounds. The real-world version is the remote quick fix: a one-liner command, a config change pushed through a dashboard, a quick Slack instruction to the person on-call, or an automated rollback trigger. You do not need to be deep in the system to apply this fix."
user-invocable: true
---

# Healing Word

Send a quick fix from a distance without being fully hands-on.

## Overview

Healing Word is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Healing Word (spell)

Provider target: OpenClaw

## When To Use

- A problem can be fixed with a quick remote action: a config change, a restart, a rollback.
- You are advising someone else on what to do and need to give them a precise, executable instruction.
- The fix is simple enough that hands-on debugging is not required — you just need to apply the remedy.

## Workflow

1. Assess whether the problem can be fixed remotely with a simple action.
2. Formulate the fix as a single executable instruction or command.
3. Deliver the instruction with context on what it does and how to verify it worked.
4. If the problem is too complex for a remote fix, escalate to Cure Wounds (hands-on triage).

## Deliverables

- A single executable fix instruction: the command, config change, or action to take.
- Verification steps: how to confirm the fix worked.

## Guardrails

- Healing Word is for simple, well-understood problems. If the diagnosis is uncertain, do not guess — escalate to hands-on triage.
- Remote fixes should be reversible. Do not push irreversible changes without deeper investigation.

## Default Invocation

Use $healing-word to give me a quick, executable fix for this [issue/error/problem] that I can apply without deep investigation.

