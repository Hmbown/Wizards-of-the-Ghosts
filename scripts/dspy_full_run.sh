#!/usr/bin/env bash
# Full DSPy compile + eval run with a local CLI backend
# Run: DSPY_MODEL=qwen/default DSPY_TEMPERATURE=0 DSPY_MAX_TOKENS=256 bash scripts/dspy_full_run.sh
set -euo pipefail
cd "$(dirname "$0")/.."

export DSPY_MODEL="${DSPY_MODEL:-qwen/default}"
export DSPY_TEMPERATURE="${DSPY_TEMPERATURE:-0}"
export DSPY_MAX_TOKENS="${DSPY_MAX_TOKENS:-256}"

echo "=== DSPy Full Run ==="
echo "Model: $DSPY_MODEL"
echo "Temperature: $DSPY_TEMPERATURE"
echo "Max tokens: $DSPY_MAX_TOKENS"
echo "Started: $(date)"
echo ""

echo "--- Phase 3a: Compile (baseline + DSPy router) ---"
COMPILE_START=$(date +%s)
.venv/bin/python scripts/dspy_build_router.py --repo-root .
COMPILE_END=$(date +%s)
echo ""
echo "Compile finished in $((COMPILE_END - COMPILE_START)) seconds"
echo ""

echo "--- Phase 3b: Evaluate DSPy router ---"
EVAL_START=$(date +%s)
.venv/bin/python scripts/dspy_eval_router.py --repo-root . --dspy-only
EVAL_END=$(date +%s)
echo ""
echo "Eval finished in $((EVAL_END - EVAL_START)) seconds"
echo ""

echo "--- Phase 3b: Evaluate baseline (for comparison) ---"
.venv/bin/python scripts/dspy_eval_router.py --repo-root . --baseline-only
echo ""

echo "=== Done ==="
echo "Total: $((EVAL_END - COMPILE_START)) seconds"
echo "Finished: $(date)"
