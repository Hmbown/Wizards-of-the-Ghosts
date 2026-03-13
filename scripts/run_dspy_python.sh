#!/usr/bin/env bash
set -euo pipefail

if [[ ! -x ".venv/bin/python" ]]; then
  echo "Missing .venv/bin/python. Run: uv venv .venv && uv pip install --python .venv/bin/python -r requirements-dspy.txt" >&2
  exit 1
fi

exec ./.venv/bin/python "$@"
