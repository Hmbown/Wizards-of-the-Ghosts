# Wizards of the Ghosts

Unofficial Hermes Agent skill pack built from fantasy spell and skill names.

Not affiliated with or endorsed by Wizards of the Coast.

`wizardsoftheghosts` turns public fifth-edition spell and skill names into practical Hermes skills for investigation, translation, monitoring, messaging, repair, and controlled system intervention.

## Quick Install

```bash
npm run expand:blueprints
npm run build:skills
HERMES_HOME=$PWD/.hermes npm run install:hermes-skills
```

Or install into your default Hermes home:

```bash
npm run install:hermes-skills
```

## What You Get

- `122` Hermes-ready skills
- `8` Hermes category shelves for skill discovery
- slash-command-safe skill names
- generated category `DESCRIPTION.md` files for Hermes browse mode
- a public low-risk surface with the five refused coercion/memory spells excluded

## Featured Skills

Start here:

- `Detect Magic`: scan a repo or workflow for the real agent, tool, and automation surfaces
- `Identify`: explain what a file, service, artifact, or process actually does
- `Investigation`: follow clues through code, logs, and config to a real cause
- `Comprehend Languages`: translate jargon, protocols, formats, and foreign code into operational meaning
- `Mage Hand`: make small, precise changes with minimal blast radius
- `Unseen Servant`: define a persistent helper for repetitive background work
- `Knock`: resolve access friction through legitimate unlock and recovery paths
- `Glyph of Warding`: turn thresholds and trigger conditions into monitors and alerts
- `Zone of Truth`: force evidence-backed claims and labeled uncertainty
- `Foresight`: run a bounded forecast or pre-mortem before committing
- `Dream`: deliver a scheduled briefing before the receiver needs it
- `Feather Fall`: turn a bad situation already in motion into a controlled descent

Browse the full index in [GRIMOIRE.md](GRIMOIRE.md).

## Categories

- `investigation-and-preparation`: inspection, translation, verification, preflight, context loading
- `actions-access-and-automation`: manipulation, access resolution, automation, migration, interface lift
- `monitoring-and-protection`: observability, alerting, guards, privacy, defensive visibility
- `messaging-and-coordination`: communication, briefings, routing, scheduling, rhetoric
- `repair-and-recovery`: triage, repair, stabilization, restoration
- `simulation-and-staging`: mockups, staged environments, synthetic artifacts, demos
- `influence-and-behavior`: persuasion, attention design, and other ethically sharp social patterns
- `containment-and-intervention`: throttling, capability reduction, and high-impact control surfaces

## Build From Source

Source of truth:

1. `catalog/canon.json`
2. `catalog/blueprints.json`
3. `scripts/expand-blueprints.mjs`
4. `scripts/render-skills.mjs`

Default workflow:

```bash
npm run sync:canon
npm run expand:blueprints
npm run build:skills
npm run export:linear
```

Or:

```bash
npm run bootstrap
```

Generated Hermes skills land in `generated/hermes/<category>/<slug>/SKILL.md`.

## Sigils

- `shipping-now`: usable with current agents, tools, and automations
- `prototype`: plausible now, but still needs glue, permissions, or careful integration
- `speculative`: interesting, but not honest to ship as a working skill yet
- `metaphorical`: preserves the intent more than the literal fantasy effect
- `hybrid`: practical behavior with a bit of theatrical framing
- `literal`: tries to cause a directly analogous real-world effect

## Safety

These five spells are intentionally not shipped on the public Hermes surface:

- `Compulsion`
- `Dominate Monster`
- `Dominate Person`
- `Geas`
- `Modify Memory`

Treat literal or device-linked skills like real automations, not decorative lore.

## License And IP

Original code and writing in this repo are released under `CC0-1.0`.

That does not grant rights in Wizards of the Coast IP, trademarks, logos, artwork, or official rules text. This repo is meant to stay free, unofficial, and clearly separate from any official Wizards product line.

See [LEGAL.md](LEGAL.md) for the current fan-content and IP posture.
