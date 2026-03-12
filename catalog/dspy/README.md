# DSPy Artifacts

This directory holds deterministic and model-generated artifacts for applying DSPy to the Hermes spell corpus.

Phase 1 artifacts are deterministic extractions from:
- `catalog/canon.json`
- `catalog/blueprints.json`
- `generated/hermes/*/*/SKILL.md`

Current files:
- `spells_master.jsonl` — one normalized row per Hermes-public spell/skill
- `categories.json` — Hermes category metadata from `blueprints.json`
- `browse_paths.json` — Hermes browse-path metadata
- `refusal_set.json` — Hermes-refused spell slugs
- `hermes_phase1_summary.json` — extraction summary counts
- `shards/` — subagent-generated Phase 2 query shards before merge
- `hermes-train-queries.jsonl` — merged training queries
- `hermes-eval-set.jsonl` — merged held-out routing/eval queries
- `hermes-hard-negatives.jsonl` — merged confusing-neighbor negatives
- `hermes-abstain.jsonl` — merged abstain / refuse cases
- `hermes_query_summary.json` — merged query dataset summary
- `baseline_router.json` — lexical baseline category router artifact
- `baseline_eval_summary.json` — baseline eval metrics and confusion matrix
- `baseline_eval_predictions.jsonl` — one prediction row per scored baseline example
- `dspy_router_status.json` — DSPy build status / dependency status
- `dspy_eval_summary.json` — DSPy eval summary when available
- `dspy_eval_predictions.jsonl` — one prediction row per scored DSPy example when evaluation succeeds

## Python Setup

The DSPy workflow is intentionally isolated from the Node build pipeline.

```bash
uv venv .venv
uv pip install --python .venv/bin/python -r requirements-dspy.txt
```

Pinned Python dependencies live in `requirements-dspy.txt`.

## Commands

Validation and deterministic baseline:

```bash
npm run dspy:validate
npm run dspy:baseline
```

Direct Python equivalents:

```bash
.venv/bin/python scripts/dspy_build_router.py --repo-root . --validate-only
.venv/bin/python scripts/dspy_build_router.py --repo-root . --baseline-only
.venv/bin/python scripts/dspy_eval_router.py --repo-root . --baseline-only
```

Practical subset controls for live DSPy runs:

```bash
.venv/bin/python scripts/dspy_build_router.py --repo-root . --train-limit 4
.venv/bin/python scripts/dspy_eval_router.py --repo-root . --dspy-only --eval-limit 8
```

These limits are optional. If they are omitted, the scripts preserve the full existing behavior.

Live DSPy compile/eval requires explicit backend configuration:

```bash
export DSPY_MODEL=openai/qwen3.5:4b
export DSPY_API_BASE=http://127.0.0.1:11434/v1
export DSPY_API_KEY=dummy

npm run dspy:compile
npm run dspy:eval
```

Optional LM settings:

- `DSPY_TEMPERATURE`
- `DSPY_MAX_TOKENS`

No backend is assumed by default. `DSPY_MODEL` must be provider-qualified, for example `openai/qwen3.5:4b`.

Experimental Codex-backed option:

```bash
export DSPY_MODEL=codex-exec/default
```

When `DSPY_MODEL` starts with `codex-exec/`, DSPy shells out to local `codex exec` instead of using LiteLLM/OpenAI-compatible HTTP transport. This is the closest repo-native path to using Codex for DSPy runtime work, because Python code in the repo cannot call the assistant-only MCP tools directly. It is intentionally marked experimental and materially slower than the HTTP LM path because each inference starts a Codex process.

Recommended small-scale smoke test:

```bash
export DSPY_MODEL=codex-exec/default
export DSPY_TEMPERATURE=0
export DSPY_MAX_TOKENS=256

.venv/bin/python scripts/dspy_build_router.py --repo-root . --train-limit 4
.venv/bin/python scripts/dspy_eval_router.py --repo-root . --dspy-only --eval-limit 8
```

Observed repo-local result on 2026-03-11:

- Limited compile succeeded with `train_limit=4` and wrote `dspy_router_status.json` with the subset metadata (`train_limit`, `train_rows_used`, `train_rows_available`).
- Limited eval succeeded with `eval_limit=8` and wrote `dspy_eval_summary.json` with `total_eval_rows=8`, `total_available_rows=104`, `correct=5`, and `accuracy=0.625`.
- Wall-clock timings were slow enough to matter: compile took about `40.40s`, and eval took about `165.52s`.
- Treat the Codex path as a smoke-test or small-experiment lane until someone intentionally budgets for a much longer full `208`-row compile plus `104`-row eval.

Completed full-dataset Codex-backed run on 2026-03-11:

- Backend settings: `DSPY_MODEL=codex-exec/default`, `DSPY_TEMPERATURE=0`, `DSPY_MAX_TOKENS=256`
- Compile: `239s` (~4 min). BootstrapFewShot found 8 correct demos in 11 training examples.
- Eval: `2544s` (~42 min) over all 104 eval rows.
- Total wall clock: `2783s` (~46 min).
- **DSPy accuracy: 95/104 = 91.3%** vs baseline 82/104 = 78.8% (+12.5pp).
- Per-inference latency: ~20–25s via `codex exec` subprocess.
- All artifacts written: `dspy_category_router.json`, `dspy_router_status.json`, `dspy_eval_summary.json`, `dspy_eval_predictions.jsonl`.
- The full run is practical as an unattended background job. Use `bash scripts/dspy_full_run.sh` with the env vars above.

Phase 2 generation flow:
1. Generate shard files under `catalog/dspy/shards/*.jsonl`
2. Merge and validate them with:
   - `python3 scripts/dspy_generate_spell_queries.py --repo-root .`

Phase 3 routing flow:
1. Build baseline + attempt DSPy compile:
   - `npm run dspy:compile`
2. Evaluate routers:
   - `npm run dspy:eval`

Shard row contract:
- `query_id`
- `split` (`train`, `eval`, `hard_negative`, `abstain`)
- `query_type`
- `query`
- `target_slug`
- `target_category_slug`
- `target_kind`
- optional extras like `notes`, `confusable_slug`, `source`

Notes:
- These artifacts are derived data. Regenerate Phase 1 with:
  - `python3 scripts/dspy_extract_hermes_corpus.py --repo-root .`
- Merge Phase 2 with:
  - `python3 scripts/dspy_generate_spell_queries.py --repo-root .`
- `dspy_router_status.json` is always written by the validate/compile path and reports one of:
  - `ok`
  - `missing_dependency`
  - `backend_not_configured`
  - `backend_unreachable`
  - `compile_failed`
- `dspy_eval_summary.json` is always written by the DSPy eval path and explains whether evaluation ran or why it did not.
- The v1 DSPy router scores only category routing on the `eval` and optional `hard_negative` splits.
- `hermes-abstain.jsonl` is preserved for validation and future routing work, but abstain detection is not implemented in the current router.
- Do not treat this directory as the source of truth for spell meaning.
- Continue to edit `catalog/blueprints.json` and renderer logic instead of patching generated outputs directly.
