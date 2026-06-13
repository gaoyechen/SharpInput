#!/bin/bash
# SharpInput Demo Recording Script
# Usage: bash scripts/record-demo.sh
#
# Prerequisites:
#   - Hermes Agent installed and configured
#   - sharpinput skill installed in $LOCALAPPDATA/hermes/skills/sharpinput
#   - vhs (https://github.com/charmbracelet/vhs) for GIF recording
#
# To record GIF:
#   vhs scripts/demo.tape

set -euo pipefail

SKILL_DIR="$(cd "$(dirname "$0")/.." && pwd)"
HERMES_SKILLS_DIR="${LOCALAPPDATA:-$HOME/.local/share}/hermes/skills"

echo "=== SharpInput Demo ==="
echo ""

# Test 1: Level 0 Quick Rewrite
echo "--- Test 1: Level 0 Quick Rewrite ---"
hermes chat --skills sharpinput \
  -q "帮我优化：怎么学 RUP？" \
  -Q 2>/dev/null || echo "[SKIP] hermes chat not available in this environment"

echo ""
echo "--- Test 2: Level 2 Pressure (AI Subscription) ---"
hermes chat --skills sharpinput \
  -q "帮我优化：ChatGPT Plus 和 Claude Pro 选哪个？" \
  -Q 2>/dev/null || echo "[SKIP] hermes chat not available in this environment"

echo ""
echo "--- Test 3: Non-trigger (should NOT activate SharpInput) ---"
hermes chat --skills sharpinput \
  -q "直接帮我写一个 Python 排序算法" \
  -Q 2>/dev/null || echo "[SKIP] hermes chat not available in this environment"

echo ""
echo "=== Demo Complete ==="
