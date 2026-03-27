---
name: mirage-arcane
description: "Build a high-fidelity simulation, digital twin, or synthetic test environment so realistic that systems under test cannot distinguish it from production. Use when stress testing, training, or scenario planning requires production-grade fidelity with strong operator labeling and kill switches to prevent simulation-reality confusion."
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
      - simulation-and-staging
      - simulation
      - staging
      - mockup
      - testing
---
# Mirage Arcane

Build a high-fidelity simulation or digital twin that is functionally indistinguishable from the real system.

## When To Use

- Stress testing requires a simulation that services or integrations cannot distinguish from production.
- You need a digital twin or synthetic environment for realistic scenario planning or failure injection.
- Training scenarios must be immersive enough that participants treat them as real (e.g., incident response drills).

## Procedure

1. **Define fidelity requirements.** For each layer of the system, decide:
   - **Full fidelity**: must behave identically to production (e.g., API responses, latency profiles, error rates).
   - **Stub fidelity**: returns realistic data but is not backed by a real service (e.g., mock payment gateway).
   - **Out of scope**: not simulated, replaced with a clear boundary marker.

2. **Build the simulation environment.** Choose an approach based on scope:
   - **Docker Compose replica**: mirror production services locally with seeded data.
     ```yaml
     # docker-compose.mirage.yml
     services:
       api:
         image: myapp:latest
         environment:
           - DATABASE_URL=postgres://mirage:mirage@db:5432/mirage
           - MIRAGE_MODE=true  # operator-visible label
       db:
         image: postgres:16
         volumes:
           - ./seed/mirage-data.sql:/docker-entrypoint-initdb.d/seed.sql
     ```
   - **Cloud sandbox**: provision a separate environment (e.g., `terraform workspace new mirage`) with production-like config but isolated networking.
   - **Traffic replay**: capture production traffic with `tcpdump` or a service mesh, replay against the simulation with `goreplay` or similar.

3. **Implement operator labeling.** The simulation must be clearly marked for operators even if opaque to systems under test:
   - Set an environment variable (`MIRAGE_MODE=true`) checked by all logging and alerting.
   - Prefix all synthetic data with a marker (e.g., `MIRAGE-` prefix on order IDs).
   - Add a banner or header to any UI exposed during the simulation.

4. **Add a kill switch.** Provide a way to tear down the simulation immediately:
   - `docker compose -f docker-compose.mirage.yml down --volumes`
   - A CI workflow with a manual trigger that destroys the sandbox.
   - A feature flag that disables the mirage environment.

5. **Run the simulation and capture data.** Record metrics, logs, and behavioral observations. Tag all captured data as synthetic.

6. **Debrief.** Answer: what did the simulation reveal that a lower-fidelity test would have missed? Document findings and tear down the environment.

## Deliverables

- A simulation environment with documented fidelity levels per component.
- Operator-level labeling (env vars, data prefixes, UI banners) and a kill switch.
- Behavioral data from the simulation run, clearly tagged as synthetic.
- A debrief document summarizing findings and actions.

## Pitfalls / Guardrails

- Deep simulations **must always have a kill switch** and clear operator-level labeling, even if opaque to test subjects.
- Never deploy without a **debrief phase**. The risk of confusing simulation with reality scales with fidelity.
- If a simulation generates data that could be mistaken for real data, it must be **destroyed or clearly marked** after the exercise.
- Call out missing infrastructure or glue code before implying the simulation is fully operational — this is a **prototype-tier** skill.

## Example

```
User: /mirage-arcane We need to test how our payment service handles a
      spike of 10x normal traffic. Build a simulation that stresses the
      real service dependencies without touching production data.

Agent: Here is the mirage plan:

       Fidelity map:
       - Payment API: full fidelity (Docker replica with production config)
       - Stripe integration: stub fidelity (mock server returning realistic
         responses, no real charges)
       - Database: full fidelity (Postgres with 30-day production snapshot,
         all PII replaced with synthetic data)
       - Monitoring: full fidelity (Datadog agent with MIRAGE- tag prefix)

       Environment: docker-compose.mirage.yml with MIRAGE_MODE=true.
       All synthetic order IDs prefixed with MIRAGE-.

       Load test: k6 script ramping from 1x to 10x over 15 minutes.

       Kill switch: `make mirage-down` tears down all containers and
       deletes volumes.

       Shall I generate the docker-compose file and k6 script?
```
