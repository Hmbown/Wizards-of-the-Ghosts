---
name: raise-dead
description: "In D&D, Raise Dead brings a creature back to life but with penalties: reduced ability scores that recover over time. Unlike Resurrection (full recovery), Raise Dead returns the target in a weakened state. The real-world version is partial recovery: bringing a service back online in degraded mode, recovering a database with known gaps in recent data, or restoring a system from an older backup knowing that some recent state is lost."
user-invocable: true
---

# Raise Dead

Partially recover a dead system with known limitations and penalties.

## Overview

Raise Dead is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Raise Dead (spell)

Provider target: OpenClaw

## When To Use

- A system is dead and full recovery (Resurrection) is too slow or not possible.
- Partial recovery with known limitations is better than staying dead.
- You need something running now even if it is not at full capacity — a degraded-mode restart.

## Workflow

1. Assess what can be recovered: what state is preserved, what is lost, and what is uncertain.
2. Define the penalties: what limitations will the recovered system have compared to its pre-death state?
3. Execute the partial recovery with clear documentation of what is degraded.
4. Set a timeline for full restoration: when will the penalties be resolved?

## Deliverables

- A partial recovery plan: what comes back, what is lost, and what the degraded-mode limitations are.
- A timeline for full restoration from degraded mode to normal operation.

## Guardrails

- Be honest about the penalties. Partial recovery with undocumented limitations is worse than acknowledged degraded mode.
- Raise Dead is not a substitute for Resurrection — it is a faster option with real tradeoffs. Document those tradeoffs.

## Default Invocation

Use $raise-dead to bring this [system/service/environment] back in degraded mode. What do we get back, what is lost, and when will it be fully restored?

