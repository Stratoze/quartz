---
title: Piano
aliases:
  - Piano Home
  - Piano MOC
tags:
  - piano
  - moc
---
# Piano Index

## Start here
- [Start Here](Start%20Here.md)
- [Daily Card](Daily%20Card.md)
- [Practice Protocols](Resources/Practice%20Protocols.md)
- [Progression](Resources/Progression.md)
- [Roadmap](Resources/Roadmap.md)
- [FAQ](Resources/FAQ.md)

## Practice engine
- [Session Engine](Resources/Practice%20Protocols.md#session-engine)
- [Learning Protocol](Resources/Practice%20Protocols.md#learning-protocol)
- [Tempo Control](Resources/Practice%20Protocols.md#adaptive-tempo-protocol)
- [Speed Work](Resources/Practice%20Protocols.md#speed-work)
- [Variable Practice](Resources/Practice%20Protocols.md#variable-practice)
- [Q-Spots](Resources/Practice%20Protocols.md#q-spots)
- [Plateau Breaking](Resources/Practice%20Protocols.md#plateau-breaking)
- [Technique and Health](Resources/Practice%20Protocols.md#technique-and-health)

## Planning and progression
- [Practice Volume and Pacing](Resources/Progression.md#practice-volume-and-pacing)
- [Deload Weeks](Resources/Progression.md#deload-weeks)
- [Implementation Order](Resources/Progression.md#implementation-order)
- [Starting from Zero](Resources/Progression.md#starting-from-zero)
- [Skill Stages](Resources/Progression.md#skill-stages)
- [Technical Progression Ladder](Resources/Progression.md#technical-progression-ladder)
- [Macrocycle and Cycle Structure](Resources/Progression.md#macrocycle-and-cycle-structure)
- [Liszt Path](Resources/Progression.md#liszt-path)
- [Readiness Stages and Shelving](Resources/Progression.md#readiness-stages-and-shelving)
- [Method Book Protocol](Resources/Progression.md#method-book-protocol)
- [Teacher and Feedback](Resources/Progression.md#teacher-and-feedback-checkpoints)
- [Exam Calibration](Resources/Progression.md#exam-calibration-only)
- [Repertoire and 12-Week Goals](Resources/Repertoire%20and%2012-Week%20Goals.md)

## Pieces and logs
- [README](README.md)
- [Global Error Logs](Logs/Error%20Logs.md)

### Piece templates
- [Piece Note](Templates/Piece%20Note.md)
- [Piece Daily Note](Templates/Piece%20Daily%20Note.md)
- [Piece Error Log](Templates/Piece%20Error%20Log.md)
- [Piece Tempo Log](Templates/Piece%20Tempo%20Log.md)

## Musicianship
- [Sight Reading](Resources/Musicianship.md#sight-reading)
- [Ear, Theory and Functional Playing](Resources/Musicianship.md#ear-theory-and-functional-playing)
- [Listening Habit](Resources/Musicianship.md#listening-habit)
- [Creative Play](Resources/Creative%20Play.md)

## Maintenance and performance
- [Maintenance and Anki](Resources/Maintenance%20and%20Performance.md#maintenance-and-anki)
- [Recording and Self-Assessment](Resources/Maintenance%20and%20Performance.md#recording-and-self-assessment)
- [Performance Simulation and Memorization](Resources/Maintenance%20and%20Performance.md#performance-simulation-and-memorization)
- [Pre-Performance Routine](Resources/Maintenance%20and%20Performance.md#pre-performance-routine)

## Resources
- [Resource List](Resources/Resource%20List.md)
- [Editions and Sources](Resources/Editions%20and%20Sources.md)
- **RCM-Syllabus-2022**

## Templates
- [Daily Practice Note](Templates/Daily%20Practice%20Note.md)
- [Weekly Review](Templates/Weekly%20Review.md)
- [12-Week Goal](Templates/12-Week%20Goal.md)

---

## Dashboards

These require the Dataview plugin. If you do not use Dataview, ignore this section.

### Recent practice sessions

```dataview
TABLE minutes, energy, mood, pieces
FROM "Daily" OR "Pieces"
WHERE type = "piano-session" OR type = "piece-session"
SORT date DESC
LIMIT 20
```

### Active pieces

```dataview
TABLE composer, status, current_tempo, target_tempo
FROM "Pieces"
WHERE type = "piece" AND status != "shelved"
SORT status ASC, composer ASC
```

### Shelved pieces

```dataview
TABLE composer, status, notes
FROM "Pieces"
WHERE type = "piece" AND status = "shelved"
SORT composer ASC
```