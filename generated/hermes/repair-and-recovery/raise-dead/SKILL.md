---
name: raise-dead
description: "In D&D, Raise Dead brings a creature back to life but with penalties: reduced ability scores that recover over time. Unlike Resurrection (full recovery), Raise Dead returns the target in a weakened state. The real-world version is partial recovery: bringing a service back online in degraded mode, recovering a database with known gaps in recent data, or restoring a system from an older backup knowing that some recent state is lost."
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
      - repair-and-recovery
      - recovery
      - repair
      - triage
      - stabilization
---
# Raise Dead
Partially recover a dead system with known limitations and penalties.
## What This Skill Does
In D&D, Raise Dead brings a creature back to life but with penalties: reduced ability scores that recover over time. Unlike Resurrection (full recovery), Raise Dead returns the target in a weakened state. The real-world version is partial recovery: bringing a service back online in degraded mode, recovering a database with known gaps in recent data, or restoring a system from an older backup knowing that some recent state is lost.
In this grimoire, Raise Dead is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Raise Dead (spell).
## When To Use

- A system is dead and full recovery (Resurrection) is too slow or not possible.
- Partial recovery with known limitations is better than staying dead.
- You need something running now even if it is not at full capacity — a degraded-mode restart.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Assess what can be recovered: what state is preserved, what is lost, and what is uncertain.
3. Define the penalties: what limitations will the recovered system have compared to its pre-death state?
4. Execute the partial recovery with clear documentation of what is degraded.
5. Set a timeline for full restoration: when will the penalties be resolved?
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A partial recovery plan: what comes back, what is lost, and what the degraded-mode limitations are.
- A timeline for full restoration from degraded mode to normal operation.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Be honest about the penalties. Partial recovery with undocumented limitations is worse than acknowledged degraded mode.
- Raise Dead is not a substitute for Resurrection — it is a faster option with real tradeoffs. Document those tradeoffs.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/raise-dead bring this [system/service/environment] back in degraded mode. What do we get back, what is lost, and when will it be fully restored?
```
