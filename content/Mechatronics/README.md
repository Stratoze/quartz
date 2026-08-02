# Mechatronics Roadmap

This folder is an Obsidian-ready mechatronics training system, engineering log, and documentation package.

The goal is hard skill acquisition:

> Build engineering judgment by repeatedly predicting, attempting, comparing, explaining the gap, integrating, and maintaining real electromechanical systems.

No Obsidian plugins are required.

---

## Start here

1. Open [ROADMAP](ROADMAP.md). Find your current milestone.
2. Open the matching file in `milestones/`. Read the landmines. Know what done looks like. Close it. Build.
3. Log one line in `journal/YYYY-MM.md`.
4. Commit before stopping.

The plan does not punish missed days. The repo waits.

---

## The normal workflow

```txt
Open ROADMAP → find current milestone
↓
Open milestone file → read landmines once
↓
Build / derive / measure / simulate
↓
Write one journal line
↓
Commit known state
```

The loop is always:

> **Predict → Attempt → Compare → Explain the gap → Integrate → Maintain**

Before: `I expect ___ because ___.`
After: `I got ___. The gap is probably ___.`

---

## Where things go

| Thing | Put it here |
|---|---|
| Phase/milestone status | `ROADMAP.md` |
| Milestone gates, landmines, before/during/after | `milestones/` |
| One-line session history | `journal/YYYY-MM.md` |
| Future ideas, not commitments | `IDEAS.md` |
| Reference material (method, safety, conventions) | `resources/` |
| Copyable formats | `templates/` |
| Evidence that proves claims | `docs/captures/` |
| Firmware code | `firmware/` (project repos) |
| Python/LTspice models | `simulations/` |
| CAD parts, assemblies, drawings | `cad/` |
| KiCad, BOMs, fab files | `pcb/` |
| Final report, video, resume | `portfolio/` |
| Maintenance scripts | `scripts/` |

When unsure, choose the place where future-you would search first.

---

## Repo map

```txt
mechatronics/
├── README.md              ← you are here
├── ROADMAP.md             ← the map. start here every session.
├── IDEAS.md               ← maybe-later. not commitments.
├── milestones/            ← the actual work.
│   ├── 00_foundations.md
│   ├── 01_signals_actuators_dynamics.md
│   ├── 02_embedded_realtime_control.md
│   ├── 03_mech_pcb_verification.md
│   ├── 04_capstone_integration.md
│   └── 05_portfolio_delivery.md
├── journal/               ← one line per session.
├── resources/             ← read when stuck or starting. not daily.
│   ├── INDEX.md           ← what's here, when to read it.
│   ├── FAQ.md             ← quick answers.
│   ├── DAILY_CARD.md
│   ├── CONVENTIONS.md
│   ├── OPERATING_SYSTEM.md
│   ├── SAFETY_CARD.md
│   └── FIELD_NOTES.md
├── templates/             ← copyable formats. use when they help.
├── scripts/               ← maintenance.
├── firmware/              ← project repos live here.
├── simulations/
├── hardware/
├── data/
├── cad/
├── pcb/
├── docs/
├── portfolio/
└── archive/
```

---

## Status ownership

Do not track the same thing in five places.

| File/folder | Owns |
|---|---|
| `ROADMAP.md` | Phase/milestone status only. Update when a milestone changes state. |
| `journal/` | Historical one-line session record. |
| `milestones/` | Gates, landmines, before/during/after notes, retros. |
| `docs/captures/` | Evidence that proves claims. |
| `IDEAS.md` | Maybe-later ideas. Not commitments. |
| Git commits | Code/design state history. |

If two places disagree, trust the file that owns that type of information.

---

## Definitions

**MVM** = Minimum Viable Milestone.
Enough evidence exists that I can move forward without lying to myself. MVM is not mastery. MVM is a clean handoff to the next layer.

**Full Pass** = the stronger version of the gate. Worth doing when the milestone feeds directly into later safety, reliability, or portfolio claims.

**Landmine** = a failure mode worth reading before starting because it can waste days if discovered in the wrong order.

---

## Sanity checks

After editing the system itself, run:

```bash
./scripts/validate.sh
```

During reviews, run:

```bash
./scripts/versions.sh
./scripts/cold_tools.sh
```

---

## Anti-Bloat Rule

Do not add a new file, checklist, tool, or ritual unless it removes repeated friction already observed at least twice, prevents expensive damage, or improves evidence quality.

The default improvement is deletion, not expansion.

The system is not the work. The work is the loop.