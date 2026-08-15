#!/usr/bin/env python3
"""Render the repo's Markdown into a static HTML site.

Every .md file becomes an .html page with shared styling and navigation.
README.md becomes index.html so folder URLs work. Any .html, images, or other
assets already in the repo are copied through untouched.

Usage: python tools/build_site.py [--out _site]
"""

import argparse
import re
import shutil
import sys
from pathlib import Path

try:
    import markdown
except ImportError:
    sys.exit("markdown is not installed — run: pip install markdown")

REPO = Path(__file__).resolve().parent.parent

# Directories never copied into the site.
SKIP_DIRS = {".git", ".github", "_site", "tools", "node_modules", "__pycache__"}

# Files never copied into the site.
SKIP_FILES = {".gitignore", ".gitkeep"}

MD_EXTENSIONS = ["tables", "fenced_code", "sane_lists", "attr_list", "md_in_html"]

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>{css}</style>
</head>
<body>
<header class="site-header">
  <a class="brand" href="{root}index.html">Project Airstream</a>
  <nav>{nav}</nav>
</header>
<main>
{breadcrumb}
{body}
</main>
<footer>
  <span>Built from <code>{source}</code></span>
  <a href="https://github.com/adrianj98/Project_airstream/blob/main/{source}">Edit on GitHub</a>
</footer>
</body>
</html>
"""

CSS = """
:root {
  --bg: #ffffff;
  --fg: #1c1e21;
  --muted: #5b6470;
  --line: #e3e6ea;
  --accent: #0b6bcb;
  --code-bg: #f4f6f8;
  --header-bg: #fbfcfd;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #14171a;
    --fg: #e6e9ec;
    --muted: #9aa4b0;
    --line: #2a2f36;
    --accent: #5aa9f5;
    --code-bg: #1c2126;
    --header-bg: #171b1f;
  }
}
* { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--fg);
  font: 16px/1.65 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}
