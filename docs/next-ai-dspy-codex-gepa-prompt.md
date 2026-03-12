# Next AI Prompt: Wire GEPA to DSPy Codex Backend

You are working in:

- repo: `/Volumes/VIXinSSD/wizardsoftheghosts`
- related Codex backend fork: `/Volumes/VIXinSSD/dspy-codex`

Your job is to make `wizardsoftheghosts` use the local Codex-backed DSPy path for GEPA work, then use that backend to continue the spell optimization lane.

## Context You Should Trust

- `wizardsoftheghosts` already has the shared GEPA contract in place under:
  - `catalog/gepa/schema/`
  - `catalog/gepa/rubric-packs/`
  - `scripts/gepa_common.py`
- The following spell workspaces are already authored and validate cleanly:
  - `catalog/gepa/spells/detect-magic/`
  - `catalog/gepa/spells/comprehend-languages/`
  - `catalog/gepa/spells/identify/`
  - `catalog/gepa/spells/mage-hand/`
  - `catalog/gepa/spells/forcecage/`
  - `catalog/gepa/spells/charm-person/`
  - `catalog/gepa/spells/light/`
- Current validation/test status in this repo was:
  - `pytest tests/test_gepa_rubric_contracts.py tests/test_gepa_workflow.py tests/test_dspy_workflow.py -q`
  - result: `41 passed`
- `.venv` already exists at `/Volumes/VIXinSSD/wizardsoftheghosts/.venv`
- Do not use bare system `python3` for DSPy/GEPA runs unless you first prove it has the right environment. The repo has a `.venv` and the previous mismatch came from using the wrong interpreter.

## The Actual Problem

`wizardsoftheghosts` currently has a repo-local Codex wrapper in:

- `scripts/dspy_codex_lm.py`

but `/Volumes/VIXinSSD/dspy-codex` is the newer fork that ships:

- `dspy.CodexLM`
- `scripts/dspy_codex_doctor.py`
- `scripts/dspy_codex_probe.py`
- `scripts/dspy_codex_smoke.py`
- `scripts/dspy_codex_gepa.py`

The goal is to use the real `dspy-codex` backend, not keep growing the ad hoc local wrapper unless you find a concrete incompatibility.

## Read First

Open these before changing code:

- `/Volumes/VIXinSSD/dspy-codex/README.md`
- `/Volumes/VIXinSSD/dspy-codex/skills/dspy-codex/SKILL.md`
- `/Volumes/VIXinSSD/dspy-codex/skills/dspy-codex/references/runtime-selection.md`
- `/Volumes/VIXinSSD/wizardsoftheghosts/scripts/dspy_common.py`
- `/Volumes/VIXinSSD/wizardsoftheghosts/scripts/gepa_common.py`
- `/Volumes/VIXinSSD/wizardsoftheghosts/scripts/gepa_optimize_spell.py`
- `/Volumes/VIXinSSD/wizardsoftheghosts/catalog/gepa/README.md`

## What To Do

1. Verify the local `dspy-codex` fork is healthy.

From `/Volumes/VIXinSSD/dspy-codex`, run the repo’s own checks first:

```bash
uv sync --extra mcp --extra dev
uv run python scripts/dspy_codex_doctor.py --json
uv run python scripts/dspy_codex_probe.py --transport auto --json
uv run python scripts/dspy_codex_smoke.py --transport auto --json
uv run python scripts/dspy_codex_gepa.py --json
```

If `auto` is flaky, also check:

```bash
uv run python scripts/dspy_codex_probe.py --transport cli --json
uv run python scripts/dspy_codex_smoke.py --transport cli --json
```

2. Make `wizardsoftheghosts` use the local fork in its own `.venv`.

Prefer a clean, explicit path such as installing the local fork into the repo venv rather than relying on global Python state. A likely path is:

```bash
uv pip install --python /Volumes/VIXinSSD/wizardsoftheghosts/.venv/bin/python -e /Volumes/VIXinSSD/dspy-codex
```

