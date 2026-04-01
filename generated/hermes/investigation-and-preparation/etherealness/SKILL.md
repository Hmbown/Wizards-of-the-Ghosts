---
name: etherealness
description: "Etherealness is observational only. It answers \"what is happening?\" or \"what would happen?\" without changing anything. The system under study continues normally; you add a ghost layer that watches, mirrors, or dry-runs without becoming part of the live mutation path."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - prototype
      - metaphorical
      - investigation-and-preparation
      - analysis
      - discovery
      - translation
      - preflight
---
# Etherealness
Walk through the walls of a system without leaving fingerprints.
## What This Skill Does
Etherealness is observational only. It answers "what is happening?" or "what would happen?" without changing anything. The system under study continues normally; you add a ghost layer that watches, mirrors, or dry-runs without becoming part of the live mutation path.
In this grimoire, Etherealness is treated as a metaphorical spell with a prototype delivery profile.
Canonical reference input: Etherealness (spell).
## When To Use

- You need to observe production-like behavior without writing to the live system.
- A dry run, shadow deployment, or mirrored environment would answer the question more safely than direct experimentation.
- You want to inspect effects first and decide later whether crossing fully into action is justified.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify the least invasive observation surface that still answers the question. Prefer: existing metrics/logs → read replicas → shadow deployments → mirrored traffic. Escalate invasiveness only when necessary.
3. Define the trust boundary. Explicitly state what the ghost view can prove and what it cannot. Dry runs don't capture live contention. Read replicas may lag. Mirrored traffic at 1% doesn't prove behavior at 100%.
4. Return three deliverables:
5. The observation setup plan (what to deploy, where, how to connect)
6. Findings you can safely gather before acting
7. A caveat list: what ghost mode cannot prove and what requires real execution to validate
8. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A read-only or shadow-observation setup plan.
- A list of findings you can gather safely before acting.
- A caveat list for what ghost mode cannot prove.

## Pitfalls / Guardrails

- Call out the glue, permissions, or missing infrastructure before you imply this is fully operational.
- The observation itself must not become the problem. If your ghost layer adds measurable latency, consumes significant resources, or creates a new data liability, you've violated the spell. Design for lightweight passivity.
- Do not use for: Permanent logging/auditing — storing request bodies, headers, auth tokens for compliance. Etherealness is ephemeral; permanent storage is a different concern.
- Do not use for: Active interception/modification — rewriting responses, hotfix proxies, real-time traffic manipulation. Etherealness never modifies.
- Do not use for: External monitoring/scrying — watching competitor websites, market prices, third-party systems you don't control.
- Do not use for: Prediction/forecasting — crystal ball dashboards, failure prediction, trend extrapolation. Etherealness observes what is or what would be, not what will be.
- Do not use for: Concealment/invisibility — hiding services from discovery, making things undetectable. Etherealness is about seeing, not being unseen.
- Do not use for: Human surveillance — watching coworkers' screens, monitoring people. Etherealness is for systems, not people.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.
- Check that any missing glue code, permissions, or future work is labeled before the skill is treated as ready.

## Example Invocation
```text
/etherealness show me how to inspect this system in read-only ghost mode and tell me what that view can and cannot prove
```
