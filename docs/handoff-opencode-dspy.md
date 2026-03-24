# Handoff: OpenCode DSPy/GEPA Integration

You're picking up work in `/home/hmbown/Projects/wizards-of-the-ghosts`. The goal is to use DSPy/GEPA to optimize spell prompts using the OpenCode CLI as the LLM backend (instead of Codex).

## What's done

- `scripts/dspy_opencode_lm.py` — new OpenCode LM backend that calls `opencode run --format json --model <model>`
- `scripts/dspy_common.py` — updated to recognize `opencode/` model prefixes, probe the backend, and instantiate the OpenCode LM
- All 44 existing tests still pass
- `DSPY_MODEL=opencode/mimo-v2-pro-free npm run dspy:validate` succeeds — backend probe returns reachable=true

## What's broken

Running `npm run gepa:spell:optimize` with `opencode/mimo-v2-pro-free` fails for two reasons:

1. **Timeout**: Default is 120s (`DSPY_OPENCODE_TIMEOUT_SECONDS`). DSPy sends massive prompts (full instruction + demos + few-shot examples). Mimo takes too long on these. Need to either increase timeout significantly (300s+) or reduce prompt size.

2. **JSON parse failures**: DSPy's ChatAdapter expects the model to output a JSON object with `reasoning` and `response` fields. Mimo outputs free-form markdown instead. DSPy falls back to JSONAdapter which also fails. This is the core issue — the model doesn't follow the structured output format.

## Fix options to try

- **Option A**: Switch DSPy to use `ChatAdapter` only (not falling back to JSON), and add a post-processing step that extracts the response from free-form text
- **Option B**: Try `opencode/gpt-5-nano` or another model that follows JSON instructions better
- **Option C**: Override DSPy's adapter to handle the OpenCode backend differently — maybe parse the `[[ ## response ## ]]` markers that DSPy includes in its prompts
- **Option D**: Write a custom DSPy adapter for OpenCode that handles its output quirks

## Key files

- `scripts/dspy_opencode_lm.py` — the LM backend (new)
- `scripts/dspy_common.py` — model resolution + probing (edited)
- `scripts/gepa_optimize_spell.py` — the GEPA optimizer that calls DSPy
- `scripts/gepa_common.py` — shared GEPA helpers
- `catalog/gepa/spells/detect-magic/` — already-bootstrapped spell workspace with train/eval data

## Commands to test

```bash
# Validate backend works
DSPY_MODEL=opencode/mimo-v2-pro-free npm run dspy:validate

# Run GEPA optimization (this is what fails)
DSPY_MODEL=opencode/mimo-v2-pro-free GEPA_REFLECTION_MODEL=opencode/mimo-v2-pro-free npm run gepa:spell:optimize -- --slug detect-magic --auto light --train-limit 2 --eval-limit 2 --confusable-limit 1

# Tests
.venv/bin/python -m pytest tests/test_dspy_workflow.py tests/test_gepa_workflow.py tests/test_gepa_rubric_contracts.py -q
```

## Available models via OpenCode

- `opencode/mimo-v2-pro-free` (current, free, but weak at structured output)
- `opencode/gpt-5-nano` (free, may follow JSON better)
- `zai-coding-plan/glm-5-turbo` (user has rate limits on this currently)

## Priority

Get one successful GEPA optimize+eval cycle running end-to-end with any model, then scale to all spells.
