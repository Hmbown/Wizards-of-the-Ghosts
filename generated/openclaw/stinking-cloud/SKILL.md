---
name: stinking-cloud
description: "In D&D, Stinking Cloud fills an area with nauseating gas — creatures inside are incapacitated but the terrain itself is undamaged. The real-world version is area denial: making a zone, endpoint, or resource unusable to unwanted traffic without permanently destroying or modifying it. Rate limiting, IP-range blocks, honeypots, tarpits, geographic restrictions. Stinking Cloud is defensive — it protects a perimeter by making the area inside it miserable for intruders while leaving the underlying infrastructure intact."
user-invocable: true
---

# Stinking Cloud

Make an area inhospitable without destroying it.

## Overview

Stinking Cloud is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Stinking Cloud (spell)

Provider target: OpenClaw

## When To Use

- You need to deter access to a resource, endpoint, or zone without destroying it.
- Defensive measures should slow, frustrate, or redirect unwanted traffic rather than block it outright.
- You want to set up a honeypot, tarpit, or deterrent zone that wastes attackers' time and resources.

## Workflow

1. Define the area to deny: which endpoints, IP ranges, geographic zones, or resources.
2. Choose the deterrent mechanism: rate limiting, tarpitting, CAPTCHA walls, honeypots, or access throttling.
3. Deploy the deterrent and verify it affects only the intended zone.
4. Monitor for legitimate traffic caught in the cloud and create bypass mechanisms if needed.
5. Set review criteria for when the cloud should be lifted or the perimeter adjusted.

## Deliverables

- A deployed area-denial mechanism with clear boundaries.
- Monitoring for false positives: legitimate users caught in the deterrent zone.
- A review schedule for adjusting or lifting the deterrent.

## Guardrails

- Area denial must not trap legitimate users without recourse. Always provide a way for real users to verify themselves and pass through.
- Stinking Cloud is temporary and defensive. If you need permanent access control, use proper authentication and authorization.
- Honeypots and tarpits must be clearly separated from production systems to avoid contamination.

## Default Invocation

Use $stinking-cloud to set up area-denial defenses — rate limits, tarpits, honeypots, or deterrent zones that make an area inhospitable to unwanted traffic without destroying the underlying infrastructure.

