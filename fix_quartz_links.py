#!/usr/bin/env python3
"""
fix_quartz_links.py — Scan a Quartz content directory, find broken wikilinks
and markdown links, fix them for Quartz's resolution model, and optionally
patch quartz.config.ts.

Quartz resolves links differently from Obsidian:
  - Wikilinks resolve by PATH relative to content/, not just by stem.
  - [[Daily Card]] only works if the stem is unique across content/.
  - [[Piano/Daily Card]] always works (path from content root).
  - Links to .pdf / binary files become dead <a> tags unless handled.
  - Files matched by ignorePatterns in quartz.config.ts are invisible.

Usage:
    python fix_quartz_links.py ~/quartz                  # dry-run
    python fix_quartz_links.py ~/quartz --fix            # apply fixes
    python fix_quartz_links.py ~/quartz --fix --config   # + patch quartz.config.ts
"""

import argparse, json, re, sys, os
from pathlib import Path
from collections import defaultdict

# ── regexes ──────────────────────────────────────────────────────────────────

WIKILINK_RE = re.compile(
    r"\[\["
    r"(?P<target>[^\]|#]+)"
    r"(?:#(?P<heading>[^\]|]+))?"
    r"(?:\|(?P<alias>[^\]]+))?"
    r"\]\]"
)

MDLINK_RE = re.compile(
    r"(?<!\!)\[(?P<text>[^\]]*)\]\((?P<path>[^)#]+)(?:#(?P<frag>[^)]*))?\)"
)

HEADING_RE = re.compile(r"^#{1,6}\s+(.+)$", re.MULTILINE)

BINARY_EXTS = {
    ".pdf", ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp",
    ".mp3", ".mp4", ".wav", ".ogg", ".zip", ".epub", ".csv",
}

SKIP_DIRS = {".git", "node_modules", ".obsidian", ".trash", "__archived__"}


# ── index ────────────────────────────────────────────────────────────────────

def build_index(content_dir):
    by_stem    = defaultdict(list)
    by_relpath = {}
    binaries   = set()

    for f in content_dir.rglob("*"):
        if any(p in SKIP_DIRS for p in f.relative_to(content_dir).parts):
            continue
        rel = str(f.relative_to(content_dir)).replace("\\", "/")

        if f.suffix.lower() in BINARY_EXTS:
            binaries.add(rel)
            continue
        if f.suffix != ".md":
            continue

        rel_no_ext = rel[:-3]
        by_stem[f.stem].append(rel_no_ext)
        by_relpath[rel_no_ext] = rel_no_ext

    return by_stem, by_relpath, binaries


def resolve_wikilink(target, by_stem, by_relpath):
    t = target.strip().replace("\\", "/")
    if t.endswith(".md"):
        t = t[:-3]
    if t in by_relpath:
        return by_relpath[t]
    cands = by_stem.get(Path(t).stem, [])
    if len(cands) == 1:
        return cands[0]
    low = Path(t).stem.lower()
    ci = [p for s, ps in by_stem.items() if s.lower() == low for p in ps]
    if len(ci) == 1:
        return ci[0]
    return None


def resolve_mdlink(path, source_file, content_dir, by_relpath, binaries):
    p = path.strip()
    if re.match(r"^https?://", p) or p.startswith("mailto:"):
        return "external"
    if p.startswith("/"):
        p = p[1:]
    else:
        source_dir = str(source_file.relative_to(content_dir).parent).replace("\\", "/")
        if source_dir != ".":
            p = source_dir + "/" + p
    p = os.path.normpath(p).replace("\\", "/")

    if p in binaries:
        return "binary"
    if p in by_relpath:
        return by_relpath[p]
    p_no_ext = p[:-3] if p.endswith(".md") else p
    if p_no_ext in by_relpath:
        return by_relpath[p_no_ext]
    for b in binaries:
        if b == p or b.endswith("/" + Path(p).name):
            return "binary"
    return None


def suggest(target, by_stem, by_relpath):
    t = target.strip().replace("\\", "/")
    if t.endswith(".md"):
        t = t[:-3]
    stem = Path(t).stem
    for v in (t + "s", t.rstrip("s")):
        vs = Path(v).stem
        if vs in by_stem and len(by_stem[vs]) == 1:
            return by_stem[vs][0]
    low = stem.lower()
    for s, ps in by_stem.items():
        if s.lower() == low and len(ps) == 1:
            return ps[0]
    parts = [p.lower() for p in t.split()]
    if len(parts) > 1:
        hits = [rp for rp in by_relpath
                if rp.lower().replace("/", " ").split()[-len(parts):] == parts]
        if len(hits) == 1:
            return hits[0]
    hits = [ps[0] for s, ps in by_stem.items()
            if low in s.lower() and len(ps) == 1]
    if len(hits) == 1:
        return hits[0]
    return None


def heading_exists(content_dir, relpath, heading):
    fp = content_dir / (relpath + ".md")
    if not fp.exists():
        return False
    text = fp.read_text(encoding="utf-8", errors="replace")
    norm = lambda h: re.sub(r"\s+", " ", h.strip().rstrip("#").strip()).lower()
    return norm(heading) in {norm(h) for h in HEADING_RE.findall(text)}


# ── scan ─────────────────────────────────────────────────────────────────────

