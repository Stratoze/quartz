# CAD
Use for mechanical parts, assemblies, exported STEP/STL files, drawings, and release notes.
Before opening CAD, write requirements. If payload/reach/material/manufacturing method are blank, design has not started.

## Tool stack
- **Primary CAD:** Solid Edge Community Edition (Windows, free, no student ID). Download: https://resources.sw.siemens.com/en-US/download-solid-edge-community-edition/
- **FEA:** PrePoMax (Windows, portable, free). Import STEP from Solid Edge. https://prepomax.fs.um.si/
- **macOS STEP viewer:** FreeCAD (free, native macOS). For quick viewing, measurement, light edits. Not the primary design tool.
- **Exchange format:** STEP (`.step` / `.stp`) for everything. Solid Edge CE cannot open others' native files. Always export STEP.

## Suggested structure
```txt
cad/
├── requirements/
├── parts/
├── assemblies/
├── drawings/
└── exports/          ← STEP files live here
```

Use templates/cad_release.md before calling anything release-ready.


---

### 6. `pcb/README.md`

**Replace entire file:**
```markdown
Use for KiCad projects, schematics, layouts, BOMs, fabrication outputs, and bring-up notes.

## Tool stack
- **EDA:** KiCad 9 (free, open source, macOS/Windows/Linux). https://www.kicad.org/
- **Learning:** Phil's Lab (YouTube) for mixed-signal design. DigiKey KiCad series for basics. KiCad forum (forum.kicad.info) for specific errors.
- **Trace width:** use KiCad's built-in PCB Calculator (Tools → PCB Calculator) with IPC-2221. Don't guess.

## Before schematic
- Define current-sensing topology.
- Verify footprints against datasheet land patterns.
- Draw ground return paths as arrows.
- Confirm part availability.

## Suggested structure per board
```txt
pcb/board_name/
├── schematic/
├── layout/
├── fabrication/
├── assembly/
├── bringup/
└── bom/
````

Use templates/cad_release.md before calling anything release-ready.