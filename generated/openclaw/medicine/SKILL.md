---
name: medicine
description: "Use this skill for live system triage: interpreting logs as symptoms, prioritizing immediate stabilization, and applying treatments for known failure modes. It is about keeping the patient alive first and only then planning deeper corrective care."
user-invocable: true
---

# Medicine

Read the symptoms, stabilize the patient, and prescribe the next safe intervention.

## Overview

Medicine is interpreted here as a metaphorical skill with a shipping-now execution model.

Canonical source: Medicine (skill)

Provider target: OpenClaw

## When To Use

- A service is degraded, crashing, or throwing enough symptoms that triage has to happen now.
- Logs, metrics, or traces resemble a known incident pattern that may have a standard treatment.
- You need a stabilization plan before a full root-cause investigation can finish.

## Workflow

1. Take vitals from the current symptoms, severity indicators, and dependency status.
2. Choose the safest stabilizing treatment and watch the system's response before escalating.
3. Return the likely diagnosis, immediate treatment plan, and follow-up checks for aftercare.

## Deliverables

- A triage summary with the most likely condition and severity.
- Ordered treatment steps with monitor points and stop conditions.
- Escalation criteria and a short post-incident follow-up plan.

## Guardrails

- State uncertainty instead of overdiagnosing from sparse or noisy signals.
- Prefer reversible treatments during active incidents and flag any risky interventions.

## Default Invocation

Use $medicine to triage this system issue, stabilize it first, and tell me the most likely treatment path.

