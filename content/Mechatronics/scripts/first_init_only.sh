#!/usr/bin/env bash
set -u

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT" || exit 1

force="no"
if [ "${1:-}" = "--force" ]; then
  force="yes"
fi

if ! command -v git >/dev/null 2>&1; then
  echo "git not found. Install Git first."
  exit 1
fi

if [ -d .git ] && [ "$force" != "yes" ]; then
  echo "This folder already has .git/."
  echo "Refusing to run first-init again."
  echo "If you really mean it, run: ./scripts/first_init_only.sh --force"
  exit 1
fi

echo "Setting script permissions..."
chmod +x scripts/*.sh 2>/dev/null || true

echo "Ensuring required directories exist..."
required_dirs=(
  "journal"
  "milestones"
  "templates"
  "firmware/esp32"
  "firmware/stm32"
  "simulations/python"
  "simulations/ltspice"
  "hardware/wiring"
  "hardware/test_rigs"
  "data/raw"
  "data/processed"
  "cad"
  "pcb"
  "docs/datasheets"
  "docs/app_notes"
  "docs/captures"
  "portfolio"
  "archive"
)

for d in "${required_dirs[@]}"; do
  mkdir -p "$d"
done

if [ ! -d .git ]; then
  echo "Initializing Git repo..."
  git init
else
  echo "Git repo already exists; continuing because --force was provided."
fi

echo "Running validation..."
./scripts/validate.sh || {
  echo "Validation failed. Fix errors before first commit."
  exit 1
}

if git rev-parse --verify HEAD >/dev/null 2>&1; then
  echo "Repo already has at least one commit. No initial commit created."
else
  echo "Creating initial commit..."
  git add .
  if git commit -m "Initialize mechatronics roadmap"; then
    echo "Initial commit created."
  else
    echo "Commit failed. You may need to configure Git identity:"
    echo "  git config user.name 'Your Name'"
    echo "  git config user.email 'you@example.com'"
    echo "Then run:"
    echo "  git add ."
    echo "  git commit -m 'Initialize mechatronics roadmap'"
    exit 1
  fi
fi

echo ""
echo "Done. Next: open README.md, read DAILY_CARD.md, then start Phase 0."