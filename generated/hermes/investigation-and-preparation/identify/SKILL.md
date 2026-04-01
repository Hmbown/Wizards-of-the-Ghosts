---
name: identify
description: "Identify is static analysis for operational understanding. It answers \"What is this?\" by inspecting structure, naming, dependencies, and runtime touchpoints. It does NOT search for artifacts, debug failures, monitor systems, verify claims, or modify code."
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
      - investigation-and-preparation
      - analysis
      - discovery
      - translation
      - preflight
---
# Identify
Explain what a mysterious file, service, workflow, or artifact actually does.
## What This Skill Does
Identify is static analysis for operational understanding. It answers "What is this?" by inspecting structure, naming, dependencies, and runtime touchpoints. It does NOT search for artifacts, debug failures, monitor systems, verify claims, or modify code.
In this grimoire, Identify is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Identify (spell).
## When To Use

- Use this spell when a user presents a specific artifact (file, script, config, service, binary, module, chart, extension, etc.) and asks any variation of:
- "What does this do?"
- "Explain this [artifact]"
- "What is this for?"
- "What does it touch/depend on?"
- "What can we prove from inspection?"
- "What's the safest next validation step?"
- Key signal: The artifact is already in hand. The question is about understanding, not finding, fixing, watching, or changing it.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Restate boundaries: Name the target, the success condition, and any no-touch constraints before acting.
3. Inspect directly: Read the artifact's contents. Do not speculate before looking.
4. Infer from evidence: Determine purpose from structure, dependencies, naming conventions, and runtime touchpoints (ports, volumes, secrets, APIs, services).
5. Separate certainty levels: Classify findings as:
6. Confirmed (directly visible in the artifact)
7. Likely (strong inference from patterns/contexts)
8. Unknown (cannot be proven without runtime testing or external data)
9. Return structured output: Provide:
10. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A plain-English explanation of the artifact.
- Inputs, outputs, dependencies, and side effects when known.
- A confidence-rated list of unknowns.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Never overstate certainty when runtime behavior cannot be validated statically.
- Prefer source-backed explanation over assumptions or lore.
- If the user asks you to modify the artifact after identifying it, complete the Identify workflow first, then switch to the appropriate editing spell.
- Do not use for: "Find where X is defined" → Use search/locate, not Identify
- Do not use for: "Why did this break?" or "Trace the root cause" → Use debugging/incident response
- Do not use for: "Watch this system for changes" → Use monitoring/observability
- Do not use for: "Compare these claims against the code" → Use verification/audit
- Do not use for: "Change/modify/update this" → Use editing/transformation spells

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/identify Use $identify on this file, tool, or service and tell me what it does, what it touches, and what we still do not know
```
