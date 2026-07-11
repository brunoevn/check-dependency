import re
import os
from bs4 import BeautifulSoup

def compare():
    md_path = r"c:\Workspaces\kevlar-checkdeps\report.md"
    html_path = r"c:\Workspaces\kevlar-checkdeps\report.html"

    # 1. Parse report.md
    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()

    # Find the table in report.md
    # Table format: | Package | Type | Declared | Installed | Latest | Status | Vuls | Note |
    # Or: | Package | Type | Declared | Installed | Latest | Status | Note |
    md_packages = {}
    lines = md_content.splitlines()
    for line in lines:
        if line.startswith("|") and not line.strip().startswith("| ---") and not line.strip().startswith("| Package"):
            parts = [p.strip() for p in line.split("|")]
            # parts[0] is empty (since line starts with |)
            # parts[1] is Package (e.g. `@astrojs/compiler-binding`)
            # parts[2] is Type
            # parts[3] is Declared
            # parts[4] is Installed
            # parts[5] is Latest
            # parts[6] is Status
            # parts[7] is Vuls (if 9 columns) or Note (if 8 columns)
            if len(parts) >= 8:
                pkg_name = parts[1].replace("`", "").strip()
                if pkg_name:
                    md_packages[pkg_name] = {
                        "type": parts[2],
                        "declared": parts[3].replace("`", "").strip(),
                        "installed": parts[4].replace("`", "").strip(),
                        "latest": parts[5].replace("`", "").strip(),
                        "status": parts[6],
                    }

    print(f"Parsed {len(md_packages)} packages from report.md")

    # 2. Parse report.html
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, "html.parser")
    
    # Let's count stats in html
    stat_vals = soup.find_all(class_="stat-val")
    stat_lbls = soup.find_all(class_="stat-lbl")
    html_stats = {}
    for val, lbl in zip(stat_vals, stat_lbls):
        html_stats[lbl.text.strip().lower()] = val.text.strip()
    
    print(f"HTML Stats: {html_stats}")

    # Let's count package cards
    package_cards = soup.find_all(class_="package-card")
    print(f"Found {len(package_cards)} package cards in report.html")

    html_packages = {}
    for card in package_cards:
        name = card.get("data-name")
        status = card.get("data-status")
        deptype = card.get("data-deptype")
        vulnerable = card.get("data-vulnerable")
        
        # Extract versions from layout
        # Inside the card there are typically some details. Let's get installed and latest.
        # Let's search inside the card for version numbers or labels
        html_packages[name] = {
            "status": status,
            "deptype": deptype,
            "vulnerable": vulnerable,
        }

    # Compare sets of package names
    md_names = set(md_packages.keys())
    html_names = set(html_packages.keys())

    only_in_md = md_names - html_names
    only_in_html = html_names - md_names

    print(f"Only in MD: {only_in_md}")
    print(f"Only in HTML: {only_in_html}")
    
    # Compare summary stats
    # From md:
    # - **Total Checked**: 316
    # - **Up-to-date**: 216
    # - **Outdated**: 100
    # - **Security Vulnerabilities**: 0
    print("\nSummary Comparison:")
    print(f"MD Total: 316, HTML checked: {html_stats.get('checked')}")
    print(f"MD Outdated: 100, HTML outdated: {html_stats.get('outdated')}")
    print(f"MD Up-to-date: 216, HTML up-to-date: {html_stats.get('up-to-date')}")
    print(f"MD Vulnerabilities: 0, HTML vulnerable: {html_stats.get('vulnerable')}")

if __name__ == "__main__":
    compare()
