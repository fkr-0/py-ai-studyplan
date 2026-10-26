# Python + AI — local-first study plan

An eight-session, project-first introduction to Python, neural networks, LLM inference, web UI development, and a little Docker.

**Version:** 0.0.2 · [Changelog](CHANGELOG.md)

**Target:** An independent beginner can explain training vs inference, write and debug basic Python, launch a local model, and build a small browser-based chatbot. A classical Tetris solver is an optional alternative exercise.

**Budget:** About 16–23 contact hours plus 8–12 hours of exercises; budget 25–35 hours total, and more if programming is completely new. Milestones, not deadlines, determine pace.

The eight sessions are topic groups that can span several daily blocks. The 21-day track includes practice; it is not extra work on top of eight workshops. At one hour per day, allow 25–35 study days. Docker is optional and can follow the core final demo.

## Suggested study track

The course is written in English and offers a suggested sequence of **21 daily study blocks**, each 1–2 hours. Adapt the pace to your experience and leave room for catch-up.

**Start with [the 21-day daily plan](docs/21-day-mac-track.md), [Mac editor + terminal workbench](docs/01b-macos-workbench.md), and [macOS setup](docs/macos-setup.md).** The [didactic review and rationale](docs/didactic-review-2026-10-26.md) explains the teaching sequence. Choose a local model using the [hardware guidance](docs/hardware.md); the examples use `gemma3:4b`, with smaller models available as fallbacks.

## Where to start

| Audience | Read |
| --- | --- |
| Learner | [Orientation](docs/00-orientation.md), then sessions [01](docs/01-ai-intuition.md)–[08](docs/08-docker.md) |
| Instructor | [Teaching guide](docs/instructor-guide.md), [Resource catalog](docs/resources.md) |
| Hands-on | [Example applications](examples/README.md), [Project briefs](docs/projects.md) |
| Presenter | [Reveal.js deck](build-revealjs/README.md) |

## Course route

1. [What is AI doing?](docs/01-ai-intuition.md) — terminology and limits
2. [Mac workbench](docs/01b-macos-workbench.md) → [Python foundations](docs/02-python-foundations.md) — editor + terminal, shell shortcuts and copy/paste, then a rule-based chatbot
3. [Developer workflow](docs/03-dev-workflow.md) — environments, history, files, Git, optional zsh4humans (not required)
4. [Neural networks and backpropagation](docs/04-neural-networks.md) — intuition, not calculus
5. [Local language models](docs/05-local-llms.md) — Ollama, inference API, model sizes
6. [Web interface](docs/06-streamlit.md) — Streamlit app and conversational state
7. [Make it useful](docs/07-product-quality.md) — prompting, tests, validation, fallbacks
8. [DevOps without overload](docs/08-docker.md) — Dockerfile, compose, security

## Publication

The public course is hosted at **[study.fkr.dev](https://study.fkr.dev/)**. Open the presentation from the homepage or download the entire course ZIP using either of the first two slides. For deployment and DNS details, see [DEPLOYMENT.md](DEPLOYMENT.md). Changes to course materials require `make check` before pushing.

## Reveal.js presentation

Edit `build-revealjs/source.org`, then rebuild:

    make check  # builds the deck, ZIP and formatted HTML lesson pages
    make serve  # serves the exact staged Pages site from _site/

Open http://127.0.0.1:8765/build-revealjs/ (avoid `file://`: YouTube embeds may need a proper origin). **Lessons linked from slides open styled HTML pages by default**, with an explicit download/view link for the source `.md` Markdown, and an optional `curl`/VS Code exercise after the terminal introduction.
The opening slides link to `build-revealjs/py-ai-studyplan-materials.zip`.
The normal build creates the ZIP next to `index.html`, so publishing the **entire `build-revealjs/` directory** makes the download work.
It contains all local study materials: Markdown lessons, exercises, runnable examples, tests, original Reveal.js template, slide sources, generated slides and build tools.
Videos and third-party PDFs remain linked/embedded, rather than redistributed.

To link to a separately hosted archive, rebuild using:

    PY_AI_STUDYPLAN_DOWNLOAD_URL="https://your.example/path/materials.zip" make slides

This changes only the slides' link. Upload the generated ZIP separately to that address.
The default target is also editable in the opening `materials-download` anchors in `build-revealjs/source.org`.

Online JavaScript/CSS libraries and external videos/PDFs need network access. Every external embed has a visible link fallback.

The Reveal.js layout is based on the local `terminal-talk` reference copied unchanged under `template-reference/`. This project has its own course content, editable Org source, the same theme palette, and the copied chalkboard/notes/search/highlight plugin setup. No third-party video or PDF has been redistributed.

Presenter controls: arrows to navigate; `S` notes; `B` chalkboard; `C` annotation canvas; `DEL` clear.

## Constraints and safety

- No GPU or large model is required for the Python, AI-intuition, or UI-with-mock phases.
- Local Ollama is *optional* until session 5; choose a small model after checking available RAM and disk.
- Keep the Ollama HTTP endpoint on loopback; never publish unauthenticated inference or a development Streamlit server on the internet.
- The examples are local learning prototypes, not hardened deployments.
- External resources were cataloged on 2026-10-26; their URLs, availability, and iframe permissions can change.
