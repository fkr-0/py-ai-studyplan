# Python + AI · Reveal.js deck

Editable source: [source.org](source.org). Generated output: [index.html](index.html) and [complete materials ZIP](py-ai-studyplan-materials.zip).

Built on the copied Terminal Power Reveal.js template. Original source/style preserved at [../template-reference/build-revealjs/](../template-reference/build-revealjs/).

## Build

From project root:

    python3 scripts/build_slides.py

The build also refreshes `py-ai-studyplan-materials.zip` alongside `index.html`, including the complete editable course.
The opening and roadmap slides link directly to the ZIP. **Publish the whole `build-revealjs/` directory** to make the default link work.

For a different download URL, build with:

    PY_AI_STUDYPLAN_DOWNLOAD_URL="https://your.example/download/py-ai-studyplan-materials.zip" make slides

This changes only the link target: upload the new ZIP to that location. You can also edit the link in `source.org`.

Requires `pandoc` (Org-mode → Reveal.js sections). The build script copies the original template's wrapper and plugins, replaces slide content, changes the title and whiteboard storage namespace, and uses this project's CSS extensions. It fails clearly if `pandoc` is missing.

## View

    python3 -m http.server 8765 --directory .

Open http://127.0.0.1:8765/build-revealjs/. **Use localhost HTTP**, not `file://`, for better YouTube compatibility. Internet is needed for JS/CSS and embedded external media.

Resources display as embedded videos or PDF viewer when allowed by the provider. Each embed includes a direct link if blocked. External interactive tools open in a new tab.

## Present

Arrow keys: navigate; `S`: speaker notes; `F`: fullscreen; `B`: whiteboard; `C`: annotation canvas; `DEL`: clear; `/`: search.

All course notes and exercise instructions are also ordinary Markdown under [../docs/](../docs/). No third-party media is stored in this repository.
