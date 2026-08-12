"""Sync Authority Brands section and footer logo to all HTML pages."""
from __future__ import annotations

import re
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
BRANDS_TEMPLATE = ROOT_DIR / "includes" / "site-authority-brands.html"
FOOTER_BOTTOM_TEMPLATE = ROOT_DIR / "includes" / "site-footer-bottom.html"
PRIVACY_MODAL_TEMPLATE = ROOT_DIR / "includes" / "privacy-consent-modal.html"

AUTHORITY_PATTERN = re.compile(
    r"    <section class=\"section authority-brands\".*?</section>\r?\n",
    re.DOTALL,
)

MAIN_CLOSE_PATTERN = re.compile(r"(\r?\n  </main>)")

FOOTER_LOGO_MARKER = "footer-logo-link"
FOOTER_BOTTOM_MARKER = "footer-guarantee-text"

FOOTER_BOTTOM_PATTERN = re.compile(
    r"    <div class=\"footer-bottom\">[\s\S]*?(?=\s*</footer>)",
)

FOOTER_CLOSE_PATTERN = re.compile(r"(\s*</footer>)")

FOOTER_LEGAL_PATTERN = re.compile(
    r"\s*<div class=\"footer-legal\">.*?</div>\r?\n",
    re.DOTALL,
)

PRIVACY_MODAL_MARKER = 'id="privacyModal"'
PRIVACY_MODAL_PATTERN = re.compile(
    r"  <div class=\"privacy-modal\" id=\"privacyModal\"[\s\S]*?(?=\s*<script src=\"[^\"]*app\.js\">)",
)

SCRIPT_TAG_PATTERN = re.compile(r"(\s*<script src=\"[^\"]*app\.js\">)")


def get_paths(rel: str) -> dict[str, str]:
    parts = rel.replace("\\", "/").split("/")
    depth = len(parts) - 1
    root = "../" * depth if depth else ""
    home = f"{root}index.html" if rel != "index.html" else "index.html"

    if rel == "index.html":
        res = "resources/"
    elif parts[0] == "services":
        res = f"{root}resources/"
    elif parts[0] == "resources":
        if len(parts) == 2:
            res = ""
        else:
            res = "../"
    else:
        res = f"{root}resources/"

    return {"ROOT": root, "HOME": home, "RES": res}


def render_brands(rel: str, template: str) -> str:
    block = template
    for key, value in get_paths(rel).items():
        block = block.replace(f"{{{{{key}}}}}", value)
    return block


def render_footer_bottom(rel: str, template: str) -> str:
    block = template
    for key, value in get_paths(rel).items():
        block = block.replace(f"{{{{{key}}}}}", value)
    return block


def render_privacy_modal(rel: str, template: str) -> str:
    block = template
    for key, value in get_paths(rel).items():
        block = block.replace(f"{{{{{key}}}}}", value)
    return block


def inject_privacy_modal(content: str, modal_html: str) -> str:
    block = modal_html if modal_html.startswith("\n") else f"\n{modal_html}"
    if PRIVACY_MODAL_MARKER in content and PRIVACY_MODAL_PATTERN.search(content):
        return PRIVACY_MODAL_PATTERN.sub(block, content, count=1)
    if PRIVACY_MODAL_MARKER in content:
        return content
    if not SCRIPT_TAG_PATTERN.search(content):
        return content
    return SCRIPT_TAG_PATTERN.sub(block + r"\1", content, count=1)


def inject_footer_bottom(content: str, footer_bottom_html: str) -> str:
    block = footer_bottom_html if footer_bottom_html.startswith("\n") else f"\n{footer_bottom_html}"
    content = FOOTER_LEGAL_PATTERN.sub("\n", content, count=1)
    if FOOTER_BOTTOM_MARKER in content and FOOTER_BOTTOM_PATTERN.search(content):
        return FOOTER_BOTTOM_PATTERN.sub(block, content, count=1)
    if "</footer>" in content:
        return FOOTER_CLOSE_PATTERN.sub(block + r"\1", content, count=1)
    return content


