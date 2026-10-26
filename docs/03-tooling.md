# Session 03 — Tools, environments, Git and JSON

**Time:** 2–4 hours. **Output:** a reusable prompt library.

## Materials

- [MIT Missing Semester — Shell](https://missing.csail.mit.edu/2020/course-shell/)
- [MIT Missing Semester — Git](https://missing.csail.mit.edu/2020/version-control/)
- [Python venv](https://docs.python.org/3/library/venv.html)
- [Python JSON](https://docs.python.org/3/library/json.html)

## Workflow

```sh
mkdir prompt-library && cd prompt-library
git init
python3 -m venv .venv
. .venv/bin/activate
python -m pip --version
printf '.venv/\n__pycache__/\n' > .gitignore
```

Create `prompts.json` containing two named prompts. Write `main.py` that uses `json.load`, lists available prompt names, accepts a choice, and prints the selected prompt. Practice `FileNotFoundError` and `json.JSONDecodeError`. Commit source files, never `.venv`.

## Observe

The model is not involved: files store data, Python reads it, and the shell invokes Python. Where will the API boundary enter in Session 05?

## Checkpoint

From a fresh directory, the student can activate a venv, run their program and inspect Git changes.
