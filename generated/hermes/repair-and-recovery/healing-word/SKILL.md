---
name: healing-word
description: "In D&D, Healing Word heals at range with a bonus action — fast, remote, and efficient but less powerful than Cure Wounds. The real-world version is the remote quick fix: a one-liner command, a config change pushed through a dashboard, a quick Slack instruction to the person on-call, or an automated rollback trigger. You do not need to be deep in the system to apply this fix."
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
# Healing Word
Send a quick fix from a distance without being fully hands-on.
## What This Skill Does
In D&D, Healing Word heals at range with a bonus action — fast, remote, and efficient but less powerful than Cure Wounds. The real-world version is the remote quick fix: a one-liner command, a config change pushed through a dashboard, a quick Slack instruction to the person on-call, or an automated rollback trigger. You do not need to be deep in the system to apply this fix.
In this grimoire, Healing Word is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Healing Word (spell).
## When To Use

- A problem can be fixed with a quick remote action: a config change, a restart, a rollback.
- You are advising someone else on what to do and need to give them a precise, executable instruction.
- The fix is simple enough that hands-on debugging is not required — you just need to apply the remedy.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Assess whether the problem can be fixed remotely with a simple action.
3. Formulate the fix as a single executable instruction or command.
4. Deliver the instruction with context on what it does and how to verify it worked.
5. If the problem is too complex for a remote fix, escalate to Cure Wounds (hands-on triage).
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A single executable fix instruction: the command, config change, or action to take.
- Verification steps: how to confirm the fix worked.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Healing Word is for simple, well-understood problems. If the diagnosis is uncertain, do not guess — escalate to hands-on triage.
- Remote fixes should be reversible. Do not push irreversible changes without deeper investigation.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/healing-word give me a quick, executable fix for this [issue/error/problem] that I can apply without deep investigation
```
