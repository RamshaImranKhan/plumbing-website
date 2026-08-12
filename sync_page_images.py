"""Inject contextual hero images into service and resource pages."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SERVICES = ROOT / "services"
RESOURCES = ROOT / "resources"

IMG = "../assets/images"
SVC = f"{IMG}/services"

SERVICE_IMAGES: dict[str, tuple[str, str]] = {
    "bathtubs.html": (f"{SVC}/bfp-service-feature-bathtubs.webp", "Professional bathtub plumbing service in Omaha"),
    "drains.html": (f"{SVC}/bfp-service-feature-drains.webp", "Professional drain cleaning and repair"),
    "drain-cleaning.html": (f"{SVC}/bfp-service-feature-drains.webp", "Expert drain cleaning service"),
    "drain-installation.html": (f"{SVC}/bfp-service-feature-drains.webp", "Professional drain installation"),
    "hydrojetting.html": (f"{SVC}/bfp-service-feature-drains.webp", "Hydro jetting drain cleaning service"),
    "emergency-plumbing.html": (f"{SVC}/bfp-service-feature-emergency_service.webp", "24/7 emergency plumbing response"),
    "faucets.html": (f"{SVC}/bfp-service-feature-faucets.webp", "Faucet repair and installation"),
    "garbage-disposals.html": (f"{SVC}/bfp-service-feature-garbage_disposals.webp", "Garbage disposal plumbing service"),
    "garbage-disposal-repair.html": (f"{SVC}/bfp-service-feature-garbage_disposals.webp", "Garbage disposal repair"),
    "garbage-disposal-installation.html": (f"{SVC}/bfp-service-feature-garbage_disposals.webp", "Garbage disposal installation"),
    "sewers.html": (f"{SVC}/bfp-service-feature-sewers.webp", "Sewer line inspection and repair"),
    "sewer-line-repair.html": (f"{SVC}/bfp-service-feature-sewers.webp", "Sewer line repair service"),
    "sewer-line-replacement.html": (f"{SVC}/bfp-service-feature-sewers.webp", "Sewer line replacement"),
    "trenchless-sewers.html": (f"{SVC}/bfp-service-feature-sewers.webp", "Trenchless sewer repair"),
    "showers.html": (f"{SVC}/bfp-service-feature-showers.webp", "Shower plumbing installation and repair"),
    "shower-repair.html": (f"{SVC}/bfp-service-feature-showers.webp", "Shower repair service"),
    "shower-installation.html": (f"{SVC}/bfp-service-feature-showers.webp", "Shower installation"),
    "sinks.html": (f"{SVC}/bfp-service-feature-sinks.webp", "Sink plumbing installation and repair"),
    "sink-repair.html": (f"{SVC}/bfp-service-feature-sinks.webp", "Sink repair service"),
    "sink-installation.html": (f"{SVC}/bfp-service-feature-sinks.webp", "Sink installation"),
    "toilets.html": (f"{SVC}/bfp-service-feature-toilets.webp", "Toilet plumbing service"),
    "toilet-repair.html": (f"{SVC}/bfp-service-feature-toilets.webp", "Toilet repair service"),
    "toilet-installation.html": (f"{SVC}/bfp-service-feature-toilets.webp", "Toilet installation"),
    "plumbing-repairs.html": (f"{SVC}/bfp-service-feature-plumbing_repairs.webp", "Professional plumbing repair"),
    "pipe-repair.html": (f"{SVC}/bfp-service-feature-plumbing_repairs.webp", "Pipe repair service"),
    "leaking-pipes.html": (f"{SVC}/bfp-service-feature-plumbing_repairs.webp", "Leaking pipe repair"),
    "frozen-pipes.html": (f"{SVC}/bfp-service-feature-plumbing_repairs.webp", "Frozen pipe repair"),
    "piping-repiping.html": (f"{SVC}/bfp-service-feature-plumbing_repairs.webp", "Pipe repiping service"),
    "plumbing-installation.html": (f"{SVC}/bfp-service-feature-plumbing_repairs.webp", "Professional plumbing installation"),
    "plumbing-inspection.html": (f"{SVC}/bfp-service-feature-plumbing_repairs.webp", "Plumbing inspection service"),
    "outdoor-plumbing.html": (f"{SVC}/bfp-service-feature-plumbing_repairs.webp", "Outdoor plumbing service"),
    "water-lines.html": (f"{SVC}/bfp-service-feature-plumbing_repairs.webp", "Water line repair and installation"),
    "water-heaters.html": (f"{IMG}/tips/bfp-water-heater.png", "Water heater service and installation"),
    "water-heater-repair.html": (f"{IMG}/tips/bfp-water-heater.png", "Water heater repair service"),
    "water-heater-installation.html": (f"{IMG}/tips/bfp-water-heater.png", "Water heater installation"),
    "tankless-water-heaters.html": (f"{IMG}/tips/bfp-water-heater.png", "Tankless water heater service"),
    "leak-repair.html": (f"{IMG}/blog/leak_2.jpg", "Water leak repair service"),
    "leak-detection.html": (f"{IMG}/blog/leak_2.jpg", "Professional leak detection"),
    "slab-leaks.html": (f"{IMG}/blog/leak_2.jpg", "Slab leak detection and repair"),
    "pool-leak-detection.html": (f"{IMG}/blog/leak_2.jpg", "Pool leak detection service"),
    "sump-pumps.html": (f"{SVC}/bfp-service-feature-plumbing_repairs.webp", "Sump pump installation and repair"),
    "water-pumps.html": (f"{SVC}/bfp-service-feature-plumbing_repairs.webp", "Water pump service"),
    "pool-pump-plumbers.html": (f"{SVC}/bfp-service-feature-plumbing_repairs.webp", "Pool pump plumbing service"),
    "pumps.html": (f"{SVC}/bfp-service-feature-plumbing_repairs.webp", "Pump installation and repair"),
    "water-treatment.html": (f"{IMG}/hero-plumbers.png", "Water treatment and filtration service"),
    "brita-pro-filtration.html": (f"{IMG}/hero-plumbers.png", "BRITA PRO water filtration"),
    "index.html": (f"{IMG}/bfp-truck-circle.webp", "Benjamin Franklin Plumbing service van in Omaha"),
}

RESOURCE_IMAGES: dict[str, tuple[str, str]] = {
    "about.html": (f"{IMG}/hero-plumbers.png", "Benjamin Franklin Plumbing professional serving Omaha"),
    "our-guarantees.html": (f"{IMG}/bfp-truck-circle.webp", "Benjamin Franklin Plumbing on-time guarantee"),
    "club-membership.html": (f"{IMG}/hero-plumbers.png", "Benjamin Franklin Plumbing club membership"),
    "community-involvement.html": (f"{IMG}/bfp-hero-group.webp", "Benjamin Franklin Plumbing team in the community"),
    "code-of-ethics.html": (f"{IMG}/hero-plumbers.png", "Benjamin Franklin Plumbing code of ethics"),
    "in-the-media.html": (f"{IMG}/blog/sc_headshot-1_1.jpg", "Benjamin Franklin Plumbing in the media"),
    "financing.html": (f"{IMG}/bfp-truck-circle.webp", "Flexible plumbing financing in Omaha"),
    "faq.html": (f"{IMG}/bfp-truck-circle.webp", "Benjamin Franklin Plumbing FAQ"),
    "newsletter.html": (f"{IMG}/hero-plumbers.png", "Benjamin Franklin Plumbing newsletter"),
    "blog.html": (f"{IMG}/blog/clogged-drain.jpg", "Plumbing tips and advice"),
    "expert-tips.html": (f"{IMG}/blog/clogged-drain.jpg", "Expert plumbing tips from Benjamin Franklin"),
}

HERO_FEATURE_RE = re.compile(
    r'\s*<figure class="service-hero-feature">.*?</figure>\s*',
    re.DOTALL,
)

PAGE_FEATURE_RE = re.compile(
    r'\s*<figure class="page-feature-image">.*?</figure>\s*',
    re.DOTALL,
)

SERVICES_INDEX_IMAGE_RE = re.compile(
    r'\s*<figure class="services-hero-image">.*?</figure>\s*',
    re.DOTALL,
)


def hero_feature_block(src: str, alt: str) -> str:
    return f"""          <figure class="service-hero-feature">
            <img src="{src}" alt="{alt}" width="612" height="425" loading="eager">
          </figure>
