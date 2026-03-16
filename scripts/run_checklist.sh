#!/usr/bin/env bash
# Print the daily checklist for AI Data Engineer Gita workflow.
# Run from repo root: ./scripts/run_checklist.sh
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
CHECKLIST="$REPO_ROOT/.cursor/checklist.md"
if [[ -f "$CHECKLIST" ]]; then
  cat "$CHECKLIST"
else
  echo "Checklist not found: $CHECKLIST"
  exit 1
fi
exit 0
