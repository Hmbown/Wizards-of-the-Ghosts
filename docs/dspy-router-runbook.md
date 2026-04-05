# DSPy Router Runbook

This runbook keeps the Hermes DSPy path reproducible and explicit.

## 1. Create the Python Environment

```bash
uv venv .venv
uv pip install --python .venv/bin/python -r requirements-dspy.txt
```

## 2. Validate the Local Workspace

```bash
npm run dspy:validate
```

This command does not require a live model backend. It checks:

- required `catalog/dspy/` artifacts exist and parse cleanly
- `dspy` is installed in the active `.venv`
- backend configuration is present or intentionally absent
- backend reachability, if `DSPY_API_BASE` is set

The result is written to `catalog/dspy/dspy_router_status.json`.

## 3. Run the Deterministic Baseline

```bash
npm run dspy:baseline
```

This rebuilds the lexical baseline router and evaluates it on the held-out eval set. Outputs:

- `catalog/dspy/baseline_router.json`
- `catalog/dspy/baseline_eval_summary.json`
- `catalog/dspy/baseline_eval_predictions.jsonl`

## 4. Configure a DSPy Backend

No backend is assumed by default. Live DSPy compile/eval requires `DSPY_MODEL`.

Minimum required setting:

```bash
export DSPY_MODEL=qwen/default
```

Optional settings:

```bash
export DSPY_API_BASE=http://127.0.0.1:11434/v1
export DSPY_API_KEY=dummy
export DSPY_TEMPERATURE=0
export DSPY_MAX_TOKENS=512
```

### Optional OpenAI-compatible HTTP example

This is an example, not the repo default:

```bash
export DSPY_MODEL=openai/<model>
export DSPY_API_BASE=http://127.0.0.1:11434/v1
export DSPY_API_KEY=dummy
```

The provider prefix stays explicit when you use LiteLLM/OpenAI-compatible HTTP transport.

### Experimental local Codex example

```bash
export DSPY_MODEL=codex-exec/default
```

This uses local `codex exec` as the LM adapter. It does not call the assistant-only MCP tools directly from Python; instead it shells out through the installed Codex CLI. Treat it as experimental:

- each DSPy inference launches a Codex process
- compile is likely much slower than the HTTP LM path
- model suitability still matters for DSPy’s structured output needs

For a first real run, start with the subset controls instead of the full dataset:

```bash
export DSPY_MODEL=codex-exec/default
export DSPY_TEMPERATURE=0
export DSPY_MAX_TOKENS=256

.venv/bin/python scripts/dspy_build_router.py --repo-root . --train-limit 4
.venv/bin/python scripts/dspy_eval_router.py --repo-root . --dspy-only --eval-limit 8
```

Those commands leave the dataset artifacts untouched and record the limited scope in `dspy_router_status.json` and `dspy_eval_summary.json`.

### Experimental local Qwen example

```bash
export DSPY_MODEL=qwen/default
```

Use `qwen/default` when you want the repo to follow the model already selected
in your local Qwen CLI configuration.

### Experimental local OpenCode example

```bash
export DSPY_MODEL=opencode/default
```

Use `opencode/default` to follow your OpenCode default model, or
`opencode/<provider>/<model>` if you want an explicit provider model.

### Experimental GitHub Copilot example

```bash
export DSPY_MODEL=copilot/codex-5.3
```

This uses `gh copilot` in non-interactive JSON mode and targets the working
`gpt-5.3-codex` lane.

## 5. Compile and Evaluate the DSPy Router

```bash
npm run dspy:compile
npm run dspy:eval
```

Outputs:

- `catalog/dspy/dspy_category_router.json`
- `catalog/dspy/dspy_router_status.json`
- `catalog/dspy/dspy_eval_summary.json`
- `catalog/dspy/dspy_eval_predictions.jsonl`

## 6. Optional Hard-Negative Diagnostics

To score the confusable-neighbor diagnostic split:

```bash
.venv/bin/python scripts/dspy_eval_router.py --repo-root . --baseline-only --split hard_negative
.venv/bin/python scripts/dspy_eval_router.py --repo-root . --dspy-only --split hard_negative
```

You can repeat `--split` to score both `eval` and `hard_negative` in one run.

## Notes

- `hermes-abstain.jsonl` is preserved for validation and future router work, but abstain classification is not implemented in the current v1 router.
- If compile or eval fails, inspect `catalog/dspy/dspy_router_status.json` or `catalog/dspy/dspy_eval_summary.json` first; both files are intended to be user-facing diagnostics.
- Observed repo-local Codex-backed run on 2026-03-11:
  - compile with `--train-limit 4` succeeded in about `40.40s`
  - eval with `--eval-limit 8` succeeded in about `165.52s`
  - the limited eval scored `5/8` correct (`62.5%`)
- Completed full Codex-backed compile+eval on 2026-03-11:
  - backend: `DSPY_MODEL=codex-exec/default`, `DSPY_TEMPERATURE=0`, `DSPY_MAX_TOKENS=256`
  - compile: 239s (~4 min), bootstrapped 8 demos from 11 examples
  - eval: 2544s (~42 min), scored all 104 eval rows
  - **result: 95/104 = 91.3% accuracy** (vs baseline 82/104 = 78.8%)
  - total wall clock: ~46 min as an unattended background job
  - runner script: `bash scripts/dspy_full_run.sh` with env vars set
  - 9 misclassifications, several arguably debatable gold labels (e.g. hold-monster/hold-person classified as containment instead of influence)
