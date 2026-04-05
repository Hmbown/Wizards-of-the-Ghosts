---
name: invisibility
description: "Invisibility is operational quieting: trimming unnecessary logs, reducing exposed surface area, cleaning transient traces, and avoiding needless broadcast. It is not about doing forbidden things unseen. It is about keeping ordinary work from becoming gratuitously loud or overexposed."
user-invocable: true
---

# Invisibility

Lower the noise floor of an operation without lowering accountability.

## Overview

Invisibility is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Invisibility (spell)

Provider target: OpenClaw

## When To Use

- A workflow is generating more chatter, surface area, or incidental trace than it needs.
- You want tighter compartmentalization around sensitive but legitimate work.
- The goal is quiet execution, not evasion of required oversight.

## Workflow

1. Inventory what is currently exposed through logs, alerts, interfaces, metadata, or temporary artifacts.
2. Trim nonessential exposure while preserving the traces operators, auditors, and debuggers actually need.
3. Return the quieter operating pattern and the visibility that intentionally remains.

## Deliverables

- A reduced-footprint operating plan.
- A list of traces to suppress, minimize, or relocate.
- A list of audit and debugging surfaces that must remain.

## Guardrails

- Do not delete or suppress records required for security review, compliance, or incident response.
- If the request is really about hiding wrongdoing, this is the wrong spell.

## Default Invocation

Use $invisibility to reduce the unnecessary noise and exposure around this workflow while preserving the traces we are obliged to keep.

