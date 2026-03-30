---
name: arcana
description: "Explain how a system, protocol, or technology actually works under the hood — beyond what the documentation says. Use when debugging requires understanding underlying mechanisms, when architecture decisions need deep technical context, or when you need to distinguish documented behavior from actual behavior."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - skill
      - shipping-now
      - metaphorical
      - investigation-and-preparation
      - analysis
      - discovery
      - translation
      - preflight
---
# Arcana

Explain how a system, protocol, or technology actually works under the hood — beyond what the documentation says.

## When To Use

- A technical system needs to be understood at a level deeper than its documentation provides (e.g., "why does this API return 429 after only 50 requests when the docs say 100?").
- You need to explain how something **actually works** — not what it claims to do, but what it does.
- A debugging or architecture question requires knowledge of underlying mechanisms: wire protocols, memory layout, consensus algorithms, garbage collection behavior.

## Procedure

1. **Identify the target.** Name the specific system, protocol, library, or technology to analyze. State what level of depth is needed (e.g., "how does the connection pool work" vs. "what happens at the TCP level").

2. **Gather evidence.** Use available tools to observe actual behavior:
   - Read source code if available: `grep -r "retry" src/http/` to find retry logic.
   - Check runtime behavior: `strace`, `tcpdump`, `curl -v`, or debug logs.
   - Compare docs vs. reality: read the official docs, then verify claims against code or experiments.
   - Review changelogs and issues for undocumented behavior changes.

3. **Explain the mechanism.** Provide a layered explanation:
   - **Surface**: what the docs say it does.
   - **Mechanism**: how it actually implements that (data structures, algorithms, protocols).
   - **Edge cases**: where the mechanism diverges from the documented behavior.
   - **Implications**: what follows from the mechanism that is not obvious from the API surface.

4. **Tag confidence levels.** For each claim, mark it:
   - **Documented**: stated in official docs or specs.
   - **Observed**: verified through code reading, testing, or instrumentation.
   - **Inferred**: logical conclusion from the mechanism, not directly verified.

## Deliverables

- A mechanistic explanation of how the system actually works, layered from surface to internals.
- Non-obvious implications, edge cases, or failure modes that follow from the mechanism.
- Confidence tags on each claim: documented, observed, or inferred.

## Pitfalls / Guardrails

- Do not confuse documentation with behavior. The docs say what it *should* do; arcana reveals what it *does*.
- Clearly separate established knowledge from speculation when reasoning about undocumented behavior.
- Do not over-speculate. If you cannot verify a claim, say so explicitly rather than presenting inference as fact.
- Stay at the depth the user needs. Not every question requires a kernel-level explanation.

## Example

```
User: /arcana Why does our Redis cluster occasionally return stale data for
      about 2 seconds after a write, even though we are using WAIT?

Agent: Surface: Redis WAIT blocks until N replicas acknowledge the write.
       The docs imply strong consistency after WAIT returns.

       Mechanism (observed): WAIT only guarantees that replicas received the
       write in their replication buffer. It does NOT guarantee the replica
       has applied it to its keyspace. If a client reads from a replica
       immediately after WAIT returns, the replica may still be processing
       the replication stream.

       Edge case: under high replication lag (>1s buffer), WAIT returns
       successfully but reads to replicas see stale data for the duration
       of the lag. This is documented in a Redis GitHub issue (#8029) but
       not in the main WAIT docs.

       Implication: if you need read-after-write consistency, either:
       (a) read from the primary, or
       (b) use WAIT + a client-side delay equal to observed replication lag.

       Confidence:
       - WAIT semantics: documented (Redis WAIT spec)
       - Replication buffer vs. keyspace gap: observed (tested with
         redis-cli DEBUG SLEEP on replica)
       - GitHub issue #8029: documented (linked)
       - Workaround: inferred (not officially recommended)
```
