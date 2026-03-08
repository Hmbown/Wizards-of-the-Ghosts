# Handoff — Session 2026-03-08 (exploration pass)

## Product Pivot: OpenClaw-Only

The spellbook is now **OpenClaw-only**. The multi-provider strategy (Claude, OpenAI, OpenClaw) has been replaced with a single target: distributable OpenClaw skills that people install and configure for their setup.

### Why
- Claude slash commands and Codex skills were internal tooling, not a distributable product
- OpenClaw has 13,729+ community skills on ClawHub and 68K+ users — that's the distribution surface
- Skills that declare real `requires.env` and `requires.bins` connect to actual devices and services
- "Configurable for people" = users set their env vars, matching spells activate

### Architecture
- **122 OpenClaw skills** generated (5 refusal spells excluded: dominate-person, dominate-monster, modify-memory, geas, compulsion)
- **13 grounded skills** with real integration requirements (Home Assistant, Slack)
- **109 cognitive skills** with no hard requirements (always available)
- `.claude/commands/` symlink to `generated/openclaw/` for internal dev use
- Renderer produces OpenClaw output only

## What Was Done This Session

### Phase 5: Exploration and pivot
1. **Detect Magic** — scanned the repo's own capability surfaces
2. **Foresight** — evaluated the "no git repo" risk → initialized git immediately
3. **Investigation** — analyzed which spells provide real cognitive scaffolding vs. no-ops
4. **Fear** — pre-mortem on the project → identified "text-only spells can't do anything" as the kill shot
5. **OpenClaw research** — discovered real integration surfaces (Home Assistant, Slack, webhooks, CLIs)
6. **Product pivot** — dropped Claude/OpenAI targets, went OpenClaw-only with real-world grounding
7. **Grounded 13 skills** with Home Assistant and Slack integration requirements
8. **Added emojis** to all 122 skills for ClawHub listings
9. **Codex tier audit** — classified all 127 spells as REAL_MAGIC, LIGHT_SCAFFOLDING, or NO_OP

### Quality findings
The investigation identified three tiers of spell quality:
- **Real Magic** (~95 spells) — change HOW the agent thinks (mode changes, specific techniques, novel deliverable shapes)
- **Light Scaffolding** (~29 spells) — useful framing but moderate behavioral change
- **No-Op** (~3 spells: investigation, persuasion, message) — labels for things the agent already does

The key mechanism: Real Magic spells either (1) impose a mode change, (2) apply a specific technique, (3) constrain against defaults, or (4) produce novel deliverable shapes.

## Current State

### The spellbook
- **122 OpenClaw skills** with emojis, ready for ClawHub
- **13 grounded** with real integration requirements
- **5 excluded** (deliberate refusals)
- Git initialized with 4 commits on master

### Grounded skills

| Integration | Skills | Env Vars |
|---|---|---|
| Home Assistant | dancing-lights, light, sleep, awaken, glyph-of-warding, scrying | HA_URL, HA_TOKEN |
| Slack | sending, message, silence, magic-mouth, dream | SLACK_TOKEN |
| CLI (no env) | knock, detect-magic | (system tools) |

### Integration map (not yet grounded)

| Surface | Candidate Skills |
|---|---|
| Home Assistant | stinking-cloud (area denial), guards-and-wards (security), thunderwave (dramatic actions) |
| Slack | animal-messenger (async delivery), tongues (translation) |
| Email | dream (scheduled digests), animal-messenger (async) |
| Webhooks | programmed-illusion (triggered demos), symbol (policy enforcement) |
| Calendar | mordenkainen-s-sword (scheduled workers), enhance-ability (context priming) |

## Next Priorities

### Priority 1: Setup experience
Create a `setup-grimoire` meta-skill that walks users through configuring their integrations. Should detect available env vars and show which spells are active.

### Priority 2: Ground more integration skills
Extend the grounding to webhooks, email, and calendar surfaces. Target: 25-30 grounded skills total.

### Priority 3: ClawHub packaging
Research ClawHub batch publishing. Create the metadata and directory structure needed to publish the full skill pack.

### Priority 4: Quality audit of cognitive skills
The ~29 LIGHT_SCAFFOLDING skills need sharpening. The ~3 NO_OP skills need either real cognitive scaffolding or removal.

### Priority 5: README refresh
Update README.md to describe the OpenClaw skill pack product, not the multi-provider template generator.

## Files Changed (This Session)

- `catalog/blueprints.json` — 31 entries added to OpenClaw, 13 grounded with integrations, all 122 got emojis
- `catalog/blueprints.schema.json` — added requires, primaryEnv, emoji to openclaw schema
- `scripts/render-skills.mjs` — simplified to OpenClaw-only output
- `generated/openclaw/` — 122 skill folders with SKILL.md files
- `.claude/commands/` — relinked to OpenClaw output, removed 5 refusal spell symlinks
- `.gitignore` — added generated/ to ignore list
- `HANDOFF.md` — this file

## How To Continue

```bash
# Verify current state
npm run build:skills

# After editing blueprints.json
npm run build:skills

# Check a grounded skill
cat generated/openclaw/dancing-lights/SKILL.md
```
