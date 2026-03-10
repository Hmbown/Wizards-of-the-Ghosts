---
name: blindness-deafness
description: "In D&D, Blindness/Deafness selectively removes one sense — the target can still act but loses critical awareness. The real-world version is selective channel muting: blocking a process from seeing certain inputs (input filtering, API response redaction), deafening it to specific signals (suppressing webhooks, ignoring certain event streams), or cutting telemetry so a system operates without awareness of a specific data source. Unlike containment (forcecage) which restricts everything, Blindness/Deafness surgically removes one information channel while leaving the rest intact."
---

# Blindness/Deafness

Cut a system's eyes or ears — let it run, but blind to specific inputs or deaf to specific signals.

## Overview

Blindness/Deafness is interpreted here as a literal spell with a shipping-now execution model.

Canonical source: Blindness/Deafness (spell)

Provider target: OpenClaw

## When To Use

- A process should keep running, but one input, signal, or telemetry source needs to be removed from its awareness.
- You need to suppress a specific webhook, event stream, API field, or sensor channel without containing the whole system.
- You want to test or control behavior under selective sensory loss rather than full isolation.

## Workflow

1. Identify the exact channel to mute and the decisions the system currently makes from it.
2. Verify the channel is not safety-critical or load-bearing for core correctness.
3. Choose the muting mechanism: input filtering, response redaction, event suppression, or telemetry cutoff.
4. Define restoration triggers, operators, and monitoring so everyone knows the system is partially blind or deaf.
5. Return the channel-muting plan with expected behavioral changes and rollback steps.

## Deliverables

- A selective channel-muting plan naming exactly what input, signal, or telemetry was removed.
- A dependency note explaining what decisions will proceed without that awareness channel.
- Restoration triggers, rollback steps, and operator-facing documentation.

## Guardrails

- Muting a channel the system needs for safety decisions is dangerous. Verify the blinded input is not load-bearing before cutting it.
- Always document what was muted and set a restoration trigger. A system that forgets it is blind will make confident wrong decisions.

## Default Invocation

Use $blindness-deafness to selectively blind or deafen this system to one input, signal, or telemetry source while keeping the rest of it running safely.