If you choose a different installation route, keep it explicit and reproducible.

3. Update `wizardsoftheghosts` so DSPy/GEPA can use `dspy.CodexLM`.

Target behavior:

- `codex/default` should work
- `codex-exec/default` should work
- ideally `codex-mcp/default` should also be recognized if the fork/runtime supports it cleanly

Current code only has special handling for `codex-exec/...`. Fix that in the narrowest, cleanest place. Likely touch points:

- `scripts/dspy_common.py`
- `scripts/gepa_common.py`
- possibly `scripts/dspy_build_router.py` / `scripts/dspy_eval_router.py` only if needed

Prefer using the fork’s `dspy.CodexLM` client instead of maintaining `scripts/dspy_codex_lm.py` as the primary runtime path. If you keep the local file at all, either remove it from the hot path or make it a thin compatibility layer with a clear reason.

4. Verify `wizardsoftheghosts` against the Codex backend.

Use the repo venv or the repo’s own wrappers, not the wrong interpreter. Run:

```bash
cd /Volumes/VIXinSSD/wizardsoftheghosts
DSPY_MODEL=codex/default npm run dspy:validate
DSPY_MODEL=codex/default npm run dspy:baseline
```

If the generic alias is unreliable, fall back to:

```bash
DSPY_MODEL=codex-exec/default npm run dspy:validate
DSPY_MODEL=codex-exec/default npm run dspy:baseline
```

Keep the sandbox conservative. The `dspy-codex` repo defaults matter here.

5. Use the Codex backend for GEPA spell work.

Run optimize/eval for the already-authored spell workspaces first:

```bash
cd /Volumes/VIXinSSD/wizardsoftheghosts
export DSPY_MODEL=codex/default
export GEPA_REFLECTION_MODEL=codex/default
export DSPY_TEMPERATURE=0
export DSPY_MAX_TOKENS=512
export DSPY_CODEX_TRANSPORT=auto

npm run gepa:spell:optimize -- --slug detect-magic
npm run gepa:spell:eval -- --slug detect-magic

npm run gepa:spell:optimize -- --slug comprehend-languages
npm run gepa:spell:eval -- --slug comprehend-languages
```

If `codex/default` is unstable but CLI works, retry with:

```bash
export DSPY_MODEL=codex-exec/default
export GEPA_REFLECTION_MODEL=codex-exec/default
```

6. If optimization produces a credible win, continue the intended spell lane.

For each spell:

- compare baseline vs optimized eval
- update `promotion_patch.json` only when there is a real improvement
- only then promote back into `catalog/blueprints.json`
- rebuild generated surfaces if you promote anything

## Constraints

- Do not hand-edit `generated/`
- Do not regress the shared GEPA contract
- Do not replace the fork’s runtime-selection logic with new ad hoc subprocess plumbing unless the fork is genuinely insufficient
- Do not silently broaden live-action capabilities in prompt text
- Treat `detect-magic` and `comprehend-languages` as the next spell priorities because their benchmark work is already authored

## Success Criteria

You are done when all of the following are true:

1. `wizardsoftheghosts` can actually run DSPy/GEPA through the local Codex backend instead of just validating without a backend.
2. The repo recognizes the correct Codex model aliases cleanly.
3. At least one real GEPA optimize/eval pass has run in `wizardsoftheghosts` using the Codex backend.
4. `detect-magic` and `comprehend-languages` are no longer just seeded workspaces; they have actual model-backed optimization evidence.
5. Tests still pass, or any failures are narrow, explained, and directly tied to the integration work.

## Good Final Deliverable

In your final answer, include:

- what you changed to use `dspy-codex`
- exact commands that succeeded
- whether `codex/default`, `codex-exec/default`, and `codex-mcp/default` worked
- which spell optimizations actually ran
- whether any `promotion_patch.json` or `catalog/blueprints.json` changes were justified
