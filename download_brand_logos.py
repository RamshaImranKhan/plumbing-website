"""Download Authority Brands partner logos from BFP CDN."""
from __future__ import annotations

import subprocess
from pathlib import Path

BASE = "https://www.benjaminfranklinplumbing.com/img/upload/"
FILES = [
    "one-hour.png",
    "mister-sparky_2.png",
    "drymedic-logo_2.png",
    "service-team.png",
    "jnk-005_oval_logo_final_no_tagline_rgb_1.png",
    "tca-logo_2_1.png",
    "screenmobile-logo-423x180-1_1.png",
    "monster-tree-service_2.png",
    "asp_1.png",
    "msq-header-logo-sm_1.webp",
    "lsq_logo_fullcolor_7.png",
    "doody-calls_2.png",
    "woofies-logo.png",
    "homewatch-caregivers_2.png",
    "benjamin-franklin.png",
]

OUT_DIR = Path(__file__).resolve().parent / "assets" / "logos" / "brands"


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"

    for name in FILES:
        out = OUT_DIR / name
        if out.exists() and out.stat().st_size > 0:
            print(f"SKIP {name}")
            continue
        url = BASE + name
        result = subprocess.run(
            ["curl.exe", "-L", "-A", ua, url, "-o", str(out)],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0 or not out.exists() or out.stat().st_size == 0:
            print(f"FAIL {name}: {result.stderr.strip()}")
        else:
            print(f"OK   {name} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
