# Didactic review — 2026-10-26

**Scope:** 21-day English study track for a beginner using a 2024 M4 MacBook Pro with 24 GB unified memory, 1–2 hours of study per day. Sources inspected: Reveal.js Org source and generated HTML, learner schedule, macOS setup, instructor notes, Python/Ollama/Streamlit examples and project tests. The review targets **learning progression and concrete student actions**, not aesthetics alone.

## Findings and implemented changes

| Finding in previous deck | Severity | Resolution | Student evidence |
| --- | --- | --- | --- |
| First Python function appeared before editor and terminal were introduced | High | Inserted the macOS workbench before Python syntax (Session 02 / Day 02) | Opens a real project with `code .`, saves/runs `hello.py` |
| The role of Terminal, zsh, editor, interpreter and file save was implicit | High | Added a four-component map and the edit–save–run–debug loop | Learner identifies which process runs each action |
| Shell history/navigation shortcuts were missing | High | Added Control-A/E/P/N/R table and two-minute keyboard drill, repeated on Day 07 | Learner navigates and searches previous commands unaided |
| Copy/paste could be confused with interrupt | High | Distinguished **Command-C/V** from **Control-C**, with deliberate `sleep 30` exercise | Learner copies output and safely interrupts a running process |
| Linux/Windows shell references and generic model RAM choices obscured the actual Mac setup | Medium | Updated terminal lessons, Mac paths, environment setup, Ollama 4B default | Native `arm64`, project lives under home directory, model matches hardware |
| Benefits of enhanced shells could distract from first principles | Medium | Added z4h as explicitly **optional**, mentioned maintainer's limited-support warning and shell-file changes | Student completes core drill *without* installing any framework |
| Commands were easy to copy without understanding | High | Inserted active recall, prediction, own edits, deliberate error, and copy/paste safety checkpoints | Student completes independent edit and diagnoses a traceback |
| The slide deck had substantial video-heavy material | Medium | Kept videos as optional deeper vertical slides with fallback links; added labs **before** optional videos | Live session time prioritized for typing and experiments |

## Recommended instructional route

1. **Motivation (Day 01):** why there are distinct AI methods; distinguish inference from learning.
2. **Mac workbench (Day 02):** Terminal.app ↔ zsh ↔ Python, VS Code, folder, editor launcher, first saved/runnable file.
3. **Keyboard fluency (Day 03):** Control-A/E/P/N/R, Command-C/V vs Control-C; then basic Python functions.
4. **Python ownership (Days 04–06):** rule bot, branches, loops, debugging and observable tests.
5. **Project habits (Days 07–09):** venv, JSON, Git, repeat shell drills, optional z4h discussion only after fundamentals.
6. **ML intuition (Days 10–12):** neural-network visuals, gradients/backprop, Transformer; differentiate model training vs inference.
7. **Local inference (Days 13–15):** Ollama on Apple M4, `gemma3:4b`, HTTP boundary, resilient client.
8. **Product and packaging (Days 16–21):** Streamlit, history/settings, validation, optional Docker, final independent demo.

## Interactive teaching rules

- **One new idea → predict result → type/edit → run → inspect → independent change.**
- **Mac keyboard terms must be explicit:** `⌘` (Command) and `⌃` (Control) are different. The same keystroke may behave differently when the terminal or editor has focus.
- Show Windows/Linux commands only in separate portability appendix, not on core beginner slides.
- Optional tools (Homebrew, z4h, Docker, cloud inference, Copilot) must not become hidden prerequisites.
- Never teach downloading and executing arbitrary scripts as an unexamined shell exercise.
- Ask a human-meaningful explanation at each session checkpoint; do not assess by copying code or merely watching video.

## Boundaries and remaining limitations

- The curriculum cannot guarantee fluency in 21 days for someone entirely new to computing. Keep milestone-based pacing.
- A MacBook Pro M4 with 24 GB can handle common quantized 4B and 8B LLMs, but not all model/context combinations; timings are not guaranteed.
- Shell configurations/plugins can change shortcut bindings; the keyboard drill assumes **stock zsh with Emacs-style editing keys**.
- Zsh for Humans is macOS-compatible according to upstream documentation, but upstream warns: very limited maintenance/support, no planned features, and most bugs unfixed (checked 2026-10-26). Installing it modifies shell startup files.
- Video/PDF iframes depend on external providers; every embed has a direct-link fallback. An HTML static check cannot prove every provider allows playback.
- The sample chatbot is an educational local app, not hardened for multiuser or public access.

## Authoritative references

- [Apple: Terminal keyboard shortcuts](https://support.apple.com/guide/terminal/keyboard-shortcuts-trmlshtcts/mac).
- [Microsoft: VS Code on macOS](https://code.visualstudio.com/docs/setup/mac) and [integrated terminal](https://code.visualstudio.com/docs/terminal/basics).
- [Apple: macOS default zsh shell](https://support.apple.com/guide/terminal/change-the-default-shell-trml113/mac).
- [romkatv: Zsh for Humans, maintenance warning, install/caveats](https://github.com/romkatv/zsh4humans).

## Review acceptance criteria

Run `make check` from project root; confirm tests, internal Markdown links, ZIP integrity and slide source build. For visual validation use a real browser, 1400×900 and smaller viewport, and check that the workbench, key tables, exercises and materials ZIP button are readable and actionable. A live Mac keyboard lab is still recommended because Linux-based browser rendering cannot verify macOS key events.
