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

## JSON exercise

Save a file such as:

    {"prompts": [{"name": "friendly", "text": "Explain this simply."}]}

Write Python to load, list, and append prompts using `json.load` / `json.dump`. Handle missing files with a friendly error.

## Git basics

    git init
    git status
    git add .
    git commit -m "Add prompt library"

Before commit: keep `.venv/`, caches, API keys and generated files out of Git (see [.gitignore](../.gitignore)). Explain the distinction between source code, data and dependencies.

## Debugging lesson

Create a deliberate TypeError, read the *last* traceback line, inspect the offending variable, then repair the code. Use `print(repr(value))` before introducing an interactive debugger.

## Mastery checkpoint

Delete and recreate the `.venv` directory without losing project source. Describe what Git tracks and what it should not track.

[Next: neural networks](04-neural-networks.md)
