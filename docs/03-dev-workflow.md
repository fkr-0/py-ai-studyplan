# 03 — Python as a development tool

**Time:** 2–4 h. **Milestone:** create a fresh environment, run a script, read/write JSON, and commit a change.

## Sources

- [MIT Missing Semester](https://missing.csail.mit.edu/) — the shell, tools, Git, debugging.
- [Python venv documentation](https://docs.python.org/3/library/venv.html).
- [Git book](https://git-scm.com/book/en/v2).

## macOS Terminal + VS Code lab

First complete the [hands-on Mac workbench](01b-macos-workbench.md). Use native Terminal.app and VS Code, not Linux/Windows instructions, and practise **Control-A** start, **Control-E** end, **Control-P/N** previous/next history, **Control-R** reverse search. **Command-C/V** copy/paste on macOS; **Control-C** interrupts. Use `code .` to open the current folder.

The following commands work in zsh on Apple Silicon:

    mkdir -p ~/Projects/prompt-library
    cd ~/Projects/prompt-library
    python3 -m venv .venv
    source .venv/bin/activate
    python -m pip --version
    code .
    python -c 'print("Environment is ready")'

macOS uses `python3` before activating a virtual environment and generally `python` inside it. Never use `sudo pip install` for this project. After unzipping course material, use `~/Projects/py-ai-studyplan` as the working directory.

## Optional shell enhancement: Zsh for Humans

[zsh4humans](https://github.com/romkatv/zsh4humans) works on macOS and adds completion, autosuggestions and fuzzy history; its [upstream tips](https://github.com/romkatv/zsh4humans/blob/master/tips.md) include macOS key variations. **But its maintainer warns of very limited support, with most bugs unfixed.** The installer changes zsh startup files after offering backups. Teach **built-in macOS zsh first**, then discuss whether an optional shell modification is worthwhile. It is never required to graduate, and remote install scripts should not run automatically. See [workbench tradeoffs](01b-macos-workbench.md#7-zsh-for-humans-z4h-macos-compatible-optional).

## Exercise: fetch Markdown and edit it

The course's web links now open **rendered HTML** for comfortable reading. The raw `.md` sources stay downloadable for editing in VS Code. After learning shell paths, try:

```sh
cd ~/Projects/python-ai-playground
curl --fail --location --show-error \
  --output lesson.md \
  https://study.fkr.dev/docs/01-ai-intuition.md
head -n 12 lesson.md
code lesson.md
```

Explain `curl` (fetch), `--output` (save), and `code` (open in an editor). Compare with the [formatted lesson in the browser](https://study.fkr.dev/docs/01-ai-intuition.html). Do not execute downloaded scripts.

## JSON exercise

Save a file such as:

    {"prompts": [{"name": "friendly", "text": "Explain this simply."}]}

Write Python to load, list, and append prompts using `json.load` / `json.dump`. Handle missing files with a friendly error.

## Git basics

From `~/Projects/prompt-library` (your exercise project, separate from the course download), create `.gitignore` in the editor **before staging**:

    .venv/
    __pycache__/
    .env

Then save `prompts.json` and your reader as `main.py`:

    git init
    git status
    git add .gitignore main.py prompts.json
    git diff --cached
    git commit -m "Add prompt library"

Before commit: keep `.venv/`, caches, API keys and generated files out of Git (see [.gitignore](../.gitignore)). Explain the distinction between source code, data and dependencies.

## Debugging lesson

Create a deliberate TypeError, read the *last* traceback line, inspect the offending variable, then repair the code. Use `print(repr(value))` before introducing an interactive debugger.

## Mastery checkpoint

In the exercise project, deactivate and rename `.venv` to `.venv-backup`, create a new `.venv`, and run `main.py` again. Do not run the renamed environment; virtual environments should be recreated at their intended path. Describe what Git tracks and what it should not track. Keep the backup until the fresh environment works.

[Next: neural networks](04-neural-networks.md)
