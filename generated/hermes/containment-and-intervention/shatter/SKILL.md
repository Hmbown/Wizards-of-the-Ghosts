---
name: shatter
description: "In D&D, Shatter creates a painful ringing noise that is especially devastating to rigid, crystalline structures — it finds the frequency that makes things fall apart. The real-world version is chaos engineering: deliberately introducing failure to discover where systems are brittle. Fuzz testing, load testing, fault injection, game-day exercises. Shatter does not break things out of malice. It breaks things because you would rather find the cracks now, in a controlled setting, than discover them at 3 AM in production. The spell targets rigidity. Flexible systems bend; brittle systems shatter."
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
In D&D, Shatter creates a painful ringing noise that is especially devastating to rigid, crystalline structures — it finds the frequency that makes things fall apart. The real-world version is chaos engineering: deliberately introducing failure to discover where systems are brittle. Fuzz testing, load testing, fault injection, game-day exercises. Shatter does not break things out of malice. It breaks things because you would rather find the cracks now, in a controlled setting, than discover them at 3 AM in production. The spell targets rigidity. Flexible systems bend; brittle systems shatter.
In this grimoire, Shatter is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Shatter (spell).
## When To Use

- You need to find out where a system, argument, plan, or codebase will break before it breaks on its own.
- A system has never been stress-tested and you do not trust its resilience claims.
- You want to run a chaos experiment, fuzz test, or adversarial review against something you own.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Define the blast radius: what you are testing, what is in scope, and what must be protected.
3. Identify the likely resonant frequencies — the stress points, edge cases, and assumptions that have never been tested.
4. Apply controlled force: inject faults, generate adversarial inputs, simulate failures, or stress-test under load.
5. Observe what breaks, what bends, and what holds. Document the failure modes.
6. Deliver a brittleness report with prioritized remediation recommendations.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A brittleness report: what broke, at what threshold, and what the failure mode looked like.
- A prioritized list of structural weaknesses with remediation recommendations.
- A resilience scorecard: what held up, what bent gracefully, and what shattered.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Only shatter things you own or have explicit authorization to test. Unauthorized stress testing is an attack, not engineering.
- Always define a blast radius before beginning. Chaos engineering without containment is just chaos.
- If something shatters in a way that causes real damage, stop the experiment and switch to incident response.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/shatter stress-test a system, plan, or codebase by finding its resonant frequencies — the assumptions, edge cases, and structural weaknesses that would break under real pressure
```
