# World News in One Image — 23 November 2026

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/weichanghong24-lgtm/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/weichanghong24-lgtm/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

Entry for the make.fun bounty
[Sum up 23 November's world news in one image](https://make.fun/bounty/news-image-20261123)
— $100 prize pool, top 50 entries paid, deadline 25 November 2026 00:00 UTC.

## The image

A single 1024×1024 PNG that sums up Monday 23 November 2026:

- **Masthead** — "THE WORLD IN ONE DAY", Monday 23 November 2026.
- **Hero stat band** — COP31: 0 deal reached · Kospi: −3.3% · Brent crude: $90.55 (−2%).
- **Six story cards** (2 rows × 3 columns) — COP31 ends with no deal;
  Ukrainian sea drones hit Russian ships in Libya; Asian chip stocks slide;
  US sanctions on Iranian shadow banks; NATO sends an AWACS aircraft to
  Poland; Democrats' biggest US House majority since 1992.
- **Bottom ticker** — Israeli soldier suicides at a 16-year high (23 in
  2026); South Korea's education minister resigns over AI exam chaos;
  Brent crude $90.55, down ~2%.

Light warm-paper background, dark ink text, one burnt-red accent.

## Build

```sh
python3 build_image.py entry.png
```

`build_image.py` is pure Python 3 + Pillow, uses the system DejaVu fonts,
needs no network, and is deterministic — repeated runs produce a
byte-identical `entry.png` (1024×1024, under 1 MiB).

## Entrypoint

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

`main.py` (standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png`.

## Sources

Wire reports published on 23 November 2026: COP31 climate talks in Antalya;
Zelenskyy on the Benghazi sea-drone strike and the UN mission in Libya;
Asian markets after the Wall Street rout; US Treasury sanctions on Iranian
exchange houses; NATO's AWACS deployment to Poland; the North Carolina
recount (NC-5); Israeli military suicide figures; South Korea's education
minister resignation; Brent crude prices.

## License

MIT — see [LICENSE](LICENSE).

---

Built for [make.fun](https://make.fun/).
