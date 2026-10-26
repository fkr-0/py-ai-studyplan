#!/usr/bin/env python3
"""Offline smoke checks for internal links and generated slide content."""
from __future__ import annotations

import re
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    broken: list[str] = []
    markdown = [
        p for p in ROOT.rglob("*.md")
        if not any(part in {"template-reference", "_site", ".venv", ".git"} for part in p.parts)
    ]
    for doc in markdown:
        text = doc.read_text(encoding="utf-8")
        for href in re.findall(r"\]\(([^)]+)\)", text):
            if href.startswith(("https://", "http://", "mailto:", "#")):
                continue
            path = (doc.parent / href.split("#", 1)[0]).resolve()
            if not path.exists():
                broken.append(f"{doc.relative_to(ROOT)}: {href}")
    deck = (ROOT / "build-revealjs" / "index.html").read_text()
    catalog = (ROOT / "docs" / "resources.md").read_text()
    external_urls = re.findall(r"\]\((https?://[^)]+)\)", catalog)
    missing = [
        url for url in external_urls
        if url not in deck and not (
            "youtube.com/watch?v=" in url and url.partition("v=")[2] in deck
        )
    ]
    required = [
        "<div class=\"reveal\">", "Reveal.initialize(",
        "https://www.youtube-nocookie.com/embed/", "lecture0.pdf",
        "assets/studyplan.css", "Open original video",
    ]
    missing += [f"render: {term}" for term in required if term not in deck]
    archive = ROOT / "build-revealjs" / "py-ai-studyplan-materials.zip"
    if not archive.is_file():
        missing.append(f"archive: {archive.name}")
    else:
        with ZipFile(archive) as package:
            names = set(package.namelist())
            expected = {
                "py-ai-studyplan/README.md",
                "py-ai-studyplan/docs/resources.md",
                "py-ai-studyplan/examples/chat_app.py",
                "py-ai-studyplan/build-revealjs/index.html",
                "py-ai-studyplan/build-revealjs/source.org",
                "py-ai-studyplan/scripts/build_slides.py",
                "py-ai-studyplan/template-reference/build-revealjs/index.html",
            }
            missing.extend(f"zip member: {n}" for n in sorted(expected - names))
            if package.testzip() is not None:
                missing.append("zip file corruption")
            if any(n.endswith(".zip") or "/.venv/" in n or
                   "/__pycache__/" in n for n in names):
                missing.append("ZIP recursively includes archive or cache")
    if deck.count('class="materials-download') < 2:
        missing.append("missing opening/roadmap download links")
    if broken or missing:
        for item in broken + missing:
            print("FAIL:", item)
        return 1
    print(
        f"OK: {len(markdown)} Markdown docs, {len(external_urls)} curated "
        "resource links represented in Reveal.js, YouTube+PDF fallbacks present"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
