#!/usr/bin/env python3
"""Build Reveal.js slides and a downloadable, complete course materials ZIP."""
from __future__ import annotations

import html
import os
import pathlib
import shutil
import subprocess
import sys
import urllib.parse
import zipfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / "build-revealjs" / "source.org"
REF = ROOT / "template-reference" / "build-revealjs" / "index.html"
DEST = ROOT / "build-revealjs" / "index.html"
START = '<div class="reveal"><div class="slides">'
END = '  </div></div>'
ARCHIVE = DEST.with_name("py-ai-studyplan-materials.zip")
DEFAULT_ARCHIVE_LINK = ARCHIVE.name
DOWNLOAD_URL_ENV = "PY_AI_STUDYPLAN_DOWNLOAD_URL"
ARCHIVE_ROOT = "py-ai-studyplan"
BUNDLED_DIRS = frozenset({
    "build-revealjs", "docs", "examples", "scripts", "template-reference", "tests",
})
BUNDLED_FILES = frozenset({"README.md", "CHANGELOG.md", "Makefile", ".gitignore", "index.html", "studyplan.html", "CNAME", ".nojekyll", "DEPLOYMENT.md"})
EXCLUDED_DIRS = frozenset({
    ".git", ".venv", "venv", "node_modules", "__pycache__", ".pytest_cache",
    ".mypy_cache", ".ruff_cache", ".idea", ".vscode", "dist", "build",
})


def archive_files() -> list[pathlib.Path]:
    """Explicit allowlist to avoid shipping unrelated work, secrets, or caches."""
    files: list[pathlib.Path] = []
    for file in ROOT.rglob("*"):
        if not file.is_file() or file.is_symlink() or file == ARCHIVE:
            continue
        rel = file.relative_to(ROOT)
        if rel.parts[0] not in BUNDLED_DIRS and rel.as_posix() not in BUNDLED_FILES:
            continue
        if any(part in EXCLUDED_DIRS for part in rel.parts[:-1]):
            continue
        if file.suffix.lower() in {".pyc", ".pyo", ".zip", ".log"}:
            continue
        if file.name.startswith(".env") or file.name in {"secrets.toml", ".DS_Store"}:
            continue
        files.append(file)
    return sorted(files, key=lambda path: path.relative_to(ROOT).as_posix())


