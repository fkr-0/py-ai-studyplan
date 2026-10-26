#!/usr/bin/env python3
"""Stage a minimal Pages site with readable HTML versions of Markdown lessons.

Plain .md sources stay available for students who want to edit them; clicking
a lesson in the published deck opens the rendered HTML reading view.
"""
from __future__ import annotations

import html
import re
import shutil
import subprocess
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit, urlunsplit
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "_site"
FILE_PATHS = ("index.html", "studyplan.html", "CNAME", ".nojekyll")
TREE_CONTENT = {
    "docs": {".md"},
    "build-revealjs": {".html", ".css", ".zip"},
}
REPO = "https://github.com/fkr-0/py-ai-studyplan/blob/main/"
HREF = re.compile(r'(?P<start>href=")(?P<url>[^"]+)(?P<end>")')


def reading_href(url: str, document: Path) -> str:
    """Translate staged-site links without changing the original Markdown.

    A reading's local .md references become .html. Nonpublished code/template
    links lead to the matching public GitHub source rather than a Pages 404.
    """
    parts = urlsplit(html.unescape(url))
    if parts.scheme or parts.netloc or not parts.path or parts.path.startswith(("#", "/")):
        return url
    target = (document.parent / unquote(parts.path)).resolve()
    try:
        relative = target.relative_to(ROOT)
    except ValueError:
        return url
    if relative.parts[0] == "docs" and target.suffix.lower() == ".md":
        path = parts.path[:-3] + ".html"
    elif relative == Path("README.md"):
        path = "../studyplan.html"
    elif relative == Path("build-revealjs/README.md"):
        path = "../build-revealjs/"
    elif relative.as_posix() in {"index.html", "studyplan.html"}:
        path = parts.path
    elif relative.parts[0] in {"docs", "build-revealjs"} and target.suffix.lower() in {".html", ".css", ".zip"}:
        path = parts.path
    else:
        path = REPO + quote(relative.as_posix(), safe="/")
    return html.escape(urlunsplit(("", "", path, parts.query, parts.fragment)), quote=True)


def rewrite_links(markup: str, document: Path) -> str:
    return HREF.sub(
        lambda match: match.group("start") + reading_href(match.group("url"), document) + match.group("end"),
        markup,
    )


