# Politia sketch kit (art v8)

Each sketch is a simple flat SVG that an AI image-edit model later redraws as a polished game icon **with the same shapes and colours**. So the sketch decides the silhouette, layout and colours; keep it clean and readable.

## Canvas
- `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256">`, first element `<rect width="256" height="256" fill="#ffffff"/>`.
- One subject, centred, filling about 75–85% of the canvas (roughly x 24–232, y 24–228). Nothing touches the edge.
- **Straight front view only**: no perspective, no isometric, no top-down, no 3D tricks. Round things are circles/ellipses seen from the front; boxes show only their front face.
- **Buildings**: a front elevation (only the front wall, roof as an outline/gable) standing on one thin navy ground line `<rect x="20" y="214" width="216" height="8" fill="#1e2f55"/>`. No landscape, no grass, no sky, no people, no vehicles (a few props named in the subject are fine, e.g. crates, logs, ore heaps, tanks, pipes).
- Flat fills only: no gradients, filters, shadows, opacity, patterns, images, `<text>` or anything that looks like letters or numbers.

## Lines
- Outline every main shape in navy: `stroke="#1e2f55" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"` (4–5 for small details).
- Keep it simple: the main silhouette plus 3–10 detail shapes (windows, doors, bands, highlights). It must still read at 64×64 px.

## Colours
Natural colours for what the object really is; navy and gold only where they fit.
- Navy `#1e2f55` (outlines, dark parts), blue `#3d5a8c` (neutral walls/roofs/metal panels where no natural colour is obvious), light `#e8edf5` (windows, light walls), white `#ffffff`.
- Gold `#d4a42a` only for: trim/accents (a band, a door handle, a finial, a small emblem), and objects that really are gold or brass (coins, gold bars, crowns, cartridges).
- Natural colours (use these hexes): green `#5a9e4b` / dark green `#3f7a3a` (plants, banknotes `#4f8a5b`), red `#b8433a` (red barns, red cross, bricks `#a8553e`), wood brown `#8a5a3c` / light wood `#c08a55`, stone grey `#9aa3ad`, concrete `#c9ced6`, steel `#7d8794`, black/coal/oil `#222833`, glass/sky `#a8c8e8`, water `#3f8fd0`, yellow `#e8c547`, orange `#d9822b`, sand/beige `#d9c39a`, turquoise `#3fb8b0`, purple `#7b5ea7`, skin `#e0b18f`.
- At most about 5 colours per sketch, including navy.

## Interface symbols
Abstract UI icons (arrows, info, alert, gear, chat, bell, star, logout…) are drawn as a bold symbol: navy shape(s) with one gold or blue accent. No letters: "info" is an "i"-shaped dot-and-bar glyph only if unavoidable — prefer a lightbulb/round badge with a dot and bar shape; "alert" is a warning triangle with a bar and dot.

## Files
- Save each sketch as `<out>/<name>.svg`, where `<name>` is the asset id with `/` replaced by `~` (e.g. `icon~money.svg`, `product~oil.svg`, `season~0.svg`, `building~factory.svg` — buildings drop the `/L1`).
- Render each to PNG: `rsvg-convert -w 512 -h 512 <name>.svg -o <name>.png`.
- Validate: `xmllint --noout <name>.svg` must pass (or `python3 -c "import xml.dom.minidom,sys;xml.dom.minidom.parse(sys.argv[1])" <name>.svg`).

## Examples
See `examples/`: `factory.svg`, `hospital.svg`, `money.svg` (and their PNGs). Match their weight of line, simplicity and colour use.
