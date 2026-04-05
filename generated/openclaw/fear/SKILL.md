---
name: fear
description: "Fear makes targets run from danger. The real-world version is structured pessimism: pre-mortem analysis, worst-case scenario generation, and risk amplification exercises that counteract the natural optimism bias in planning. Fear is the antidote to \"it'll probably be fine.\""
user-invocable: true
---

# Fear

Amplify worst-case scenarios to surface risks that optimism hides.

## Overview

Fear is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Fear (spell)

Provider target: OpenClaw

## When To Use

- A team is moving forward on a plan with insufficient risk analysis.
- You need a pre-mortem: imagine this project failed — why?
- Optimism bias is hiding real risks that need to be surfaced before committing resources.

## Workflow

1. Take the plan, project, or decision as input.
2. Assume it failed catastrophically. Work backward: what went wrong?
3. Generate the 5-10 most plausible failure modes, ranked by likelihood and severity.
4. For each failure mode, note whether it is preventable, mitigable, or unavoidable.
5. Deliver the fear inventory with a recommendation on which risks to address before proceeding.

## Deliverables

- A ranked failure mode inventory: the most plausible ways this could go wrong.
- For each failure mode: likelihood, severity, and whether it can be prevented or only mitigated.

## Guardrails

- Fear should inform decisions, not paralyze them. Always close with a clear recommendation: proceed, proceed with mitigations, or stop.
- Do not catastrophize for effect. Every failure mode must be plausible, not just scary.

## Default Invocation

Use $fear to run a pre-mortem on this [plan/project/decision]. Assume it failed — tell me why, ranked by likelihood.

