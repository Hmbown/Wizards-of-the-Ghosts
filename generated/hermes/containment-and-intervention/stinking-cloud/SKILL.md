---
name: stinking-cloud
description: "In D&D, Stinking Cloud fills an area with nauseating gas — creatures inside are incapacitated but the terrain itself is undamaged. The real-world version is area denial: making a zone, endpoint, or resource unusable to unwanted traffic without permanently destroying or modifying it. Rate limiting, IP-range blocks, honeypots, tarpits, geographic restrictions. Stinking Cloud is defensive — it protects a perimeter by making the area inside it miserable for intruders while leaving the underlying infrastructure intact."
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
      - containment-and-intervention
      - containment
      - intervention
      - disruption
      - safety
---
# Stinking Cloud
Make an area inhospitable without destroying it.
## What This Skill Does
In D&D, Stinking Cloud fills an area with nauseating gas — creatures inside are incapacitated but the terrain itself is undamaged. The real-world version is area denial: making a zone, endpoint, or resource unusable to unwanted traffic without permanently destroying or modifying it. Rate limiting, IP-range blocks, honeypots, tarpits, geographic restrictions. Stinking Cloud is defensive — it protects a perimeter by making the area inside it miserable for intruders while leaving the underlying infrastructure intact.
In this grimoire, Stinking Cloud is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Stinking Cloud (spell).
## When To Use

- You need to deter access to a resource, endpoint, or zone without destroying it.
- Defensive measures should slow, frustrate, or redirect unwanted traffic rather than block it outright.
- You want to set up a honeypot, tarpit, or deterrent zone that wastes attackers' time and resources.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Define the area to deny: which endpoints, IP ranges, geographic zones, or resources.
3. Choose the deterrent mechanism: rate limiting, tarpitting, CAPTCHA walls, honeypots, or access throttling.
4. Deploy the deterrent and verify it affects only the intended zone.
5. Monitor for legitimate traffic caught in the cloud and create bypass mechanisms if needed.
6. Set review criteria for when the cloud should be lifted or the perimeter adjusted.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A deployed area-denial mechanism with clear boundaries.
- Monitoring for false positives: legitimate users caught in the deterrent zone.
- A review schedule for adjusting or lifting the deterrent.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Area denial must not trap legitimate users without recourse. Always provide a way for real users to verify themselves and pass through.
- Stinking Cloud is temporary and defensive. If you need permanent access control, use proper authentication and authorization.
- Honeypots and tarpits must be clearly separated from production systems to avoid contamination.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/stinking-cloud set up area-denial defenses — rate limits, tarpits, honeypots, or deterrent zones that make an area inhospitable to unwanted traffic without destroying the underlying infrastructure
```
