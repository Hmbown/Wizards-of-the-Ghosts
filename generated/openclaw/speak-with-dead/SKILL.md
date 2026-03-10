---
name: speak-with-dead
description: "Use this spell when the answers you need are buried in dead codebases, sunset APIs, archived documentation, or the tribal knowledge frozen in old commits and departed contributors."
user-invocable: true
---

# Speak with Dead

Extract knowledge from abandoned, deprecated, or legacy systems.

## Overview

Speak with Dead is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Speak with Dead (spell)

Provider target: OpenClaw

## When To Use

- A legacy system, deprecated API, or archived project holds knowledge you need for current work.
- The original authors or maintainers are gone and only artifacts remain.
- You need to understand why something was built the way it was, not just what it does now.

## Workflow

1. Identify the dead system and the specific questions you need answered.
2. Excavate available artifacts: git history, archived docs, old issues, README files, commit messages, and code comments.
3. Reconstruct the dead system's intent, architecture, and known failure modes from evidence.
4. Return answers to the posed questions with explicit confidence levels and source references.

## Deliverables

- Answers to specific questions drawn from the dead system's artifacts.
- A reconstruction of the system's original intent and known failure modes.
- A clear separation between what the dead system actually recorded and what you are inferring.

## Guardrails

- Do not fabricate answers the dead system never contained — clearly label inference versus evidence.
- Respect that archived systems may have been archived for reasons including security, legal, or deliberate deprecation.

## Default Invocation

Use $speak-with-dead to interrogate this legacy system and tell me what it knew, what it intended, and where the evidence runs out.

