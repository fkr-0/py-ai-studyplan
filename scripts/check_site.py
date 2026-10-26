#!/usr/bin/env python3
"""Validate staged Pages navigation so lessons don't open raw Markdown by default."""
from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hrefs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag not in {"a", "link"}:
            return
        self.hrefs.extend(value for key, value in attrs if key == "href" and value)


def check() -> None:
    problems: list[str] = []
    pages = [SITE / "index.html", SITE / "studyplan.html", SITE / "build-revealjs/index.html"]
    lessons = sorted((SITE / "docs").glob("*.html"))
    sources = sorted((SITE / "docs").glob("*.md"))
    if not lessons or len(lessons) != len(sources):
        problems.append(f"HTML lessons ({len(lessons)}) must match raw Markdown sources ({len(sources)})")
    pages += lessons
    links = 0
    for page in pages:
        if not page.is_file():
            problems.append(f"Missing required page: {page}")
            continue
        parser = LinkParser()
        markup = page.read_text(encoding="utf-8")
        parser.feed(markup)
        if page.suffix == ".html" and page.parent.name == "docs":
            if "Original Markdown (.md)" not in markup:
                problems.append(f"Missing source Markdown control: {page}")
        for link in parser.hrefs:
            parts = urlsplit(link)
            if not parts.path or parts.scheme or parts.netloc or parts.path.startswith("#"):
                continue
            if parts.path.startswith("/"):
                problems.append(f"Root-relative URL not portable to Pages: {page}: {link}")
                continue
            target = (page.parent / unquote(parts.path)).resolve()
            links += 1
            if not target.is_relative_to(SITE) or not target.exists():
                problems.append(f"Broken relative link: {page.relative_to(SITE)}: {link}")
        if page == SITE / "build-revealjs/index.html":
            for raw in ("../docs/21-day-mac-track.md", "../docs/01b-macos-workbench.md"):
                if raw in markup:
                    problems.append(f"Public slides still use raw Markdown: {raw}")
            for url in ("../docs/21-day-mac-track.html", "../docs/01b-macos-workbench.html"):
                if url not in markup:
                    problems.append(f"Expected rendered HTML link: {url}")
        if page == SITE / "docs/01-ai-intuition.html":
            if "Imagine asking a chatbot" not in markup or "No drawing" not in markup:
                problems.append("First guided checkpoint not present in rendered lesson")
    if not (SITE / "build-revealjs/py-ai-studyplan-materials.zip").exists():
        problems.append("No materials ZIP")
    else:
        with ZipFile(SITE / "build-revealjs/py-ai-studyplan-materials.zip") as z:
            if z.testzip() is not None:
                problems.append("Damaged materials ZIP")
    if problems:
        for problem in problems:
            print("FAIL:", problem)
        raise SystemExit(1)
    print(f"PASS: {len(lessons)} HTML readings, {len(sources)} Markdown sources, {links} local site links")


if __name__ == "__main__":
    check()
