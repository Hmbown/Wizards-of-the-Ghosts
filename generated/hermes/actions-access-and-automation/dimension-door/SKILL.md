---
name: dimension-door
description: "Dimension Door is the quick-switch spell: branch to branch, environment to environment, project to project. It is not a migration and it is not discovery. It assumes both endpoints are known, prepared, and close enough in shape that you can step across with only the context you actually need."
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
      - actions-access-and-automation
      - execution
      - automation
      - access
      - actuation
---
# Dimension Door
Jump cleanly between two known contexts without dragging the whole room.
## What This Skill Does
Dimension Door is the quick-switch spell: branch to branch, environment to environment, project to project. It is not a migration and it is not discovery. It assumes both endpoints are known, prepared, and close enough in shape that you can step across with only the context you actually need.
In this grimoire, Dimension Door is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Dimension Door (spell).
## When To Use

- "switch between", "jump to", "toggle", "context switch", "hop over"
- Named endpoints: "from X to Y", "branch A to branch B", "staging to prod"
- "come back", "get back to", "without losing", "keep alive"
- Temporary investigation: "quickly check", "need to look at", "then return"
- Parallel sessions: "both need to stay live", "keep both running"
- User names specific source AND destination (branches, environments, accounts, clusters, terminals, workspaces)
- The switch is temporary and reversible
- The challenge is preserving state/context, not transforming systems

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. LOCK SOURCE STATE: Identify exactly what must be preserved — open files, running processes, env vars, credentials, branch state, terminal history, REPL state.
3. PACKAGE CONTEXT: Create the minimum viable snapshot — bookmark current location, save env state, note uncommitted changes, record running service PIDs.
4. EXECUTE SWITCH: Provide the exact commands to move to destination — git checkout, kubectl config use-context, aws configure, tmux switch, etc.
5. PREPARE REENTRY: Give the reverse commands and state-restoration steps so the user can return to source without confusion.
6. CALL OUT HIDDEN STATE: Warn about any state left behind that could cause confusion (running servers, uncommitted work, active sessions).
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- Context-switch checklist (what to save before leaving)
- State inventory (what travels with you)
- Switch commands (source → destination)
- Reentry commands (destination → source)
- Hidden state warnings

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Do not use quick-switch assumptions for migrations, unknown environments, or destructive cutovers.
- Call out any hidden state that would be left behind and cause confusion on arrival.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/dimension-door help me jump between these two known contexts with only the state I actually need to carry
```
