---
name: blindness-deafness
description: "In D&D, Blindness/Deafness selectively removes one sense — the target can still act but loses critical awareness. The real-world version is selective channel muting: blocking a process from seeing certain inputs (input filtering, API response redaction), deafening it to specific signals (suppressing webhooks, ignoring certain event streams), or cutting telemetry so a system operates without awareness of a specific data source. Unlike containment (forcecage) which restricts everything, Blindness/Deafness surgically removes one information channel while leaving the rest intact."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - shipping-now
      - literal
      - containment-and-intervention
      - containment
      - intervention
      - disruption
      - safety
---
# Blindness/Deafness
Cut a system's eyes or ears — let it run, but blind to specific inputs or deaf to specific signals.
## What This Skill Does
In D&D, Blindness/Deafness selectively removes one sense — the target can still act but loses critical awareness. The real-world version is selective channel muting: blocking a process from seeing certain inputs (input filtering, API response redaction), deafening it to specific signals (suppressing webhooks, ignoring certain event streams), or cutting telemetry so a system operates without awareness of a specific data source. Unlike containment (forcecage) which restricts everything, Blindness/Deafness surgically removes one information channel while leaving the rest intact.
In this grimoire, Blindness/Deafness is treated as a literal spell with a shipping-now delivery profile.
Canonical reference input: Blindness/Deafness (spell).
## When To Use

- A process should keep running, but one input, signal, or telemetry source needs to be removed from its awareness.
- You need to suppress a specific webhook, event stream, API field, or sensor channel without containing the whole system.
- You want to test or control behavior under selective sensory loss rather than full isolation.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify the exact channel to mute and the decisions the system currently makes from it.
3. Verify the channel is not safety-critical or load-bearing for core correctness.
4. Choose the muting mechanism: input filtering, response redaction, event suppression, or telemetry cutoff.
5. Define restoration triggers, operators, and monitoring so everyone knows the system is partially blind or deaf.
6. Return the channel-muting plan with expected behavioral changes and rollback steps.
7. Stop for explicit confirmation before taking a live action that changes access, triggers an alert, or touches a real system boundary.
8. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A selective channel-muting plan naming exactly what input, signal, or telemetry was removed.
- A dependency note explaining what decisions will proceed without that awareness channel.
- Restoration triggers, rollback steps, and operator-facing documentation.

## Pitfalls / Guardrails

- Treat the live action surface as real operational work, not decorative lore.
- Muting a channel the system needs for safety decisions is dangerous. Verify the blinded input is not load-bearing before cutting it.
- Always document what was muted and set a restoration trigger. A system that forgets it is blind will make confident wrong decisions.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the exact live target, confirmation gate, and rollback or recovery path are explicit.

## Example Invocation
```text
/blindness-deafness selectively blind or deafen this system to one input, signal, or telemetry source while keeping the rest of it running safely
```
