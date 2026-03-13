# GEPA Spell Optimization Spec

This document defines the minimum contract for spell-level GEPA work in `wizardsoftheghosts`.

## Goal

Optimize spell behavior, not category routing.

The unit of work is one spell. The optimizing agent should improve how the spell behaves as a prompt system under realistic prompts, then promote winning changes back into `catalog/blueprints.json`.

## Artifact Contract

Shared contract artifacts live under:

```text
catalog/gepa/schema/
catalog/gepa/rubric-packs/
```

The rubric-pack manifest at `catalog/gepa/rubric-packs/index.json` is part of that shared contract and should validate alongside the individual category packs.

For each spell, the agent works under:

```text
catalog/gepa/spells/<slug>/
```

Required artifacts:
- `spell.json`
- `train.jsonl`
- `eval.jsonl`
- `confusables.jsonl`
- `rubric.json`
- `promotion_patch.json`
- `optimization_status.json`
- `baseline_eval.json`
- `optimized_eval.json`
- `optimized_module.json`

## Spell-Level Workflow

1. Bootstrap the spell workspace.
2. Resolve the shared contract in this order:
   - `catalog/gepa/schema/scoring-contract.json`
   - `catalog/gepa/rubric-packs/<category>.json`
   - `catalog/gepa/spells/<slug>/rubric.json`
3. Fill in `train.jsonl`, `eval.jsonl`, `confusables.jsonl`, and specialize `rubric.json`.
4. Run GEPA optimization for the spell.
5. Run held-out evaluation and compare baseline vs optimized scores.
6. If the optimized spell is genuinely better, write reviewed changes into `promotion_patch.json`.
7. Promote the patch back into `catalog/blueprints.json`.
8. Rebuild generated surfaces and verify the repo.

## Benchmark Expectations

Each spell benchmark should contain:
- positive prompts that clearly fit the spell
- confusable prompts that resemble neighboring spells
- held-out prompts that test generalization instead of memorized phrasing
- out-of-scope or risky prompts when refusal or boundary handling matters

Each row should use the shared benchmark contract:
- `prompt_id`
- `prompt`
- `scenario_type`
- `risk_level`
- `target_outcome`
- `expected_behavior`
- `must_include`
- `must_not_include`
- `judge_focus`
- `safety_flags`

The row contract lives in `catalog/gepa/schema/benchmark-row.schema.json`.

## Scoring Expectations

At minimum, the rubric should measure:
- deterministic checks with low evaluator drift
- judge-model criteria for spell identity and usefulness
- optional human review gates for higher-risk prompts or spell traits

Deterministic checks should cover:
- required section presence
- row and rubric `must_include` coverage
- row and rubric `must_not_include` compliance
- behavior gates like refusal, clarification, redirect, or live-action caution

Judge-model criteria should cover:
- deliverable completeness
- guardrail visibility
- reality-boundary honesty
- separation from neighboring spells

Agents should not optimize for prettier prose if the spell gets less precise, less safe, or less distinct.

## Promotion Surface

Only these blueprint fields should be changed by the scaffolded promotion path:
- `tagline`
- `description`
- `when_to_use`
- `workflow`
- `deliverables`
- `guardrails`
- `default_prompt`
- `openai.short_description`

Generated files under `generated/` remain build artifacts.

## Review Policy

Agent-automerge is acceptable for:
- clearly software-first, low-risk, metaphorical spells
- improvements that raise eval score without weakening guardrails
- changes that do not materially broaden live-action claims

Human review is required for:
- literal or hybrid spells that can touch live systems, accounts, alerts, or devices
- influence-heavy spells
- coercive, memory, or deception-adjacent spells
- any change that broadens the claimed runtime capability
- any spell where the optimized version scores better but becomes less honest

The shared human-review gate also escalates prompts tagged with high-risk safety flags, risky scenarios, or live-action expected behavior.

## Inheritance Model

Every spell issue should inherit and specialize, not replace, the shared rubric stack:

1. Start with `catalog/gepa/schema/scoring-contract.json`.
2. Inherit the category pack from `catalog/gepa/rubric-packs/<category>.json`.
3. Keep `catalog/gepa/spells/<slug>/rubric.json` focused on:
   - `spell_focus`
   - `confusable_with`
   - `judge_examples`
   - `row_overrides`

Use spell-local overrides to add spell-specific `global_must_include`, `global_must_not_include`, judge criteria, or review notes. Do not fork the whole category pack unless the category boundary itself is wrong.

Category packs are stored in their raw authored format and validated against `catalog/gepa/schema/rubric-pack.schema.json`. `scripts/gepa_common.py` is responsible for validating that raw shape and normalizing it into the compatibility fields used by the current GEPA runtime helpers.

## Recommended First Wave

Use the ranked GEPA Linear backlog as the default order of operations. The first wave should stay small enough for tight review:
- ranks 1-12 as the initial batch
- one or two concrete pilot spells before broader batching if the workflow changes materially

## Operational Notes

- The repo currently uses `dspy.GEPA` through the existing Python environment.
- Task LM and reflection LM may be different; the reflection LM should usually be the stronger one.
- Promotion is intentionally explicit so agents cannot silently rewrite the spellbook.
