---
name: shatter
description: "Shatter is proactive, controlled destruction for learning. You are the attacker against your own system. The goal is a brittleness report with remediation priorities."
user-invocable: true
---

# Shatter

Find the resonant frequency and break it on purpose.

## Overview

Shatter is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Shatter (spell)

Provider target: OpenClaw

## When To Use

- Activate Shatter when the user wants to deliberately break, stress, or adversarially test a system they own to discover weaknesses before real failures occur. This is proactive brittleness discovery, not reactive incident response.

## Workflow

1. Define blast radius: What is in scope? What must be protected? What is the rollback plan? Never test without containment boundaries.
2. Identify resonant frequencies: What assumptions have never been tested? Where are the single points of failure? What edge cases are unexercised?
3. Apply controlled force: Inject faults (kill nodes, drop packets, fill disks), generate adversarial inputs, simulate load spikes, or run game-day scenarios. One variable at a time unless testing cascade behavior.
4. Observe failure modes: What broke? What bent gracefully? What held? Document thresholds, error messages, recovery behavior, and unexpected side effects.
5. Deliver brittleness report: Ranked structural weaknesses, resilience scorecard (held/bent/shattered), and prioritized remediation recommendations.

## Deliverables

- A brittleness report: what broke, at what threshold, and what the failure mode looked like.
- A prioritized list of structural weaknesses with remediation recommendations.
- A resilience scorecard: what held up, what bent gracefully, and what shattered.

## Guardrails

- Only test systems you own or have explicit authorization to test
- Always define blast radius and rollback plan before beginning
- If real damage occurs, stop immediately and switch to incident response
- Chaos engineering without containment is just chaos

## Default Invocation

Use $shatter to stress-test a system, plan, or codebase by finding its resonant frequencies — the assumptions, edge cases, and structural weaknesses that would break under real pressure.

