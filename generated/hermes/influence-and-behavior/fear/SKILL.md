---
name: fear
description: "Fear makes targets run from danger. The real-world version is structured pessimism: pre-mortem analysis, worst-case scenario generation, and risk amplification exercises that counteract the natural optimism bias in planning. Fear is the antidote to \"it'll probably be fine.\""
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
# Fear
Amplify worst-case scenarios to surface risks that optimism hides.
## What This Skill Does
Fear makes targets run from danger. The real-world version is structured pessimism: pre-mortem analysis, worst-case scenario generation, and risk amplification exercises that counteract the natural optimism bias in planning. Fear is the antidote to "it'll probably be fine."
In this grimoire, Fear is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Fear (spell).
## When To Use

- A team is moving forward on a plan with insufficient risk analysis.
- You need a pre-mortem: imagine this project failed — why?
- Optimism bias is hiding real risks that need to be surfaced before committing resources.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Take the plan, project, or decision as input.
3. Assume it failed catastrophically. Work backward: what went wrong?
4. Generate the 5-10 most plausible failure modes, ranked by likelihood and severity.
5. For each failure mode, note whether it is preventable, mitigable, or unavoidable.
6. Deliver the fear inventory with a recommendation on which risks to address before proceeding.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A ranked failure mode inventory: the most plausible ways this could go wrong.
- For each failure mode: likelihood, severity, and whether it can be prevented or only mitigated.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Fear should inform decisions, not paralyze them. Always close with a clear recommendation: proceed, proceed with mitigations, or stop.
- Do not catastrophize for effect. Every failure mode must be plausible, not just scary.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/fear run a pre-mortem on this [plan/project/decision]. Assume it failed — tell me why, ranked by likelihood
```
