# Build log — news-image-20261123

## v1 — first write + first run (2026-11-23)

- Wrote `build_image.py` fresh in this session (Python 3 + Pillow, system
  DejaVu fonts, no network, deterministic). Layout: masthead header with
  date, hero stat band (COP31 0 deal / Kospi −3.3% / Brent $90.55), six
  story cards in a 2×3 grid, thin bottom ticker strip.
- First run: `python3 build_image.py entry.png` → 1024×1024 PNG,
  113,436 bytes, sha256
  `367a654f41d5e107a1bb7009d1c28fa8e029da60ca270b187e7eedca05ac9613`.
- Visual check found one defect: the bottom ticker text was too long and
  overflowed both edges (cut off at "RAELI..." on the left and "DOWN ~2"
  on the right). The auto-shrink loop had hit its size floor and still
  did not fit. Card bodies were also a touch small for the card height.

## v2 — revision + re-run (2026-11-23)

- Revised `build_image.py`:
  - Shortened the ticker to "ISRAELI SOLDIER SUICIDES: 16-YEAR HIGH (23) ·
    SK EDUCATION MINISTER RESIGNS · BRENT $90.55, -2%" so it fits the
    strip at full size.
  - Body font 17 → 18 pt and body line spacing 23 → 24 px, to fill the
    cards better.
- Re-ran: `python3 build_image.py entry.png` → 1024×1024 PNG,
  118,527 bytes, sha256
  `b87ed1b20a6e84fee82b61ca46afc8c345ca5af87daa954d685c9071c8f4169d`.
- Visual check: clean — masthead, stat band, all six cards and the ticker
  fully legible, no text overflow or cut-off anywhere.
- Determinism: two further runs produced byte-identical PNGs with the
  same sha256 (`b87ed1b2...`).
- `main.py` (fresh, stdlib only) verified twice into two fresh folders;
  both outputs matched the entry sha256.

## v3 — factual fix by the parent agent (2026-11-23)

- Fixed one wording error in the IRAN card: "20+ dozen" was wrong (the
  report said "more than two dozen"), changed to "two dozen-plus".
- Re-ran build_image.py twice: both runs byte-identical, 1024×1024 PNG,
  118,336 bytes, sha256
  `03f1847b8a02ceba149cabef7278de2026a2667bdcb23ec9a1f08997edf3c956`.
- main.py re-verified twice into two fresh folders; both outputs matched.
- Visual check of the fixed image: clean, no overflow.
