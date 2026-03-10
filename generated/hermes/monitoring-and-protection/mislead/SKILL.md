---
name: mislead
description: "Mislead is defensive deception: honeypots, canary tokens, decoy endpoints, fake datasets, and other convincing false presences that reveal who is snooping. The goal is not to trick legitimate users for sport. The goal is to create an instrumented fake that attracts unauthorized curiosity while the real system remains elsewhere. This makes the spell powerful and ethically sharp-edged. It needs explicit boundaries, isolation, and a clear monitoring objective before it should be deployed."
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
# Mislead
Set a false campfire and watch who gathers around it.
## What This Skill Does
Mislead is defensive deception: honeypots, canary tokens, decoy endpoints, fake datasets, and other convincing false presences that reveal who is snooping. The goal is not to trick legitimate users for sport. The goal is to create an instrumented fake that attracts unauthorized curiosity while the real system remains elsewhere. This makes the spell powerful and ethically sharp-edged. It needs explicit boundaries, isolation, and a clear monitoring objective before it should be deployed.
In this grimoire, Mislead is treated as a hybrid spell with a prototype delivery profile.
Canonical reference input: Mislead (spell).
## When To Use

- You need a honeypot, canary token, or decoy endpoint to detect unauthorized discovery or access attempts.
- The real requirement is defensive visibility into who comes looking for sensitive assets.
- You can isolate the decoy from production behavior and document the response path if it gets touched.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Define the monitoring objective, the expected adversary behavior, and what evidence the decoy should capture.
3. Design a believable false surface that is attractive enough to probe but isolated enough not to create production risk.
4. Instrument the decoy with alerts, logging, and tripwires that capture contact without escalating harm.
5. Specify the response playbook: who gets notified, how evidence is retained, and what actions are explicitly out of scope.
6. Return the decoy design with the ethical boundary conditions that make it defensive rather than abusive.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A decoy or honeypot design with isolation boundaries.
- A tripwire and alerting plan for when the false surface is touched.
- A response playbook covering evidence handling and operator follow-up.

## Pitfalls / Guardrails

- Call out the glue, permissions, or missing infrastructure before you imply this is fully operational.
- Use Mislead only for defensive detection, never for fraud, manipulation of legitimate users, or offensive entrapment.
- Keep fake data, decoy endpoints, and real systems cleanly separated so the spell cannot spill into production harm.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check which parts are concrete actions versus framing, so the user can tell what is real now.
- Check that any missing glue code, permissions, or future work is labeled before the skill is treated as ready.

## Example Invocation
```text
/mislead design a defensive decoy, honeypot, or canary setup that tells us who is snooping without creating collateral damage
```
