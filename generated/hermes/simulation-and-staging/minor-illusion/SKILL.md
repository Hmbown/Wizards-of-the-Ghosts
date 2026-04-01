---
name: minor-illusion
description: "Minor Illusion produces artifacts that are explicitly labeled as disposable and exist only to provoke reaction. If the artifact could be mistaken for finished work, you're casting the wrong spell."
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
      - simulation-and-staging
      - simulation
      - staging
      - mockup
      - testing
---
# Minor Illusion
Conjure a quick sketch of an idea — just real enough to communicate.
## What This Skill Does
Minor Illusion produces artifacts that are explicitly labeled as disposable and exist only to provoke reaction. If the artifact could be mistaken for finished work, you're casting the wrong spell.
In this grimoire, Minor Illusion is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Minor Illusion (spell).
## When To Use

- Activate this spell when the user needs a quick, low-fidelity artifact to make an idea visible for discussion. The goal is communication speed, not quality.
- Words: "sketch", "mockup", "wireframe", "rough", "placeholder", "throwaway", "napkin", "lorem ipsum", "fake data", "just to communicate", "before we build", "just enough to"
- Patterns: User describes a concept that needs to be made concrete for alignment, comparison, or stakeholder conversation
- Timeframe implied: minutes, not hours; disposable, not shippable
- Explicit statements: "don't overthink it", "this is just to start the conversation", "label it as a sketch"

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify the single concept that needs to be made visible. If there are multiple, pick the one blocking the conversation.
3. Pick the cheapest format that communicates the idea: ASCII layout, text mockup, rough diagram, placeholder code, or described wireframe. Do not reach for tools or frameworks.
4. Create it fast — spend minutes, not hours. Use lorem ipsum, fake values, bracketed descriptions like [logo here]. Fidelity is failure here.
5. Label it explicitly as a sketch, mockup, or throwaway. Add a header like "ROUGH SKETCH — NOT FOR PRODUCTION" or similar.
6. Present it for reaction, not approval. Ask what feels wrong or missing. Use the response to decide whether to invest in a real version.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- The artifact itself (sketch, wireframe, placeholder, diagram)
- A clear label: "This is a disposable sketch, not a commitment"
- One sentence on what question this sketch is meant to answer

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Do NOT activate when:
- Do not use for: The user asks for a working prototype with validation, state, or API calls → that's a different spell (higher fidelity, shippable)
- Do not use for: The user wants a small code change (update a button color, fix a typo) → that's a direct edit, not a sketch
- Do not use for: The user requests a complete design system or production-ready component library → that's a build spell, not an illusion
- Do not use for: The user asks for visual deception (fake loading indicators, spoofed identities, dark patterns) → that's manipulation, not communication
- Do not use for: The user wants physical organization (desk setup, cable management) → literal, not metaphorical

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/minor-illusion quickly sketch an idea — a wireframe, placeholder, rough diagram, or throwaway prototype — just real enough to get a reaction
```
