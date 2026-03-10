---
name: intimidation
description: "Use this skill when a message must sound serious because the situation is serious: security findings, compliance obligations, deadline-backed escalations, or non-optional remediation notices. It is about calibrated force, not bluster; the tone should match the facts and consequences."
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
      - messaging-and-coordination
      - messaging
      - coordination
      - handoffs
      - rhetoric
---
# Intimidation
Write with enough authority that the recipient understands the risk and the deadline.
## What This Skill Does
Use this skill when a message must sound serious because the situation is serious: security findings, compliance obligations, deadline-backed escalations, or non-optional remediation notices. It is about calibrated force, not bluster; the tone should match the facts and consequences.
In this grimoire, Intimidation is treated as a metaphorical skill with a shipping-now delivery profile.
Canonical reference input: Intimidation (skill).
## When To Use

- A security, compliance, or operational issue requires firm language and explicit accountability.
- A polite draft would understate genuine urgency or make the required action seem optional.
- You need a serious escalation that names the consequence of delay without theatrics.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify the authority chain, required action, deadline, and real consequence of inaction.
3. Draft direct language that matches the severity level and makes the next step unmistakable.
4. Return the escalation message with a note on why the severity is justified and when to soften it.
5. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A stern but defensible message draft.
- A clear call to action, deadline, and owner.
- A short rationale for the tone and severity level.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Do not invent legal, security, or employment consequences that are not real.
- Avoid humiliation, personal threats, or bullying when firm language will do the job.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/intimidation draft a serious, authoritative message that matches the actual risk and required action
```
