---
name: etherealness
description: "Etherealness is read-only ghost mode for systems you need to study without disturbing. It maps to shadow environments, dry runs, read replicas, mirrored traffic, and observational tooling that lets you see behavior without becoming part of it. The promise is visibility with minimal touch, not perfect impossibility of side effects."
user-invocable: true
---

# Etherealness

Walk through the walls of a system without leaving fingerprints.

## Overview

Etherealness is interpreted here as a metaphorical spell with a prototype execution model.

Canonical source: Etherealness (spell)

Provider target: OpenClaw

## When To Use

- You need to observe production-like behavior without writing to the live system.
- A dry run, shadow deployment, or mirrored environment would answer the question more safely than direct experimentation.
- You want to inspect effects first and decide later whether crossing fully into action is justified.

## Workflow

1. Choose the least invasive observation surface that still answers the question.
2. Define what can be trusted in the ghost view and what may differ from live mutation paths.
3. Return a read-only observation plan plus the gaps that remain invisible until real execution.

## Deliverables

- A read-only or shadow-observation setup plan.
- A list of findings you can gather safely before acting.
- A caveat list for what ghost mode cannot prove.

## Guardrails

- Do not assume mirrored or dry-run environments perfectly predict live writes, latency, or contention.
- Confirm that the observation path is actually isolated before treating it as consequence-free.

## Default Invocation

Use $etherealness to show me how to inspect this system in read-only ghost mode and tell me what that view can and cannot prove.

