---
name: attune
description: "In D&D, attunement is how you bond with a magic item so it works specifically for you. The real-world version is workflow profiling: the grimoire interviews you about your stack, your systems, your automation surface, and your priorities — then generates a personalized spell loadout, category weights, and domain vocabulary so routing, optimization, and every subsequent spell invocation is tuned to your actual work instead of generic defaults."
user-invocable: true
---

# Attune

Bond this spellbook to your workflow so every spell knows your stack, your tools, and your priorities.

## Overview

Attune is interpreted here as a metaphorical skill with a shipping-now execution model.

Canonical source: Attune (skill)

Provider target: OpenClaw

## When To Use

- You just installed the grimoire and want it configured to your workflow before using anything else.
- Your stack, tools, or priorities have changed and you want the spellbook to re-learn your context.
- You want to generate a personalized spell loadout instead of browsing 122 entries blind.

## Workflow

1. Interview the user about their stack: languages, frameworks, infrastructure, deployment targets, and daily tools.
2. Map their workflow surface: what they automate, what they monitor, what breaks, what they communicate about, and what they wish was easier.
3. Score each grimoire category against their stated workflow to produce category weights.
4. Select a prioritized spell loadout — the 10-15 spells most likely to be useful immediately, plus stretch picks they might not have considered.
5. Write the attunement profile to ~/.hermes/attunement.json (or $HERMES_HOME/attunement.json) so the DSPy router and future spell invocations can read it.
6. Optionally trigger GEPA re-optimization of the top spells using the user's domain vocabulary as training signal.

## Deliverables

- A personalized attunement profile written to disk.
- A prioritized spell loadout with reasons for each pick.
- Category weights so the DSPy router biases toward relevant shelves.
- A shortlist of spells worth GEPA-optimizing for the user's domain.

## Guardrails

- Do not assume the user's stack from the current directory alone — ask, then verify.
- Do not overwrite an existing attunement without confirmation.
- Keep the interview conversational and short — five good questions beats twenty generic ones.

## Default Invocation

Use $attune to configure this spellbook to my workflow — interview me about my stack and generate a personalized spell loadout.

