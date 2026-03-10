---
name: mislead
description: "Mislead is defensive deception: honeypots, canary tokens, decoy endpoints, fake datasets, and other convincing false presences that reveal who is snooping. The goal is not to trick legitimate users for sport. The goal is to create an instrumented fake that attracts unauthorized curiosity while the real system remains elsewhere. This makes the spell powerful and ethically sharp-edged. It needs explicit boundaries, isolation, and a clear monitoring objective before it should be deployed."
user-invocable: false
disable-model-invocation: true
---

# Mislead

Set a false campfire and watch who gathers around it.

## Overview

Mislead is interpreted here as a hybrid spell with a prototype execution model.

Canonical source: Mislead (spell)

Provider target: OpenClaw

## When To Use

- You need a honeypot, canary token, or decoy endpoint to detect unauthorized discovery or access attempts.
- The real requirement is defensive visibility into who comes looking for sensitive assets.
- You can isolate the decoy from production behavior and document the response path if it gets touched.

## Workflow

1. Define the monitoring objective, the expected adversary behavior, and what evidence the decoy should capture.
2. Design a believable false surface that is attractive enough to probe but isolated enough not to create production risk.
3. Instrument the decoy with alerts, logging, and tripwires that capture contact without escalating harm.
4. Specify the response playbook: who gets notified, how evidence is retained, and what actions are explicitly out of scope.
5. Return the decoy design with the ethical boundary conditions that make it defensive rather than abusive.

## Deliverables

- A decoy or honeypot design with isolation boundaries.
- A tripwire and alerting plan for when the false surface is touched.
- A response playbook covering evidence handling and operator follow-up.

## Guardrails

- Use Mislead only for defensive detection, never for fraud, manipulation of legitimate users, or offensive entrapment.
- Keep fake data, decoy endpoints, and real systems cleanly separated so the spell cannot spill into production harm.

## Default Invocation

Use $mislead to design a defensive decoy, honeypot, or canary setup that tells us who is snooping without creating collateral damage.

