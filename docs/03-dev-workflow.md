# 03 — Python as a development tool

**Time:** 2–4 h. **Milestone:** create a fresh environment, run a script, read/write JSON, and commit a change.

## Sources

- [MIT Missing Semester](https://missing.csail.mit.edu/) — the shell, tools, Git, debugging.
- [Python venv documentation](https://docs.python.org/3/library/venv.html).
- [Git book](https://git-scm.com/book/en/v2).

## Terminal lab (Linux/macOS)

    mkdir python-ai-lab && cd python-ai-lab
    python3 -m venv .venv
    source .venv/bin/activate
    python -m pip --version
    python -c 'print("Environment is ready")'

Windows PowerShell activation: ` .venv\Scripts\Activate.ps1 `. Use `python` / `py` as appropriate. Never `sudo pip install` into the system interpreter for a beginner project.

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
