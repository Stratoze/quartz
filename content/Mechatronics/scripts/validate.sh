#!/usr/bin/env bash
# Roadmap validation. Not project validation.
set -u

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT" || exit 1

fail=0

say()  { printf '%s\n' "$*"; }
err()  { printf 'ERROR: %s\n' "$*" >&2; fail=1; }
warn() { printf 'WARN: %s\n' "$*" >&2; }

say "## Roadmap Validation"
say "root: $ROOT"
say ""

required_files=(
  "README.md"
  "ROADMAP.md"
  "IDEAS.md"
  "RESOURCE_INDEX.md"
)

required_dirs=(
  "journal"
  "milestones"
  "templates"
  "scripts"
  "resources"
)

milestone_files=(
  "milestones/00_foundations.md"
  "milestones/01_signals_actuators_dynamics.md"
  "milestones/02_embedded_realtime_control.md"
  "milestones/03_mech_pcb_verification.md"
  "milestones/04_capstone_integration.md"
  "milestones/05_portfolio_delivery.md"
)

resource_files=(
  "resources/FAQ.md"
  "resources/DAILY_CARD.md"
  "resources/CONVENTIONS.md"
  "resources/OPERATING_SYSTEM.md"
  "resources/SAFETY_CARD.md"
  "resources/FIELD_NOTES.md"
)

say "Checking core files..."
for f in "${required_files[@]}"; do
  [ -f "$f" ] || err "missing file: $f"
done

say "Checking directories..."
for d in "${required_dirs[@]}"; do
  [ -d "$d" ] || err "missing folder: $d"
done

say "Checking milestone files..."
for f in "${milestone_files[@]}"; do
  [ -f "$f" ] || err "missing milestone: $f"
done

say "Checking resource files..."
for f in "${resource_files[@]}"; do
  [ -f "$f" ] || err "missing resource: $f"
done

say "Checking Bash syntax..."
for f in scripts/*.sh; do
  [ -e "$f" ] || continue
  bash -n "$f" || err "bash syntax failed: $f"
done

say "Checking for CRLF line endings..."
crlf_count=0
while IFS= read -r -d '' f; do
  if grep -qP '\r$' "$f" 2>/dev/null; then
    warn "CRLF in: $f"
    crlf_count=$((crlf_count + 1))
  fi
done < <(find . -type f \( -name "*.sh" -o -name "*.md" -o -name "*.csv" -o -name "*.txt" -o -name "*.py" \) -not -path "./.clipper/*" -print0 2>/dev/null)
if [ "$crlf_count" -gt 0 ]; then
  warn "$crlf_count file(s) have CRLF. Fix: sed -i 's/\\r\$//' <file>"
fi

say "Checking wikilink file targets..."
if command -v python3 >/dev/null 2>&1; then
  python3 - <<'PY' || fail=1
from pathlib import Path
import re

root = Path('.')

# Build index: stem -> path, and relative path string -> path
# Obsidian resolves [[NAME]] by filename regardless of folder.
md_by_stem = {}
md_by_relpath = {}
for f in root.rglob('*.md'):
    if '.clipper' in str(f):
        continue
    md_by_stem[f.stem] = f
    md_by_relpath[str(f.with_suffix('')).replace('\\', '/')] = f
    md_by_relpath[str(f).replace('\\', '/')] = f

missing = []
for p in root.rglob('*.md'):
    if '.clipper' in str(p):
        continue
    text = p.read_text(encoding='utf-8')
    for m in re.finditer(r'\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\\?\|[^\]]+)?\]\]', text):
        target = m.group(1).strip()
        # Check by relative path first, then by stem
        if target in md_by_relpath:
            continue
        if target + '.md' in md_by_relpath:
            continue
        stem = Path(target).stem
        if stem in md_by_stem:
            continue
        missing.append((str(p), target))

if missing:
    for p, target in missing:
        print(f'ERROR: missing wikilink target in {p}: [[{target}]]')
    raise SystemExit(1)
else:
    print('  all wikilink targets resolve')
PY
else
  warn "python3 not found; skipped wikilink check"
fi

say "Checking ROADMAP heading links..."
if command -v python3 >/dev/null 2>&1; then
  python3 - <<'PY'
from pathlib import Path
import re

roadmap = Path('ROADMAP.md')
if not roadmap.exists():
    raise SystemExit(0)

text = roadmap.read_text(encoding='utf-8')
broken = []

for m in re.finditer(r'\[\[([^\]|#]+)#([^\]|]+?)(?:\\?\|[^\]]+)?\]\]', text):
    file_target = m.group(1).strip()
    # Strip trailing backslash from Obsidian's \| alias syntax
    heading = m.group(2).strip().rstrip('\\')
    file_path = Path(file_target + '.md')
    if not file_path.exists():
        broken.append((file_target, heading, 'file missing'))
        continue
    content = file_path.read_text(encoding='utf-8')
    headings_in_file = re.findall(r'^#{1,6}\s+(.+)$', content, re.MULTILINE)
    if heading not in headings_in_file:
        broken.append((file_target, heading, 'heading not found'))

if broken:
    for f, h, reason in broken:
        print(f'ERROR: {f}#{h} -- {reason}')
    raise SystemExit(1)
else:
    print('  all ROADMAP heading links resolve')
PY
  [ $? -ne 0 ] && fail=1
else
  warn "python3 not found; skipped heading check"
fi

say "Checking landmine tags..."
if command -v python3 >/dev/null 2>&1; then
  python3 - <<'PY'
from pathlib import Path
import re

valid_tags = {'HYPOTHESIS', 'COMMUNITY', 'DATASHEET', 'VERIFIED', 'RETIRED'}
issues = []

for p in sorted(Path('milestones').glob('*.md')):
    text = p.read_text(encoding='utf-8')
    for m in re.finditer(r'\[([A-Z][A-Z ]+?)(?:\s*\u2014\s*[^\]]+)?\]', text):
        tag = m.group(1).strip()
        if tag not in valid_tags:
            issues.append((str(p), m.group(0), tag))

if issues:
    for p, full, tag in issues:
        print(f'WARN: unknown landmine tag in {p}: {full} (base: "{tag}")')
else:
    print('  all landmine tags valid')
PY
else
  warn "python3 not found; skipped landmine tag check"
fi

say ""
if [ "$fail" -eq 0 ]; then
  say "Roadmap validation passed."
else
  say "Roadmap validation failed."
fi
exit "$fail"