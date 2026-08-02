#!/usr/bin/env bash
set -u

echo "## Cold-Toolchain Report — $(date +%F)"
echo ""

THRESHOLD_DAYS="${THRESHOLD_DAYS:-21}"

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Not inside a Git repository."
  exit 1
fi

patterns=(
  ":(glob)**/*.kicad_sch|KiCad schematic"
  ":(glob)**/*.kicad_pcb|KiCad PCB"
  ":(glob)**/*.py|Python"
  ":(glob)**/*.c|C"
  ":(glob)**/*.cpp|C++"
  ":(glob)**/*.h|Headers"
  ":(glob)**/*.ld|Linker scripts"
  ":(glob)**/*.asc|LTspice"
  ":(glob)**/*.step|CAD STEP"
  ":(glob)**/*.stl|CAD STL"
)

now=$(date +%s)

for item in "${patterns[@]}"; do
  pathspec="${item%%|*}"
  label="${item##*|}"
  epoch=$(git log -1 --format=%ct -- "$pathspec" 2>/dev/null | head -n 1)
  if [ -z "$epoch" ]; then
    echo "- $label: never touched"
    continue
  fi
  days=$(( (now - epoch) / 86400 ))
  if [ "$days" -gt "$THRESHOLD_DAYS" ]; then
    echo "- ⚠️ COLD $label: last touched $days day(s) ago"
  else
    echo "- ✅ $label: last touched $days day(s) ago"
  fi
done