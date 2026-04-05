---
name: mirage-arcane
description: "In D&D, Mirage Arcane goes beyond Hallucinatory Terrain — the illusory terrain actually has substance. You can walk on illusory bridges, feel illusory walls. The real-world version is the deep simulation: digital twins, high-fidelity synthetic environments, test harnesses so realistic that systems under test cannot distinguish them from production. Mirage Arcane is the most dangerous illusion because its power is in being indistinguishable from reality. That same power makes it the most useful for stress testing, training, and scenario planning — but it requires the strongest labeling discipline."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - prototype
      - hybrid
      - simulation-and-staging
      - simulation
      - staging
      - mockup
      - testing
---
# Mirage Arcane
Build a simulation so convincing it is functionally indistinguishable from real.
## What This Skill Does
In D&D, Mirage Arcane goes beyond Hallucinatory Terrain — the illusory terrain actually has substance. You can walk on illusory bridges, feel illusory walls. The real-world version is the deep simulation: digital twins, high-fidelity synthetic environments, test harnesses so realistic that systems under test cannot distinguish them from production. Mirage Arcane is the most dangerous illusion because its power is in being indistinguishable from reality. That same power makes it the most useful for stress testing, training, and scenario planning — but it requires the strongest labeling discipline.
In this grimoire, Mirage Arcane is treated as a hybrid spell with a prototype delivery profile.
Canonical reference input: Mirage Arcane (spell).
## When To Use

- Testing requires a simulation that systems cannot distinguish from production.
- A digital twin or high-fidelity synthetic environment is needed for realistic scenario planning.
- Training scenarios must be immersive enough that participants treat them as real.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Define the scope and fidelity requirements for the simulation.
3. Build the simulation with enough depth that systems under test respond as they would to reality.
4. Implement strong boundaries: the simulation must be clearly labeled to operators even if opaque to systems under test.
5. Run the simulation and capture behavioral data.
6. Debrief: what did the simulation reveal that would not have been visible in a lower-fidelity test?
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A high-fidelity simulation environment that behaves indistinguishably from the real system.
- Operator-level labeling and kill switches to clearly separate simulation from reality.
- Behavioral data from the simulation run.

## Pitfalls / Guardrails

- Call out the glue, permissions, or missing infrastructure before you imply this is fully operational.
- Deep simulations must always have a kill switch and clear operator-level labeling, even if they are opaque to test subjects.
- Never deploy Mirage Arcane without a debrief phase. The risk of confusing simulation with reality scales with fidelity.
- If a simulation generates data that could be mistaken for real data, it must be destroyed or clearly marked after the exercise.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check which parts are concrete actions versus framing, so the user can tell what is real now.
- Check that any missing glue code, permissions, or future work is labeled before the skill is treated as ready.

## Example Invocation
```text
/mirage-arcane build a deep simulation or digital twin so realistic that systems or participants treat it as real — with strong labeling and kill switches for operators
```
