# Piano Vault

A modular, research-informed piano practice system for long-term self-directed learning.

## Structure

```text
Piano/
  00 Index.md              — dashboard and links
  01 Daily Card.md         — daily action card (no explanations, just do)
  START HERE.md            — onboarding for new users or low-motivation days
  README.md                — this file

  Logs/
    Error Log.md           — global error inbox

  Pieces/
    README.md              — folder conventions and workflow
    Composer/
      Piece Title/
        Piece Title.md
        Piece Title - Error Log.md
        Piece Title - Tempo Log.md
        daily/
          YYYY-MM-DD.md

  Resources/
    Practice Protocols.md  — how to practice (session engine, learning, tempo, problems, health)
    Progression.md         — long-term development (pacing, stages, technique, Liszt path)
    Roadmap.md             — stage-by-stage repertoire and etude lists
    Repertoire and 12-Week Goals.md — slot system, piece folders, cycle structure
    Musicianship.md        — sight-reading, ear, theory, listening
    Maintenance and Performance.md — Anki, recording, performance simulation
    FAQ.md                 — common frustrations and quick fixes
    Editions and Sources.md — edition guidance and sourcing
    Resource List.md       — books, apps, tools, external feedback

  Templates/
    Daily Practice Note.md
    Weekly Review.md
    12-Week Goal.md
    Piece Note.md
    Piece Daily Note.md
    Piece Error Log.md
    Piece Tempo Log.md
```

## How it works

- **Daily Card** is the front door. Sit down, pick from the menu, play.
- **Practice Protocols** is the reference. Consult when troubleshooting or learning new material.
- **Progression** is the long game. Pacing, stages, technical ladder, deload weeks, macrocycles.
- **Roadmap** is the repertoire library. Stage-by-stage piece and etude suggestions.
- **Pieces/** is where active work lives. Each serious piece gets its own folder with logs.
- **Logs/Error Log.md** is a quick inbox. Recurring errors get moved into piece-specific logs.

## Key design principles

- Progress is gated by skills, not time.
- Daily practice beats weekend marathons. Sleep consolidates motor skills.
- Interleave material within sessions. Rotate every 5–8 minutes.
- Rule of Almost: leave passages almost secure, return later for retrieval practice.
- Two concurrent pieces minimum: one learning, one polishing.
- Deload every 4–5 weeks. Plateaus are consolidation, not failure.
- Listening is mandatory before learning a new piece, not optional enrichment.
- Exam boards are calibration only. The real goal is skill and musicality.

## Optional: Dataview

The vault works without plugins. If you install Dataview, the Index includes queries for:

- recent practice sessions
- active pieces
- shelved pieces

Frontmatter fields in templates are compatible with Dataview out of the box.

## Migration notes

This vault was rebuilt from an original monolithic `Practice Manual.pdf`, decomposed into modular files. The original content is preserved by decomposition, not deleted.

## Next steps after setup

1. Read [Start Here](Start%20Here.md).
2. Create your first piece folder if you have an active piece.
3. Set a [12-Week Goal](Templates/12-Week%20Goal.md).
4. Sit down and play.