def fix_broken_footer(content: str, footer_bottom_html: str, rel: str) -> str:
    if "</footer>" in content:
        return content

    paths = get_paths(rel)
    script_path = f'{paths["ROOT"]}app.js'
    quote = f'{paths["HOME"]}#quote'
    block = footer_bottom_html if footer_bottom_html.startswith("\n") else f"\n{footer_bottom_html}"
    mobile = (
        f'  <div class="mobile-cta" aria-label="Quick actions">\n'
        f'    <a href="tel:4029228334" class="mobile-cta-call">Call</a>\n'
        f'    <a href="{quote}" class="mobile-cta-book">Book Now</a>\n'
        f"  </div>\n  "
    )

    pattern = re.compile(
        rf'(<footer class="site-footer">[\s\S]*?)(  <script src="{re.escape(script_path)}">)',
        re.DOTALL,
    )

    def replacer(match: re.Match[str]) -> str:
        footer_part = match.group(1).rstrip()
        open_divs = footer_part.count("<div")
        close_divs = footer_part.count("</div>")
        if open_divs > close_divs:
            footer_part += "\n    </div>"
        return f"{footer_part}{block}  </footer>\n{mobile}{match.group(2)}"

    return pattern.sub(replacer, content, count=1)


def inject_authority_brands(content: str, brands_html: str) -> str:
    block = brands_html if brands_html.startswith("\n") else f"\n{brands_html}"
    if AUTHORITY_PATTERN.search(content):
        return AUTHORITY_PATTERN.sub(block, content, count=1)
    if "</main>" not in content:
        return content
    return MAIN_CLOSE_PATTERN.sub(block + r"\1", content, count=1)


def inject_footer_logo(content: str, rel: str) -> str:
    if FOOTER_LOGO_MARKER in content:
        return content

    paths = get_paths(rel)
    logo = (
        f'      <a href="{paths["HOME"]}" class="footer-logo-link" aria-label="Benjamin Franklin Plumbing of Omaha home">\n'
        f'        <img class="footer-logo" src="{paths["ROOT"]}assets/logos/bfp-logo-white.svg" '
        f'alt="Benjamin Franklin Plumbing" width="180" height="72" loading="lazy">\n'
        f"      </a>\n"
    )

    updated = content.replace("<div class=\"footer-brand\">", f'<div class="footer-brand">\n      {logo}', 1)
    return updated


def iter_pages() -> list[Path]:
    pages: list[Path] = [ROOT_DIR / "index.html"]
    for folder in ("services", "resources"):
        for path in (ROOT_DIR / folder).rglob("*.html"):
            if "scraped" in path.parts:
                continue
            pages.append(path)
    return sorted(set(pages))


def main() -> None:
    brands_template = BRANDS_TEMPLATE.read_text(encoding="utf-8")
    footer_bottom_template = FOOTER_BOTTOM_TEMPLATE.read_text(encoding="utf-8")
    privacy_modal_template = PRIVACY_MODAL_TEMPLATE.read_text(encoding="utf-8")
    updated = 0
    skipped = 0

    for path in iter_pages():
        rel = path.relative_to(ROOT_DIR).as_posix()
        content = path.read_text(encoding="utf-8")
        brands_html = render_brands(rel, brands_template)
        footer_bottom_html = render_footer_bottom(rel, footer_bottom_template)
        privacy_modal_html = render_privacy_modal(rel, privacy_modal_template)

        if "</main>" not in content and "<footer" not in content:
            print(f"SKIP (no main/footer): {rel}")
            skipped += 1
            continue

        new_content = inject_authority_brands(content, brands_html)
        new_content = inject_footer_logo(new_content, rel)
        new_content = fix_broken_footer(new_content, footer_bottom_html, rel)
        new_content = inject_footer_bottom(new_content, footer_bottom_html)
        new_content = inject_privacy_modal(new_content, privacy_modal_html)

        if new_content != content:
            path.write_text(new_content, encoding="utf-8", newline="\n")
            print(f"UPDATED: {rel}")
            updated += 1
        else:
            print(f"UNCHANGED: {rel}")

    print(f"\nDone: {updated} updated, {skipped} skipped.")


if __name__ == "__main__":
    main()
