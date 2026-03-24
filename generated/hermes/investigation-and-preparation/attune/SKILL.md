---
name: attune
description: "In D&D, attunement is how you bond with a magic item so it works specifically for you. The real-world version is workflow profiling: the grimoire interviews you about your stack, your systems, your automation surface, and your priorities — then generates a personalized spell loadout, category weights, and domain vocabulary so routing, optimization, and every subsequent spell invocation is tuned to your actual work instead of generic defaults."
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
# Attune
Bond this spellbook to your workflow so every spell knows your stack, your tools, and your priorities.
## What This Skill Does
In D&D, attunement is how you bond with a magic item so it works specifically for you. The real-world version is workflow profiling: the grimoire interviews you about your stack, your systems, your automation surface, and your priorities — then generates a personalized spell loadout, category weights, and domain vocabulary so routing, optimization, and every subsequent spell invocation is tuned to your actual work instead of generic defaults.
In this grimoire, Attune is treated as a metaphorical skill with a shipping-now delivery profile.
Canonical reference input: Attune (skill).
## When To Use

- You just installed the grimoire and want it configured to your workflow before using anything else.
- Your stack, tools, or priorities have changed and you want the spellbook to re-learn your context.
- You want to generate a personalized spell loadout instead of browsing 122 entries blind.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Interview the user about their stack: languages, frameworks, infrastructure, deployment targets, and daily tools.
3. Map their workflow surface: what they automate, what they monitor, what breaks, what they communicate about, and what they wish was easier.
4. Score each grimoire category against their stated workflow to produce category weights.
5. Select a prioritized spell loadout — the 10-15 spells most likely to be useful immediately, plus stretch picks they might not have considered.
6. Write the attunement profile to ~/.hermes/attunement.json (or $HERMES_HOME/attunement.json) so the DSPy router and future spell invocations can read it.
7. Optionally trigger GEPA re-optimization of the top spells using the user's domain vocabulary as training signal.
8. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A personalized attunement profile written to disk.
- A prioritized spell loadout with reasons for each pick.
- Category weights so the DSPy router biases toward relevant shelves.
- A shortlist of spells worth GEPA-optimizing for the user's domain.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Do not assume the user's stack from the current directory alone — ask, then verify.
- Do not overwrite an existing attunement without confirmation.
- Keep the interview conversational and short — five good questions beats twenty generic ones.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/attune configure this spellbook to my workflow — interview me about my stack and generate a personalized spell loadout
```
