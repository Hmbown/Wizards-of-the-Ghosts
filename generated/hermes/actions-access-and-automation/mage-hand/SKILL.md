---
name: mage-hand
description: "Use this skill for small, careful remote manipulations where dexterity matters more than force."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - shipping-now
      - hybrid
      - actions-access-and-automation
      - execution
      - automation
      - access
      - actuation
---
# Mage Hand
Manipulate files, records, and lightweight system state with precision and minimal blast radius.
## Sigil

```text
     __
  .-'  `-.
 /  .--.  \\
|  / /\\ \\ |
|  | \\/ | |
 \\  `--'  /
  `-.__.-'
```

## What This Skill Does
Use this skill for small, careful remote manipulations where dexterity matters more than force.
In this grimoire, Mage Hand is treated as a hybrid spell with a shipping-now delivery profile.
Canonical reference input: Mage Hand (spell).
## When To Use

- Trigger this spell when the request asks for surgical, narrow edits to existing objects with explicit boundaries on what NOT to touch. Look for:
- Specific identifiers: file paths, ticket IDs, record keys, field names, audience names
- Constraint language: "only", "but don't touch", "leave X alone", "if X then stop"
- Single-field or single-value changes: "change max_attempts from 3 to 4", "patch reply_to_email"
- Conditional execution with early-exit: "only if each has approval, otherwise stop and return the exception list"
- Audit expectations: "show the diff", "tell me the exact line", "report skipped IDs"
- Small batch operations with per-item validation: "move tickets A, B, C but skip any missing X"

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Restate boundaries before acting: Name the exact target, the success condition, and what must NOT be touched.
3. Scope to the smallest edit surface: Change one field, one line, one ticket state. Do not rewrite surrounding content.
4. Apply with diff or state proof: Show what changed. Confirm adjacent values are untouched.
5. Report exceptions, not just successes: If any item in a batch fails validation or lacks a prerequisite, stop and return the failure list. Do not silently skip.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A minimal, well-scoped change.
- A short audit trail of touched surfaces.
- A note on adjacent objects that were intentionally left alone.

## Pitfalls / Guardrails

- Keep the theatrical framing, but name the concrete mechanism that makes the skill useful right now.
- Do NOT route here when the request involves:
- Do not use for: Building new interfaces or features ("give this script a chat front end", "create a dashboard")
- Do not use for: Setting up recurring automation ("every Friday", "whenever X happens, do Y automatically")
- Do not use for: Debugging, forensics, or tracing ("find what changed", "trace which integration sent this")
- Do not use for: System recovery or access restoration ("token expired, find the recovery path")
- Do not use for: Performance tuning or capacity changes ("slow down the queue", "scale up workers")
- Do not use for: Broad refactors or rewrites ("rewrite this module", "restructure the config")
- Do not use for: The key differentiator: Mage Hand moves or edits existing specific objects with known targets. It does not build, automate recurring tasks, investigate, or recover.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check which parts are concrete actions versus framing, so the user can tell what is real now.

## Example Invocation
```text
/mage-hand make the smallest safe change needed here and show exactly what you touched
```
