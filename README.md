# Wizards of the Ghosts

> An unofficial fan grimoire of Hermes Agent skills built from fantasy spell and skill names.
>
> Not affiliated with or endorsed by Wizards of the Coast.

`wizardsoftheghosts` packages public fifth-edition spell and skill names as practical Hermes Agent skills for investigation, automation, monitoring, messaging, repair, and controlled system intervention.

The costume is whimsical. The mechanisms are often real.

This repository is published as a free unofficial fan project, not as a paid or official product line.

## Quick Install

Build the Hermes skill pack:

```bash
npm run expand:blueprints
npm run build:skills
```

Install into a local Hermes home:

```bash
HERMES_HOME=$PWD/.hermes npm run install:hermes-skills
```

Install into your default Hermes runtime:

```bash
npm run install:hermes-skills
```

Once installed, Hermes can discover the skills through its normal category browser, `skills_list`, `skill_view`, and slash-command flow.

## What You Get

- `122` Hermes-ready skills generated from one source catalog
- `8` Hermes category shelves designed for agent discovery
- slash-command-safe skill names
- generated `DESCRIPTION.md` category summaries for Hermes browse mode
- a low-risk public surface that keeps the five refused coercion/memory spells off Hermes

## What This Repo Is

Fantasy magic is the design language. Real agent workflows are the substrate.

This repo treats spells and skills as ways to describe:

- repo and system investigation
- translation across code, tools, and human language
- monitoring, alerts, and trigger conditions
- precise software manipulation
- async messaging and scheduled briefings
- recovery, containment, and other bounded operational interventions

Some entries are mostly cognitive framing. Some are grounded in real integrations. Some stay at `prototype` because pretending otherwise would be corny.

## Start With These Skills

If someone opens the repo cold, these are the best first pages to hand them.

| Entry | What it actually means | Why it earns front-page space |
| --- | --- | --- |
| `Detect Magic` | Scan a repo, workflow, or system for the real agent, tool, and automation surfaces before acting. | It explains the whole thesis in one move and maps directly to Hermes discovery work. |
| `Identify` | Figure out what a mysterious file, service, artifact, or process actually does. | Clean, useful, and immediately legible to almost any user. |
| `Investigation` | Follow clues through code, logs, and config until the real cause becomes clear. | Shows that the spellbook is not just cute naming; it is a practical debugging surface. |
| `Comprehend Languages` | Translate jargon, protocols, formats, or foreign code into operational meaning. | A perfect example of metaphor becoming practical. |
| `Mage Hand` | Make small, precise file or state changes with minimal blast radius. | Quietly one of the most believable and reusable skills in the book. |
| `Unseen Servant` | Run a persistent background helper that keeps mundane tasks moving. | Very close to how people actually want Hermes to help once the novelty wears off. |
| `Knock` | Resolve access friction through legitimate unlock paths and recovery workflows. | Literal enough to be fun, grounded enough to be honest. |
| `Glyph of Warding` | Turn thresholds, monitors, and trigger conditions into watchful boundaries. | This is where the joke starts touching real automation. |
| `Zone of Truth` | Force evidence-backed claims, labeled uncertainty, and cleaner reasoning. | It teaches the repo's quality bar and makes the agentic posture explicit. |
| `Foresight` | Run a bounded forecast or pre-mortem before a plan, launch, or migration. | Serious planning with just enough moonlight on it. |
| `Dream` | Deliver a briefing on the receiver's clock, not the sender's. | Good example of theatrical framing that still does real work. |
| `Feather Fall` | Turn a bad situation already in motion into a controlled descent. | A strong example of graceful degradation and incident thinking, not just clever flavor text. |

## Hermes Categories

The Hermes packaging uses eight operational categories designed for agent discovery:

- `investigation-and-preparation` for inspection, translation, verification, preflight, and context loading
- `actions-access-and-automation` for manipulation, access resolution, automation, migration, and interface lift
- `monitoring-and-protection` for observability, alerting, guards, privacy, and defensive visibility
- `messaging-and-coordination` for communication, briefings, routing, scheduling, and rhetoric
- `repair-and-recovery` for triage, repair, stabilization, and restoration
- `simulation-and-staging` for mockups, staged environments, synthetic artifacts, and demos
- `influence-and-behavior` for persuasion, attention design, and other ethically sharp social patterns
- `containment-and-intervention` for throttling, capability reduction, and high-impact control surfaces

Browse the GitHub-native index in [GRIMOIRE.md](GRIMOIRE.md).

## Build From Source

The source of truth is intentionally simple:

1. `catalog/canon.json`
   Machine-generated public canon list.
2. `catalog/blueprints.json`
   The reinterpretation layer and Hermes release metadata.
3. `scripts/expand-blueprints.mjs`
   Hermes category assignment and surface construction.
4. `scripts/render-skills.mjs`
   Generator for `generated/hermes/`.

Default local workflow:

```bash
npm run sync:canon
npm run expand:blueprints
npm run build:skills
npm run export:linear
```

Or run the whole ritual:

```bash
npm run bootstrap
```

Generated Hermes skills land in `generated/hermes/<category>/<slug>/SKILL.md`. The `generated/` tree is intentionally gitignored.

## Reading The Sigils

- `shipping-now`: usable with current agents, tools, and automations
- `prototype`: plausible now, but still needs glue, permissions, or careful integration
- `speculative`: interesting, but not honest to ship as a working spell yet
- `metaphorical`: preserves the intent more than the literal fantasy effect
- `hybrid`: practical behavior with a bit of theatrical costume left on
- `literal`: tries to cause a directly analogous real-world effect

## Safety And Refusals

The public Hermes surface is intentionally conservative about coercion, memory alteration, and hard-control metaphors. These five spells are intentionally not shipped:

- `Compulsion`
- `Dominate Monster`
- `Dominate Person`
- `Geas`
- `Modify Memory`

Literal or device-linked skills should be treated like real automations, not decorative lore. If you wire `Glyph of Warding`, `Scrying`, `Dream`, or `Dancing Lights` into live systems, the blast radius is real even if the naming remains theatrical.

## License And IP

Original code and original writing in this repo are released under `CC0-1.0`.

That does not grant rights in Wizards of the Coast IP, trademarks, logos, artwork, or official rules text. The project is meant to stay free, unofficial, and clearly separate from any official Wizards product line.

See [LEGAL.md](LEGAL.md) for the repo's current fan-content and IP posture.
