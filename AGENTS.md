# AGENTS.md

## Mission

`wizardsoftheghosts` turns D&D spells and skills into practical AI skills across three targets:

- Codex / OpenAI
- Claude
- OpenClaw

The point is not parody for its own sake. The point is to treat fantasy magic as a design language for real AI capabilities: workflow orchestration, translation, monitoring, reasoning, simulation, device control, and careful acts of software manipulation.

## Source Of Truth

Always work from these files in this order:

1. `catalog/canon.json`
   Generated public canon list.
2. `catalog/blueprints.json`
   Actual reinterpretation layer.
3. `scripts/render-skills.mjs`
   Provider-specific output generator.
4. `catalog/linear-seed.json` and `catalog/linear-seed.csv`
   Linear backlog export artifacts.

Never hand-edit generated output in `generated/` unless you are explicitly testing a change to the renderer.

## Core Model

Each entry must preserve these axes:

- `reality_tier`
  - `shipping-now`
  - `prototype`
  - `speculative`
- `literalness`
  - `metaphorical`
  - `hybrid`
  - `literal`

Use `shipping-now` when the skill is actually operational today with current tools.
Use `prototype` when the idea is plausible now but needs glue code, plugins, webhooks, or device boundaries.
Use `speculative` when the idea is interesting but not honestly deliverable yet.

## Workflow

Default local workflow:

```bash
npm run sync:canon
npm run expand:blueprints
npm run build:skills
npm run export:linear
```

Or just:

```bash
npm run bootstrap
```

## Project Codex Skills

This repo ships project-local Codex skills under `generated/openai/`.

- The workspace-local install target is `.codex/skills/`.
- Run `CODEX_HOME=$PWD/.codex npm run install:codex-skills` to mirror every generated OpenAI skill into that local Codex skill directory.
- If a user invokes `$skill-name` and `.codex/skills/<skill-name>/SKILL.md` exists, treat it as a local project skill and follow it.
- The generated skill folders are build artifacts. Do not hand-edit them; update the renderer or blueprints instead, then rebuild and reinstall.

## Quality Bar

Do not let the spellbook collapse into generic AI slop.

Every good entry should have:

- a clear real-world interpretation
- a reason the spell metaphor is still meaningful
- a crisp boundary between what is real now and what is theatrical or speculative
- obvious guardrails when the skill can influence people, actuate systems, or trigger devices

Preserve the hand-written showcase entries as the tone reference. Bulk-generated entries are allowed to be rough, but they should move toward the showcase quality over time.

## Role Split

When multiple agents are involved, use this split:

- Claude: creative lead, product direction, naming, metaphor quality, experience design, spell identity, prioritization
- Codex agents: implementation, schema updates, generators, rendering, backlog export, Linear syncing, testable repo work

If a task is mostly backend plumbing, generation logic, or repo mechanics, push it to Codex.
If a task is mostly about what a spell should mean, how bold or literal it should be, or which entries deserve bespoke treatment, keep it at the creative-director layer first.

## Editing Rules

- Keep `catalog/canon.json` machine-generated.
- Keep `catalog/blueprints.json` valid against `catalog/blueprints.schema.json`.
- Prefer improving archetypes and renderer logic over manually patching hundreds of generated rows.
- Treat OpenClaw as a stricter target for software-first skills.
- Be conservative with OpenClaw for coercive, deceptive, dangerous, or device-linked skills.

## Linear

The Linear project is `wizardsoftheghosts`.

Current structure:

- architecture and policy issues live at the project root
- per-spell and per-skill issues are seeded under the manifest epic

Do not flood Linear with duplicate issues. Use exported seed artifacts or an idempotent sync path.

## Immediate Priority

The repo has full public-canon coverage already. The next real work is quality:

1. upgrade the best spells from stub to bespoke entries
2. sharpen the archetype system so the generated entries feel intentional
3. define stronger safety policy for literal and influence-heavy skills
4. keep OpenClaw focused on the software-first subset
