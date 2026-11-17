# Politia art sketches

Flat vector sketches for the art of the game Politia (art v8, 2026-11-18). Each sketch sets the shape, layout and colours of one game picture; an AI image-edit model redraws it as a finished icon with the same shapes and colours.

- `sketches/<name>.svg` — the sketch (name = asset id with `/` replaced by `~`, e.g. `icon~money`, `product~oil`, `season~0`, `building~factory`).
- `sketches/<name>.png` — the same sketch rendered at 512×512 (`rsvg-convert -w 512 -h 512`); this is the file the AI reads.
- `SKETCH-KIT.md` — the drawing rules (canvas, line weight, colours).
- `tools/` — the scripts that generated the first set.

To change a picture's shape or colours: edit its SVG, re-render its PNG, commit. Sketches only; no game code lives here.