.site-header {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 0.5rem 1.5rem;
  padding: 0.9rem 1.5rem;
  border-bottom: 1px solid var(--line);
  background: var(--header-bg);
}
.brand { font-weight: 650; text-decoration: none; color: var(--fg); }
.site-header nav { display: flex; flex-wrap: wrap; gap: 1rem; font-size: 0.9rem; }
.site-header nav a { color: var(--muted); text-decoration: none; }
.site-header nav a:hover { color: var(--accent); }
main { max-width: 52rem; margin: 0 auto; padding: 2rem 1.5rem 3rem; }
.breadcrumb { font-size: 0.85rem; color: var(--muted); margin-bottom: 1.5rem; }
.breadcrumb a { color: var(--muted); }
h1, h2, h3 { line-height: 1.25; margin-top: 2rem; }
h1 { margin-top: 0; font-size: 1.9rem; }
h2 { font-size: 1.35rem; padding-bottom: 0.3rem; border-bottom: 1px solid var(--line); }
a { color: var(--accent); }
hr { border: 0; border-top: 1px solid var(--line); margin: 2rem 0; }
code {
  background: var(--code-bg);
  padding: 0.15em 0.4em;
  border-radius: 4px;
  font-size: 0.9em;
}
pre {
  background: var(--code-bg);
  padding: 1rem;
  border-radius: 8px;
  overflow-x: auto;
}
pre code { background: none; padding: 0; }
.table-wrap { overflow-x: auto; margin: 1rem 0; }
table { border-collapse: collapse; width: 100%; font-size: 0.93rem; }
th, td { text-align: left; padding: 0.55rem 0.7rem; border-bottom: 1px solid var(--line); }
th { font-weight: 600; background: var(--code-bg); }
blockquote {
  margin: 1rem 0;
  padding: 0.2rem 1rem;
  border-left: 3px solid var(--line);
  color: var(--muted);
}
li.task { list-style: none; margin-left: -1.3rem; }
li.task .box { color: var(--muted); margin-right: 0.4rem; }
li.task.done { color: var(--muted); text-decoration: line-through; }
footer {
  max-width: 52rem;
  margin: 0 auto;
  padding: 1.2rem 1.5rem 3rem;
  border-top: 1px solid var(--line);
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem 1rem;
  justify-content: space-between;
  font-size: 0.85rem;
  color: var(--muted);
}
footer a { color: var(--muted); }
"""


def md_files(root: Path):
    for path in sorted(root.rglob("*.md")):
        rel = path.relative_to(root)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        yield rel


def asset_files(root: Path):
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix == ".md":
            continue
        rel = path.relative_to(root)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        if path.name in SKIP_FILES:
            continue
        yield rel


def out_path(rel: Path) -> Path:
    """README.md -> index.html so folder URLs resolve; everything else keeps its name."""
    name = "index.html" if rel.name.lower() == "readme.md" else rel.stem + ".html"
    return rel.parent / name


def rewrite_links(html: str) -> str:
    """Point in-repo .md links at their generated .html counterparts."""

    def fix(match):
        quote, href = match.group(1), match.group(2)
        if re.match(r"^[a-z]+:", href, re.I) or href.startswith("#") or href.startswith("//"):
            return match.group(0)
        target, _, frag = href.partition("#")
        if target.lower().endswith("readme.md"):
            target = target[: -len("README.md")] + "index.html"
        elif target.lower().endswith(".md"):
            target = target[:-3] + ".html"
        elif target.endswith("/"):
            # Folder link — make it explicit so it also works opening files locally.
            target = target + "index.html"
        else:
            return match.group(0)
        return f'href={quote}{target}{"#" + frag if frag else ""}{quote}'

    return re.sub(r'href=(["\'])(.*?)\1', fix, html)


def render_tasks(html: str) -> str:
    """Turn `- [ ]` / `- [x]` list items into readable checkboxes."""
    html = re.sub(r"<li>\[ \]\s*", '<li class="task"><span class="box">&#9744;</span>', html)
    html = re.sub(r"<li>\[[xX]\]\s*", '<li class="task done"><span class="box">&#9745;</span>', html)
    return html


def wrap_tables(html: str) -> str:
    """Let wide tables scroll instead of blowing out the page on mobile."""
    html = html.replace("<table>", '<div class="table-wrap"><table>')
    return html.replace("</table>", "</table></div>")


def page_title(html: str, rel: Path) -> str:
    match = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S)
    if match:
        return re.sub(r"<[^>]+>", "", match.group(1)).strip()
    return rel.stem.replace("-", " ").title()


def build_nav(projects, root_prefix: str) -> str:
    links = [f'<a href="{root_prefix}index.html">Master report</a>']
    for slug, title in projects:
        links.append(f'<a href="{root_prefix}projects/{slug}/index.html">{title}</a>')
    return "".join(links)


def build_breadcrumb(rel: Path, root_prefix: str) -> str:
    if rel == Path("README.md"):
        return ""
    parts = [f'<a href="{root_prefix}index.html">Master report</a>']
    if rel.parts[0] == "projects" and len(rel.parts) > 2:
        slug = rel.parts[1]
        title = slug.replace("-", " ")
        if rel.name.lower() != "readme.md":
            parts.append(f'<a href="{root_prefix}projects/{slug}/index.html">{title}</a>')
        else:
            parts.append(title)
    return f'<div class="breadcrumb">{" / ".join(parts)}</div>'


def discover_projects(root: Path):
    projects = []
    projects_dir = root / "projects"
    if not projects_dir.is_dir():
        return projects
    for entry in sorted(projects_dir.iterdir()):
        readme = entry / "README.md"
        if entry.is_dir() and readme.is_file():
            first = readme.read_text(encoding="utf-8").lstrip().splitlines()[:1]
            title = first[0].lstrip("# ").strip() if first else entry.name
            projects.append((entry.name, title))
    return projects


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="_site", help="output directory (default: _site)")
    args = parser.parse_args()

    out_dir = (REPO / args.out).resolve()
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)

    projects = discover_projects(REPO)
    converter = markdown.Markdown(extensions=MD_EXTENSIONS)
    count = 0

    for rel in md_files(REPO):
        converter.reset()
        html = converter.convert((REPO / rel).read_text(encoding="utf-8"))
        html = wrap_tables(render_tasks(rewrite_links(html)))

        depth = len(out_path(rel).parent.parts)
        root_prefix = "../" * depth

        page = PAGE.format(
            title=f"{page_title(html, rel)} — Project Airstream",
            css=CSS,
            nav=build_nav(projects, root_prefix),
            breadcrumb=build_breadcrumb(rel, root_prefix),
            body=html,
            root=root_prefix,
            source=rel.as_posix(),
        )

        dest = out_dir / out_path(rel)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(page, encoding="utf-8")
        count += 1

    # A folder listing for projects/, unless the folder ships its own README.
    projects_index = out_dir / "projects" / "index.html"
    if projects and not projects_index.exists():
        items = "".join(
            f'<li><a href="{slug}/index.html">{title}</a></li>' for slug, title in projects
        )
        projects_index.parent.mkdir(parents=True, exist_ok=True)
        projects_index.write_text(
            PAGE.format(
                title="Projects — Project Airstream",
                css=CSS,
                nav=build_nav(projects, "../"),
                breadcrumb='<div class="breadcrumb"><a href="../index.html">Master report</a></div>',
                body=f"<h1>Projects</h1><ul>{items}</ul>",
                root="../",
                source="projects/",
            ),
            encoding="utf-8",
        )
        count += 1

    assets = 0
    for rel in asset_files(REPO):
        dest = out_dir / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(REPO / rel, dest)
        assets += 1

    # Tell GitHub Pages not to run Jekyll over the output.
    (out_dir / ".nojekyll").write_text("", encoding="utf-8")

    print(f"Built {count} page(s) and copied {assets} asset(s) into {out_dir}")

    broken = check_links(out_dir)
    if broken:
        print(f"\nWarning: {len(broken)} link(s) point at pages that don't exist:")
        for item in broken:
            print(f"  {item}")


def check_links(out_dir: Path):
    """Report internal links with no matching file — usually a typo or a moved page."""
    broken = []
    for page in sorted(out_dir.rglob("*.html")):
        for href in re.findall(r'href="([^"]*)"', page.read_text(encoding="utf-8")):
            if re.match(r"^[a-z]+:", href, re.I) or href.startswith(("#", "//")):
                continue
            target = (page.parent / href.split("#")[0]).resolve()
            if not target.exists():
                broken.append(f"{page.relative_to(out_dir)} -> {href}")
    return broken


if __name__ == "__main__":
    main()
