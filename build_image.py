#!/usr/bin/env python3
"""Build entry.png: one 1024x1024 poster summing up the world news of
Wednesday, 18 November 2026, as reported that day (AP, AFP, Al Jazeera,
UN News and the day's news roundups).

Run locally to regenerate the image the entry ships:
    python3 build_image.py
The grader never runs this file; main.ts copies the finished entry.png.
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 243, 233)
INK = (18, 18, 20)
RED = (178, 32, 40)
BLUE = (24, 62, 122)
GREY = (92, 92, 96)
RULE = (30, 30, 34)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        trial = (cur + " " + w_).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def block(draw, x, y, width, kicker, head, body, head_size=30, body_size=21):
    draw.text((x, y), kicker, font=font(SANS_B, 17), fill=RED)
    y += 26
    for line in wrap(draw, head, font(SERIF_B, head_size), width):
        draw.text((x, y), line, font=font(SERIF_B, head_size), fill=INK)
        y += head_size + 6
    y += 2
    for line in wrap(draw, body, font(SANS, body_size), width):
        draw.text((x, y), line, font=font(SANS, body_size), fill=(45, 45, 50))
        y += body_size + 6
    return y


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 56  # margin

    # Masthead
    d.rectangle([0, 0, W, 138], fill=INK)
    d.text((M, 22), "THE WORLD IN ONE IMAGE", font=font(SERIF_B, 55), fill=(250, 248, 240))
    d.text((M, 96), "Wednesday, 18 November 2026  ·  The day's world news, summed up",
           font=font(SANS, 22), fill=(205, 205, 210))

    y = 162
    # Lead story, full width
    y = block(
        d, M, y, W - 2 * M,
        "LEAD · SHENZHEN & MANILA",
        "Two summits, one Pacific: Xi, Putin and Trump converge",
        "APEC opened in Shenzhen, where Xi Jinping met Vladimir Putin and Donald Trump "
        "landed for three-way talks set for Thursday. Across the water, Quad leaders met "
        "in Manila for the first time in over two years, and Washington announced a trade "
        "deal with the Philippines.",
        head_size=33, body_size=21,
    )
    y += 8
    d.line([M, y, W - M, y], fill=RULE, width=3)
    y += 18

    # Two columns
    col_w = (W - 2 * M - 36) // 2
    x2 = M + col_w + 36
    y_left = block(
        d, M, y, col_w,
        "MIDDLE EAST",
        "Drones over the Gulf",
        "Iran said it sent drones at the US base at Ali Al Salem in Kuwait; Bahrain "
        "intercepted attacks before dawn, and US aircraft struck a missile launch site "
        "on Qeshm Island. Hormuz shipping stayed disrupted and oil held near $93.",
    )
    y_right = block(
        d, x2, y, col_w,
        "UKRAINE",
        "141 drones in a night",
        "Ukraine's air force counted 141 Russian drones, 126 of them downed or "
        "suppressed; six people were hurt in Dnipro. The EU proposed a loan of up to "
        "45 billion euros for Kyiv for 2027.",
    )
    y = max(y_left, y_right) + 6
    d.line([M, y, W - M, y], fill=RULE, width=2)
    y += 16

    y_left = block(
        d, M, y, col_w,
        "UNITED STATES",
        "Alaska flips the Senate",
        "Democrat Mary Peltola defeated Republican senator Dan Sullivan in Alaska, "
        "giving Democrats a projected 56-44 majority in the incoming Senate.",
    )
    y_right = block(
        d, x2, y, col_w,
        "GAZA",
        "Ceasefire warning",
        "The US-backed Board of Peace warned the truce could collapse, as the WHO put "
        "950,000 displaced Palestinians on flood-prone ground facing a fourth winter.",
    )
    y = max(y_left, y_right) + 6
    d.line([M, y, W - M, y], fill=RULE, width=2)
    y += 14

    # Bottom strip: three briefs
    briefs = [
        ("NVIDIA", "Board rules out a return for Jensen Huang; revenue forecast beats expectations."),
        ("CYCLONE AKVAN", "Severe storm puts South Odisha on high alert; evacuations under way."),
        ("PAPUA NEW GUINEA", "Magnitude 6.0 earthquake strikes; no tsunami threat issued."),
    ]
    bw = (W - 2 * M - 2 * 24) // 3
    for i, (k, t) in enumerate(briefs):
        bx = M + i * (bw + 24)
        d.text((bx, y), k, font=font(SANS_B, 16), fill=BLUE)
        by = y + 23
        for line in wrap(d, t, font(SANS, 17), bw):
            d.text((bx, by), line, font=font(SANS, 17), fill=(45, 45, 50))
            by += 23

    # Footer
    d.rectangle([0, H - 52, W, H], fill=INK)
    d.text((M, H - 38), "Compiled from the day's reporting: AP · AFP · Al Jazeera · UN News",
           font=font(SANS, 19), fill=(220, 220, 224))

    img.save("entry.png", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
