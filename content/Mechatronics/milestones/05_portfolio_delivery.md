# Phase 5 — Portfolio & Delivery

## Outcome

Documentation, media, and presentation that make the engineering process visible. Not marketing — a technical record that proves you can think, build, debug, and explain.

This phase is deload-shaped. The learning is in the doing: refactoring reveals what you didn't understand, documentation reveals what you skipped, presentation reveals what you can't yet explain.

---

## Phase Pass Condition

### MVM

- [ ] 20+ page engineering report exists
- [ ] One demo video: workcell running
- [ ] Code repo clean and navigable

### Full Pass

- [ ] Report: requirements → design → build → test → results → lessons
- [ ] All hand calcs, FEA, schematics, firmware architecture included
- [ ] FMEA or equivalent
- [ ] Decision records and verified Landmines compiled
- [ ] Calibration records, interface contracts, and test evidence paths compiled
- [ ] Verification matrix compiled: requirement → test → evidence → result; calibration/uncertainty records included.
- [ ] Video: well-lit, stable, shows cold-boot → run → shutdown
- [ ] Code refactored, consistent naming, no dead code
- [ ] Resume: 4–6 metric-driven bullets
- [ ] 5-minute presentation practiced and delivered

---

# Milestone 5.1 — Portfolio + Documentation

## Deliverable

Complete engineering documentation package: report, video, clean repo, resume bullets, practiced presentation.

## Pass Condition

### MVM

- [ ] Report draft: overview, block diagram, key calcs, key decisions, test results
- [ ] One video: full cycle
- [ ] README.md: what this is, how to build it, what I learned

### Full Pass

- [ ] Report 20+ pages with all technical content
- [ ] FMEA: what can fail, what happens, what mitigates
- [ ] Decision records compiled from milestone files
- [ ] Verified Landmines compiled: what actually tripped me
- [ ] Calibration records, interface contracts, and capture paths compiled into the report appendix
- [ ] Video: narrated or captioned
- [ ] Code: refactored, tagged `v1.0-release`
- [ ] Resume bullets: specific tools, specific metrics
- [ ] 5-min presentation: what it is, how it works, one trade-off, one surprise, what I'd do differently

## ⚠️ Landmines

1. **Documentation is the last engineering task, not "writing it up."** `[HYPOTHESIS]`

   Explaining the system reveals gaps in understanding. If you can't explain why you chose star grounding, you don't understand why.

2. **Don't write from scratch. Compile.** `[HYPOTHESIS]`

   Decision records, verified Landmines, hand calcs, FEA plots, retros — already written in milestone files. The report assembles them.

3. **The video needs to be real, not polished.** `[HYPOTHESIS]`

   Phone on tripod, good lighting, 60-second cold-boot-to-run. Show one failure and recovery if you have it. Authenticity > production.

4. **Resume bullets are evidence, not job descriptions.** `[HYPOTHESIS]`

   Not: "Worked on a robotic arm project."

   Instead: "Designed custom STM32 FOC controller achieving ±20mA Id tracking; designed 4-layer PCB; implemented dual-channel hardware E-Stop per IEC 62061 principles."

## Dependencies that waste your week if hit backwards

- Open all milestone files and pull raw material BEFORE writing. Don't stare at a blank page.
- Refactor code BEFORE writing the firmware architecture section. The section describes the refactored version, not the messy one.
- Practice the presentation BEFORE recording the video. The practice reveals what you can't explain; the video captures what you can.

## Before

If this takes longer than expected, the most likely reason is:

Predicted failure mode, and why:

## During

`Date | Predicted → Got → Gap`

## After

What I'd tell someone starting this:

Actual time vs. range: 3–5 weeks

---

# Final Retro

Actual total time vs. range, 12–24 months:

The three things I understand now that I couldn't have imagined at Day 1:

The landmine that cost the most time:

The prediction that was most wrong:

What I'd tell Day-1 me:
