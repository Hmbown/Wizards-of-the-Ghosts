---
name: tongues
description: "Tongues is universal translation across languages, formats, and protocols. It can mean English to Spanish, JSON to XML, REST to GraphQL, Python to JavaScript, or one team's business vocabulary to another team's schema. The spell is not just about swapping tokens. It is about preserving meaning while crossing into a different representation. Good Tongues work makes both sides feel native. Bad Tongues work creates a smooth-looking mistranslation that fails at the edges."
user-invocable: true
---

# Tongues

Make unlike systems understand the same sentence.

## Overview

Tongues is interpreted here as a metaphorical spell with a shipping-now execution model.

Canonical source: Tongues (spell)

Provider target: OpenClaw

## When To Use

- You need to translate between human languages, programming languages, data formats, or protocol styles.
- Two systems or teams mean roughly the same thing but encode it in incompatible ways.
- You need a faithful bridge, not a lossy paraphrase that only works on the happy path.

## Workflow

1. Define the source and target dialects, including the meaning that must survive the crossing.
2. Map concepts, structures, and edge cases rather than translating token-by-token.
3. Test the translation on representative examples and identify where fidelity is perfect, approximate, or impossible.
4. Return the translated artifact with notes on equivalence, lossiness, and any adapter logic still required.

## Deliverables

- A translated artifact in the target language, format, or protocol.
- A concept map showing how source meanings land on the destination side.
- A list of lossy edges, incompatibilities, or adapter code still needed.

## Guardrails

- Do not claim literal one-to-one equivalence when the target system lacks the source concept.
- Preserve semantics first; surface-level fluency is not enough if the meaning has drifted.

## Default Invocation

Use $tongues to translate this language, format, or protocol into the target form while telling me exactly what meaning survives and what gets lost.

