```
    ╔═══════════════════════════════════════════════════╗
    ║                                                   ║
    ║    W I Z A R D S   O F   T H E   G H O S T S     ║
    ║                                                   ║
    ║      123 spells for the ghost in the machine      ║
    ║                                                   ║
    ╚═══════════════════════════════════════════════════╝
```

**A skill pack that teaches your AI agent 123 real capabilities — named after fantasy spells.**

`Detect Magic` scans a repo for hidden automation. `Feather Fall` turns a hard crash into a controlled descent. `Mage Hand` edits files with minimal blast radius. `Zone of Truth` forces sourced claims. These aren't jokes — they're procedural skills that install into [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (Hermes Agent) and become `/slash-commands` your agent actually uses.

The metaphor is the interface. The capabilities are real.

> Not affiliated with or endorsed by Wizards of the Coast. See [LEGAL.md](LEGAL.md).

---

## What This Is

This repo contains **123 AI agent skills** organized across **8 shelves**, generated from a structured catalog of reinterpreted D&D spell and skill names. Each skill is a procedural markdown document with YAML frontmatter that installs into Claude Code's skill system.

The skills cover: investigation, automation, monitoring, messaging, repair, staging, influence, and containment. They range from immediately practical (`shipping-now`) to exploratory (`prototype`), and from direct software operations (`literal`) to reasoning frameworks (`metaphorical`).

The pack also ships:
- A **DSPy router** (91.3% accuracy) that routes plain-English requests to the right shelf — you don't need to know spell names
- A **GEPA optimization forge** that uses the agent itself as the backend to sharpen individual spells against scored benchmarks
- A structured **attunement flow** that personalizes the spellbook to your specific stack and workflow

```
    ┌────────────────────────────────────────────────────────────────────┐
    │ Simulation (8)       Investigation (29)   Actions (19)            │
    │ Influence (18)       GHOST IN THE MACHINE Monitoring (17)         │
    │ Containment (10)     Repair (13)          Messaging (9)           │
    └────────────────────────────────────────────────────────────────────┘
```

---

## Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/Hmbown/Wizards-of-the-Ghosts.git
cd Wizards-of-the-Ghosts

# 2. Build and install skills into Claude Code
npm run bootstrap
npm run install:hermes-skills

# 3. Open Claude Code in any project
claude

# 4. Paste the wizard initiation prompt (one time)
#    Copy the contents of BECOME-A-WIZARD.md and paste it into the session.
#    This teaches the agent about its spellbook.

# 5. Cast your first spell
/detect-magic
```

That's it. After `/detect-magic` scans your project, run `/attune` to personalize the spellbook to your workflow.

---

## Prerequisites

- **Node.js ≥ 20** (for build scripts and install)
- **Claude Code** (the Hermes Agent runtime — skills install into `~/.hermes/skills/`)
- **npm** (ships with Node)

Optional, for DSPy/GEPA optimization work:
- **Python 3.10+** and **uv** (for the DSPy router and spell optimization forge)

---

## Install

### Standard install (into your default Claude Code skill directory)

```bash
npm run bootstrap          # Build everything from source
npm run install:hermes-skills   # Copy skills to ~/.hermes/skills/
```

### Workspace-local install (for testing)

```bash
npm run bootstrap
HERMES_HOME=$PWD/.hermes npm run install:hermes-skills
```

### What `bootstrap` does

It runs four steps in order:
1. `npm run sync:canon` — pulls the public canon list
2. `npm run expand:blueprints` — expands blueprint templates
3. `npm run build:skills` — renders skill markdown into `generated/hermes/`
4. `npm run export:linear` — exports the Linear backlog seed

### After install

Every skill becomes a `/slash-command` in Claude Code: `/forcecage`, `/true-seeing`, `/dream`, etc.

Skills are procedural markdown, not executable plugins. They work as reasoning modes, investigation checklists, and operating procedures. Skills that reference external systems (Home Assistant, Slack, APIs) only become operational if your environment already has those tools and credentials.

---

## How It Works

### The Spellbook

The core unit is a **skill**: a markdown document with YAML frontmatter that describes a specific AI capability. Skills live on **shelves** (categories) that group related capabilities.

**Source of truth:** `catalog/blueprints.json` → rendered by `scripts/render-skills.mjs` → installed from `generated/hermes/`

### The 8 Shelves

| Shelf | Count | When to reach for it |
| --- | --- | --- |
| **Investigation and Preparation** | 29 | You need to understand before you act |
| **Actions, Access, and Automation** | 19 | You need to change something precisely |
| **Monitoring and Protection** | 17 | You need to watch, guard, or add observability |
| **Messaging and Coordination** | 9 | You need the right message at the right place |
| **Repair and Recovery** | 13 | Something is already broken |
| **Simulation and Staging** | 8 | You need to mock, test, or rehearse first |
| **Influence and Behavior** | 18 | You're handling people, teams, or attention |
| **Containment and Intervention** | 10 | You need to box in blast radius or stop something |

### The DSPy Router

The repo includes a trained category router under `catalog/dspy/` that maps plain-English requests to the correct shelf.

- **91.3% accuracy** on held-out evaluation (95/104 correct)
- **+12.5pp** over the lexical baseline (78.8%)
- Routes from natural language — you describe what you need, and it finds the right shelf

This means you don't need to memorize 123 spell names. Say "I need to understand what this service does" and the router lands you on Investigation. Say "something is on fire" and it lands you on Repair.

### The GEPA Forge

GEPA is the spell optimization pipeline. It takes an individual spell, runs it against a gauntlet of test scenarios (positive examples, confusable neighbors, edge cases), scores it with a rubric, then rewrites the instruction text to score better.

Example: Forcecage went from 61.8% → 89.3% after a GEPA run. The optimized version is sharper about containment boundaries, outside-the-cage observation, and explicit release conditions.

The interesting part: **the agent is both the user of spells and the engine that optimizes them.** When someone runs `/attune`, the agent interviews them about their workflow, and can then GEPA-optimize their top spells using their domain vocabulary as training signal.

### The Attunement Flow

1. **`/detect-magic`** — Scan a project for hidden automation, tool hooks, and capability surfaces
2. **`/attune`** — Interview the user about their stack, generate a personalized spell loadout, and write an attunement profile
3. **Use spells naturally** — the DSPy router handles discovery from plain language

See [BECOME-A-WIZARD.md](BECOME-A-WIZARD.md) for the full initiation prompt.

---

## Best Entry Points

| | |
|---|---|
| 🔗 **[Attune](generated/hermes/investigation-and-preparation/attune/SKILL.md)** — Bond this spellbook to your workflow so every spell knows your stack, your tools, and your priorities. | 🔮 **[Detect Magic](generated/hermes/investigation-and-preparation/detect-magic/SKILL.md)** — Surface hidden AI affordances, agents, automations, and tool hooks before acting. |
| 🔍 **[Identify](generated/hermes/investigation-and-preparation/identify/SKILL.md)** — Explain what a mysterious file, service, workflow, or artifact actually does. | 🗺️ **[Comprehend Languages](generated/hermes/investigation-and-preparation/comprehend-languages/SKILL.md)** — Translate code, jargon, protocol surfaces, or human language into operational meaning. |
| 🕵️ **[Investigation](generated/hermes/investigation-and-preparation/investigation/SKILL.md)** — Follow evidence through a system until the hidden mechanism becomes legible. | 🖐️ **[Mage Hand](generated/hermes/actions-access-and-automation/mage-hand/SKILL.md)** — Manipulate files, records, and lightweight system state with precision and minimal blast radius. |
| 🔒 **[Forcecage](generated/hermes/containment-and-intervention/forcecage/SKILL.md)** — Contain untrusted code, agents, or operations inside a tested cage before anything leaves it. | 🛡️ **[Glyph of Warding](generated/hermes/monitoring-and-protection/glyph-of-warding/SKILL.md)** — Set monitors, watches, or trigger conditions that alert when a boundary is crossed. |
| 🌙 **[Dream](generated/hermes/messaging-and-coordination/dream/SKILL.md)** — Deliver the briefing before the recipient wakes up needing it. | 🪂 **[Feather Fall](generated/hermes/repair-and-recovery/feather-fall/SKILL.md)** — Turn a hard crash into a controlled descent. |

---

## Browse the Spellbook

### By intent

| If you want to... | Start here | Full shelf |
| --- | --- | --- |
| Figure out what you're looking at | [Detect Magic](generated/hermes/investigation-and-preparation/detect-magic/SKILL.md), [Identify](generated/hermes/investigation-and-preparation/identify/SKILL.md), [Investigation](generated/hermes/investigation-and-preparation/investigation/SKILL.md) | [Investigation and Preparation (29)](GRIMOIRE.md#investigation-and-preparation) |
| Change the system without a battleaxe | [Mage Hand](generated/hermes/actions-access-and-automation/mage-hand/SKILL.md), [Unseen Servant](generated/hermes/actions-access-and-automation/unseen-servant/SKILL.md), [Awaken](generated/hermes/actions-access-and-automation/awaken/SKILL.md) | [Actions, Access, and Automation (19)](GRIMOIRE.md#actions-access-and-automation) |
| Light up the black box | [Dancing Lights](generated/hermes/monitoring-and-protection/dancing-lights/SKILL.md), [Glyph of Warding](generated/hermes/monitoring-and-protection/glyph-of-warding/SKILL.md), [Scrying](generated/hermes/monitoring-and-protection/scrying/SKILL.md) | [Monitoring and Protection (17)](GRIMOIRE.md#monitoring-and-protection) |
| Get the right message to the right place | [Message](generated/hermes/messaging-and-coordination/message/SKILL.md), [Sending](generated/hermes/messaging-and-coordination/sending/SKILL.md), [Dream](generated/hermes/messaging-and-coordination/dream/SKILL.md) | [Messaging and Coordination (9)](GRIMOIRE.md#messaging-and-coordination) |
| Stop the bleeding | [Cure Wounds](generated/hermes/repair-and-recovery/cure-wounds/SKILL.md), [Feather Fall](generated/hermes/repair-and-recovery/feather-fall/SKILL.md), [Mending](generated/hermes/repair-and-recovery/mending/SKILL.md) | [Repair and Recovery (13)](GRIMOIRE.md#repair-and-recovery) |
| Mock it before you ship it | [Minor Illusion](generated/hermes/simulation-and-staging/minor-illusion/SKILL.md), [Major Image](generated/hermes/simulation-and-staging/major-image/SKILL.md), [Deception](generated/hermes/simulation-and-staging/deception/SKILL.md) | [Simulation and Staging (8)](GRIMOIRE.md#simulation-and-staging) |
| Handle people with care | [Calm Emotions](generated/hermes/influence-and-behavior/calm-emotions/SKILL.md), [Heroism](generated/hermes/influence-and-behavior/heroism/SKILL.md), [Fear](generated/hermes/influence-and-behavior/fear/SKILL.md) | [Influence and Behavior (18)](GRIMOIRE.md#influence-and-behavior) |
| Box in blast radius | [Forcecage](generated/hermes/containment-and-intervention/forcecage/SKILL.md), [Blindness/Deafness](generated/hermes/containment-and-intervention/blindness-deafness/SKILL.md), [Power Word Stun](generated/hermes/containment-and-intervention/power-word-stun/SKILL.md) | [Containment and Intervention (10)](GRIMOIRE.md#containment-and-intervention) |

### Deeper

- **[GRIMOIRE.md](GRIMOIRE.md)** — Full browse layer with featured shelf, intent paths, and linked category index with all 123 skills
- **[BECOME-A-WIZARD.md](BECOME-A-WIZARD.md)** — The initiation prompt that teaches your agent about its own spellbook
- **`generated/hermes/<category>/<skill>/SKILL.md`** — Individual skill documents (after `npm run build:skills`)
- **`catalog/blueprints.json`** — Source of truth for all skill definitions

---

## DSPy Router Setup

The DSPy router is optional — the spellbook works without it. But if you want natural-language shelf routing or want to run GEPA optimization:

```bash
# Set up Python environment
uv venv .venv
uv pip install --python .venv/bin/python -r requirements-dspy.txt

# Validate the pipeline (no LLM needed)
npm run dspy:validate

# Run baseline evaluation
npm run dspy:baseline

# Full DSPy compile + eval (requires an LLM backend)
# Use hermes/default to have the agent optimize its own spells:
export DSPY_MODEL=hermes/default
export DSPY_TEMPERATURE=0
export DSPY_MAX_TOKENS=4096
bash scripts/dspy_full_run.sh
```

See [`catalog/dspy/README.md`](catalog/dspy/README.md) and [`docs/dspy-router-runbook.md`](docs/dspy-router-runbook.md) for the full runbook.

---

## GEPA Spell Optimization

To optimize an individual spell:

```bash
# Optimize a spell against its benchmark gauntlet
npm run gepa:spell:optimize -- --slug detect-magic

# Evaluate results
npm run gepa:spell:eval -- --slug detect-magic

# If it's better, promote back to blueprints.json
npm run gepa:spell:promote -- --slug detect-magic

# Rebuild and verify
npm run build:skills
npm run verify
```

See [`docs/gepa-spell-optimization-spec.md`](docs/gepa-spell-optimization-spec.md) for the full contract.

---

## Verification

```bash
npm run verify
```

Checks generated Hermes and OpenClaw surfaces, then runs sandbox installs into temporary directories to catch packaging drift before release.

---

## Safety

The public skill surface intentionally refuses 5 spells that could model coercion or memory manipulation: `Compulsion`, `Dominate Monster`, `Dominate Person`, `Geas`, and `Modify Memory`.

Skills that touch influence, behavior, or containment include ethical guardrails and consent requirements in their procedures.

---

## Contributing

The source of truth is `catalog/blueprints.json`. Don't edit files in `generated/` — they're build artifacts.

To improve a skill:
1. Edit `catalog/blueprints.json`
2. Run `npm run build:skills`
3. Run `npm run verify`

To improve the rendering or install logic, work in `scripts/`.

For GEPA-backed improvements, see the [spell optimization spec](docs/gepa-spell-optimization-spec.md).

---

## License

Original code and writing: **CC0-1.0** (public domain dedication).

This does not grant rights in Wizards of the Coast IP, trademarks, logos, artwork, or official rules text. This is a free, unofficial fan project. See [LEGAL.md](LEGAL.md).
