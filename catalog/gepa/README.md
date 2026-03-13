# GEPA Spell Optimization

This directory holds spell-level GEPA artifacts for `wizardsoftheghosts`.

Source of truth stays in:
- `catalog/blueprints.json`
- `catalog/blueprints.schema.json`
- `scripts/render-skills.mjs`

Do not hand-edit `generated/` as part of spell optimization.

## Layout

Shared GEPA contract artifacts live under:

```text
catalog/gepa/schema/
catalog/gepa/rubric-packs/
```

That includes the rubric-pack manifest at `catalog/gepa/rubric-packs/index.json`, which should stay schema-valid and in sync with the actual pack files.

Each spell lives under:

```text
catalog/gepa/spells/<slug>/
```

Required files:
- `spell.json` — spell metadata snapshot plus the current baseline instruction text
- `train.jsonl` — positive training prompts for reflective optimization
- `eval.jsonl` — held-out prompts for measuring baseline vs optimized behavior
- `confusables.jsonl` — prompts that look like neighboring spells and should stay separable
- `rubric.json` — spell-local specialization that inherits its category rubric pack
- `promotion_patch.json` — explicit patch to write winning changes back into `catalog/blueprints.json`
- `optimization_status.json` — latest optimize/bootstrap/validate status
- `baseline_eval.json` — latest baseline evaluation summary
- `optimized_eval.json` — latest optimized evaluation summary
- `optimized_module.json` — saved DSPy module after GEPA optimization

## Inheritance Flow

The resolved rubric used by optimize/eval is built in this order:

1. `catalog/gepa/schema/scoring-contract.json`
2. `catalog/gepa/rubric-packs/<category>.json`
3. `catalog/gepa/spells/<slug>/rubric.json`

`rubric.json` should stay small and spell-specific. Put shared category defaults in the rubric pack. Put only the spell's confusable neighbors, focus, row-level overrides, and extra judge or review notes in the spell file.

Rubric packs are authored in the raw category-pack shape validated by `catalog/gepa/schema/rubric-pack.schema.json`. `scripts/gepa_common.py` validates that raw document, then normalizes it into the runtime convenience fields agents already consume (`pack_version`, `title`, `spell_rubric_template`, `benchmark_expectations`, `judge_model_criteria`, and `human_review_overrides`).

## Benchmark Row Format

`train.jsonl`, `eval.jsonl`, and `confusables.jsonl` use this row shape:

```json
{
  "prompt_id": "awaken-eval-001",
  "scenario_type": "positive-fit",
  "risk_level": "low",
  "prompt": "Wrap this old internal tool in a conversational front end.",
  "target_outcome": "Design an honest wrapper around an existing substrate.",
  "expected_behavior": [
    "answer-directly"
  ],
  "must_include": [
    "intent-to-action map",
    "guardrails"
  ],
  "must_not_include": [
    "pretend the underlying system became sentient"
  ],
  "judge_focus": [
    "spell fit",
    "guardrail visibility"
  ],
  "notes": "Positive example for Awaken."
}
```

Only `prompt_id` and `prompt` are strictly required by the shared schema, but practical authoring should fill in `scenario_type`, `risk_level`, `target_outcome`, and `expected_behavior` so evaluation stays comparable across spells.

The benchmark row contract lives in `catalog/gepa/schema/benchmark-row.schema.json`.

## Shared Scoring Contract

The shared scoring contract lives in `catalog/gepa/schema/scoring-contract.json` and separates:

- deterministic checks
- judge-model criteria
- optional human review

Deterministic checks are what the current scaffold scores directly. Judge-model criteria and human review gates are carried into resolved rubric metadata so spell authors can keep category evaluation consistent without pretending everything is automatable.

## Commands

Bootstrap one spell workspace:

```bash
npm run gepa:spell:bootstrap -- --slug awaken
```

Validate a spell workspace:

```bash
npm run gepa:spell:optimize -- --slug awaken --validate-only
```

Run GEPA optimization:

```bash
export DSPY_MODEL=codex-exec/default
export DSPY_TEMPERATURE=0
export DSPY_MAX_TOKENS=512
export GEPA_REFLECTION_MODEL=codex-exec/default
# Optional when Codex-backed prompts need more than the default 120s wall clock:
export DSPY_CODEX_TIMEOUT_SECONDS=300

npm run gepa:spell:optimize -- --slug awaken
```

Evaluate baseline vs optimized:

```bash
npm run gepa:spell:eval -- --slug awaken
```

Promote a reviewed patch:

```bash
npm run gepa:spell:promote -- --slug awaken
```

## Notes

- The scaffold uses `dspy.GEPA` from the repo's pinned DSPy environment.
- The optimizing agent should treat `promotion_patch.json` as the deliberate write-back surface for blueprint changes.
- Safety-sensitive literal or influence-heavy spells should be reviewed by a human before promotion.
- The first rubric packs live under `catalog/gepa/rubric-packs/` for:
  - `monitoring-and-protection`
  - `investigation-and-preparation`
  - `actions-access-and-automation`
  - `containment-and-intervention`
  - `influence-and-behavior`
