# HermesAgent Notes

These are practical notes from Hermes after loading and smoke-testing the current `wizardsoftheghosts` spell pack inside a real Hermes runtime.

## Short version

The spellbook has strong identity and good taste. The biggest opportunity is to make more spells feel like they are ready for Hermes to *do something useful immediately*, not just explain a stance.

In practice that means each spell should keep the magic flavor, but hide a more concrete operator runbook underneath it.

## What makes a spell feel Hermes-native

A Hermes-native spell usually has most of these:

1. A clear default operating mode
   - read-only
   - synthetic demo
   - copied workspace
   - approval-gated live action

2. Concrete tool choreography
   - what Hermes should inspect with `search_files` / `read_file`
   - what it should execute with `terminal`
   - when to use `process`, `todo`, `clarify`, `delegate_task`

3. A strong first move
   - not just the philosophy of the spell
   - the first safe action Hermes should take by default

4. A safe demo mode
   - something testable in `/tmp`, a copied workspace, or a dry-run path
   - this makes the spell fun, evaluable, and believable

5. Explicit confirmation gates
   - before device triggers
   - before access changes
   - before destructive actions
   - before touching a live system boundary

6. Deliverables shaped like real outputs
   - commands run
   - files created
   - observed behavior
   - rollback path
   - recommendation for the next move

## Suggested execution contract block

A reusable block worth adding to many Hermes-targeted spells:

```md
## Hermes Execution Contract
- Default mode: synthetic or copied-workspace first
- Preferred tools: search_files, read_file, terminal, process, todo
- Avoid by default: live mutations, credential use, external side effects
- Ask for confirmation before: real-world effects, account changes, production mutations, irreversible actions
- Return format:
  1. Goal
  2. Scope / boundary
  3. Actions taken
  4. Observations
  5. Risks / assumptions
  6. Recommended next move
```

## Concrete upgrades that would make the spells stronger

### Forcecage
Very good core metaphor already.

To make it more Hermes-native:
- default to a copied workspace or `/tmp` sandbox
- say which tools to use for inspection vs execution
- require a release condition in the output
- add a canned safe demo recipe

Good safe demo:
- create a tiny sandbox in `/tmp`
- put an allowed file inside it
- put a blocked file outside it
- run a harmless probe with a stripped environment
- report what was readable vs denied

That demo already works well as a proof-of-concept for the spell.

### Dancing Lights
This is a great candidate for becoming *literally* magical.

Right now it reads as lightweight indicators. That is fine, but for Hermes it could be split into modes:
- terminal/status mode: colored text, spinners, status pips, dashboards
- messaging mode: tiny heartbeat notices to Telegram/Discord/Slack
- device mode: literal Hue or smart-light status mapping

This is the exact kind of spell that can justify a `literal` path.

Example literal implementations:
- green pulse when a long-running job completes successfully
- red scene on failure or breached boundary
- blue idle state for a watcher
- yellow blink for human approval needed

If OpenHue or Home Assistant is available, `Dancing Lights` could become a real room-status spell instead of only a metaphor.

### Thunderwave
Strong theme, but currently more theatrical than operational.

To improve usability:
- define `simulate`, `prepare`, and `execute` modes
- default to simulated effects unless the user explicitly wants a real trigger
- specify rollback / shutdown path in the output

### Power Word Stun
Already maps well to a real action.

To make it stronger:
- require exact target identity
- require a reversible mechanism
- always emit resume instructions
- always emit a review deadline

Recommended output fields:
- target
- freeze mechanism
- timestamp
- preserved-state evidence
- resume command
- reviewer / next checkpoint

### Shatter
Probably the easiest spell to make operational immediately.

Useful default escalation ladder:
1. malformed input
2. boundary values
3. concurrency / load
4. recovery behavior

And always require a blast radius before any test.

## General spell-design pattern that seems promising

A good future template for many spells could be:

1. Spell fantasy
2. Real-world interpretation
3. Safe demo mode
4. Hermes execution contract
5. Approval gate
6. Deliverables
7. Literal extensions, if connected tools exist

That keeps the writing fun without making the spell vague.

## Why the existing Hermes skill pack is a useful reference

The local Hermes runtime skill library contains lots of examples where the skill is not just thematic — it also tells Hermes exactly how to proceed.

See the symlink in this repo:
- `hermes-runtime-skills -> ~/.hermes/skills`

That library shows the upper bound for practical execution scaffolding, including:
- linked references/templates/scripts
- dependency/setup sections
- exact commands
- decision flow
- clear fallback behavior

Not every spell here should become that detailed, but the strongest showcase spells probably should.

## Recommendation

I would not de-magic the spellbook.

I would keep the flavor and upgrade the best spells into showcase entries that are:
- more concrete
- more demoable
- more tool-aware
- more literal when an integration exists

The obvious showcase candidates from a Hermes perspective:
- Forcecage
- Dancing Lights
- Glyph of Warding
- Thunderwave
- Power Word Stun
- Scrying
- Magic Mouth
- Awaken

Especially `Dancing Lights`: if a room can actually change color based on agent state, the metaphor stops being merely cute and starts being product magic.
