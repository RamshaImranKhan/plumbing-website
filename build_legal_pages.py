"""Build accessibility, site-map, privacy-policy, and terms-of-use pages."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TEMPLATE = ROOT / "resources" / "code-of-ethics.html"
PRIVACY_TXT = Path(r"C:\Users\DELL\.cursor\projects\d-website\agent-tools\ede709fd-50a0-4fc3-8ad7-5592c3afc6e0.txt")

BODY_REPLACE = re.compile(
    r"<div class=\"service-breadcrumb\">.*?</section>\s*(\s*<section class=\"section authority-brands\")",
    re.DOTALL,
)

SKIP_DIRS = {"scraped", "includes", "assets", "__pycache__"}
SERVICE_ORDER = [
    "index.html", "emergency-plumbing.html", "drains.html", "water-heaters.html",
    "sewers.html", "toilets.html", "sinks.html", "showers.html", "pumps.html",
]


def page_shell(title: str, description: str, breadcrumb: str, body_html: str) -> str:
    template = TEMPLATE.read_text(encoding="utf-8")
    template = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", template, count=1)
    template = re.sub(
        r'<meta name="description" content="[^"]*">',
        f'<meta name="description" content="{description}">',
        template,
        count=1,
    )
    breadcrumb_html = (
        f'<div class="service-breadcrumb"><div class="container">'
        f'<a href="../index.html">Home</a> / <span>{breadcrumb}</span></div></div>\n    '
    )
    section = (
        f'{breadcrumb_html}'
        f'<section class="section">\n'
        f'      <div class="container about-page-content legal-page-content">\n'
        f'        {body_html}\n'
        f'      </div>\n'
        f'    </section>\n\n\n\n    '
    )
    if not BODY_REPLACE.search(template):
        raise RuntimeError("Template main body marker not found")
    return BODY_REPLACE.sub(section + r"\1", template, count=1)


def accessibility_body() -> str:
    return """<h1>Accessibility</h1>
        <div class="about-page-body">
          <p class="legal-lead">Working to Improve Accessibility to Our Website and Strive to Create an Accessible and Barrier-free Environment</p>
          <h2>Our Commitment</h2>
          <p>Benjamin Franklin Plumbing is committed to providing individuals with disabilities access to information, goods, services and privileges offered on this website, www.benjaminfranklinplumbing.com, and is in an ongoing process of improving its accessibility. We are making every effort to provide a website in which functionality and content is accessible to all individuals, and we are actively updating and monitoring our website to make it as accessible as possible.</p>
          <p>If you experience difficulty accessing any part of this website, or if you have suggestions for improving accessibility, please contact us at <a href="tel:4029228334">(402) 922-8334</a> or through our <a href="../index.html#quote">online request form</a>.</p>
        </div>"""


def terms_body() -> str:
    return """<h1>Terms of Use</h1>
        <div class="about-page-body">
          <h2>Introduction</h2>
          <p>You have accessed the website of Authority Brands, Inc., and its parents, subsidiaries and affiliates ("Authority Brands"). For purposes of these Terms of Use, the "Site" includes the website of Benjamin Franklin Plumbing (www.benjaminfranklinplumbing.com/). Please read these Terms of Use carefully before using the Site. By accessing and browsing the Site, you agree to these Terms of Use with Authority Brands. If you do not agree to all of these Terms of Use please exit from this site immediately.</p>
          <p>The Site is comprised of various documents and web pages created and maintained by Authority Brands. While accessing and using the Site, you may be able to order services or conduct other business with Authority Brands through the Site (the "Services"). The Site and the Services are offered to you on the condition that you accept, without modification, the terms and conditions contained in this document. Your use of the Site and any Services constitutes your agreement to all such terms and conditions.</p>
          <p>Authority Brands may revise and update these Terms of Use at any time without notice. Please periodically review the Terms of Use posted at this website. Your continued use of the website will mean acceptance of those changes.</p>
          <p>The terms "Authority Brands," "Company," "we," and "our" are used in this site for purposes of convenience and are intended to refer to Authority Brands and/or its affiliates, subsidiaries or related parties either individually or collectively, as the context may require. These references are not intended to suggest that the various Authority Brands companies referred to are not independent corporate entities having separate corporate identities and management.</p>

          <h2>Communication and Privacy</h2>
          <p>Authority Brands owns the Site. If you have any questions about our Website Terms of Use and Policies, you may contact us by mail at: Authority Brands, Inc. c/o Corporate Marketing, Digital Services, 7120 Samuel Morse Drive Suite 300, Columbia, MD 21046.</p>
          <p>We know that many visitors to our site are concerned about the information they may provide and how we may use that information. Our <a href="privacy-policy.html">Privacy Policy</a> governs the collection, use, retention and disclosure of information we gather from the Site, and is available on the Site.</p>

          <h2>No Solicitation</h2>
          <p>The information provided through the Site is intended solely for the general knowledge of visitors to the Site and does not constitute an offer or a solicitation of an offer for the purchase or sale of any shares or other securities of Authority Brands. The information contained in this Website does not constitute advice or an offer to sell or deal in any securities and must not be relied upon in connection with any investment decision.</p>

          <h2>Currency and Accuracy of Information</h2>
          <p>Although Authority Brands makes reasonable efforts to ensure that the information provided through the Site is current and accurate, Authority Brands makes no representations or warranties as to the accuracy, reliability, completeness or timeliness of such information. All information is provided "as is" without any representation, warranty or condition as to its accuracy or reliability.</p>
          <p>Certain documents and other materials on the Site speak only as of the dates on which such documents and materials were filed or otherwise used by Authority Brands. The contents of such documents or materials may become out-of-date; however, Authority Brands makes no commitment and disclaims any duty to update those documents and materials.</p>

          <h2>Intellectual Property</h2>
          <p>The Site and its contents are protected by copyright, trademark and other proprietary rights of Authority Brands or third parties. Benjamin Franklin Plumbing names and logos, and all related product and service names, design marks and slogans are the trademarks or service marks of Authority Brands. Except as expressly permitted herein, no portion of this website or its contents may be reproduced, displayed or used in any form without prior written permission.</p>
          <p>Authority Brands hereby grants to you a non-exclusive and non-transferable license to view and print documents and web pages located on the Site for non-commercial or educational use within your organization only, subject to applicable conditions including retention of copyright notices.</p>
          <p>No other use of the information is authorized. Authority Brands reserves the right to require you to delete, destroy or otherwise remove any content that is used in a manner that in Authority Brands' sole opinion is contrary or otherwise inappropriate, derogatory or offensive.</p>

          <h2>Use of the Site</h2>
          <p>You may use the Site for lawful purposes only. You are prohibited from use on the Site, or transmitting to or through the Site, any unlawful, threatening, obscene, defamatory, libelous, harassing, pornographic, hateful or ethnically, racially or otherwise objectionable material, or any material that would contribute to a civil or criminal offense, otherwise violates any law, or which infringes on any intellectual property right.</p>
          <p>Any information submitted or communicated to Authority Brands through use of the Site or Services that does not include personal information or data about you is non-confidential and non-proprietary and Authority Brands may, without compensation to you, incorporate, distribute or otherwise use such information for any commercial or non-commercial purpose. Any personal information or data submitted to Authority Brands through use of the Services or Site is governed by the terms of the Privacy Policy.</p>

          <h2>Disclaimer of Liability</h2>
          <p>The Site contains general information and may contain errors, omissions and inaccuracies. Authority Brands assumes no liability or responsibility for any such errors, omissions or inaccuracies or any other limitation that may arise in relation to the Site. THE SITE IS PROVIDED "AS IS" AND "AS AVAILABLE" AND IS USED BY YOU STRICTLY AT YOUR SOLE RISK.</p>
          <p>IN NO EVENT SHALL AUTHORITY BRANDS BE LIABLE FOR ANY SPECIAL, INDIRECT, PUNITIVE OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA, REVENUE OR PROFITS, WHETHER RESULTING FROM AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORT OR CLAIM, ARISING OUT OF OR IN CONNECTION WITH THE USE OR RELIANCE UPON THE INFORMATION ON THIS SITE OR THE INTERNET GENERALLY.</p>
          <p>IN ALL OTHER CIRCUMSTANCES, AUTHORITY BRANDS' AGGREGATE AND COMPLETE LIABILITY TO YOU OR ANY THIRD PARTY, HOWEVER ARISING, SHALL BE LIMITED TO A MAXIMUM OF $10.00 (USD).</p>

          <h2>References and Links to Third Party Sites</h2>
          <p>The Site may contain links and other references to other websites. These Links are supplied to you merely as a convenience and the inclusion of any Link does not imply any approval or endorsement or recommendation of that third party or their related information, products or services. Authority Brands is not responsible for the content of any third party sites linked to or from the Site.</p>

          <h2>Additional Terms</h2>
          <p>Authority Brands may revise and update these Terms of Use at any time without notice. If any part of this agreement is found to be invalid or unenforceable, the remaining provisions in these Terms of Use shall continue in full force and effect.</p>

          <h2>Jurisdiction and Arbitration</h2>
          <p>Access to this website is governed by all applicable federal, state, provincial and local laws. Use of this website and the Terms of Use shall be governed and construed in accordance with the laws of the state of Texas, without regard to the choice of the law provisions thereof. You also agree that any disputes or claim relating to or arising out of or in connection with the use of the Site or the Terms of Use are to be settled by binding arbitration in Columbia, Maryland using the Commercial Arbitration Rules of the American Arbitration Association.</p>

          <h2>Acceptance of Terms of Use</h2>
          <p>Authority Brands maintains the Site to provide you with Services and information about Authority Brands. By using the Site, you agree that you have read, understood and agree to be bound by these Terms of Use. If you do not agree to the Terms of Use, do not use the Site.</p>
          <p>This agreement constitutes the entire understanding and agreement between you and Authority Brands with respect to the Site and your use of same.</p>
          <p><em>Last Amended: 9/19/2023</em></p>
        </div>"""


def title_case_heading(line: str) -> bool:
    if len(line) > 80 or len(line) < 4:
        return False
    if line.startswith("|") or line.startswith("http") or "@" in line:
        return False
    if line.endswith(".") and not line.endswith("..."):
        return False
    return True


def privacy_body() -> str:
    if not PRIVACY_TXT.exists():
        raise FileNotFoundError(f"Privacy source not found: {PRIVACY_TXT}")
    raw = PRIVACY_TXT.read_text(encoding="utf-8")
    lines = raw.splitlines()
    start = 0
    for i, line in enumerate(lines):
        if line.strip() == "Privacy Policy" and i > 0:
            start = i + 1
            break
    stop = len(lines)
    for i, line in enumerate(lines):
        if line.strip().startswith("##### Part of the"):
            stop = i
            break
    content_lines = lines[start:stop]
    html_parts = ['<h1>Privacy Policy</h1>\n        <div class="about-page-body">']
    in_table = False
    table_rows: list[str] = []
    skipped_intro = False

    def flush_table() -> None:
        nonlocal table_rows, in_table
        if not table_rows:
            in_table = False
            return
        html_parts.append('<table class="legal-table"><tbody>')
        header_done = False
        for row in table_rows:
            if row.startswith("| ---"):
                continue
            cells = [c.strip() for c in row.strip("|").split("|")]
            tag = "th" if not header_done else "td"
            header_done = True
            html_parts.append("<tr>" + "".join(f"<{tag}>{c}</{tag}>" for c in cells) + "</tr>")
        html_parts.append("</tbody></table>")
        table_rows = []
        in_table = False

    i = 0
    while i < len(content_lines):
        line = content_lines[i].strip()
        i += 1
        if not line or line == "Privacy Policy":
            continue
        if not skipped_intro:
            if line.startswith("Privacy Policy |") or line == "# Privacy Policy":
                continue
            if line.startswith("Effective Date:"):
                skipped_intro = True
            else:
                continue
        if line.startswith("|"):
            in_table = True
            if not line.startswith("| ---"):
                table_rows.append(line)
            continue
        if in_table:
            flush_table()
        if line.startswith("Effective Date:"):
            html_parts.append(f"<p><strong>{line}</strong></p>")
            continue
        if line.startswith("Last Updated:") or line.startswith("Click for"):
            html_parts.append(f"<p><em>{line}</em></p>")
            continue
        if title_case_heading(line) and line.isupper() is False and line[0].isupper():
            html_parts.append(f"<h2>{line}</h2>")
            continue
        if line.startswith("IMPORTANT ADDITIONAL INFORMATION FOR RESIDENTS OF CERTAIN U.S. STATES"):
            html_parts.append('<h2 id="your-privacy-choices">Your Privacy Choices</h2>')
            html_parts.append(f"<h2>{line}</h2>")
            continue
        html_parts.append(f"<p>{line}</p>")

    if in_table:
        flush_table()
    html_parts.append("</div>")
    return "\n          ".join(html_parts)


def link_for(path: Path) -> tuple[str, str]:
    label = path.stem.replace("-", " ").title()
    if path.name == "index.html" and path.parent.name == "services":
        return "../services/index.html", "All Services"
    if path.parent.name == "services":
        return f"../services/{path.name}", label
    if path.parent.name == "blog":
        return f"blog/{path.name}", label
    if path.parent.name == "expert-tips":
        return f"expert-tips/{path.name}", label
    if path.parent.name == "resources":
        return path.name, label
    return path.name, label


def site_map_body() -> str:
    sections: list[tuple[str, list[tuple[str, str]]]] = [
        ("Main Pages", [("../index.html", "Home"), ("../services/index.html", "Plumbing Services"), ("../index.html#areas", "Areas We Service"), ("../index.html#quote", "Get a Quote")]),
        ("About Us", []),
        ("Resources", []),
        ("Legal", [
            ("accessibility.html", "Accessibility"),
            ("site-map.html", "Site Map"),
            ("privacy-policy.html", "Privacy Policy"),
            ("#privacy-choices", "Your Privacy Choices"),
            ("terms-of-use.html", "Terms of Use"),
        ]),
    ]
    about_pages = sorted((ROOT / "resources").glob("*.html"))
    about_names = {
        "about.html": "About Us",
        "in-the-media.html": "In The Media",
        "code-of-ethics.html": "Code of Ethics",
        "community-involvement.html": "Community Involvement",
        "our-guarantees.html": "Our Guarantees",
        "club-membership.html": "Club Membership",
    }
    resource_pages = [
        ("blog.html", "Blog"),
        ("expert-tips.html", "Expert Tips"),
        ("newsletter.html", "Newsletter"),
        ("financing.html", "Financing"),
        ("faq.html", "FAQ"),
    ]
    for fname, label in about_names.items():
        if (ROOT / "resources" / fname).exists():
            sections[1][1].append((fname, label))
    sections[2][1].extend(resource_pages)

    service_links: list[tuple[str, str]] = []
    for path in sorted((ROOT / "services").glob("*.html")):
        if path.name == "index.html":
            continue
        href, label = link_for(path)
        service_links.append((href, label.replace(" Html", "")))
    sections.insert(2, ("Plumbing Services", service_links))

    cols = []
    for title, links in sections:
        items = "".join(f'<li><a href="{href}">{label}</a></li>' for href, label in links)
        cols.append(f'<div class="sitemap-col"><h2>{title}</h2><ul class="sitemap-list">{items}</ul></div>')
    grid = "\n          ".join(cols)
    return f"""<h1>Omaha Site Map</h1>
        <div class="about-page-body sitemap-body">
          <p>Browse all pages on the Benjamin Franklin Plumbing® of Omaha website.</p>
          <div class="sitemap-grid">
          {grid}
          </div>
        </div>"""


def main() -> None:
    pages = {
        "accessibility.html": (
            "Accessibility | Benjamin Franklin Plumbing Omaha",
            "Website accessibility commitment for Benjamin Franklin Plumbing® of Omaha.",
            "Accessibility",
            accessibility_body(),
        ),
        "site-map.html": (
            "Site Map | Benjamin Franklin Plumbing Omaha",
            "Complete site map for Benjamin Franklin Plumbing® of Omaha.",
            "Site Map",
            site_map_body(),
        ),
        "privacy-policy.html": (
            "Privacy Policy | Benjamin Franklin Plumbing Omaha",
            "Privacy Policy for Benjamin Franklin Plumbing® of Omaha.",
            "Privacy Policy",
            privacy_body(),
        ),
        "terms-of-use.html": (
            "Terms of Use | Benjamin Franklin Plumbing Omaha",
            "Terms of Use for Benjamin Franklin Plumbing® of Omaha.",
            "Terms of Use",
            terms_body(),
        ),
    }
    out_dir = ROOT / "resources"
    for filename, (title, desc, crumb, body) in pages.items():
        html = page_shell(title, desc, crumb, body)
        (out_dir / filename).write_text(html, encoding="utf-8", newline="\n")
        print(f"Wrote {filename}")


if __name__ == "__main__":
    main()
