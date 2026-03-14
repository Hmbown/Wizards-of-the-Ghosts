# DSPy Hermes Spell Corpus Phase 1 Implementation Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** Build a deterministic, DSPy-friendly Hermes spell corpus artifact from Wizards of the Ghosts source-of-truth files and generated Hermes skills.

**Architecture:** Add one stdlib-only Python extractor that reads `catalog/canon.json`, `catalog/blueprints.json`, and `generated/hermes/*/*/SKILL.md`, then writes normalized artifacts under `catalog/dspy/`. Keep generated skills read-only and treat `catalog/blueprints.json` as the semantic source of truth.

**Tech Stack:** Python 3 stdlib, existing Node-based repo pipeline, JSON/JSONL artifacts.

---

### Task 1: Create Phase 1 extractor script

**Objective:** Add a deterministic extractor that can build normalized Hermes corpus artifacts without external dependencies.

**Files:**
- Create: `scripts/dspy_extract_hermes_corpus.py`

**Step 1: Write the script skeleton**
- Add argparse entrypoint
- Accept `--repo-root`
- Define helpers for loading JSON and scanning generated skill files

**Step 2: Implement deterministic loaders**
- Read:
  - `catalog/canon.json`
  - `catalog/blueprints.json`
- Build:
  - canon-by-slug lookup
  - Hermes category-by-slug mapping
  - Hermes browse-path mapping
  - refused-entry set

**Step 3: Implement generated SKILL.md scan**
- Parse frontmatter/body split
- Extract:
  - tags
  - section names
  - whether Setup section exists
  - explicit confirmation heuristic
  - example invocation
  - env-var mentions when present

**Step 4: Build normalized rows**
Each row should include at minimum:
- slug
- name
- kind
- canonical_id
- category slug/title/description
- reality_tier
- literalness
- provider_targets
- tagline
- description
- when_to_use
- workflow
- deliverables
- guardrails
- default_prompt
- openai_short_description
- tags
- requires_env
- requires_bins
- primary_env
- has_setup_section
- requires_explicit_confirmation
- featured_entry
- browse_paths
- refused_for_hermes
- canon source metadata
- generated_skill_path

**Step 5: Write outputs**
Create under `catalog/dspy/`:
- `spells_master.jsonl`
- `categories.json`
- `browse_paths.json`
- `refusal_set.json`
- `hermes_phase1_summary.json`

**Step 6: Verify**
Run:
- `python3 scripts/dspy_extract_hermes_corpus.py --repo-root .`
Expected:
- summary JSON printed
- output files created under `catalog/dspy/`

### Task 2: Document Phase 1 artifacts

**Objective:** Explain what the DSPy artifact directory contains and how to regenerate it.

**Files:**
- Create: `catalog/dspy/README.md`

**Step 1: Describe purpose**
- State this directory holds deterministic and model-generated DSPy artifacts
- Clarify source-of-truth remains in `catalog/` and renderer logic

**Step 2: Document current files**
- Describe each Phase 1 artifact in one line

**Step 3: Add regeneration command**
- `python3 scripts/dspy_extract_hermes_corpus.py --repo-root .`

### Task 3: Save the implementation plan in-repo

**Objective:** Preserve the phased plan for follow-on DSPy work.

**Files:**
- Create: `docs/plans/2026-03-11-dspy-hermes-phase1.md`

**Step 1: Record immediate scope**
- Phase 1 is deterministic extraction only
- No model calls yet

**Step 2: Record next phases**
- Phase 2: query generation via subagents
- Phase 3: DSPy category router
- Phase 4: overlap/hard-negative analysis
- Phase 5: held-out gold eval

### Task 4: Run extraction and inspect outputs

**Objective:** Prove the extractor works on the real repo.

**Files:**
- Modify indirectly by running the extractor and generating outputs

**Step 1: Run extractor**
Run:
- `python3 scripts/dspy_extract_hermes_corpus.py --repo-root .`

**Step 2: Inspect summary**
Check:
- total Hermes entries is 122
- refused count is 5
- category counts match current shelves

**Step 3: Spot-check output shape**
Inspect:
- first few lines of `catalog/dspy/spells_master.jsonl`
- `catalog/dspy/hermes_phase1_summary.json`

### Task 5: Prepare Phase 2 handoff

**Objective:** Make the next DSPy steps obvious.

**Files:**
- No new file required beyond the plan unless needed later

**Step 1: Define Phase 2 outputs**
Planned artifacts:
- `catalog/dspy/hermes-train-queries.jsonl`
- `catalog/dspy/hermes-eval-set.jsonl`
- `catalog/dspy/hermes-hard-negatives.jsonl`

**Step 2: Define subagent batching strategy**
- Batch by category first
- Use one subagent per category or category pair
- Generate positives, ambiguities, and abstain/refusal cases

**Step 3: Define Phase 3 target**
- Hierarchical DSPy router:
  - safety gate
  - category router
  - spell retriever/ranker

## Verification Checklist

- `python3 scripts/dspy_extract_hermes_corpus.py --repo-root .`
- confirm `catalog/dspy/spells_master.jsonl` exists
- confirm `catalog/dspy/hermes_phase1_summary.json` exists
- confirm Hermes entry count is 122
- confirm refused count is 5
- confirm no generated skill files were edited

## Notes

- Do not use `.hermes/skills` as modeling input; it mirrors generated Hermes output and risks duplicate leakage.
- Do not mutate `generated/` directly.
- Keep Phase 1 dependency-free; defer DSPy package setup until Phase 2/3.
