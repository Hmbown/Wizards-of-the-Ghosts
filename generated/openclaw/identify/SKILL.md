---
name: identify
description: "Identify is static analysis for operational understanding. It answers \"What is this?\" by inspecting structure, naming, dependencies, and runtime touchpoints. It does NOT search for artifacts, debug failures, monitor systems, verify claims, or modify code."
user-invocable: true
---

# Identify

Explain what a mysterious file, service, workflow, or artifact actually does.

## Overview

Identify is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Identify (spell)

Provider target: OpenClaw

## When To Use

- Use this spell when a user presents a specific artifact (file, script, config, service, binary, module, chart, extension, etc.) and asks any variation of:
- "What does this do?"
- "Explain this [artifact]"
- "What is this for?"
- "What does it touch/depend on?"
- "What can we prove from inspection?"
- "What's the safest next validation step?"
- Key signal: The artifact is already in hand. The question is about understanding, not finding, fixing, watching, or changing it.

## Workflow

1. Restate boundaries: Name the target, the success condition, and any no-touch constraints before acting.
2. Inspect directly: Read the artifact's contents. Do not speculate before looking.
3. Infer from evidence: Determine purpose from structure, dependencies, naming conventions, and runtime touchpoints (ports, volumes, secrets, APIs, services).
4. Separate certainty levels: Classify findings as:
5. Confirmed (directly visible in the artifact)
6. Likely (strong inference from patterns/contexts)
7. Unknown (cannot be proven without runtime testing or external data)
8. Return structured output: Provide:

## Deliverables

- A plain-English explanation of the artifact.
- Inputs, outputs, dependencies, and side effects when known.
- A confidence-rated list of unknowns.

## Guardrails

- Never overstate certainty when runtime behavior cannot be validated statically.
- Prefer source-backed explanation over assumptions or lore.
- If the user asks you to modify the artifact after identifying it, complete the Identify workflow first, then switch to the appropriate editing spell.
- Do not use for: "Find where X is defined" → Use search/locate, not Identify
- Do not use for: "Why did this break?" or "Trace the root cause" → Use debugging/incident response
- Do not use for: "Watch this system for changes" → Use monitoring/observability
- Do not use for: "Compare these claims against the code" → Use verification/audit
- Do not use for: "Change/modify/update this" → Use editing/transformation spells

## Default Invocation

Use $identify on this file, tool, or service and tell me what it does, what it touches, and what we still do not know.