def scan(quartz_root, fix=False):
    content_dir = quartz_root / "content"
    if not content_dir.is_dir():
        if (quartz_root / "quartz.config.ts").exists():
            sys.exit("error: content/ directory not found in quartz root")
        content_dir = quartz_root

    by_stem, by_relpath, binaries = build_index(content_dir)
    md_files = sorted(
        f for f in content_dir.rglob("*.md")
        if not any(p in SKIP_DIRS for p in f.relative_to(content_dir).parts)
    )

    broken_wiki, broken_md, heading_warn = [], [], []
    fixed_n = 0

    for md in md_files:
        text  = md.read_text(encoding="utf-8", errors="replace")
        lines = text.split("\n")
        out, changed = [], False

        for lno, line in enumerate(lines, 1):
            new = line

            # wikilinks
            for m in WIKILINK_RE.finditer(line):
                tgt     = m.group("target").strip()
                heading = m.group("heading")
                alias   = m.group("alias")
                if not tgt:
                    continue
                if any(tgt.lower().endswith(e) for e in BINARY_EXTS):
                    continue

                res = resolve_wikilink(tgt, by_stem, by_relpath)
                if res is None:
                    sug = suggest(tgt, by_stem, by_relpath)
                    broken_wiki.append((md, lno, m.group(0), tgt, sug))
                    if fix and sug:
                        a = alias
                        if a and a.strip() == tgt.strip():
                            a = None
                        repl = f"[[{sug}"
                        if heading: repl += f"#{heading}"
                        if a:       repl += f"|{a}"
                        repl += "]]"
                        new = new.replace(m.group(0), repl, 1)
                        changed = True
                        fixed_n += 1
                elif heading and not heading_exists(content_dir, res, heading):
                    heading_warn.append((md, lno, m.group(0), res, heading))

            # markdown links
            for m in MDLINK_RE.finditer(new):
                path = m.group("path").strip()
                if not path or path.startswith("#"):
                    continue
                res = resolve_mdlink(path, md, content_dir, by_relpath, binaries)
                if res is None:
                    broken_md.append((md, lno, m.group(0), path))

            out.append(new)

        if fix and changed:
            md.write_text("\n".join(out), encoding="utf-8")

    # report
    print(f"\n{'='*70}")
    print(f"  Quartz root:      {quartz_root}")
    print(f"  Content dir:      {content_dir}")
    print(f"  Files scanned:    {len(md_files)}")
    print(f"  Broken wikilinks: {len(broken_wiki)}")
    print(f"  Broken md links:  {len(broken_md)}")
    if fix:
        print(f"  Auto-fixed:       {fixed_n}")
        print(f"  Manual review:    {len(broken_wiki) - fixed_n}")
    print(f"  Heading warnings: {len(heading_warn)}")
    print(f"{'='*70}\n")

    if broken_wiki:
        print("BROKEN WIKILINKS")
        print("-" * 70)
        for fp, ln, link, tgt, sug in broken_wiki:
            rel = fp.relative_to(content_dir)
            tag = (f"  → FIXED [[{sug}]]" if fix and sug else
                   f"  (suggest: [[{sug}]])" if sug else
                   "  ⚠ MANUAL")
            print(f"  {rel}:{ln}  {link}{tag}")
        print()

    if broken_md:
        print("BROKEN MARKDOWN LINKS")
        print("-" * 70)
        for fp, ln, link, path in broken_md:
            rel = fp.relative_to(content_dir)
            print(f"  {rel}:{ln}  {link}")
        print()

    if heading_warn:
        print("HEADING NOT FOUND")
        print("-" * 70)
        for fp, ln, link, res, h in heading_warn:
            rel = fp.relative_to(content_dir)
            print(f"  {rel}:{ln}  {link}  →  #{h} missing in {res}.md")
        print()

    return broken_wiki, broken_md


# ── config patch ─────────────────────────────────────────────────────────────

def patch_config(quartz_root):
    cfg_path = quartz_root / "quartz.config.ts"
    if not cfg_path.exists():
        print("  ⚠ quartz.config.ts not found — skipping")
        return

    text = cfg_path.read_text(encoding="utf-8")
    original = text

    desired_ignores = ["private", "templates", ".obsidian", "__archived__"]

    ip_match = re.search(r"(ignorePatterns\s*:\s*\[)([^\]]*)(\])", text)
    if ip_match:
        existing = ip_match.group(2)
        additions = [f'"{p}"' for p in desired_ignores if p not in existing]
        if additions:
            new_inner = existing.rstrip().rstrip(",")
            if new_inner:
                new_inner += ",\n    "
            new_inner += ",\n    ".join(additions)
            text = (text[:ip_match.start(2)] + " " + new_inner + " "
                    + text[ip_match.start(3):])
            print(f"  ✓ ignorePatterns: added {', '.join(additions)}")
        else:
            print("  ✓ ignorePatterns already complete")
    else:
        print("  ⚠ could not find ignorePatterns in quartz.config.ts")

    if text != original:
        cfg_path.write_text(text, encoding="utf-8")
        print(f"  ✓ wrote {cfg_path.name}")
    else:
        print("  ✓ no config changes needed")


# ── main ─────────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(description="Fix broken links in a Quartz site")
    ap.add_argument("quartz", type=Path, help="Path to Quartz project root")
    ap.add_argument("--fix",    action="store_true", help="rewrite files in-place")
    ap.add_argument("--config", action="store_true", help="patch quartz.config.ts")
    args = ap.parse_args()

    quartz = args.quartz.expanduser().resolve()
    if not quartz.is_dir():
        sys.exit(f"error: {quartz} is not a directory")

    print(f"\n  mode: {'FIX' if args.fix else 'DRY RUN (add --fix)'}")
    bw, bm = scan(quartz, fix=args.fix)

    if args.config:
        print("\n  config:")
        patch_config(quartz)

    total = len(bw) + len(bm)
    if not args.fix and total:
        n = sum(1 for *_, s in bw if s)
        print(f"\n  re-run with --fix to apply {n} auto-fixable wikilinks.\n")

    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
