#!/usr/bin/env python3
"""Create a minimal GitHub Pages artifact after validating the course.

Only HTML, course Markdown, CSS, CNAME and the generated ZIP are published.
The complete examples, lesson sources and scripts remain available in the ZIP.
"""
from __future__ import annotations

import shutil
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "_site"
FILE_PATHS = ("index.html", "studyplan.html", "CNAME", ".nojekyll")
TREE_CONTENT = {
    "docs": {".md"},
    "build-revealjs": {".html", ".css", ".zip"},
}


def stage() -> list[str]:
    """Build a clean allowlisted directory; never follow source symlinks."""
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
        # GitHub Pages configuration can manage (and delete) the tracked CNAME.
        # Preserve the public domain in the artifact even when that happens.
        if name == "CNAME" and not (ROOT / name).exists():
            (DEST / "CNAME").write_text("study.fkr.dev\n", encoding="utf-8")
            published.append("CNAME")
        else:
            copy(ROOT / name)

    for directory, allowed in TREE_CONTENT.items():
        for source in sorted((ROOT / directory).rglob("*")):
            if source.is_file() and source.suffix.lower() in allowed:
                copy(source)

    deck = (DEST / "build-revealjs" / "index.html").read_text(encoding="utf-8")
    archive = DEST / "build-revealjs" / "py-ai-studyplan-materials.zip"
    if deck.count('href="py-ai-studyplan-materials.zip"') < 2:
        raise RuntimeError("Deck lost one of the two visible ZIP links")
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
    print(f"Prepared _site/ with {len(staged)} files")
    for filename in staged:
        print(f"  {filename}")
