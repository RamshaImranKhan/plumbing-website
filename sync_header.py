"""Sync the shared site header to all HTML pages."""
from __future__ import annotations

import re
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
TEMPLATE_PATH = ROOT_DIR / "includes" / "site-header.html"

ABOUT_PAGES = {
    "about.html",
    "in-the-media.html",
    "code-of-ethics.html",
    "community-involvement.html",
    "our-guarantees.html",
    "club-membership.html",
}

HEADER_PATTERN = re.compile(
    r"  (?:<!-- Forbes announcement bar -->\s*)?"
    r"<div class=\"forbes-bar\".*?"
    r"</header>\r?\n",
    re.DOTALL,
)


def get_paths(rel: str) -> dict[str, str]:
    parts = rel.replace("\\", "/").split("/")
    depth = len(parts) - 1
    root = "../" * depth if depth else ""

    if rel == "index.html":
        return {
            "ROOT": "",
            "HOME": "index.html",
            "SVC": "services/",
            "RES": "resources/",
            "AREAS": "#areas",
            "QUOTE": "#quote",
            "LOC": "#services",
            "ACTIVE_SERVICES": " bfp-nav-btn-active",
            "ACTIVE_RESOURCES": "",
            "ACTIVE_ABOUT": "",
        }

    filename = parts[-1]
    section = parts[0]

    home = f"{root}index.html"
    areas = f"{home}#areas"
    quote = f"{home}#quote"

    if section == "services":
        svc = ""
        res = f"{root}resources/"
        loc = "index.html"
        active_services = " bfp-nav-btn-active"
        active_resources = ""
        active_about = ""
    elif section == "resources":
        if len(parts) == 2:
            svc = f"{root}services/"
            res = ""
        else:
            svc = f"{root}services/"
            res = "../"
        loc = f"{svc}index.html"
        active_services = ""
        if filename in ABOUT_PAGES:
            active_resources = ""
            active_about = " bfp-nav-btn-active"
        else:
            active_resources = " bfp-nav-btn-active"
            active_about = ""
    else:
        svc = f"{root}services/"
        res = f"{root}resources/"
        loc = f"{svc}index.html"
        active_services = ""
        active_resources = ""
        active_about = ""

    return {
        "ROOT": root,
        "HOME": home,
        "SVC": svc,
        "RES": res,
        "AREAS": areas,
        "QUOTE": quote,
        "LOC": loc,
        "ACTIVE_SERVICES": active_services,
        "ACTIVE_RESOURCES": active_resources,
        "ACTIVE_ABOUT": active_about,
    }


def render_header(rel: str, template: str) -> str:
    paths = get_paths(rel)
    header = template
    for key, value in paths.items():
        header = header.replace(f"{{{{{key}}}}}", value)
    return header


def iter_pages() -> list[Path]:
    pages: list[Path] = [ROOT_DIR / "index.html"]
    for folder in ("services", "resources"):
        for path in (ROOT_DIR / folder).rglob("*.html"):
            if "scraped" in path.parts:
                continue
            pages.append(path)
    return sorted(set(pages))


def main() -> None:
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    updated = 0
    skipped = 0

    for path in iter_pages():
        rel = path.relative_to(ROOT_DIR).as_posix()
        content = path.read_text(encoding="utf-8")
        header = render_header(rel, template)

        if not HEADER_PATTERN.search(content):
            print(f"SKIP (no header match): {rel}")
            skipped += 1
            continue

        new_content = HEADER_PATTERN.sub(header, content, count=1)
        if new_content != content:
            path.write_text(new_content, encoding="utf-8", newline="\n")
            print(f"UPDATED: {rel}")
            updated += 1
        else:
            print(f"UNCHANGED: {rel}")

    print(f"\nDone: {updated} updated, {skipped} skipped.")


if __name__ == "__main__":
    main()
