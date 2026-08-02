# FAQ

Quick answers. If you need more, the full reference is linked.

---

## I'm stuck. What do I do?

1. **15 min solo.** Document what you tried. Binary-search: cut the problem in half.
2. **AI scaffold.** Ask for the 5 registers, not the code. Ask for a hint, not a solution.
3. **Lateral move.** Easier task, same domain. Close with a small win. Come back tomorrow.

20–30 min per stuck point. Then rotate. Same failure 3× → the approach is wrong, not the effort.

Full protocol: [OPERATING_SYSTEM §5](OPERATING_SYSTEM.md)

---

## What units do I use?

SI. Always. Angle in code = radians. Angle in notes = degrees, labeled. Every number gets a unit. Convert at the boundary, not inside logic.

Full table: [CONVENTIONS](CONVENTIONS.md)

---

## Is this safe?

**Kill power now** if: unexpected heat, smoke, burning smell, current jump, uncommanded motion, LiPo swelling.

Before power: current limit set. One hand near switch. DMM on expected rail. Know what current you expect.

Before motors: clear path. No loose clothing. Motor mounted. E-stop path known. Low voltage first.

Full card: [SAFETY_CARD](SAFETY_CARD.md)

---

## How do I log this?

One line. 30 seconds.

```
Date | Domain | Milestone | Predicted → Got → Gap | Tomorrow
```

In `journal/YYYY-MM.md`. That's it. Don't write an essay.

---

## What's MVM vs Full Pass?

**MVM** = Minimum Viable Milestone. Enough evidence to move forward without lying to yourself. Not mastery. A clean handoff.

**Full Pass** = the stronger gate. Worth doing when the milestone feeds into safety, reliability, or portfolio claims.

You pass MVM, you move on. Full Pass is earned over the journey.

---

## I don't feel like working.

"After I [coffee / laptop / board], I sit down."
"I'll just write one prediction." *(That counts.)*
Missed a day? Fine. Missed a week? Still fine. The plan doesn't punish you.

Full psychology: [OPERATING_SYSTEM §19](OPERATING_SYSTEM.md)

---

## How do I use AI without cheating?

| Zone | Examples | Rule |
|---|---|---|
| **Green** | typos, formatting, compiler errors, datasheet navigation | Use freely |
| **Yellow** | code skeletons, derivation hints, circuit suggestions | Reconstruct from understanding before using |
| **Red** | safety design, final values, FOC, control gains, load ratings | Independent verification required |

Scaffold prompt: *"Don't give me the code. Give me the 5 registers in order. I'll write it."*

Full policy: [OPERATING_SYSTEM §2](OPERATING_SYSTEM.md)

---

## When do I use a template?

When it removes friction. Not before. Not as homework.

The smallest template that prevents future confusion. If you wouldn't search for it later, don't write it.

Index: [templates/README.md](../templates/README.md)

---

## How do I read a datasheet?

5–10 min. Scan title → features → block diagram. Find YOUR section. Note absolute max, recommended operating, typical application. Don't stop on every detail. 2–3 sentences in the log after.

Full protocol: [OPERATING_SYSTEM §10](OPERATING_SYSTEM.md)

---

## What's the Hypothesis Loop?

**Predict → Attempt → Compare → Explain the gap.**

Before: `I expect ___ because ___.`
After: `I got ___. The gap is probably ___.`

One sentence each. 30 seconds. This is the whole game. The delta between prediction and reality is where your mental model gets corrected.

Full explanation: [OPERATING_SYSTEM §11](OPERATING_SYSTEM.md)

---

## What's a landmine?

A failure mode worth reading before starting because it can waste days if discovered in the wrong order.

Tags: `[HYPOTHESIS]` expected · `[COMMUNITY]` commonly reported · `[DATASHEET]` from manufacturer · `[VERIFIED]` you hit it · `[RETIRED]` no longer relevant

When you hit one, change the tag: `[VERIFIED — 2026-08-14]`

---

## How do I know when a milestone is done?

The pass condition says so. MVM = you can move on. Full Pass = you can build on it.

A milestone is not complete because you remember doing it. Leave one artifact: derivation, plot, scope screenshot, video, commit hash, measurement table. Store in `docs/captures/`.

Full ladder: [OPERATING_SYSTEM §12](OPERATING_SYSTEM.md)