---
name: greater-restoration
description: "In D&D, Greater Restoration ends charm, petrification, curses, ability score reductions, and hit point maximum reductions — the serious, long-term ailments. The real-world version is deep system recovery: unfucking a database that has been gradually corrupted, restoring a codebase that has accumulated technical debt to the point of dysfunction, or recovering from a long-running misconfiguration that has silently degraded performance."
user-invocable: true
---

# Greater Restoration

Undo deep corruption and restore a system degraded by accumulated damage.

## Overview

Greater Restoration is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Greater Restoration (spell)

Provider target: OpenClaw

## When To Use

- A system has been gradually degraded by accumulated problems and no single fix will restore it.
- Corruption, misconfiguration, or technical debt has built up to the point where triage is insufficient.
- The system needs a comprehensive restoration plan, not a hotfix.

## Workflow

1. Assess the scope of degradation: how many subsystems are affected, and how deep does the damage go?
2. Identify the root causes: what introduced the corruption and is it still active?
3. Design the restoration plan: the ordered sequence of fixes, migrations, or rebuilds needed.
4. Execute restoration with verification at each stage — do not batch this without checkpoints.
5. Deliver the restored system with a post-restoration health check.

## Deliverables

- A restoration plan: ordered steps to undo accumulated damage.
- Root-cause identification: what caused the degradation and how to prevent recurrence.
- A post-restoration health check confirming the system is back to full function.

## Guardrails

- Greater Restoration is expensive and disruptive. Verify that Lesser Restoration or Cure Wounds cannot solve the problem first.
- Do not restore to a previous known-good state without checking whether that state had its own problems. Rolling back is not the same as restoring.

## Default Invocation

Use $greater-restoration to assess this [system/codebase/database] for accumulated damage and design a comprehensive restoration plan.

