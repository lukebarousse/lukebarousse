#!/usr/bin/env python3
"""Generate the small pill link-buttons used in the course table."""
import os

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets")
FONT = ("-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,"
        "'Liberation Sans',sans-serif")

# simple-icons (CC0) / material (Apache-2.0) 24x24 paths
ICONS = {
    "youtube": "M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z",
    "github": "M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12",
    "cap": "M12 3 1 9l11 6 9-4.91V17h2V9L12 3zM5 13.18v4L12 21l7-3.82v-4L12 17l-7-3.82z",
}

# advance widths as a fraction of font-size, semibold sans
NARROW = set("iljtfr.,:;!|'")
WIDE = set("mwMW@")
UPPER = set("ABCDEFGHIJKLMNOPQRSTUVXYZ")

def text_width(s, size):
    w = 0.0
    for ch in s:
        if ch == " ":
            w += 0.28
        elif ch in NARROW:
            w += 0.31
        elif ch in WIDE:
            w += 0.86
        elif ch in UPPER:
            w += 0.68
        elif ch.isdigit():
            w += 0.57
        else:
            w += 0.56
    return w * size

def button(label, icon, bg, path):
    size, h, rx = 12.5, 26, 8
    pad_l, ic, gap, pad_r = 9, 15, 6, 11
    tw = text_width(label, size)
    w = round(pad_l + ic + gap + tw + pad_r)
    tx = pad_l + ic + gap
    ty = 1 + h / 2 + size * 0.35
    scale = ic / 24
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h + 4}" viewBox="0 0 {w} {h + 4}" role="img" aria-label="{label}">
  <title>{label}</title>
  <rect x="0" y="3" width="{w}" height="{h}" rx="{rx}" fill="#000000" opacity="0.20"/>
  <rect x="0" y="1" width="{w}" height="{h}" rx="{rx}" fill="{bg}"/>
  <path d="M{rx} 1 h{w - 2 * rx} a{rx} {rx} 0 0 1 {rx} {rx} v6 h-{w} v-6 a{rx} {rx} 0 0 1 {rx} -{rx} z" fill="#ffffff" opacity="0.13"/>
  <g transform="translate({pad_l} {1 + (h - ic) / 2}) scale({scale:.5f})"><path d="{ICONS[icon]}" fill="#ffffff"/></g>
  <text x="{tx}" y="{ty:.1f}" font-family="{FONT}" font-size="{size}" font-weight="600" fill="#ffffff">{label}</text>
</svg>
'''
    open(os.path.join(OUT, path), "w").write(svg)
    print(f"  {path:28s} {w}x{h+4}  '{label}'")

button("Watch", "youtube", "#24292F", "btn-video.svg")
button("Code", "github", "#24292F", "btn-repo.svg")
button("Unlock", "cap", "#24292F", "btn-resources.svg")
