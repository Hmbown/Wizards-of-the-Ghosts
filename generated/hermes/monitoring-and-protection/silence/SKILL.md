---
name: silence
description: "Use this spell when you are drowning in notifications, verbose logs, irrelevant alerts, or context that does not serve the current task."
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
      - monitoring-and-protection
      - observability
      - monitoring
      - guardrails
      - privacy
      - integration
      - slack
---
# Silence
Suppress noise, filter irrelevant signals, and create focused working environments.
## What This Skill Does
Use this spell when you are drowning in notifications, verbose logs, irrelevant alerts, or context that does not serve the current task.
In this grimoire, Silence is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Silence (spell).
## When To Use

- Activate this spell when the user asks to reduce, filter, suppress, or mute noisy output from an existing system. Look for these patterns:
- Noise complaints: "too noisy", "drowning in", "flooded with", "alert fatigue", "can't find the signal"
- Filter requests: "filter down to", "keep only", "suppress X but keep Y", "reduce verbosity"
- Mute/DND actions: "mute channels", "set do not disturb", "quiet mode", "silence notifications"
- Deduplication: "same alert fires repeatedly", "deduplicate", "suppress repeats"
- Log verbosity: "too verbose", "reduce log level", "filter out debug/trace", "show only errors/warnings"
- The core pattern: there is a working system producing too much output, and the user wants less of it without breaking anything.

## Prerequisites

- Environment variables available to Hermes: `SLACK_TOKEN`.
- Primary credential or token: `SLACK_TOKEN`.
- Binaries on PATH: `curl`.

## Setup

1. Confirm the required environment variables are available inside the active Hermes runtime, not just in a shell profile.
2. Verify the required binaries resolve on PATH before you rely on them in a procedure.
3. Choose a non-production or low-risk target first if the skill can page, unlock, alert, or touch a live integration.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify source and signal: Ask or infer what system is noisy (Slack, logs, CI, monitoring) and what output the user actually needs to see.
3. Define filter criteria: Specify exactly what gets suppressed (keywords, severity levels, channels, patterns) and what passes through. Write these criteria down before applying anything.
4. Apply suppression: Use the appropriate mechanism — Slack DND/mute APIs, log level configuration, alert rule silences, grep/awk filters, or notification preferences. Apply the narrowest filter that solves the problem.
5. Document the boundary: Record what is silenced, what is not, and why. This is critical so the user (or their team) can audit the filter later.
6. Provide restore: Give explicit instructions to undo the silence — which setting to revert, which API call to make, or which config to restore. Never leave a suppression in place without a documented off-ramp.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A filter or suppression configuration that reduces noise to signal.
- Clear documentation of what is silenced and what passes through.
- A restore mechanism to lift the silence when the focused session ends.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Never silence errors, critical alerts, security warnings, or health-check failures.
- Always preserve an audit trail of what was suppressed.
- Prefer narrowing the filter over broadening it. If unsure, keep the signal.
- Do NOT activate this spell for:
- Do not use for: Stealth/obfuscation: Making a service invisible to DNS, scanners, or network discovery. Silence filters output; it does not hide infrastructure.
- Do not use for: Security/anonymity: Stripping headers, rotating IPs, encrypting logs, or making traffic untraceable. This is about signal-to-noise, not evasion.
- Do not use for: Social moderation: Calming hostile conversations, managing team dynamics, or reducing emotional reactivity. Silence is technical, not interpersonal.
- Do not use for: Process redesign: Redesigning on-call rotations, changing team workflows, or restructuring alerting philosophy. This spell applies filters to existing systems; it does not redesign them.
- Do not use for: Deleting data: Removing logs permanently or purging history. Silence suppresses display/routing; it does not destroy records.
- Do not rely on a live integration until credentials, target scope, and rollback expectations are verified.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.
- Check the required environment variables and binaries in the active Hermes runtime before trusting the procedure on a live target.

## Example Invocation
```text
/silence filter the noise here down to what actually matters, and tell me what you are suppressing
```