def lesson_html(source: Path) -> str:
    """Use Pandoc's Markdown parser, then wrap output in an accessible reading UI."""
    title = next((line[2:].strip() for line in source.read_text(encoding="utf-8").splitlines()
                  if line.startswith("# ")), source.stem.replace("-", " ").title())
    converted = subprocess.run(
        ["pandoc", "--from=gfm", "--to=html5", "--wrap=none", str(source)],
        capture_output=True, text=True, check=True,
    ).stdout
    body = rewrite_links(converted, source)
    safe_title = html.escape(title, quote=True)
    raw_url = quote(source.name)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="dark">
  <title>{safe_title} · Python + AI</title>
  <style>
    :root {{ color-scheme: dark; }}
    body {{ background:#17191e; color:#dce0df; font:1.05rem/1.7 system-ui,Arial,sans-serif;
            margin:0; padding:0 1.3rem; overflow-wrap:anywhere; }}
    header,main,footer {{ max-width:800px; margin:0 auto; }}
    header {{ display:flex; align-items:center; flex-wrap:wrap; gap:.5rem 1rem;
              padding:1.2rem 0; border-bottom:1px solid #494d56; }}
    header a {{ font-size:.9rem; white-space:nowrap; }}
    main {{ padding:1rem 0 2rem; }}
    h1,h2,h3 {{ line-height:1.25; color:#a6c4df; }}
    h1 {{ font-size:clamp(1.8rem,5vw,2.7rem); }} h2 {{ margin-top:2.2rem; }}
    a {{ color:#9dd5cf; text-underline-offset:.18em; }}
    a:focus-visible {{ outline:3px solid #e8c57d; outline-offset:3px; }}
    pre {{ overflow-x:auto; white-space:pre; padding:1rem; border:1px solid #555e69;
           background:#101115; font-size:.88rem; line-height:1.5; }}
    code {{ font: .92em ui-monospace,SFMono-Regular,Menlo,Consolas,monospace; }}
    :not(pre)>code {{ color:#ecc783; padding:.1rem .18rem; background:#282c33; }}
    blockquote {{ border-left:4px solid #a88ab8; margin:1rem 0; padding:.2rem 1rem; background:#282932; }}
    table {{ width:100%; display:block; overflow-x:auto; border-collapse:collapse; font-size:.92rem; }}
    th,td {{ border:1px solid #555e69; padding:.4rem .65rem; text-align:left; }}
    th {{ background:#292d34; }}
    img {{ max-width:100%; }} li {{ margin:.35rem 0; }}
    footer {{ border-top:1px solid #494d56; padding:1.5rem 0 2.5rem; font-size:.9rem; }}
    .pill {{ background:#242a31; border:1px solid #606b70; padding:.3rem .6rem; text-decoration:none; }}
  </style>
</head>
<body>
  <header aria-label="Course navigation">
    <a class="pill" href="../build-revealjs/">← Slides</a>
    <a href="../studyplan.html">Course overview</a>
    <a href="{raw_url}" download>Original Markdown (.md)</a>
    <a href="../build-revealjs/py-ai-studyplan-materials.zip" download>All materials (.zip)</a>
  </header>
  <main>{body}</main>
  <footer>Readable HTML lesson · The original Markdown is preserved for editing in VS Code.
    <a href="{raw_url}">View source Markdown</a>.</footer>
</body>
</html>
"""


def stage() -> list[str]:
    if DEST.is_symlink():
        raise RuntimeError("Refusing to replace a symlink at _site")
    if DEST.exists():
        shutil.rmtree(DEST)
    DEST.mkdir()
    published: list[str] = []

    def copy(source: Path) -> None:
        if source.is_symlink() or not source.is_file():
            raise RuntimeError(f"Missing or unsafe source: {source}")
        relative = source.relative_to(ROOT)
        target = DEST / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        published.append(relative.as_posix())

    for name in FILE_PATHS:
        if name == "CNAME" and not (ROOT / name).exists():
            (DEST / "CNAME").write_text("study.fkr.dev\n", encoding="utf-8")
            published.append("CNAME")
        else:
            copy(ROOT / name)

    for directory, allowed in TREE_CONTENT.items():
        for source in sorted((ROOT / directory).rglob("*")):
            if source.is_file() and source.suffix.lower() in allowed:
                copy(source)

    # Publish browser-friendly handouts alongside the original source files.
    for source in sorted((ROOT / "docs").glob("*.md")):
        dest = DEST / "docs" / (source.stem + ".html")
        dest.write_text(lesson_html(source), encoding="utf-8")
        published.append(dest.relative_to(DEST).as_posix())

    # The Org deck intentionally stores editable .md source links; rewrite only
    # staged HTML so the public site opens a reading page instead of raw text.
    deck_file = DEST / "build-revealjs" / "index.html"
    deck_file.write_text(rewrite_links(deck_file.read_text(encoding="utf-8"), ROOT / "build-revealjs/index.html"),
                         encoding="utf-8")

    deck = deck_file.read_text(encoding="utf-8")
    archive = DEST / "build-revealjs" / "py-ai-studyplan-materials.zip"
    if deck.count('href="py-ai-studyplan-materials.zip"') < 2:
        raise RuntimeError("Deck lost one of the two visible ZIP links")
    if re.search(r'href="\.\./docs/[^"]+\.md', deck):
        raise RuntimeError("Public slides still open raw Markdown instead of HTML")
    with ZipFile(archive) as zip_file:
        if zip_file.testzip() is not None or len(zip_file.namelist()) < 40:
            raise RuntimeError("Course ZIP missing files or failed checksum")
    if (DEST / "CNAME").read_text(encoding="utf-8").strip() != "study.fkr.dev":
        raise RuntimeError("Published CNAME does not match study.fkr.dev")
    for secret in (".git", ".env", "node_modules", "template-reference", "examples"):
        if (DEST / secret).exists():
            raise RuntimeError(f"Unexpected private/unbundled path: {secret}")
    return published


if __name__ == "__main__":
    staged = stage()
    print(f"Prepared _site/ with {len(staged)} files including rendered Markdown lessons")
