# Wizards of the Ghosts

`wizardsoftheghosts` turns D&D spells and skills into practical AI skills.

The working premise is simple: as of March 8, 2026, some "magic" is already real if you reinterpret it as agent workflows, tool orchestration, device control, monitoring, research, translation, or probabilistic forecasting. This repo creates one source of truth that can emit three targets:

- Codex / OpenAI skill folders with `SKILL.md` and `agents/openai.yaml`
- Claude-compatible skill folders with `SKILL.md`
- OpenClaw-compatible skill folders with `SKILL.md` and optional OpenClaw frontmatter

## Scope

The first pass separates the world into three tiers:

- `shipping-now`: straightforward with current agents, tools, MCP servers, and automations
- `prototype`: plausible now, but needs custom glue, plugins, webhooks, or device bridges
- `speculative`: interesting idea, but not yet cleanly operational in a safe way

It also separates spell behavior by interpretation:

- `metaphorical`: the skill preserves the intent, not the literal fantasy effect
- `hybrid`: mostly practical, with a light theatrical wrapper
- `literal`: tries to cause a directly analogous real-world effect

## Canon Strategy

The repo keeps two datasets:

- `catalog/canon.json`: generated from official public D&D pages
- `catalog/blueprints.json`: the actual AI reinterpretations we want to build

As verified on March 8, 2026, the current scraper resolves:

- 18 core skills from the official 2024 Free Rules "Playing the Game" page
- 109 public spell names from the D&D Beyond Basic Rules spells index

Why the split:

- The 2024 Free Rules skills page exposes the skill list cleanly.
- The public `free-rules/spells` page currently behaves more like rules text than a clean spell index, while the public Basic Rules spells page still exposes a parseable list of spell names.
- That makes the current spell canon seed a pragmatic public-source baseline, not necessarily the final edition-complete corpus.

## Repository Layout

- `catalog/blueprints.json`: hand-authored spell and skill reinterpretations
- `catalog/blueprints.schema.json`: schema for blueprint entries
- `catalog/canon.json`: generated canonical source list
- `scripts/sync-canon.mjs`: scrapes official public source pages into `catalog/canon.json`
- `scripts/render-skills.mjs`: emits provider-specific skill folders into `generated/`
- `generated/openai/`: Codex/OpenAI-ready skill folders
- `generated/claude/`: Claude-ready skill folders
- `generated/openclaw/`: OpenClaw-ready skill folders

## Current State

The repo now has full bespoke coverage for the current public canon:

- `127/127` bespoke blueprint entries in `catalog/blueprints.json`
- `0` remaining stubs
- `345` rendered provider-specific skill folders under `generated/`
- `127` Linear-ready seed entries in `catalog/linear-seed.json` and `catalog/linear-seed.csv`

The original hand-written entries are still the "showcase" set that define the tone and quality bar for the broader generated manifest.

## Current Showcase Set

The initial blueprints lean toward "usable now" while leaving room for weirdness:

- `detect-magic`
- `mage-hand`
- `identify`
- `comprehend-languages`
- `glyph-of-warding`
- `foresight`
- `thunderwave`
- `investigation`
- `stealth`
- `persuasion`

OpenClaw is a good fit for the software-first set because its skills are AgentSkills-compatible `SKILL.md` folders. The immediate OpenClaw candidates are the skills that mostly need instructions and existing tools: `detect-magic`, `identify`, `comprehend-languages`, `mage-hand`, `glyph-of-warding`, `investigation`, `stealth`, and `persuasion`.

## Commands

```bash
npm run sync:canon
npm run expand:blueprints
npm run build:skills
npm run export:linear
npm run bootstrap
npm run install:codex-skills
```

`npm run install:codex-skills` symlinks every folder in `generated/openai/` into `~/.codex/skills` (or `$CODEX_HOME/skills`) so Codex can discover the spellbook as local skills. Restart Codex after running it.

## Next Steps

1. Upgrade the best entries from solid bespoke coverage to higher-polish showcase quality.
2. Keep the Linear export and sync path clean and idempotent as naming and labeling conventions evolve.
3. Introduce evaluation harnesses for risky skills, especially anything literal or device-connected.
