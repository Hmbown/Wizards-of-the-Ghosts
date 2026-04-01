---
name: sleight-of-hand
description: "Sleight of Hand is not about solving a problem — the solution is already known. It is about executing a known change with zero collateral damage. The skill is precision, not creativity."
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
      - actions-access-and-automation
      - execution
      - automation
      - access
      - actuation
---
# Sleight of Hand
Make the tiny exact change that fixes the problem without disturbing the room.
## What This Skill Does
Sleight of Hand is not about solving a problem — the solution is already known. It is about executing a known change with zero collateral damage. The skill is precision, not creativity.
In this grimoire, Sleight of Hand is treated as a metaphorical skill with a shipping-now delivery profile.
Canonical reference input: Sleight of Hand (skill).
## When To Use

- Activate this spell when the user requests a surgical, minimal edit where:
- The exact change is known (before value → after value)
- Only 1–3 specific locations need modification
- The user names the file, line, or exact string to change
- The request emphasizes precision: "just this", "only this one", "don't touch anything else"

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Isolate: Identify the smallest possible surface area that carries the fix. Confirm the exact match target — file, line, or pattern. If the match is ambiguous (could hit multiple places), stop and ask for clarification. Never guess.
3. Stage: Show the exact change before applying it. Present a before-and-after diff of only the affected lines. Verify that neighboring lines, formatting, and unrelated occurrences are untouched.
4. Deliver: Apply the edit. Return: (a) the minimal diff, (b) a confidence statement confirming what was changed and what was intentionally left alone, (c) a one-line rollback instruction (the inverse edit).
5. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A targeted patch, replacement pattern, or edit instruction.
- Proof of what changed and what was intentionally left alone.
- A rollback note in case the tiny move still misfires.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Never run global replacements when the match surface is ambiguous.
- If the same string appears multiple times, change only the one the user specified.
- Preserve all surrounding whitespace, formatting, and behavior.
- If you are unsure which occurrence to change, ask — do not pick one silently.
- Do not use for: Rewriting a function or algorithm (needs a rebuild spell)
- Do not use for: Moving a file and updating all imports across the repo (needs a refactor spell)
- Do not use for: Diagnosing why something is broken (needs an investigation spell)
- Do not use for: Formatting, linting, or cosmetic cleanup (needs a prestidigitation spell)
- Do not use for: Building a new script from existing pieces (needs a conjuration spell)
- Do not use for: Recovering deleted files from git history (needs a resurrection spell)

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/sleight-of-hand make the smallest safe edit here and show me exactly what moved
```
