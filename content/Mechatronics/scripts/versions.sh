#!/usr/bin/env bash
set -u

echo "## Toolchain Snapshot — $(date +%F)"
echo ""

check() {
  local label="$1"
  shift
  if command -v "$1" >/dev/null 2>&1; then
    local out
    out=$("$@" 2>&1 | head -n 1)
    echo "- $label: $out"
  else
    echo "- $label: not found"
  fi
}

check arm-none-eabi-gcc arm-none-eabi-gcc --version
check cmake cmake --version
check openocd openocd --version
check python3 python3 --version
check git git --version
check gcc gcc --version
check kicad-cli kicad-cli version
echo "- OS: $(uname -sr)"