"""


def page_feature_block(src: str, alt: str) -> str:
    return f"""        <figure class="page-feature-image">
          <img src="{src}" alt="{alt}" width="560" height="400" loading="lazy">
        </figure>
"""


def services_index_image_block(src: str, alt: str) -> str:
    return f"""          <figure class="services-hero-image">
            <img src="{src}" alt="{alt}" width="480" height="480" loading="eager">
          </figure>
"""


def cleanup_html(html: str) -> str:
    html = re.sub(
        r'(<figure class="service-hero-feature">.*?</figure>)\s*\n\s*(<div class="forbes-badge">)',
        r"\1\n\n          \2",
        html,
        flags=re.DOTALL,
    )
    html = re.sub(
        r'(<figure class="services-hero-image">.*?</figure>)\s*\n\s*(<div class="forbes-badge">)',
        r"\1\n\n            \2",
        html,
        flags=re.DOTALL,
    )
    return html


def inject_service_hero(html: str, src: str, alt: str) -> str:
    html = HERO_FEATURE_RE.sub("\n", html)
    needle = '<div class="service-hero-aside">\n'
    block = needle + hero_feature_block(src, alt)
    if '<div class="service-hero-aside">' not in html.replace('\r\n', '\n'):
        return html
    if 'class="service-hero-feature"' in html:
        return cleanup_html(html)
    return cleanup_html(html.replace('<div class="service-hero-aside">', block, 1))


def inject_resource_image(html: str, src: str, alt: str, filename: str = "") -> str:
    html = PAGE_FEATURE_RE.sub("\n", html)
    if 'class="page-feature-image"' in html:
        return html

    if 'class="faq-intro"' in html:
        needle = '<div class="faq-intro">'
        return html.replace(
            needle,
            needle + "\n          " + page_feature_block(src, alt).strip(),
            1,
        )

    if "about-page-content" in html:
        match = re.search(r'(<div class="container about-page-content[^"]*">)', html)
        if match:
            needle = match.group(1)
            return html.replace(
                needle,
                needle + "\n" + page_feature_block(src, alt),
                1,
            )

    if 'class="post-list-header"' in html:
        needle = '<div class="post-list-header">'
        return html.replace(
            needle,
            page_feature_block(src, alt) + needle,
            1,
        )

    if 'class="services-hero-lead"' in html and filename == "newsletter.html":
        match = re.search(r'(<p class="services-hero-lead">.*?</p>)', html, re.DOTALL)
        if match:
            block = "\n" + services_index_image_block(src, alt)
            return html[: match.end()] + block + html[match.end() :]

    if 'class="service-hero-content"' in html and filename == "financing.html":
        match = re.search(
            r'(<p>Don\'t put plumbing repairs on hold\.[^<]*</p>)',
            html,
        )
        if match:
            block = "\n      " + page_feature_block(src, alt).strip() + "\n"
            return html[: match.end()] + block + html[match.end() :]

    return html


def inject_services_index(html: str, src: str, alt: str) -> str:
    html = SERVICES_INDEX_IMAGE_RE.sub("\n", html)
    if 'class="services-hero-image"' in html:
        return cleanup_html(html)
    match = re.search(
        r'(<p class="services-hero-lead">.*?</p>)',
        html,
        re.DOTALL,
    )
    if not match:
        return html
    insert_at = match.end()
    block = "\n" + services_index_image_block(src, alt)
    return cleanup_html(html[:insert_at] + block + html[insert_at:])


def main() -> None:
    updated = 0
    for name, (src, alt) in SERVICE_IMAGES.items():
        path = SERVICES / name
        if not path.exists():
            print(f"missing {path}")
            continue
        text = path.read_text(encoding="utf-8")
        if name == "index.html":
            new_text = inject_services_index(text, src, alt)
        else:
            new_text = inject_service_hero(text, src, alt)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            updated += 1
            print(f"service: {name}")

    for name, (src, alt) in RESOURCE_IMAGES.items():
        path = RESOURCES / name
        if not path.exists():
            print(f"missing {path}")
            continue
        text = path.read_text(encoding="utf-8")
        new_text = inject_resource_image(text, src, alt, name)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            updated += 1
            print(f"resource: {name}")

    print(f"Done. Updated {updated} pages.")


if __name__ == "__main__":
    main()
