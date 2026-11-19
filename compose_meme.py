#!/usr/bin/env python3
"""Compose the gta6-meme-x-01 meme (meme.png) from the AI-generated Vice City
scene + the official make.fun ghost mark + PIL-rendered caption text.

Inputs (same directory): scene PNG (AI-generated, no text), makefun ghost mark.
Output: meme.png, 1024x1024, square.

Joke (original): GTA 6 took 13 years to make; my AI agent made this meme in
13 seconds — and got paid for it. The make.fun ghost stands in the scene
(bottom right) with the make.fun name beside it.
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
SCENE = HERE / "scene.png"
GHOST = Path("/tmp/makefun-mark-1024.png")
OUT = HERE / "meme.png"

FONT_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

W = 1024
TOP_H = 118      # top black caption bar
BOT_H = 160      # bottom black caption bar
SCENE_H = W - TOP_H - BOT_H


def fit_font(draw, text, start, max_w):
    size = start
    while size > 10:
        f = ImageFont.truetype(FONT_BOLD, size)
        if draw.textlength(text, font=f) <= max_w:
            return f
        size -= 2
    return ImageFont.truetype(FONT_BOLD, 10)


def centered(draw, y, text, font, fill="white", anchor="ma"):
    draw.text((W // 2, y), text, font=font, fill=fill, anchor=anchor,
              stroke_width=3, stroke_fill="black")


def main():
    scene = Image.open(SCENE).convert("RGB")
    # Centre-crop the scene to 1024 x SCENE_H
    sw, sh = scene.size
    target_ratio = W / SCENE_H
    if sw / sh > target_ratio:  # too wide: crop sides
        nw = int(sh * target_ratio)
        x0 = (sw - nw) // 2
        scene = scene.crop((x0, 0, x0 + nw, sh))
    else:  # too tall: crop top/bottom
        nh = int(sw / target_ratio)
        y0 = (sh - nh) // 2
        scene = scene.crop((0, y0, sw, y0 + nh))
    scene = scene.resize((W, SCENE_H), Image.LANCZOS)

    canvas = Image.new("RGB", (W, W), "black")
    canvas.paste(scene, (0, TOP_H))
    draw = ImageDraw.Draw(canvas)

    # --- captions (PIL text: spelling guaranteed, unlike AI-gen text) ---
    top_font = fit_font(draw, "GTA 6 TOOK 13 YEARS", 62, W - 48)
    centered(draw, TOP_H // 2, "GTA 6 TOOK 13 YEARS", top_font, anchor="mm")

    bot1 = "MY AI AGENT MADE THIS MEME"
    bot2 = "IN 13 SECONDS \u2014 AND GOT PAID"
    f1 = fit_font(draw, bot1, 56, W - 48)
    f2 = fit_font(draw, bot2, 56, W - 48)
    # two lines centred in the bottom bar
    line_h = 56
    y1 = TOP_H + SCENE_H + (BOT_H - 2 * line_h) // 2 + 4
    centered(draw, y1, bot1, f1)
    centered(draw, y1 + line_h, bot2, f2)

    # --- make.fun ghost mark, worked into the scene (bottom right) ---
    ghost = Image.open(GHOST).convert("RGBA")
    G = 200
    ghost = ghost.resize((G, G), Image.LANCZOS)
    gx, gy = W - G - 20, TOP_H + SCENE_H - G - 14
    canvas.paste(ghost, (gx, gy), ghost)

    # "make.fun" name beside the ghost, white bold with black outline
    label = "make.fun"
    lf = fit_font(draw, label, 60, gx - 24 - 24)
    tw = draw.textlength(label, font=lf)
    ly = gy + G // 2
    draw.text((gx - 24 - tw, ly), label, font=lf, fill="white", anchor="lm",
              stroke_width=4, stroke_fill="black")

    canvas.save(OUT, "PNG")
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    sys.exit(main())
