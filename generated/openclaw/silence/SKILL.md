---
name: silence
description: "Use this spell when you are drowning in notifications, verbose logs, irrelevant alerts, or context that does not serve the current task."
user-invocable: true
metadata:
  openclaw:
    requires:
      env:
        - SLACK_TOKEN
      bins:
        - curl
    primaryEnv: SLACK_TOKEN
    emoji: "🤫"
---

# Silence

Suppress noise, filter irrelevant signals, and create focused working environments.

## Overview

Silence is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Silence (spell)

Provider target: OpenClaw

## When To Use

- Activate this spell when the user asks to reduce, filter, suppress, or mute noisy output from an existing system. Look for these patterns:
- Noise complaints: "too noisy", "drowning in", "flooded with", "alert fatigue", "can't find the signal"
- Filter requests: "filter down to", "keep only", "suppress X but keep Y", "reduce verbosity"
- Mute/DND actions: "mute channels", "set do not disturb", "quiet mode", "silence notifications"
- Deduplication: "same alert fires repeatedly", "deduplicate", "suppress repeats"
- Log verbosity: "too verbose", "reduce log level", "filter out debug/trace", "show only errors/warnings"
- The core pattern: there is a working system producing too much output, and the user wants less of it without breaking anything.

## Workflow

1. Identify source and signal: Ask or infer what system is noisy (Slack, logs, CI, monitoring) and what output the user actually needs to see.
2. Define filter criteria: Specify exactly what gets suppressed (keywords, severity levels, channels, patterns) and what passes through. Write these criteria down before applying anything.
3. Apply suppression: Use the appropriate mechanism — Slack DND/mute APIs, log level configuration, alert rule silences, grep/awk filters, or notification preferences. Apply the narrowest filter that solves the problem.
4. Document the boundary: Record what is silenced, what is not, and why. This is critical so the user (or their team) can audit the filter later.
5. Provide restore: Give explicit instructions to undo the silence — which setting to revert, which API call to make, or which config to restore. Never leave a suppression in place without a documented off-ramp.

## Deliverables

- A filter or suppression configuration that reduces noise to signal.
- Clear documentation of what is silenced and what passes through.
- A restore mechanism to lift the silence when the focused session ends.

## Guardrails

- Never silence errors, critical alerts, security warnings, or health-check failures.
- Always preserve an audit trail of what was suppressed.
- Prefer narrowing the filter over broadening it. If unsure, keep the signal.
- Do NOT activate this spell for:
- Do not use for: Stealth/obfuscation: Making a service invisible to DNS, scanners, or network discovery. Silence filters output; it does not hide infrastructure.
- Do not use for: Security/anonymity: Stripping headers, rotating IPs, encrypting logs, or making traffic untraceable. This is about signal-to-noise, not evasion.
- Do not use for: Social moderation: Calming hostile conversations, managing team dynamics, or reducing emotional reactivity. Silence is technical, not interpersonal.
- Do not use for: Process redesign: Redesigning on-call rotations, changing team workflows, or restructuring alerting philosophy. This spell applies filters to existing systems; it does not redesign them.
- Do not use for: Deleting data: Removing logs permanently or purging history. Silence suppresses display/routing; it does not destroy records.

## Default Invocation

Use $silence to filter the noise here down to what actually matters, and tell me what you are suppressing.

