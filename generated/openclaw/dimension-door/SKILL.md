---
name: dimension-door
description: "Dimension Door is the quick-switch spell: branch to branch, environment to environment, project to project. It is not a migration and it is not discovery. It assumes both endpoints are known, prepared, and close enough in shape that you can step across with only the context you actually need."
user-invocable: true
---

# Dimension Door

Jump cleanly between two known contexts without dragging the whole room.

## Overview

Dimension Door is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Dimension Door (spell)

Provider target: OpenClaw

## When To Use

- "switch between", "jump to", "toggle", "context switch", "hop over"
- Named endpoints: "from X to Y", "branch A to branch B", "staging to prod"
- "come back", "get back to", "without losing", "keep alive"
- Temporary investigation: "quickly check", "need to look at", "then return"
- Parallel sessions: "both need to stay live", "keep both running"
- User names specific source AND destination (branches, environments, accounts, clusters, terminals, workspaces)
- The switch is temporary and reversible
- The challenge is preserving state/context, not transforming systems

## Workflow

1. LOCK SOURCE STATE: Identify exactly what must be preserved — open files, running processes, env vars, credentials, branch state, terminal history, REPL state.
2. PACKAGE CONTEXT: Create the minimum viable snapshot — bookmark current location, save env state, note uncommitted changes, record running service PIDs.
3. EXECUTE SWITCH: Provide the exact commands to move to destination — git checkout, kubectl config use-context, aws configure, tmux switch, etc.
4. PREPARE REENTRY: Give the reverse commands and state-restoration steps so the user can return to source without confusion.
5. CALL OUT HIDDEN STATE: Warn about any state left behind that could cause confusion (running servers, uncommitted work, active sessions).

## Deliverables

- Context-switch checklist (what to save before leaving)
- State inventory (what travels with you)
- Switch commands (source → destination)
- Reentry commands (destination → source)
- Hidden state warnings

## Guardrails

- Do not use quick-switch assumptions for migrations, unknown environments, or destructive cutovers.
- Call out any hidden state that would be left behind and cause confusion on arrival.

## Default Invocation

Use $dimension-door to help me jump between these two known contexts with only the state I actually need to carry.

