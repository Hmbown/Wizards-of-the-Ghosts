---
name: mirage-arcane
description: "In D&D, Mirage Arcane goes beyond Hallucinatory Terrain — the illusory terrain actually has substance. You can walk on illusory bridges, feel illusory walls. The real-world version is the deep simulation: digital twins, high-fidelity synthetic environments, test harnesses so realistic that systems under test cannot distinguish them from production. Mirage Arcane is the most dangerous illusion because its power is in being indistinguishable from reality. That same power makes it the most useful for stress testing, training, and scenario planning — but it requires the strongest labeling discipline."
---

# Mirage Arcane

Build a simulation so convincing it is functionally indistinguishable from real.

## Overview

Mirage Arcane is interpreted here as a hybrid spell with a prototype execution model.

Canonical source: Mirage Arcane (spell)

Provider target: OpenClaw

## When To Use

- Testing requires a simulation that systems cannot distinguish from production.
- A digital twin or high-fidelity synthetic environment is needed for realistic scenario planning.
- Training scenarios must be immersive enough that participants treat them as real.

## Workflow

1. Define the scope and fidelity requirements for the simulation.
2. Build the simulation with enough depth that systems under test respond as they would to reality.
3. Implement strong boundaries: the simulation must be clearly labeled to operators even if opaque to systems under test.
4. Run the simulation and capture behavioral data.
5. Debrief: what did the simulation reveal that would not have been visible in a lower-fidelity test?

## Deliverables

- A high-fidelity simulation environment that behaves indistinguishably from the real system.
- Operator-level labeling and kill switches to clearly separate simulation from reality.
- Behavioral data from the simulation run.

## Guardrails

- Deep simulations must always have a kill switch and clear operator-level labeling, even if they are opaque to test subjects.
- Never deploy Mirage Arcane without a debrief phase. The risk of confusing simulation with reality scales with fidelity.
- If a simulation generates data that could be mistaken for real data, it must be destroyed or clearly marked after the exercise.

## Default Invocation

Use $mirage-arcane to build a deep simulation or digital twin so realistic that systems or participants treat it as real — with strong labeling and kill switches for operators.

