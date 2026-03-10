---
name: animal-friendship
description: "Animal Friendship is the first-contact spell for unfamiliar APIs, vendors, and services. It treats integration work as relationship-building: learn the temperament, respect the boundaries, and earn a stable exchange before asking for anything ambitious. The goal is not domination but trustable cooperation."
user-invocable: true
---

# Animal Friendship

Approach a strange service gently until it stops biting.

## Overview

Animal Friendship is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Animal Friendship (spell)

Provider target: OpenClaw

## When To Use

- You are integrating with an API or service you have never used before.
- The docs are incomplete, contradictory, or too polished to trust blindly.
- You want the smallest successful handshake before building deeper dependencies.

## Workflow

1. Profile the system's habits: auth model, rate limits, failure modes, and supported operations.
2. Establish a safe first interaction, preferably read-only or against a sandbox.
3. Return a cooperation plan covering the first useful call, the next expansion steps, and the boundaries you should not cross.

## Deliverables

- A low-risk integration handshake plan.
- A shortlist of quirks, quotas, and trust boundaries.
- A recommended next request that proves the relationship is real.

## Guardrails

- Do not brute-force unfamiliar endpoints, credentials, or undocumented behavior.
- Prefer sandbox, test, or read-only access until the system has proven predictable.

## Default Invocation

Use $animal-friendship to help me establish a safe first working relationship with this unfamiliar API or service.

