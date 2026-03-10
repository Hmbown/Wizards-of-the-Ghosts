---
name: bane
description: "Bane curses targets, making them worse at everything they try. The real-world version is systematic weakness analysis: finding every crack, bad assumption, and failure mode in a plan, architecture, or argument. Unlike Vicious Mockery (which delivers the critique sharply), Bane is comprehensive and methodical — it maps the full attack surface."
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
      - influence-and-behavior
      - influence
      - behavior
      - attention
      - engagement
---
# Bane
Surface every weakness in a plan, system, or argument.
## What This Skill Does
Bane curses targets, making them worse at everything they try. The real-world version is systematic weakness analysis: finding every crack, bad assumption, and failure mode in a plan, architecture, or argument. Unlike Vicious Mockery (which delivers the critique sharply), Bane is comprehensive and methodical — it maps the full attack surface.
In this grimoire, Bane is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Bane (spell).
## When To Use

- You need a thorough weakness analysis before committing to a plan, architecture, or strategy.
- Something feels fragile and you want to know exactly where it will break.
- You want a pre-mortem focused specifically on vulnerabilities rather than general risks.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Accept the target: the plan, system, argument, or design to analyze.
3. Systematically probe each component, assumption, and dependency for weaknesses.
4. Categorize weaknesses by severity and exploitability.
5. Deliver a ranked vulnerability map with the most dangerous weaknesses first.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A ranked weakness map: every identified vulnerability sorted by severity.
- For each weakness, a brief note on how it could be exploited or how it would fail.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Bane finds weaknesses, it does not exploit them. The output is a diagnostic, not an attack plan.
- If the target has no significant weaknesses, say so. Forced negativity is as dishonest as forced positivity.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/bane find every weakness in this [plan/system/argument]. Give me a ranked vulnerability map
```
