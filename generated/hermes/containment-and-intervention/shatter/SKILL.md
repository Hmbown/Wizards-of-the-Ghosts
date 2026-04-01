---
name: shatter
description: "Shatter is proactive, controlled destruction for learning. You are the attacker against your own system. The goal is a brittleness report with remediation priorities."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - shipping-now
      - metaphorical
      - containment-and-intervention
      - containment
      - intervention
      - disruption
      - safety
---
# Shatter
Find the resonant frequency and break it on purpose.
## What This Skill Does
Shatter is proactive, controlled destruction for learning. You are the attacker against your own system. The goal is a brittleness report with remediation priorities.
In this grimoire, Shatter is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Shatter (spell).
## When To Use

- Activate Shatter when the user wants to deliberately break, stress, or adversarially test a system they own to discover weaknesses before real failures occur. This is proactive brittleness discovery, not reactive incident response.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Define blast radius: What is in scope? What must be protected? What is the rollback plan? Never test without containment boundaries.
3. Identify resonant frequencies: What assumptions have never been tested? Where are the single points of failure? What edge cases are unexercised?
4. Apply controlled force: Inject faults (kill nodes, drop packets, fill disks), generate adversarial inputs, simulate load spikes, or run game-day scenarios. One variable at a time unless testing cascade behavior.
5. Observe failure modes: What broke? What bent gracefully? What held? Document thresholds, error messages, recovery behavior, and unexpected side effects.
6. Deliver brittleness report: Ranked structural weaknesses, resilience scorecard (held/bent/shattered), and prioritized remediation recommendations.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A brittleness report: what broke, at what threshold, and what the failure mode looked like.
- A prioritized list of structural weaknesses with remediation recommendations.
- A resilience scorecard: what held up, what bent gracefully, and what shattered.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Only test systems you own or have explicit authorization to test
- Always define blast radius and rollback plan before beginning
- If real damage occurs, stop immediately and switch to incident response
- Chaos engineering without containment is just chaos

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/shatter stress-test a system, plan, or codebase by finding its resonant frequencies — the assumptions, edge cases, and structural weaknesses that would break under real pressure
```
