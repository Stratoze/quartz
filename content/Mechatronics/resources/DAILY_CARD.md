# Daily Card

## Before I power on

0. Open the current milestone file. Re-read the landmines. 30 seconds.
1. What am I building / solving / understanding today?
2. **Predict:** what do I expect to happen, and why?
3. What will I do if I am wrong?

---

## The only rules

- Sit down. Do something. One derivation, one wire, one commit — counts.
- Work on one problem. Mode may shift (theory → code → hardware → sim) as the problem demands. A *different problem* mid-session doesn't.
- Same failure 3× → change the approach, not the effort.
- Stuck 20–30 min → unblock routine or rotate.
- Tired? Minimum session. No guilt.
- End in a known state. Commit before standing up.

---

## The Loop

> **Predict → Attempt → Compare → Explain the gap → Integrate → Maintain**

Before: `I expect ___ because ___.`
After:  `I got ___. The gap is probably ___.`

One line each. 30 seconds. This is the whole game.

---

## Menu

- Theory — derive, explain, verify
- Hardware — wire, solder, measure, characterize
- Code — firmware, drivers, algorithms
- Simulation — predict BEFORE running
- Reading — datasheet / app note, scan for structure
- Integration — join subsystems, test the seam
- Maintain — Anki, 5–15 min
- Fun — tinker, break something, no deliverable

---

## Debug triage

| Situation | Response |
|-----------|----------|
| First failure | Retry once. |
| Same failure 2× | Stop guessing. Binary-search: cut in half. |
| Same failure 3×+ | Approach is wrong. Measure an assumption. |
| Works alone, fails integrated | Seam: ground, levels, timing, fit. |
| Worked yesterday | `git diff`. Something changed. |
| Heat / smoke / smell | **Kill power now.** |
| Frustration / fog | Lateral move, or stop. Never debug angry. |

---

## Emergency safety

- Heat / smoke → kill power. Now.
- Mains / high voltage → verified-off, one-hand rule, never tired.
- LiPo swelling → isolate outdoors. Don't puncture.
- Solder fumes → ventilation. Always.
- Clipping / drilling → glasses.

---

## One log line

`Date | Domain | Milestone | Predicted → Got → Gap | Tomorrow`

---

## Weekly review, Sunday, 10 min

- What works now that didn't last week?
- What's stuck? 2+ weeks → plateau-breaking.
- What's gone cold? Run `./scripts/cold_tools.sh`.
- Inside the honest range, or mis-scoped?
- Body: eyes, wrists, back, sleep?

---

## When I don't feel like it

- "After I [coffee / laptop / board], I sit down."
- "I'll just write one prediction." *(That counts.)*
- Missed a day? Fine. Missed a week? Still fine.
- The plan doesn't punish me. It's there when I return.