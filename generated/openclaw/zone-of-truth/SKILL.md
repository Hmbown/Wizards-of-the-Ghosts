---
name: zone-of-truth
description: "Use this spell to enter a mode where every assertion is backed by evidence, confidence is calibrated, speculation is flagged, and hallucination is actively resisted."
user-invocable: true
---

# Zone of Truth

Establish a high-integrity epistemic environment where claims must be sourced and uncertainty labeled.

## Overview

Zone of Truth is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Zone of Truth (spell)

Provider target: OpenClaw

## When To Use

- You are making a high-stakes decision and need maximum epistemic rigor from the agent.
- A previous conversation has drifted into speculation and you want to reset to verified ground.
- You want the agent to clearly separate what it knows, what it infers, and what it is guessing.

## Workflow

1. Activate truth-zone discipline: all claims require sources or explicit confidence labels.
2. Re-examine any prior assertions in the conversation and flag unsupported ones.
3. For each new claim, provide the evidence basis or clearly mark it as inference, estimation, or speculation.
4. Maintain the zone until the user explicitly dismisses it or the conversation ends.

## Deliverables

- A conversation mode where every claim is sourced or confidence-labeled.
- A re-audit of prior unsupported assertions if the zone is activated mid-conversation.
- Clear visual markers distinguishing fact, inference, and speculation.

## Guardrails

- Do not claim this mode eliminates all error — it reduces unsourced assertions, not all mistakes.
- Do not use the zone framing to imply that the agent's normal mode is dishonest.

## Default Invocation

Use $zone-of-truth to switch into high-integrity mode: source every claim, label every uncertainty, and flag anything speculative.

