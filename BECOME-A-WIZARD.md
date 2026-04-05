# Become a Wizard

This repo already has the spellbook. The missing part is installing it where your local agent runtime can actually cast it.

## Local Wizard Setup

```bash
npm run wizard:install
```

That does three things:

1. rebuilds the generated skill surfaces
2. installs Hermes skills into `./.hermes/skills`
3. installs Codex/OpenClaw skills into `./.codex/skills`

If you want the global install targets instead, use:

```bash
npm run install:hermes-skills
npm run install:codex-skills
```

## First Spells

Start with the spells that teach you the shape of the repo:

- `/detect-magic` to surface automation hooks, pipelines, and capability seams
- `/identify` to explain an unfamiliar file, script, or artifact
- `/mage-hand` for precise edits with minimal blast radius
- `/forcecage` before you let an untrusted script or agent touch anything important
- `/zone-of-truth` when you need sourced claims instead of vibes

## Spell Forge

The repo can tune its own spell prompts through DSPy and GEPA.

### Validate the toolchain

```bash
npm run dspy:validate
```

### Preferred local backends

Qwen via the local Qwen CLI:

```bash
export DSPY_MODEL=qwen/default
```

OpenCode via your locally configured default model:

```bash
export DSPY_MODEL=opencode/default
```

GitHub Copilot on the working Codex lane:

```bash
export DSPY_MODEL=copilot/codex-5.3
```

If you know your exact OpenCode provider model, you can be explicit instead:

```bash
export DSPY_MODEL=opencode/<provider>/<model>
```

### Router compile/eval

```bash
npm run dspy:compile
npm run dspy:eval
```

### Spell-level GEPA loop

```bash
npm run gepa:spell:optimize -- --slug detect-magic
npm run gepa:spell:eval -- --slug detect-magic
```

Batch helpers:

```bash
bash scripts/gepa_batch_run.sh
bash scripts/gepa_batch_promote.sh
```

## Notes

- `qwen/default` is the safest way to use the Qwen CLI lane here because it follows your local Qwen configuration instead of hardcoding a stale model name.
- `opencode/default` does the same for OpenCode.
- `copilot/codex-5.3` is now a first-class DSPy alias in this repo and probes successfully through `gh copilot`.
- The generated skills under `generated/` are build artifacts. Change source material or renderer logic, then rebuild.
