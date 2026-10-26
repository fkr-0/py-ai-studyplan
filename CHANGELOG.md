# Changelog

## Unreleased

- Remove unexplained **Git**, **inference** and other advanced vocabulary from opening slides, defining each concept at its first practical appearance.
- Add a plain-English course glossary and a macOS key-symbol slide: **^C = ⌃C = Ctrl+C = Control-C**, not Command+C.
- Add explanations for **training, model, JSON, Git, venv, pip, API, HTTP** and basic folder commands before students use them.
- Update beginner lesson notes, instructor prompts and automated tests to catch future vocabulary regressions.
- Render every published Markdown lesson as a readable HTML page, while preserving the raw `.md` version and pointing code references to GitHub source instead of broken site paths.
- Route links from the published Reveal.js presentation and welcome page to HTML lessons; add navigation, original Markdown and ZIP links to every lesson.
- Teach a safe `curl --output lesson.md` → `code lesson.md` exercise after introducing the terminal.
- Replace the unclear first drawing checkpoint with a three-card chatbot question exercise and a separate worked answer slide.
- Validate generated HTML lessons and internal site navigation before GitHub Pages deployment.

- Remove personal learner context and machine specifications from public materials; generalize setup guidance and rebuild the downloadable course archive.
- Open slide 1 directly from the site root, with a small link back to the preserved welcome page at `studyplan.html`.
- Add a GitHub repository icon in the top-right corner throughout the presentation.

## [0.0.2] — 2026-10-26

### Added

- Course timetable as the third slide, mapping the 21-day sequence to eight topic groups and practical outcomes.
- A welcome page with course overview, setup guidance, slide entry and course ZIP download, replacing the immediate redirect.
- Changelog included in the downloadable course materials.

### Improved

- Clarified daily time budgets, catch-up checkpoints and the distinction between core work and optional Docker practice.
- Aligned the assessment with taught skills and distinguished starter features from learner extensions.
- Clarified which tests cover message preparation and which UI/model interactions still require manual checks.

### Fixed

- Corrected the Day 14 project path and standardized installation on the course requirements file.
- Created ignore rules before staging the Git exercise and replaced broad staging with explicit source files.
- Aligned supplementary model examples with the course's `gemma3:4b` default.
- Made the new-terminal activation steps explicit in the first Ollama slide.
- Corrected Markdown-style emphasis in the Org slide source so shortcut instructions render cleanly.

Earlier development commits were not tagged; this changelog starts with 0.0.2.
