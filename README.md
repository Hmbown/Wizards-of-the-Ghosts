# Wizards of the Ghosts

> An unofficial fan grimoire for people who keep accidentally inventing wizard interfaces for agents, automations, and software systems.
>
> Not affiliated with or endorsed by Wizards of the Coast.

`wizardsoftheghosts` turns public fifth-edition fantasy spell and skill names into AI skills, workflow patterns, and automation rituals for Hermes Agent, OpenClaw, and local development workflows.

It is not a totally serious project.

It is also not only a joke.

The costume is whimsical. The mechanisms are often real. The right way to read it is: as serious as you want it to be.

This repository is published as a free unofficial fan project, not as a paid or official product line.

## What This Is

Fantasy magic is the design language here. Real-world capability is the substrate.

This repo treats spells and skills as ways to describe:

- repo and system investigation
- translation across code, tools, and human language
- monitoring, alerts, and trigger conditions
- lightweight software manipulation
- async messaging and coordination
- literal-ish automations when a spell can honestly be wired to a device or service

Some entries are mostly cognitive framing. Some are grounded in actual integrations. Some are kept at `prototype` because pretending otherwise would be corny.

## At A Glance

- `127` canon entries reinterpreted from public fantasy spell and skill names
- `122` OpenClaw-ready skills currently rendered from the blueprint catalog
- `122` Hermes-ready skills currently rendered from the same source catalog
- `11` grounded OpenClaw skills with real `env` and `bin` requirements
- `5` spells intentionally refused on the public Hermes and OpenClaw surfaces
- `0` remaining stubs in `catalog/blueprints.json`

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

## Navigate The Grimoire

The generated skill output is a local build artifact, so the easiest GitHub-native way to browse the spellbook is the curated grimoire index:

- [Quick-Start Shelf](GRIMOIRE.md#quick-start-shelf)
- [Investigation and Preparation](GRIMOIRE.md#investigation-and-preparation)
- [Actions, Access, and Automation](GRIMOIRE.md#actions-access-and-automation)
- [Monitoring and Protection](GRIMOIRE.md#monitoring-and-protection)
- [Messaging and Coordination](GRIMOIRE.md#messaging-and-coordination)
- [Repair and Recovery](GRIMOIRE.md#repair-and-recovery)
- [Simulation and Staging](GRIMOIRE.md#simulation-and-staging)
- [Influence and Behavior](GRIMOIRE.md#influence-and-behavior)
- [Containment and Intervention](GRIMOIRE.md#containment-and-intervention)
- [Grounded Circles](GRIMOIRE.md#grounded-circles)
- [The Spellbook Refuses These](GRIMOIRE.md#the-spellbook-refuses-these)

## How The Spellbook Works

The source of truth is intentionally simple:

1. `catalog/canon.json`
   Machine-generated public canon list.
2. `catalog/blueprints.json`
   The actual reinterpretation layer.
3. `scripts/render-skills.mjs`
   Renderer for generated skill output.
4. `catalog/linear-seed.json` and `catalog/linear-seed.csv`
   Backlog export artifacts.

Current public-canon coverage is:

- `18` core skills from the official 2024 Free Rules "Playing the Game" page
- `109` public spell names harvested from the D&D Beyond Basic Rules index as reference metadata

The source data now drives two first-class generated release surfaces:

- `generated/openclaw/`
- `generated/hermes/`

The Hermes surface keeps the same low-risk public release posture as the current OpenClaw surface, but packages the skills in a Hermes-native shape with category roots, `DESCRIPTION.md` files, slash-command-safe frontmatter names, and procedural `SKILL.md` bodies.

## License And IP

Original code and original writing in this repo are released under `CC0-1.0`.

That does not grant rights in Wizards of the Coast IP, trademarks, logos, artwork, or official rules text. The project is meant to stay free, unofficial, and clearly separate from any official Wizards product line.

See [LEGAL.md](LEGAL.md) for the repo's current fan-content and IP posture.

## Reading The Sigils

- `shipping-now`: usable with current agents, tools, and automations
- `prototype`: plausible now, but still needs glue, permissions, or careful integration
- `speculative`: interesting, but not honest to ship as a working spell yet

- `metaphorical`: preserves the intent more than the literal fantasy effect
- `hybrid`: practical behavior with a bit of theatrical costume left on
- `literal`: tries to cause a directly analogous real-world effect

## Build The Spellbook

This repo has no runtime dependencies beyond Node for the local scripts.

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

Rendered skills land in `generated/openclaw/` and `generated/hermes/`. The whole `generated/` tree is intentionally gitignored, so build it locally when you want the actual `SKILL.md` output.

## Hermes Agent

Hermes is now a first-class output target for this repo.

- Generated Hermes skills land in `generated/hermes/<category>/<slug>/SKILL.md`.
- Category descriptions land in `generated/hermes/<category>/DESCRIPTION.md`.
- Frontmatter `name` uses the slug-safe spell or skill slug so Hermes slash commands stay command-safe.
- Runtime install targets are copied into `~/.hermes/skills/` or `$HERMES_HOME/skills/`, not into the Hermes git repo.

The current Hermes release surface intentionally mirrors the repo's lowest-risk public subset. It stays a free unofficial fan project, keeps the same five refused spells off the public Hermes surface, and does not add copied rules text, Wizards logos, or official trade dress.

### Install Into A Local Hermes Home

For workspace-local testing:

```bash
HERMES_HOME=$PWD/.hermes npm run install:hermes-skills
```

For the default runtime home:

```bash
npm run install:hermes-skills
```

Once installed, Hermes can discover the skills through its normal scanner and slash-command flow.

### Hermes Category Strategy

The Hermes packaging uses eight operational categories designed for agent discovery:

- `investigation-and-preparation` — inspection, translation, verification, preflight, context loading
- `actions-access-and-automation` — manipulation, access resolution, automation, migration, interface lift
- `monitoring-and-protection` — observability, alerting, guards, privacy
- `messaging-and-coordination` — communication, briefings, scheduling, rhetoric
- `repair-and-recovery` — triage, repair, stabilization, recovery
- `simulation-and-staging` — mockups, staged environments, synthetic data, demos
- `influence-and-behavior` — attention design, behavior shaping, ethical guardrails
- `containment-and-intervention` — containment, capability reduction, high-impact controls, safety gates

For local Codex experimentation, you can mirror the generated skills into a workspace-local Codex directory:

```bash
CODEX_HOME=$PWD/.codex npm run install:codex-skills
```

## Safety And Refusals

The public Hermes and OpenClaw surfaces are intentionally conservative about coercion, memory alteration, and hard-control metaphors. These five spells are intentionally not shipped there:

- `Compulsion`
- `Dominate Monster`
- `Dominate Person`
- `Geas`
- `Modify Memory`

Literal or device-linked skills should be treated like actual automations, not decorative lore. If you wire `Glyph of Warding`, `Scrying`, `Dream`, or `Dancing Lights` into live systems, the blast radius is real even if the naming remains theatrical.
