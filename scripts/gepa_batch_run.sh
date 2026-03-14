#!/usr/bin/env bash
# Batch GEPA optimization runner using Qwen CLI backend.
# Usage: bash scripts/gepa_batch_run.sh [--slugs slug1,slug2,...] [--limit N] [--dry-run]
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PYTHON="${REPO_ROOT}/.venv/bin/python"
LOG_DIR="${REPO_ROOT}/catalog/gepa/logs"
BATCH_LOG="${LOG_DIR}/batch_$(date +%Y%m%d_%H%M%S).log"
mkdir -p "$LOG_DIR"

export DSPY_MODEL="${DSPY_MODEL:-qwen/default}"
export GEPA_REFLECTION_MODEL="${GEPA_REFLECTION_MODEL:-qwen/default}"
export DSPY_QWEN_TIMEOUT_SECONDS="${DSPY_QWEN_TIMEOUT_SECONDS:-180}"

LIMIT=0
DRY_RUN=false
SLUGS=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --slugs) SLUGS="$2"; shift 2 ;;
        --limit) LIMIT="$2"; shift 2 ;;
        --dry-run) DRY_RUN=true; shift ;;
        *) echo "Unknown arg: $1"; exit 1 ;;
    esac
done

log() {
    echo "[$(date +%H:%M:%S)] $*" | tee -a "$BATCH_LOG"
}

log "=== GEPA Batch Run ==="
log "Backend: $DSPY_MODEL"
log "Log: $BATCH_LOG"

# Get list of slugs to process
if [ -n "$SLUGS" ]; then
    IFS=',' read -ra SLUG_LIST <<< "$SLUGS"
else
    # All non-refusal, non-already-optimized spells with benchmark data
    mapfile -t SLUG_LIST < <("$PYTHON" -c "
import json, os
bp = json.load(open('catalog/blueprints.json'))
refusal = {'dominate-person','dominate-monster','modify-memory','geas','compulsion'}
for e in bp['entries']:
    slug = e['slug']
    if slug in refusal:
        continue
    train = f'catalog/gepa/spells/{slug}/train.jsonl'
    status_f = f'catalog/gepa/spells/{slug}/optimization_status.json'
    # Skip if already optimized
    if os.path.exists(status_f):
        try:
            s = json.load(open(status_f))
            if s.get('status') in ('optimized', 'ok'):
                continue
        except: pass
    # Skip if no benchmark data
    if not os.path.exists(train) or os.path.getsize(train) < 10:
        continue
    print(slug)
")
fi

TOTAL=${#SLUG_LIST[@]}
if [ "$LIMIT" -gt 0 ] && [ "$LIMIT" -lt "$TOTAL" ]; then
    TOTAL=$LIMIT
fi
log "Processing $TOTAL spells"

SUCCEEDED=0
FAILED=0
SKIPPED=0

for i in "${!SLUG_LIST[@]}"; do
    if [ "$LIMIT" -gt 0 ] && [ "$((i+1))" -gt "$LIMIT" ]; then
        break
    fi

    SLUG="${SLUG_LIST[$i]}"
    log "[$((i+1))/$TOTAL] Optimizing: $SLUG"

    if $DRY_RUN; then
        log "  [dry-run] Would optimize $SLUG"
        continue
    fi

    # Run optimization
    if "$PYTHON" scripts/gepa_optimize_spell.py --slug "$SLUG" >> "$BATCH_LOG" 2>&1; then
        log "  OK: $SLUG optimized"
        SUCCEEDED=$((SUCCEEDED + 1))
    else
        log "  FAIL: $SLUG optimization failed (see log)"
        FAILED=$((FAILED + 1))
    fi
done

log "=== Batch Complete ==="
log "Succeeded: $SUCCEEDED  Failed: $FAILED  Skipped: $SKIPPED"
log "Log saved to: $BATCH_LOG"
