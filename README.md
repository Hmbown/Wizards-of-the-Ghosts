```
    ╔═══════════════════════════════════════════════════╗
    ║                                                   ║
    ║    W I Z A R D S   O F   T H E   G H O S T S     ║
    ║                                                   ║
    ║      122 spells for the ghost in the machine      ║
    ║                                                   ║
    ╚═══════════════════════════════════════════════════╝
```

A skill pack for [Hermes Agent](https://github.com/anthropics/hermes) that turns D&D spell and skill names into real agent operating modes — investigation, containment, repair, messaging, automation, monitoring, simulation, and tightly scoped intervention.

Not affiliated with or endorsed by Wizards of the Coast.

## Start Here

Pick the skill that matches the job. You don't need to know the spell name — just scan the one-liners.

| Skill | What it actually does |
| --- | --- |
| 🔮 [Detect Magic](generated/hermes/investigation-and-preparation/detect-magic/SKILL.md) | Scan a repo, system, or workflow for hidden AI agents, automations, and tool hooks before you touch anything. |
| 🔒 [Forcecage](generated/hermes/containment-and-intervention/forcecage/SKILL.md) | Run untrusted code, agents, or operations inside a tested sandbox. Nothing leaves the cage until you verify it. |
| 🔍 [Identify](generated/hermes/investigation-and-preparation/identify/SKILL.md) | Explain what a mysterious file, service, or artifact actually does. |
| 🖐️ [Mage Hand](generated/hermes/actions-access-and-automation/mage-hand/SKILL.md) | Manipulate files, records, and system state with precision and minimal blast radius. |
| 🗺️ [Comprehend Languages](generated/hermes/investigation-and-preparation/comprehend-languages/SKILL.md) | Translate code, jargon, protocols, or human language into operational meaning. |
| 🕵️ [Investigation](generated/hermes/investigation-and-preparation/investigation/SKILL.md) | Follow evidence through a system until the hidden mechanism becomes legible. |
| 🛡️ [Glyph of Warding](generated/hermes/monitoring-and-protection/glyph-of-warding/SKILL.md) | Set monitors, watches, or triggers that alert when a boundary is crossed. |
| 🪂 [Feather Fall](generated/hermes/repair-and-recovery/feather-fall/SKILL.md) | Turn a hard crash into a controlled descent. |
| 🌙 [Dream](generated/hermes/messaging-and-coordination/dream/SKILL.md) | Deliver the briefing before the recipient wakes up needing it. |

**Forcecage** got a major upgrade: a spell-level optimization pass improved its eval score from 61.8% to 89.3% (+27.5pp). The upgraded version is sharper about tested containment boundaries, outside-the-cage observation, and explicit release conditions. See [the GEPA section](#spell-level-optimization-gepa) for how that works.

## Quick Install

```bash
npm run build:skills
npm run install:hermes-skills
```

Skills install to `~/.hermes/skills/`. Override with `HERMES_HOME=$PWD/.hermes npm run install:hermes-skills` for a local install.

## Find Your Shelf

```
    ┌────────────────────────────────────────────────────────────────────┐
    │ Simulation (8)       Investigation (28)   Actions (19)         │
    │ Influence (18)       GHOST IN THE MACHINE Monitoring (17)      │
    │ Containment (10)     Repair (13)          Messaging (9)        │
    └────────────────────────────────────────────────────────────────────┘
```

| If you want to... | Start here | Shelf |
| --- | --- | --- |
| Figure out what you're looking at | Detect Magic, Identify, Investigation, Comprehend Languages | [Investigation and Preparation (28)](GRIMOIRE.md#investigation-and-preparation) |
| Change the system without a battleaxe | Mage Hand, Sleight of Hand, Unseen Servant, Awaken | [Actions, Access, and Automation (19)](GRIMOIRE.md#actions-access-and-automation) |
| Light up the black box | Dancing Lights, Light, Glyph of Warding, Scrying | [Monitoring and Protection (17)](GRIMOIRE.md#monitoring-and-protection) |
| Get the right message to the right place | Message, Sending, Dream, Magic Mouth | [Messaging and Coordination (9)](GRIMOIRE.md#messaging-and-coordination) |
| Stop the bleeding | Cure Wounds, Mending, Feather Fall, Animal Handling | [Repair and Recovery (13)](GRIMOIRE.md#repair-and-recovery) |
| Mock it before you ship it | Minor Illusion, Major Image, Deception, Programmed Illusion | [Simulation and Staging (8)](GRIMOIRE.md#simulation-and-staging) |
| Handle people with care | Calm Emotions, Heroism, Fear, Plant Growth | [Influence and Behavior (18)](GRIMOIRE.md#influence-and-behavior) |
| Box in blast radius | Forcecage, Blindness/Deafness, Feeblemind, Power Word Stun | [Containment and Intervention (10)](GRIMOIRE.md#containment-and-intervention) |

Open [GRIMOIRE.md](GRIMOIRE.md) for the full browse layer with every skill linked.

## What Ships

- **122** Hermes skills from **127** public canon names (109 spells, 18 skills)
- **8** shelves for progressive discovery instead of one giant list
- **9** featured entry points and **8** intent-driven browse paths
- **5** coercion/memory spells intentionally refused (Compulsion, Dominate Monster, Dominate Person, Geas, Modify Memory)

Skills are procedural markdown with YAML frontmatter — reasoning modes and operator checklists, not executable plugins. Skills that mention env vars or external systems (Home Assistant, Slack) only become real if your Hermes session already has the matching tools and credentials.

## Plain-Language Routing (DSPy)

The pack ships an optional smart router so you can describe what you need in plain English and land on the right shelf — no need to memorize spell names.

- **91.3%** accuracy on held-out routing (95/104 queries), up from **78.8%** for the keyword baseline (+12.5pp)
- Routes plain-English prompts into the correct shelf out of 8 categories
- Makes less-obvious skills actually discoverable — things like [Awaken](generated/hermes/actions-access-and-automation/awaken/SKILL.md), [Animate Objects](generated/hermes/actions-access-and-automation/animate-objects/SKILL.md), [Foresight](generated/hermes/investigation-and-preparation/foresight/SKILL.md), and [Symbol](generated/hermes/monitoring-and-protection/symbol/SKILL.md) that you'd never find by guessing the D&D name

Details and runbook: [`catalog/dspy/README.md`](catalog/dspy/README.md)

<a id="spell-level-optimization-gepa"></a>
## Spell-Level Optimization (GEPA)

Individual spells can be optimized with GEPA (Grounded Eval, Prompt, Align) — a benchmark-driven loop that measures how well a skill's prompt actually performs, then rewrites it based on evidence.

**How it works:** each spell gets a rubric, eval cases, and confusable-skill negatives. GEPA runs baseline eval, optimizes the prompt, re-evaluates, and only promotes the result back into the spellbook if there's a real improvement.

**Forcecage** was the first spell promoted this way — full eval jumped from 61.8% to 89.3%. The optimized prompt is tighter about:
- requiring tested containment boundaries (not just "use a sandbox")
- observing from outside the cage before trusting output
- explicit release conditions before anything escapes

Spell workspaces live under `catalog/gepa/spells/<slug>/`. See [`catalog/gepa/README.md`](catalog/gepa/README.md) for the contract and workflow.

## Build From Source

```bash
npm run bootstrap          # sync canon → expand blueprints → build skills
```

Or step by step:

```bash
npm run sync:canon         # pull canon.json updates
npm run expand:blueprints  # expand blueprints.json with computed fields
npm run build:skills       # render Hermes + OpenClaw surfaces
```

Verify everything:

```bash
npm run verify             # checks surfaces + sandbox installs
```

## Safety and IP

Original code and writing: [CC0-1.0](LICENSE). This does not grant rights in Wizards of the Coast IP, trademarks, logos, artwork, or official rules text. See [LEGAL.md](LEGAL.md) for the full fan-content and IP posture.
