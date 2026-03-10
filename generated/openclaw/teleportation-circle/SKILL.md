---
name: teleportation-circle
description: "Use this spell when you need a permanent, reliable portal between two environments — a CI/CD pipeline, a standing data sync, a repeatable deployment, or a migration path you will use more than once."
user-invocable: true
---

# Teleportation Circle

Establish reusable deployment pipelines, standing sync routes, and repeatable migration paths.

## Overview

Teleportation Circle is interpreted here as a literal spell with a prototype execution model.

Canonical source: Teleportation Circle (spell)

Provider target: OpenClaw

## When To Use

- You are setting up a CI/CD pipeline or deployment workflow that will be used repeatedly.
- Two systems need a standing sync route that runs reliably without manual intervention.
- A migration path needs to be codified so it can be re-run, tested, and trusted.

## Workflow

1. Define the source, destination, and what travels through the circle: code, data, configuration, or artifacts.
2. Build the pipeline or sync route with explicit triggers, validation steps, and failure handling.
3. Test the circle end-to-end before relying on it for production traffic.
4. Document the circle's configuration, monitoring, and maintenance requirements.

## Deliverables

- A configured, tested pipeline or sync route between source and destination.
- Documentation of triggers, validation steps, failure modes, and rollback procedures.
- A monitoring and maintenance plan — permanent portals need ongoing attention.

## Guardrails

- Do not create a circle and forget about it. Permanent portals need health checks, alerting, and maintenance.
- Test the circle in a non-production environment before routing real traffic through it.

## Default Invocation

Use $teleportation-circle to establish a reusable pipeline between these environments, with testing and monitoring built in.

