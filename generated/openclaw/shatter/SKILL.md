---
name: shatter
description: "In D&D, Shatter creates a painful ringing noise that is especially devastating to rigid, crystalline structures — it finds the frequency that makes things fall apart. The real-world version is chaos engineering: deliberately introducing failure to discover where systems are brittle. Fuzz testing, load testing, fault injection, game-day exercises. Shatter does not break things out of malice. It breaks things because you would rather find the cracks now, in a controlled setting, than discover them at 3 AM in production. The spell targets rigidity. Flexible systems bend; brittle systems shatter."
user-invocable: true
---

# Shatter

Find the resonant frequency and break it on purpose.

## Overview

Shatter is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Shatter (spell)

Provider target: OpenClaw

## When To Use

- You need to find out where a system, argument, plan, or codebase will break before it breaks on its own.
- A system has never been stress-tested and you do not trust its resilience claims.
- You want to run a chaos experiment, fuzz test, or adversarial review against something you own.

## Workflow

1. Define the blast radius: what you are testing, what is in scope, and what must be protected.
2. Identify the likely resonant frequencies — the stress points, edge cases, and assumptions that have never been tested.
3. Apply controlled force: inject faults, generate adversarial inputs, simulate failures, or stress-test under load.
4. Observe what breaks, what bends, and what holds. Document the failure modes.
5. Deliver a brittleness report with prioritized remediation recommendations.

## Deliverables

- A brittleness report: what broke, at what threshold, and what the failure mode looked like.
- A prioritized list of structural weaknesses with remediation recommendations.
- A resilience scorecard: what held up, what bent gracefully, and what shattered.

## Guardrails

- Only shatter things you own or have explicit authorization to test. Unauthorized stress testing is an attack, not engineering.
- Always define a blast radius before beginning. Chaos engineering without containment is just chaos.
- If something shatters in a way that causes real damage, stop the experiment and switch to incident response.

## Default Invocation

Use $shatter to stress-test a system, plan, or codebase by finding its resonant frequencies — the assumptions, edge cases, and structural weaknesses that would break under real pressure.

