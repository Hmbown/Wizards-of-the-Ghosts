---
name: mage-hand
description: "Use this skill for small, careful remote manipulations where dexterity matters more than force."
user-invocable: true
---

# Mage Hand

Manipulate files, records, and lightweight system state with precision and minimal blast radius.

## Overview

Mage Hand is interpreted here as a hybrid spell with a shipping-now execution model.

Canonical source: Mage Hand (spell)

Provider target: OpenClaw

## When To Use

- Trigger this spell when the request asks for surgical, narrow edits to existing objects with explicit boundaries on what NOT to touch. Look for:
- Specific identifiers: file paths, ticket IDs, record keys, field names, audience names
- Constraint language: "only", "but don't touch", "leave X alone", "if X then stop"
- Single-field or single-value changes: "change max_attempts from 3 to 4", "patch reply_to_email"
- Conditional execution with early-exit: "only if each has approval, otherwise stop and return the exception list"
- Audit expectations: "show the diff", "tell me the exact line", "report skipped IDs"
- Small batch operations with per-item validation: "move tickets A, B, C but skip any missing X"

## Workflow

1. Restate boundaries before acting: Name the exact target, the success condition, and what must NOT be touched.
2. Scope to the smallest edit surface: Change one field, one line, one ticket state. Do not rewrite surrounding content.
3. Apply with diff or state proof: Show what changed. Confirm adjacent values are untouched.
4. Report exceptions, not just successes: If any item in a batch fails validation or lacks a prerequisite, stop and return the failure list. Do not silently skip.

## Deliverables

- A minimal, well-scoped change.
- A short audit trail of touched surfaces.
- A note on adjacent objects that were intentionally left alone.

## Guardrails

- Do NOT route here when the request involves:
- Do not use for: Building new interfaces or features ("give this script a chat front end", "create a dashboard")
- Do not use for: Setting up recurring automation ("every Friday", "whenever X happens, do Y automatically")
- Do not use for: Debugging, forensics, or tracing ("find what changed", "trace which integration sent this")
- Do not use for: System recovery or access restoration ("token expired, find the recovery path")
- Do not use for: Performance tuning or capacity changes ("slow down the queue", "scale up workers")
- Do not use for: Broad refactors or rewrites ("rewrite this module", "restructure the config")
- Do not use for: The key differentiator: Mage Hand moves or edits existing specific objects with known targets. It does not build, automate recurring tasks, investigate, or recover.

## Default Invocation

Use $mage-hand to make the smallest safe change needed here and show exactly what you touched.

