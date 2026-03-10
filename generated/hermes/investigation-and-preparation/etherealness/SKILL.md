---
name: etherealness
description: "Etherealness is read-only ghost mode for systems you need to study without disturbing. It maps to shadow environments, dry runs, read replicas, mirrored traffic, and observational tooling that lets you see behavior without becoming part of it. The promise is visibility with minimal touch, not perfect impossibility of side effects."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - prototype
      - metaphorical
      - investigation-and-preparation
      - analysis
      - discovery
      - translation
      - preflight
---
# Etherealness
Walk through the walls of a system without leaving fingerprints.
## What This Skill Does
Etherealness is read-only ghost mode for systems you need to study without disturbing. It maps to shadow environments, dry runs, read replicas, mirrored traffic, and observational tooling that lets you see behavior without becoming part of it. The promise is visibility with minimal touch, not perfect impossibility of side effects.
In this grimoire, Etherealness is treated as a metaphorical spell with a prototype delivery profile.
Canonical reference input: Etherealness (spell).
## When To Use

- You need to observe production-like behavior without writing to the live system.
- A dry run, shadow deployment, or mirrored environment would answer the question more safely than direct experimentation.
- You want to inspect effects first and decide later whether crossing fully into action is justified.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Choose the least invasive observation surface that still answers the question.
3. Define what can be trusted in the ghost view and what may differ from live mutation paths.
4. Return a read-only observation plan plus the gaps that remain invisible until real execution.
5. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A read-only or shadow-observation setup plan.
- A list of findings you can gather safely before acting.
- A caveat list for what ghost mode cannot prove.

## Pitfalls / Guardrails

- Call out the glue, permissions, or missing infrastructure before you imply this is fully operational.
- Do not assume mirrored or dry-run environments perfectly predict live writes, latency, or contention.
- Confirm that the observation path is actually isolated before treating it as consequence-free.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.
- Check that any missing glue code, permissions, or future work is labeled before the skill is treated as ready.

## Example Invocation
```text
/etherealness show me how to inspect this system in read-only ghost mode and tell me what that view can and cannot prove
```
