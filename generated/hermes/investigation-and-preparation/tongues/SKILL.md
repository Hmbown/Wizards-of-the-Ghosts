---
name: tongues
description: "Tongues is universal translation across languages, formats, and protocols. It can mean English to Spanish, JSON to XML, REST to GraphQL, Python to JavaScript, or one team's business vocabulary to another team's schema. The spell is not just about swapping tokens. It is about preserving meaning while crossing into a different representation. Good Tongues work makes both sides feel native. Bad Tongues work creates a smooth-looking mistranslation that fails at the edges."
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
      - investigation-and-preparation
      - analysis
      - discovery
      - translation
      - preflight
---
# Tongues
Make unlike systems understand the same sentence.
## What This Skill Does
Tongues is universal translation across languages, formats, and protocols. It can mean English to Spanish, JSON to XML, REST to GraphQL, Python to JavaScript, or one team's business vocabulary to another team's schema. The spell is not just about swapping tokens. It is about preserving meaning while crossing into a different representation. Good Tongues work makes both sides feel native. Bad Tongues work creates a smooth-looking mistranslation that fails at the edges.
In this grimoire, Tongues is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Tongues (spell).
## When To Use

- You need to translate between human languages, programming languages, data formats, or protocol styles.
- Two systems or teams mean roughly the same thing but encode it in incompatible ways.
- You need a faithful bridge, not a lossy paraphrase that only works on the happy path.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Define the source and target dialects, including the meaning that must survive the crossing.
3. Map concepts, structures, and edge cases rather than translating token-by-token.
4. Test the translation on representative examples and identify where fidelity is perfect, approximate, or impossible.
5. Return the translated artifact with notes on equivalence, lossiness, and any adapter logic still required.
6. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A translated artifact in the target language, format, or protocol.
- A concept map showing how source meanings land on the destination side.
- A list of lossy edges, incompatibilities, or adapter code still needed.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Do not claim literal one-to-one equivalence when the target system lacks the source concept.
- Preserve semantics first; surface-level fluency is not enough if the meaning has drifted.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/tongues translate this language, format, or protocol into the target form while telling me exactly what meaning survives and what gets lost
```