def create_archive() -> tuple[int, int]:
    """Bundle the built deck, all Markdown docs, examples, source and template.

    The ZIP is written alongside index.html so hosting build-revealjs/
    automatically makes the initial-slide download link work. ZIP metadata is
    fixed for reproducible archives and the ZIP never contains itself.
    """
    files = archive_files()
    if not files or DEST not in files:
        raise RuntimeError("Cannot bundle slides: generated index.html is missing")
    with zipfile.ZipFile(ARCHIVE, mode="w", compression=zipfile.ZIP_DEFLATED,
                         compresslevel=9, strict_timestamps=True) as output:
        for file in files:
            rel = file.relative_to(ROOT).as_posix()
            info = zipfile.ZipInfo(f"{ARCHIVE_ROOT}/{rel}", date_time=(2026, 10, 26, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            output.writestr(info, file.read_bytes(), compress_type=zipfile.ZIP_DEFLATED,
                            compresslevel=9)
    return len(files), ARCHIVE.stat().st_size


def configured_download_url() -> str:
    """Use local relative link by default; optional override for CDN hosting."""
    url = os.environ.get(DOWNLOAD_URL_ENV, DEFAULT_ARCHIVE_LINK).strip()
    parsed = urllib.parse.urlsplit(url)
    if not url or parsed.scheme not in {"", "https", "http"} or url.startswith("//"):
        raise RuntimeError(f"{DOWNLOAD_URL_ENV} must be a relative path or HTTP(S) URL")
    return url



def build() -> None:
    if shutil.which("pandoc") is None:
        raise RuntimeError("pandoc not found; install pandoc to rebuild the Reveal.js deck")
    source = SRC.read_text(encoding="utf-8")
    converted = subprocess.run(
        ["pandoc", "--from=org", "--to=revealjs", "--slide-level=2",
         "--wrap=none"],
        input=source, text=True, capture_output=True, check=True,
    ).stdout
    # Pandoc's Org -> Reveal.js writer emits a phantom empty first slide
    # when the document has #+TITLE metadata. Strip that wrapper so the
    # opening presentation page is our actual cover and ZIP button.
    converted = converted.lstrip()
    phantom = '<section class="slide level2">\n\n\n</section>'
    if converted.startswith(phantom):
        converted = converted[len(phantom):].lstrip()
    if converted.startswith('<section class="slide level2">'):
        raise RuntimeError("Unexpected initial empty Reveal.js slide")
    if converted.count("<section") < 15:
        raise RuntimeError("Slide export unexpectedly short")
    needle = f'href="{DEFAULT_ARCHIVE_LINK}"'
    if converted.count(needle) < 2:
        raise RuntimeError("The opening slides must contain the materials ZIP links")
    converted = converted.replace(
        needle, f'href="{html.escape(configured_download_url(), quote=True)}"'
    )
    template = REF.read_text(encoding="utf-8")
    assert template.count(START) == 1, "Reveal template marker missing"
    head, tail = template.split(START, 1)
    assert END in tail, "Reveal template closing marker missing"
    _old_content, foot = tail.rsplit(END, 1)
    head = head.replace("<title>Terminal Power</title>",
                        "<title>Python + AI · Study Plan</title>")
    # The original terminal-talk HTML references two theme URLs absent
    # from the published reveal.js 5.1.0 distribution (404). Use valid
    # core stylesheets; retain the copied Tomorrow Night CSS overrides.
    head = head.replace("/dist/theme/tokyo-night.css", "/dist/theme/night.css")
    head = head.replace("/plugin/highlight/tokyo-night.css",
                        "/plugin/highlight/monokai.css")
    head = head.replace(
        '<link rel="stylesheet" href="assets/tomorrow-night-terminal.css">',
        '<link rel="stylesheet" href="assets/tomorrow-night-terminal.css">\n'
        '  <link rel="stylesheet" href="assets/studyplan.css">'
    )
    head = head.replace('<meta charset="utf-8">',
                        '<meta charset="utf-8">\n'
                        '  <meta name="referrer" content="strict-origin-when-cross-origin">')
    foot = foot.replace("terminal-power-whiteboard", "py-ai-studyplan-whiteboard")
    # Chalkboard's background option expects URLs, not CSS colors. The copied
    # terminal-talk values caused /rgba(...) 404s. Keep theme defaults.
    foot = foot.replace(
        "background: [ 'rgba(255,255,255,0.03)', 'rgba(255,255,255,0.92)' ], ",
        "",
    )
    foot = foot.replace("transition: 'slide', width: 1400, height: 900",
                        "transition: 'slide', width: 1400, height: 900")
    repo_link = '''
<a class="repository-link" href="https://github.com/fkr-0/py-ai-studyplan" target="_blank" rel="noopener noreferrer" aria-label="View the study plan repository on GitHub" title="Study plan on GitHub">
<svg viewBox="0 0 16 16" width="24" height="24" aria-hidden="true" focusable="false" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82A7.65 7.65 0 0 1 8 3.86c.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8Z"/></svg>
</a>
'''
    body = head + START + "\n" + converted.strip() + "\n" + END + repo_link + foot
    DEST.write_text(body, encoding="utf-8")
    count, size = create_archive()
    print(f"Built {DEST.relative_to(ROOT)} ({converted.count('<section')} sections)")
    print(f"Bundled {ARCHIVE.relative_to(ROOT)} ({count} files, {size:,} bytes)")
    if configured_download_url() != DEFAULT_ARCHIVE_LINK:
        print(f"Hosted download link override: {configured_download_url()}")



if __name__ == "__main__":
    try:
        build()
    except (RuntimeError, subprocess.CalledProcessError, AssertionError) as exc:
        print(f"Build failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
