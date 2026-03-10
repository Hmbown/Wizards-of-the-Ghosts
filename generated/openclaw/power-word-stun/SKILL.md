---
name: power-word-stun
description: "In D&D, Power Word Stun locks a creature in place — alive but unable to act. The real-world version is SIGSTOP: a hard freeze that preserves state but halts all activity. Account lockouts, emergency process suspension, administrative holds. Unlike Power Word Kill, the target can be unfrozen. The spell is for situations where something must stop right now but destruction is not warranted — you need the process alive for investigation, for later resumption, or because killing it would cause worse problems than freezing it."
user-invocable: true
---

# Power Word Stun

Freeze a process instantly — hard pause, state preserved, resumable.

## Overview

Power Word Stun is interpreted here as a hybrid spell with a shipping-now execution model.

Canonical source: Power Word Stun (spell)

Provider target: OpenClaw

## When To Use

- A process or account must be frozen immediately but not destroyed.
- You suspect compromise or abuse and need to preserve state for investigation.
- Emergency suspension is needed while a human decides the next step.

## Workflow

1. Confirm the target and verify that a hard freeze (not a graceful pause) is actually required.
2. Execute the freeze: SIGSTOP, account lock, administrative hold, or service suspension.
3. Preserve the frozen state for investigation or later resumption.
4. Set a review timer — stunned processes should not stay frozen indefinitely without human review.
5. Document the freeze decision and hand off to the appropriate reviewer.

## Deliverables

- Confirmation that the target is frozen and its state is preserved.
- A review timeline: who will assess the frozen target and when.
- Documentation of why the freeze was necessary.

## Guardrails

- Frozen processes must have a review deadline. Indefinite freezes without oversight are soft kills.
- If the freeze affects a person's account or access, ensure a human can review and appeal.
- Power Word Stun is temporary by design. If you need permanent termination, use Power Word Kill and own that decision.

## Default Invocation

Use $power-word-stun to immediately freeze a process, account, or system in place — preserving its state for investigation or later resumption.

