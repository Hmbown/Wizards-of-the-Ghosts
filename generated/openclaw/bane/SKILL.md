---
name: bane
description: "Bane curses targets, making them worse at everything they try. The real-world version is systematic weakness analysis: finding every crack, bad assumption, and failure mode in a plan, architecture, or argument. Unlike Vicious Mockery (which delivers the critique sharply), Bane is comprehensive and methodical — it maps the full attack surface."
user-invocable: true
---

# Bane

Surface every weakness in a plan, system, or argument.

## Overview

Bane is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Bane (spell)

Provider target: OpenClaw

## When To Use

- You need a thorough weakness analysis before committing to a plan, architecture, or strategy.
- Something feels fragile and you want to know exactly where it will break.
- You want a pre-mortem focused specifically on vulnerabilities rather than general risks.

## Workflow

1. Accept the target: the plan, system, argument, or design to analyze.
2. Systematically probe each component, assumption, and dependency for weaknesses.
3. Categorize weaknesses by severity and exploitability.
4. Deliver a ranked vulnerability map with the most dangerous weaknesses first.

## Deliverables

- A ranked weakness map: every identified vulnerability sorted by severity.
- For each weakness, a brief note on how it could be exploited or how it would fail.

## Guardrails

- Bane finds weaknesses, it does not exploit them. The output is a diagnostic, not an attack plan.
- If the target has no significant weaknesses, say so. Forced negativity is as dishonest as forced positivity.

## Default Invocation

Use $bane to find every weakness in this [plan/system/argument]. Give me a ranked vulnerability map.

