# Operating System

> Method only. No phase content. Consult when stuck, during reviews, or when choosing strategy. Milestone files hold the content.
>
> This file changes rarely.

## Contents

- [0. Starting from Zero](#0-starting-from-zero)
- [1. Session Options](#1-session-options)
- [2. The Protocols](#2-the-protocols)
- [3. Learning Protocol, Theory](#3-learning-protocol-theory)
- [4. Building Protocol, Hardware and Code](#4-building-protocol-hardware-and-code)
- [5. Q-Spots](#5-q-spots)
- [6. Readiness and Shelving](#6-readiness-and-shelving)
- [7. Deload](#7-deload)
- [8. Maintenance and Anki](#8-maintenance-and-anki)
- [9. Logging and Decision Records](#9-logging-and-decision-records)
- [10. Datasheet and App Note Reading](#10-datasheet-and-app-note-reading)
- [11. The One Loop](#11-the-one-loop)
- [12. Verification Ladder and Red Team](#12-verification-ladder-and-red-team)
- [13. Plateau-Breaking](#13-plateau-breaking)
- [14. Project Management and 12-Week Goals](#14-project-management-and-12-week-goals)
- [15. Safety and Sustainability](#15-safety-and-sustainability)
- [16. Resources](#16-resources)
- [17. Landmine Tags](#17-landmine-tags)
- [18. Implementation Order](#18-implementation-order)
- [19. The Psychology](#19-the-psychology)

---

## 0. Starting from Zero

First session only. After that, use the Daily Card.

**Setup, 20 min, once:**
- Workspace: clear desk, board visible, supply reachable, scope/meter in reach.
- Safety: ventilation on, ESD strap, glasses in fixed spot, current-limited supply as DEFAULT, fire extinguisher accessible, LiPo area defined.
- Software: editor, terminal, Git, toolchain verified, compile + flash blinky.
- Git: `git init`. First commit.
- Anki: create deck. Zero cards is fine.

**First session:**
1. Sit down. Pick one concept. Work it. 15–20 min.
2. Write one prediction before. One comparison after.
3. Log line. Commit. Done.

---

## 1. Session Options

**Minimum, 15–25 min:** yesterday's log → one task → Anki or check → log → commit.

**Standard, 45–75 min:** log + Q-spots, 3–5 min → main block, 20–35 min, mode may shift → reading or intuition check, 5–10 min → Anki, 5–10 min → log + commit, 3 min.

**Deep, no ceiling, block structure:** 45–60 min blocks. 5–10 min breaks. Never grind one bug 60+ min. After 3 blocks, real break. Stop when quality degrades.

**Weekly aims:** 4–6 sessions. 1 rest day. Each week: at least one integration run, one datasheet read, one hypothesis check, one Anki review.

3 focused days > 7 half-attention days.

---

## 2. The Protocols

### Sprint & Deload

Sprint 2–3 weeks. Deload when triggered or at phase gates. See Section 7.

### AI Use Zones

#### Green — allowed freely
- typo fixes
- formatting
- documentation cleanup
- test data generation
- boilerplate scripts
- explaining compiler errors
- datasheet navigation
- harsh review of my work

#### Yellow — allowed with reconstruction
- code skeletons
- register checklists
- derivation hints
- circuit topology suggestions

Rule: if AI gives a solution, I must reconstruct it from understanding before using it.

#### Red — not accepted without independent verification
- safety-critical design
- final circuit values
- motor power-stage design
- FOC implementation
- control gains
- mechanical load ratings
- anything involving mains, high current, LiPo, or moving machinery

**Scaffold prompt:** "Don't give me the code. Give me the 5 registers in order. I'll write it. Review mine when done."

**Review prompt:** "Here's my [netlist / FBD / FMEA]. Be a harsh Senior Reviewer."

**Feynman prompt:** "I'll explain [concept]. Stop me when I'm wrong."

### 3-Tier Unblock

1. 15-min solo struggle. Document what you tried.
2. AI scaffold / targeted query. Specific concept, not full solution.
3. Lateral move. Easier task, same domain. Close with a small win.

20–30 min per stuck point. Then rotate.

### External Review Gates

At minimum, get outside review at these points:
- End of Phase 1: sensor/motor architecture review.
- Before PCB order: schematic + layout review.
- Before high-power motor test: safety review.
- Before final portfolio: documentation review.

The reviewer does not need to solve it. They need to find one thing I missed.

---

## 3. Learning Protocol, Theory

1. **Preview, 3–5 min:** What is this? Where does it fit? Physical intuition? Skim. Note the 2–3 hardest parts.
2. **Chunk:** One equation, one circuit stage, one mechanism. Smaller when lost.
3. **Engage actively:** Derive before reading. Draw from memory. Explain aloud. Predict before simulating. Sketch before probing.
4. **Feynman test:** Close materials. Explain aloud or whiteboard from memory. Stumble = the gap. Return for that gap only.
5. **Error triage:**

| Situation | Response |
|-----------|----------|
| Isolated slip | Redo once. |
| Same mistake 2× | Stop. Identify cause. Change method. |
| Can't start | Chunk too big. First step only. |
| "Foggy" | Memorizing, not understanding. Draw the physics. |
| Breakdown | Prerequisite missing? Step back. |

After 3 identical failures: change resource, representation, or chunk size.

6. **Connect:** Where does this link to last week? Modify the problem — still solvable?
7. **Stop:** 20–30 min per concept. Results appear later.

---

## 4. Building Protocol, Hardware and Code

**Before, 2 min:** What does it do? Inputs/outputs? Interface?
Write the pass condition BEFORE building. Quick mental FMEA.

**Hardware:** Breadboard first. Power first. One subsystem at a time. Measure, don't assume. Datasheet in reach. Test the seam.

**Code:** Test first. One module at a time. Commit after every working state. Read the error. Actually read it.

**Error triage:**

| Situation | Response |
|-----------|----------|
| Won't compile / wire mismatch | Read error. Trace wire. Systematic. |
| Same bug 3×+ | Binary search. Cut in half. |
| Works alone, fails integrated | Seam: ground, levels, timing, fit. |
| Intermittent | Loose connection, marginal timing, sag, thermal. Add logging. |
| "Worked yesterday" | `git diff`. Something changed. |
| Heat / smoke | **Kill power NOW.** |

### Measurement Sanity

Before trusting a measurement:
- DMM: verify continuity mode and measure a known voltage.
- Scope: compensate probe, confirm 1x/10x setting, ground clip safe.
- Bench supply: set voltage and current limit before connecting load.
- Logic analyzer: confirm voltage threshold matches target logic level.
- Current measurement: know whether meter/shunt is in series or clamp-based.
- Thermals: first touchless check if high current or unknown fault.

Rule: if the measurement contradicts physics, suspect the measurement setup before inventing a new theory.

**End:** known state. Commit. Log line with prediction → result → gap.

---

## 5. Q-Spots

1. **Identify:** exact problem. Not "FOC doesn't work." Instead: "Park output oscillates at 2× electrical frequency with encoder-sourced angle."
2. **Isolate:**

| Fault class | Tool |
|-------------|------|
| Math confusion | Re-derive. Draw geometrically. |
| Code bug | Binary search. Minimal reproduction. |
| Hardware fault | Isolate subsystem. Probe each node. Power first. |
| Conceptual gap | Different explanation: video, book, AI scaffold. |
| Integration failure | Test the seam. |

3. **Time-box:** 20–30 min. Rotate.
4. **Revisit:** next day. And the next.
5. **Reintegrate:** verify in context.
6. **Log it:** problem AND solution. Past-you left a ladder.

---

## 6. Readiness and Shelving

**Concepts — 4 stages, 1 gate:**

| Stage | Meaning |
|---|---|
| Encountered | Read/watched. Vague sense. |
| Understood | Can explain and derive with notes. |
| **✅ Applied, GATE** | **Solved a NEW problem. Enough to move on.** |
| Fluent | Can teach, debug, build on it. Earned over the journey. |

**Modules — 4 stages, 1 gate:**

| Stage | Meaning |
|---|---|
| Built | Works once, in isolation. |
| **✅ Tested, GATE** | **Passes written pass condition. Edge cases checked.** |
| Robust | Survives faults, cold starts, long runs. Required for high current/voltage, moving parts, safety. |
| Maintained | Still works after weeks away. |

Perfection is asymptotic. Not the entry requirement.

**Pacing:** advance on deliverables, not dates. Honest ranges in [ROADMAP](../ROADMAP.md) distinguish normal struggle from mis-scoping. All numbers are heuristics.

**Shelving, no guilt:** blocked 3+ weeks · prerequisite missing · off critical path · budget changed. Log WHY. Shelving is data.

---

## 7. Deload

**Triggered, anytime, 2–7 days:** 2–3 weeks without consolidation · reading same paragraph 3× · error rate climbing · dread/avoidance · fab order placed, wait IS the deload.

**Guaranteed, every phase gate, 1–3 days:** close books, re-derive from memory, red-pen gaps, update mind map, run system cold. Compress to 1 day only if you can pass the previous phase's gate test cold, right now.

**Avoidance check:** "Am I saturated across the whole phase, or avoiding one hard problem?" One problem → Unblock Routine, not deload.

**What it looks like:** NO new inputs. Refactor, re-wire, re-derive, document, tidy, rest. Walk. Sleep. Eat well.

---

## 8. Maintenance and Anki

**What goes in / what doesn't:**

| Good | NOT good |
|------|----------|
| Formulas + physical meaning | "How to debug SPI", procedural |
| Register names, bit fields | Circuit design intuition |
| Pinouts, protocol timings | "How to tune a PID", experiential |
| Material properties | System architecture decisions |
| Diagnostic: "Motor vibrates 2× freq. Top 3 causes?" | Physical intuition, comes from doing |

**Rules:** 5–15 min, not card count. 1–2 cards/day. Delete pointless cards. No active module unreviewed > 2 weeks. Tag cards: `mech:FOC`, `mech:P0`, etc.

**Cold-toolchain:** run `cold_tools.sh` during weekly review. No manual table.

---

## 9. Logging and Decision Records

**Code log:** git commit history. Structured messages.

**Learning log:** one line in journal. 30 seconds.

`Date | Domain | Milestone | Predicted → Got → Gap | Tomorrow`

**Decision records:** two lines per non-obvious choice. Written AT the time. Format and example in [CONVENTIONS](CONVENTIONS.md#decision-records).

**Capture:** baselines · milestones · surprises · demos · waveform screenshots · before/after plots · hardware photos. Not everything.

### Evidence Rule

A milestone is not complete because I remember doing it.

For each completed milestone, leave at least one artifact:
- derivation photo or Markdown note
- plot
- scope screenshot
- short video
- commit hash
- measurement table
- schematic/CAD/PCB file
- terminal output
- report snippet

Store evidence under:

```txt
docs/captures/YYYY-MM-DD_short_name.*
```

The artifact can be ugly. It just has to prove the claim.

## 10. Datasheet and App Note Reading

Engineering sight-reading. 5–10 min, 2–3×/week.

**Before:** What component? What do I need? Scan title, features, block diagram.

**During:** Read for structure. Find your section. Note absolute max, recommended operating, typical application. Don't stop on every detail.

**After:** 2–3 sentences in log.

## 11. The One Loop

> **Predict → Attempt → Compare → Explain the gap → Integrate → Maintain**

Canonical explanation here. The one-liner lives on the Card.

**Three zoom levels:**

|**Zoom**|**Where**|**What you write**|
|---|---|---|
|Session|Journal line|`Predicted → Got → Gap`|
|Milestone|Milestone file: Before / During / After|Pre-mortem → decisions → retro|
|Cycle|12-week review|Actual pace vs. honest range → recalibrate|

**Why this is the center:** the delta between prediction and reality is where the model in your head gets corrected. This is also the skill that lets you hold a real technical conversation with someone far more experienced: you show up with a falsifiable model, not just facts.

**Evidence:** meta-analysis, 64 studies, randomized controlled trials, g ≈ 0.55. Self-generated explanation outperforms presented explanation.

**Cost:** one sentence before, one sentence after. 30 seconds.

**This is not overhead. This IS the real work.**

**Supporting habits:**
- Before calculating: Fermi estimate. Then calculate. Match?
- Before simulating: sketch the expected curve. Then run.
- Before building: trace the signal/force/current path with a finger.
- When debugging: "What law of physics is being violated?"
- When reading: translate the equation into a physical sentence.

**Vocabulary prompts:**
- "What law of physics is being violated or ignored?"
- "What is the Input, the Output, and the Transformation?"
- "Where can I split this in half to prove which side works?"

## 12. Verification Ladder and Red Team

|**Rung**|**Question**|**Evidence**|
|---|---|---|
|Paper|Does the math work?|Derivations, block diagrams|
|Simulation|Does the model behave?|Python, SPICE, FEA|
|Module|Does the isolated unit work?|Bench test|
|Integration|Do modules work together?|System test, seam check|
|Stress|Does it survive edge cases?|Fault injection, thermal, EMI|
|Performance|Does it work reliably, cold?|Demo-ready, extended run|

Don't skip rungs. Don't claim rung 5 if you've only tested rung 3.

**Red Team, at Stress rung:** "If I were trying to break this, what would I do?" Write 3–5 scenarios. Run them. Pull a wire. Send garbage over UART. Power-cycle during a write. Stall the motor. Disconnect the encoder mid-FOC.

## 13. Plateau-Breaking

Pick 1–2:
- Shrink to minimum working version. Rebuild.
- Change representation: math → sim → hardware → drawing → code.
- Change resource: different book, video, app note.
- Teach it: rubber duck, friend, AI Feynman prompt.
- Build it wrong on purpose. Understand WHY it breaks.
- Take 3–5 days off. Return fresh.
- Ask someone: r/embedded, EEVblog, Stack Exchange.
- Shelve honestly. Return in a month.

## 14. Project Management and 12-Week Goals

**Always maintain:**
- 1 learning topic, at the edge.
- 1 building project, applying recent concepts.
- Maintenance pool, completed modules, Anki.
- Optional: 1 fun/tinker, below level.

**12-week review:** use `templates/12_week_review.md`.

## 15. Safety and Sustainability

**Electrical:** current-limited supply for every first power-on · mains/>48V: verified-off, one-hand rule, never tired · LiPo: non-flammable surface, never unattended, never swollen · ESD: strap before ICs · capacitors: discharge before touching.

**Mechanical:** safety glasses when clipping/drilling/cutting · no loose clothing near rotating shafts · deburr machined parts.

**Chemical:** solder ventilation always on · wash hands after leaded solder · resin: gloves, ventilation.

**Ergonomics:** every 30 min: stand, 20-20-20 rule, roll wrists · **sleep is a debugging tool** · dread is a signal, not a character flaw · physical activity not optional.

**Response protocol:** heat/smoke → kill power · LiPo swelling → isolate outdoors · mains contact → cut power first · solder burn → cool water 10 min · eye impact → flush 15 min, seek medical.

## 16. Resources

**Textbooks:** Ulaby, signals/math · Nise, control/dynamics · Horowitz & Hill, circuits/power · Rizzoni, fundamentals · White, embedded · FreeRTOS manual · Lospinoso, C++.

**Reference:** STM32 Ref Manual + Datasheet · component datasheets · ST/TI app notes, AN1086, SLUA171 · KiCad 9 docs (docs.kicad.org) · Solid Edge tutorials (solidedge.siemens.com/en/resources/tutorials) · PrePoMax docs + Jakub Michalski YouTube series · Phil's Lab YouTube (KiCad + PCB) · IPC-2221 · SKF/NSK bearing catalogs.

**Video:** 3Blue1Brown · Efficient Engineer · EEVblog · Afrotechmods.

**Tools:** Falstad · LTspice · Python, scipy/matplotlib · PlotJuggler · KiCad 9 · Solid Edge Community Edition (Windows) · PrePoMax (free FEA, CalculiX solver, Windows) · FreeCAD (macOS STEP viewer + backup FEA) · Velxio (local MCU emulator: ESP32/Arduino/RP2040, self-hosted, free — velxio.dev) · CMake + arm-none-eabi-gcc · OpenOCD + GDB · Git · Anki, FSRS.

**Communities:** r/embedded · r/AskElectronics · EEVblog forum · Stack Exchange · STM32 community.

## Tool Purchase Rule

Do not buy a tool because it is interesting.

Buy when one of these is true:
- Safety requires it.
- Progress is blocked twice by not having it.
- It replaces a bad measurement with a trustworthy one.
- It is required by the current milestone gate.

Write the reason in the journal or a decision record.

## Resource Intake Rule

One active resource per concept by default.

Do not collect five books/videos before doing the problem. If the current resource fails after real effort, switch deliberately and log why.

## Done / Shelved / Abandoned

**Done:** pass condition met and evidence exists.

**Shelved:** still valuable, intentionally paused, reason written down.

**Abandoned:** approach is no longer worth preserving except as a lesson. Archive or delete it.

A project with no next action is not active.

## 17. Landmine Tags

- `[HYPOTHESIS]` — expected failure mode; verify or retire later.
- `[COMMUNITY]` — common trap reported by practitioners.
- `[DATASHEET]` — directly from manufacturer documentation.
- `[VERIFIED]` — personally encountered and confirmed.
- `[RETIRED]` — no longer relevant after design/tooling changed.

When a landmine actually happens, change its tag or add a note:

`[VERIFIED — 2026-08-14]`

## 18. Implementation Order

**Day 1:** Just the Card. Sit down. One thing. 20 min.

**Week 1:** Open OS. Read Sections 2–4. Start Phase 0. Set up safety.

**Week 2:** Open first milestone file. Read Landmines. Know what done looks like. Build. Anki, 1–2 cards/day, tag: `mech:P0`.

**Phase 0 deload:** Create next 2–3 milestone files using `templates/milestone_file.md`. Verify scripts. 1–2 hrs.

**Month 2:** Decision records, datasheet reading, Q-spot protocol. First weekly review.

**Month 3:** First 12-week goal. First integration test. One form of external feedback — book it now.

**Ongoing:** every 12 weeks: review, re-scope on actual pace. Every milestone: fill the After section. Run `versions.sh`. Every deload: run `cold_tools.sh`, review verified Landmines.

## 19. The Psychology

**"I don't feel like it."** Anchor it. "I'll just write one prediction." Forgive the skip.

**"This is impossible."** You're not stupid. The material is hard. Shrink the chunk. Look at your git log from 3 months ago.

**"Everyone else gets it."** They don't. Highlight reel.

**"This feels pointless."** Build something you care about. Tinker for 10 min. Make a motor spin. Remember why.

**"The plan is overwhelming."** Look at the Card. One problem. Do it.

**"Debugging at 1 AM."** Sleep is a debugging tool. Commit. Hypothesis. Bed.

**The meta-rule:** A theoretically perfect plan you abandon in three weeks loses to a simpler plan you run for three years.

**Consistency beats completeness.**

**The last landmine:**

> ⚠️ Iterating on the plan is not iterating on the skill.
>
> Every hour restructuring templates is an hour not deriving an equation, wiring a sensor, or scoping a waveform. Ship the imperfect system. Use it for one full phase. Then, and only then, refactor.