# 02 — Python fundamentals

**Time:** 2–4 h, plus individual practice. **Goal:** write short functions without copying verbatim.

## Start with editor + terminal, not a notebook

First complete the [macOS workbench](01b-macos-workbench.md). Keep **VS Code** and **Terminal.app** open on the same folder. Type a function in `hello.py`, save with **Command-S**, run with `python3 hello.py`, then change/save/rerun using **Control-P** to recall the command. The tight edit–save–run–inspect loop matters more than typing speed.

## Resource

Harvard's [CS50P Week 0](https://cs50.harvard.edu/python/weeks/0/) (functions/variables), [Week 1](https://cs50.harvard.edu/python/weeks/1/) (conditions) and [Week 2](https://cs50.harvard.edu/python/weeks/2/) (loops). The [Week 0 PDF slides](https://cdn.cs50.net/python/2022/x/lectures/0/lecture0.pdf) are useful on a second screen; use the lecture pages for current materials.

## Minimum syllabus

- Variables, `str`, `int`, `float`, `bool`, operators.
- `print`, `input`, `if`/`elif`/`else`, `for` and `while`.
- `def`, arguments and return values, list and dictionary operations.
- `None`, exceptions as observable failures rather than mysterious errors.

## First micro-lab: observe an edit

Create `hello.py` in VS Code, type the following, save with Command-S, then run `python3 hello.py` in Terminal:

    name = 'friend'
    print(f'Hello, {name}!')

Change the name in the editor; save; recall the command with Control-P; intentionally introduce a typo and fix it. The console executes the *saved* file; a changed but unsaved editor buffer is not automatically the same thing.

## Guided lab: predictable responses

Start with:

    def respond(message: str) -> str:
        text = message.lower().strip()
        if "hello" in text:
            return "Hello!"
        if text.endswith("?"):
            return "I cannot answer that yet."
        return "Tell me more."

Add five rules. Separate input/output from the core function so you can test it.

Work from [examples/rule_bot.py](../examples/rule_bot.py). Run:

    python3 examples/rule_bot.py

## Independent exercises

1. Turn the rules into a dictionary and add a default response.
2. Count turns in the conversation and stop on `quit`.
3. Write a pure function that detects whether a number is even.
4. Create two tests: greeting and unknown question.

## Mastery checkpoint

Without looking up a complete solution, implement a function that takes a list of strings and returns only the ones containing "python" (case-insensitively). Talk through its return type and test one edge case.

[Next: development workflow](03-dev-workflow.md)
