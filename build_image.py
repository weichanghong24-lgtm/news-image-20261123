#!/usr/bin/env python3
"""Render the 23 November 2026 world-news summary as a single 1024x1024 PNG.

Layout (fresh for this entry): masthead header with date, a hero stat band,
then six story cards in a 2-row x 3-column grid, plus a thin bottom ticker.
Deterministic: fixed fonts, fixed layout, no network, no timestamps.
Usage: python3 build_image.py [output_path]   (default: entry.png)
"""
import sys
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 241, 227)      # warm paper
INK = (30, 27, 22)           # dark ink
INK_SOFT = (74, 68, 58)
ACCENT = (179, 64, 42)       # burnt red
ACCENT_DARK = (140, 48, 30)
CARD_BG = (255, 252, 244)
RULE = (30, 27, 22)
TICKER_BG = (30, 27, 22)
TICKER_FG = (247, 241, 227)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"


def font(name, size):
    return ImageFont.truetype(FONT_DIR + name, size)


F_TITLE = font("DejaVuSerif-Bold.ttf", 58)
F_DATE = font("DejaVuSans-Bold.ttf", 21)
F_KICKER = font("DejaVuSans-Bold.ttf", 15)
F_HEAD = font("DejaVuSans-Bold.ttf", 25)
F_BODY = font("DejaVuSans.ttf", 18)
F_STAT_NUM = font("DejaVuSans-Bold.ttf", 40)
F_STAT_LBL = font("DejaVuSans-Bold.ttf", 14)
F_TICKER = font("DejaVuSans-Bold.ttf", 15)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap by pixel width; returns list of lines."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_centered(draw, cx, y, text, fnt, fill):
    draw.text((cx - draw.textlength(text, font=fnt) / 2, y), text,
              font=fnt, fill=fill)


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else "entry.png"
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- Masthead -------------------------------------------------------
    d.rectangle([0, 0, W, 96], fill=INK)
    draw_centered(d, W // 2, 14, "THE WORLD IN ONE DAY", F_TITLE, PAPER)
    # date line under masthead
    draw_centered(d, W // 2, 104, "MONDAY  ·  23 NOVEMBER 2026",
                  F_DATE, ACCENT_DARK)
    d.line([(36, 138), (W - 36, 138)], fill=RULE, width=2)

    # ---- Hero stat band -------------------------------------------------
    stats = [
        ("0", "COP31 DEAL REACHED"),
        ("-3.3%", "KOSPI CLOSE"),
        ("$90.55", "BRENT CRUDE  -2%"),
    ]
    band_y, band_h = 152, 96
    col_w = (W - 72) // 3
    for i, (num, lbl) in enumerate(stats):
        cx = 36 + col_w * i + col_w // 2
        draw_centered(d, cx, band_y + 4, num, F_STAT_NUM, ACCENT_DARK)
        draw_centered(d, cx, band_y + 58, lbl, F_STAT_LBL, INK_SOFT)
        if i:
            x = 36 + col_w * i
            d.line([(x, band_y + 10), (x, band_y + band_h - 10)],
                   fill=(200, 190, 170), width=1)
    d.line([(36, band_y + band_h + 8), (W - 36, band_y + band_h + 8)],
           fill=RULE, width=2)

    # ---- Six story cards, 2 rows x 3 columns ---------------------------
    cards = [
        ("CLIMATE", "COP31 ends with no deal",
         "Antalya talks ran past Friday into late Sunday \u2014 the longest "
         "UN climate conference ever \u2014 split over fossil fuels and money."),
        ("UKRAINE", "Sea drones hit Russian ships in Libya",
         "Zelenskyy says Ukrainian drones set the merchant vessel Sparta II "
         "ablaze in Benghazi; the UN mission called for an independent probe."),
        ("MARKETS", "Asian chip stocks slide",
         "Kospi closed -3.3% after a Wall Street rout on AI-spending doubts; "
         "Samsung -3.1%, SK Hynix -2.5%."),
        ("IRAN", "US sanctions shadow banks",
         "Treasury hit two dozen-plus Iranian exchange houses and fronts; Tehran "
         "claims $290bn damages; Trump leans to new strikes after New Year."),
        ("NATO", "AWACS aircraft to Poland",
         "NATO will send an early-warning aircraft after Russian missiles "
         "came down in Poland on Friday."),
        ("USA", "Democrats' biggest House majority since 1992",
         "Chuck Hubbard won a North Carolina recount (NC-5), sealing the "
         "largest Democratic majority since 1992."),
    ]
    gx, gy = 36, 276
    gap = 16
    cw = (W - 2 * gx - 2 * gap) // 3
    ch = 316
    for idx, (kicker, head, body) in enumerate(cards):
        r, c = divmod(idx, 3)
        x0 = gx + c * (cw + gap)
        y0 = gy + r * (ch + gap)
        d.rounded_rectangle([x0, y0, x0 + cw, y0 + ch], radius=10,
                            fill=CARD_BG, outline=(210, 198, 176), width=1)
        # accent kicker bar
        d.rectangle([x0 + 18, y0 + 18, x0 + 54, y0 + 22], fill=ACCENT)
        d.text((x0 + 18, y0 + 30), kicker, font=F_KICKER, fill=ACCENT_DARK)
        inner = cw - 36
        lines = wrap(d, head, F_HEAD, inner)
        y = y0 + 58
        for ln in lines[:3]:
            d.text((x0 + 18, y), ln, font=F_HEAD, fill=INK)
            y += 30
        y += 6
        for ln in wrap(d, body, F_BODY, inner)[:6]:
            d.text((x0 + 18, y), ln, font=F_BODY, fill=INK_SOFT)
            y += 24

    # ---- Bottom ticker strip -------------------------------------------
    ticker = ("ISRAELI SOLDIER SUICIDES: 16-YEAR HIGH (23)   \u00b7   "
              "SK EDUCATION MINISTER RESIGNS   \u00b7   "
              "BRENT $90.55, -2%")
    ty = 940
    d.rectangle([0, ty, W, H], fill=TICKER_BG)
    # shrink ticker font if it would overflow
    tf = F_TICKER
    while d.textlength(ticker, font=tf) > W - 48 and tf.size > 11:
        tf = font("DejaVuSans-Bold.ttf", tf.size - 1)
    draw_centered(d, W // 2, ty + 12, ticker, tf, TICKER_FG)
    d.text((W // 2 - d.textlength("SOURCES: WIRE REPORTS, 23 NOV 2026",
            font=F_STAT_LBL) / 2, ty + 44),
           "SOURCES: WIRE REPORTS, 23 NOV 2026", font=F_STAT_LBL,
           fill=(170, 160, 145))

    img.save(out, "PNG", optimize=True)
    print("wrote", out)


if __name__ == "__main__":
    main()
