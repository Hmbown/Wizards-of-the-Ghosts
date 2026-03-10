---
name: guards-and-wards
description: "In D&D, Guards and Wards fills an area with layered minor defenses — fog, locked doors, illusory walls, confusion effects — that individually are trivial but collectively make navigation exhausting. The real-world version is defense in depth through volume: honeypots mixed with real services, rotating credentials alongside decoy credentials, overlapping rate limiters and CAPTCHAs and behavioral analysis and IP reputation checks. No single ward stops a determined attacker. The maze does."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - prototype
      - hybrid
      - monitoring-and-protection
      - observability
      - monitoring
      - guardrails
      - privacy
---
# Guards and Wards
Layer many small defenses into a maze that exhausts intruders before they reach anything valuable.
## What This Skill Does
In D&D, Guards and Wards fills an area with layered minor defenses — fog, locked doors, illusory walls, confusion effects — that individually are trivial but collectively make navigation exhausting. The real-world version is defense in depth through volume: honeypots mixed with real services, rotating credentials alongside decoy credentials, overlapping rate limiters and CAPTCHAs and behavioral analysis and IP reputation checks. No single ward stops a determined attacker. The maze does.
In this grimoire, Guards and Wards is treated as a hybrid spell with a prototype delivery profile.
Canonical reference input: Guards and Wards (spell).
## When To Use

- You are deploying, inheriting, or auditing a system and need a full security review.
- Multiple attack surfaces — secrets, permissions, dependencies, network exposure — need to be assessed together.
- A single Glyph of Warding is not enough; you need layered, system-wide defenses.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Inventory all surfaces: permissions, secrets management, dependency versions, network exposure, authentication, and access controls.
3. Assess each surface for vulnerabilities, misconfigurations, and unnecessary exposure.
4. Prioritize fixes by severity and exploitability, starting with the most dangerous gaps.
5. Apply hardening measures and return a report of what was secured, what remains exposed, and what needs ongoing monitoring.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A security audit report covering all assessed surfaces.
- Prioritized remediation steps, starting with the most critical exposures.
- A residual risk summary of what could not be fully secured and recommended monitoring.

## Pitfalls / Guardrails

- Call out the glue, permissions, or missing infrastructure before you imply this is fully operational.
- Layered defenses rot if unmaintained. Each ward needs an owner and a freshness date — stale wards create false confidence.
- The maze must not trap legitimate users. If your own team cannot navigate the wards, the defense has become a denial of service against yourself.
- Document the ward map. Undocumented defenses become undocumented attack surface when the original caster leaves.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check which parts are concrete actions versus framing, so the user can tell what is real now.
- Check that any missing glue code, permissions, or future work is labeled before the skill is treated as ready.

## Example Invocation
```text
/guards-and-wards perform a full security audit of this system and prioritize what needs hardening first
```
