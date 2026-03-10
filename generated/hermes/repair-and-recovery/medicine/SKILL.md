---
name: medicine
description: "Use this skill for live system triage: interpreting logs as symptoms, prioritizing immediate stabilization, and applying treatments for known failure modes. It is about keeping the patient alive first and only then planning deeper corrective care."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - skill
      - shipping-now
      - metaphorical
      - repair-and-recovery
      - recovery
      - repair
      - triage
      - stabilization
---
# Medicine
Read the symptoms, stabilize the patient, and prescribe the next safe intervention.
## What This Skill Does
Use this skill for live system triage: interpreting logs as symptoms, prioritizing immediate stabilization, and applying treatments for known failure modes. It is about keeping the patient alive first and only then planning deeper corrective care.
In this grimoire, Medicine is treated as a metaphorical skill with a shipping-now delivery profile.
Canonical reference input: Medicine (skill).
## When To Use

- A service is degraded, crashing, or throwing enough symptoms that triage has to happen now.
- Logs, metrics, or traces resemble a known incident pattern that may have a standard treatment.
- You need a stabilization plan before a full root-cause investigation can finish.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Take vitals from the current symptoms, severity indicators, and dependency status.
3. Choose the safest stabilizing treatment and watch the system's response before escalating.
4. Return the likely diagnosis, immediate treatment plan, and follow-up checks for aftercare.
5. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A triage summary with the most likely condition and severity.
- Ordered treatment steps with monitor points and stop conditions.
- Escalation criteria and a short post-incident follow-up plan.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- State uncertainty instead of overdiagnosing from sparse or noisy signals.
- Prefer reversible treatments during active incidents and flag any risky interventions.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/medicine triage this system issue, stabilize it first, and tell me the most likely treatment path
```
