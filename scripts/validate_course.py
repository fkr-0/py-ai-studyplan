#!/usr/bin/env python3
"""Validate internal Markdown links, Reveal.js structure and media fallbacks.

Run: python3 scripts/validate_course.py
This is intentionally read-only and never fetches external media.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
DOCS = sorted(ROOT.rglob("*.md"))
SKIP = ("template-reference", ".venv", "node_modules")
failures: list[str] = []
checked_links = 0
for md in DOCS:
    if any(piece in SKIP for piece in md.relative_to(ROOT).parts):
        continue
    text = md.read_text(encoding="utf-8")
    # Markdown inline links; external URLs are deliberately not fetched here.
    for match in re.finditer(r"(?<!!)\[[^\]]+\]\(([^\s)]+)(?:\s+[^)]*)?\)", text):
        link = match.group(1).strip("<>")
        if link.startswith(("http:", "https:", "mailto:", "#", "data:")):
            continue
        target = (md.parent / unquote(link.split("#", 1)[0])).resolve()
        checked_links += 1
        if not target.exists():
            failures.append(f"{md.relative_to(ROOT)}: missing {link}")

deck_path = ROOT / "build-revealjs" / "index.html"
if deck_path.exists():
    deck = deck_path.read_text(encoding="utf-8")
    for token in ['class="reveal"', "Reveal.initialize", "reveal.js", "assets/tomorrow-night-terminal.css"]:
        if token not in deck:
            failures.append(f"Deck lacks: {token}")
    if not re.search(r"(youtube-nocookie\.com|youtube\.com)/embed/", deck):
        failures.append("Deck has no embedded video")
    if "lecture0.pdf" not in deck:
        failures.append("Deck has no course PDF")
    if "target=\"_blank\"" not in deck and "target='_blank'" not in deck:
        failures.append("Deck has no fallback external links")
else:
    failures.append("Generated Reveal.js index.html does not exist")

print(f"Markdown docs: {len(DOCS)}, local links checked: {checked_links}")
for problem in failures:
    print("FAIL:", problem)
if failures:
    sys.exit(1)
print("PASS: internal links and presentation media checks")
