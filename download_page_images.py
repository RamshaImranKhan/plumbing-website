"""Download BFP page images used across service and resource pages."""
from __future__ import annotations

import ssl
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE = "https://www.benjaminfranklinplumbing.com/img/upload/"
OUT = ROOT / "assets" / "images"
SERVICES = ROOT / "assets" / "images" / "services"

FILES = [
    ("about-us-hero-image_1.jpg", OUT),
    ("bfp-service-feature-water_heaters.webp", SERVICES),
    ("bfp-service-feature-pumps.webp", SERVICES),
    ("bfp-service-feature-leak_detection.webp", SERVICES),
    ("bfp-service-feature-water_treatment.webp", SERVICES),
    ("bfp-service-feature-outdoor_plumbing.webp", SERVICES),
    ("bfp-service-feature-piping_repiping.webp", SERVICES),
]

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def download(name: str, dest_dir: Path) -> None:
    dest_dir.mkdir(parents=True, exist_ok=True)
    out = dest_dir / name
    if out.exists() and out.stat().st_size > 1000:
        print(f"skip {name} ({out.stat().st_size} bytes)")
        return
    url = BASE + name
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        data = urllib.request.urlopen(req, timeout=60, context=ctx).read()
    except Exception as exc:
        print(f"fail {name}: {exc}")
        return
    if len(data) < 500:
        print(f"skip {name} (too small: {len(data)} bytes)")
        return
    out.write_bytes(data)
    print(f"ok   {name} ({len(data)} bytes)")


if __name__ == "__main__":
    for filename, folder in FILES:
        download(filename, folder)
