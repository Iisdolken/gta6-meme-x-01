#!/usr/bin/env python3
"""Compose the gta6-meme-x-01 meme from the base scene.

Opens scene.png, pastes the official make.fun ghost mascot in the
lower-right corner, renders the top and bottom captions with PIL, and
saves the result as meme.png.

Provenance script only: the meme.png shipped in this repo is the final
image that was posted on X.
"""

from PIL import Image, ImageDraw, ImageFont

SCENE = "scene.png"
GHOST = "/tmp/makefun-mark-1024.png"
OUTPUT = "meme.png"

TOP_TEXT = "GTA 6 TOOK 13 YEARS"
BOTTOM_LINES = ["MY AI AGENT MADE THIS MEME", "IN 13 SECONDS — AND GOT PAID"]


def load_font(size: int) -> ImageFont.FreeTypeFont:
    for path in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ):
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def draw_outlined(draw: ImageDraw.ImageDraw, x: int, y: int, text: str,
                  font: ImageFont.FreeTypeFont) -> None:
    """Draw white text with a black outline so it reads over neon."""
    draw.text((x, y), text, font=font, fill="black",
              stroke_width=6, stroke_fill="black", anchor="ma")
    draw.text((x, y), text, font=font, fill="white", anchor="ma")


def main() -> None:
    img = Image.open(SCENE).convert("RGB")
    width, height = img.size
    draw = ImageDraw.Draw(img)

    # Captions.
    top_font = load_font(64)
    bottom_font = load_font(52)
    draw_outlined(draw, width // 2, 40, TOP_TEXT, top_font)
    line_height = 64
    first_bottom_y = height - 40 - len(BOTTOM_LINES) * line_height
    for i, line in enumerate(BOTTOM_LINES):
        draw_outlined(draw, width // 2, first_bottom_y + i * line_height,
                      line, bottom_font)

    # Ghost mascot, lower-right corner, placed ABOVE the bottom caption
    # (earlier draft put it at height-190, overlapping the caption lines).
    ghost = Image.open(GHOST).convert("RGBA")
    ghost_size = 130
    ghost = ghost.resize((ghost_size, ghost_size))
    ghost_x = width - ghost_size - 24
    ghost_y = height - ghost_size - 340
    img.paste(ghost, (ghost_x, ghost_y), ghost)
    draw = ImageDraw.Draw(img)
    label_font = load_font(36)
    draw.text((ghost_x - 12, ghost_y + ghost_size // 2 - 18), "make.fun",
              font=label_font, fill="white", stroke_width=4,
              stroke_fill="black", anchor="ra")

    img.save(OUTPUT)
    print(f"Wrote {OUTPUT} ({width}x{height})")


if __name__ == "__main__":
    main()
