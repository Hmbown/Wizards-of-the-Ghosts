---
name: power-word-stun
description: "In D&D, Power Word Stun locks a creature in place — alive but unable to act. The real-world version is SIGSTOP: a hard freeze that preserves state but halts all activity. Account lockouts, emergency process suspension, administrative holds. Unlike Power Word Kill, the target can be unfrozen. The spell is for situations where something must stop right now but destruction is not warranted — you need the process alive for investigation, for later resumption, or because killing it would cause worse problems than freezing it."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - shipping-now
      - hybrid
      - containment-and-intervention
      - containment
      - intervention
      - disruption
      - safety
---
# Power Word Stun
Freeze a process instantly — hard pause, state preserved, resumable.
## What This Skill Does
In D&D, Power Word Stun locks a creature in place — alive but unable to act. The real-world version is SIGSTOP: a hard freeze that preserves state but halts all activity. Account lockouts, emergency process suspension, administrative holds. Unlike Power Word Kill, the target can be unfrozen. The spell is for situations where something must stop right now but destruction is not warranted — you need the process alive for investigation, for later resumption, or because killing it would cause worse problems than freezing it.
In this grimoire, Power Word Stun is treated as a hybrid spell with a shipping-now delivery profile.
Canonical reference input: Power Word Stun (spell).
## When To Use

- A process or account must be frozen immediately but not destroyed.
- You suspect compromise or abuse and need to preserve state for investigation.
- Emergency suspension is needed while a human decides the next step.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Confirm the target and verify that a hard freeze (not a graceful pause) is actually required.
3. Execute the freeze: SIGSTOP, account lock, administrative hold, or service suspension.
4. Preserve the frozen state for investigation or later resumption.
5. Set a review timer — stunned processes should not stay frozen indefinitely without human review.
6. Document the freeze decision and hand off to the appropriate reviewer.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- Confirmation that the target is frozen and its state is preserved.
- A review timeline: who will assess the frozen target and when.
- Documentation of why the freeze was necessary.

## Pitfalls / Guardrails

- Keep the theatrical framing, but name the concrete mechanism that makes the skill useful right now.
- Frozen processes must have a review deadline. Indefinite freezes without oversight are soft kills.
- If the freeze affects a person's account or access, ensure a human can review and appeal.
- Power Word Stun is temporary by design. If you need permanent termination, use Power Word Kill and own that decision.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check which parts are concrete actions versus framing, so the user can tell what is real now.

## Example Invocation
```text
/power-word-stun immediately freeze a process, account, or system in place — preserving its state for investigation or later resumption
```
