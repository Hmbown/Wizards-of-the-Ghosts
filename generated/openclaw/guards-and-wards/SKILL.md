---
name: guards-and-wards
description: "In D&D, Guards and Wards fills an area with layered minor defenses — fog, locked doors, illusory walls, confusion effects — that individually are trivial but collectively make navigation exhausting. The real-world version is defense in depth through volume: honeypots mixed with real services, rotating credentials alongside decoy credentials, overlapping rate limiters and CAPTCHAs and behavioral analysis and IP reputation checks. No single ward stops a determined attacker. The maze does."
user-invocable: true
---

# Guards and Wards

Layer many small defenses into a maze that exhausts intruders before they reach anything valuable.

## Overview

Guards and Wards is interpreted here as a hybrid spell with a prototype execution model.

Canonical source: Guards and Wards (spell)

Provider target: OpenClaw

## When To Use

- You are deploying, inheriting, or auditing a system and need a full security review.
- Multiple attack surfaces — secrets, permissions, dependencies, network exposure — need to be assessed together.
- A single Glyph of Warding is not enough; you need layered, system-wide defenses.

## Workflow

1. Inventory all surfaces: permissions, secrets management, dependency versions, network exposure, authentication, and access controls.
2. Assess each surface for vulnerabilities, misconfigurations, and unnecessary exposure.
3. Prioritize fixes by severity and exploitability, starting with the most dangerous gaps.
4. Apply hardening measures and return a report of what was secured, what remains exposed, and what needs ongoing monitoring.

## Deliverables

- A security audit report covering all assessed surfaces.
- Prioritized remediation steps, starting with the most critical exposures.
- A residual risk summary of what could not be fully secured and recommended monitoring.

## Guardrails

- Layered defenses rot if unmaintained. Each ward needs an owner and a freshness date — stale wards create false confidence.
- The maze must not trap legitimate users. If your own team cannot navigate the wards, the defense has become a denial of service against yourself.
- Document the ward map. Undocumented defenses become undocumented attack surface when the original caster leaves.

## Default Invocation

Use $guards-and-wards to perform a full security audit of this system and prioritize what needs hardening first.

