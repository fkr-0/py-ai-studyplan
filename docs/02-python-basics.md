# Session 02 — Python fundamentals

**Time:** 2–4 hours, slower for complete beginners. **Output:** terminal chatbot.

## Watch/read

[CS50P Week 0 (functions and variables)](https://cs50.harvard.edu/python/weeks/0/), [Week 1 (conditionals)](https://cs50.harvard.edu/python/weeks/1/), [Week 2 (loops)](https://cs50.harvard.edu/python/weeks/2/). Read/exercise selectively, not whole lectures before coding. Week 0 [PDF slides](https://cdn.cs50.net/python/2022/x/lectures/0/lecture0.pdf).

## Ideas

Variables and types → `if`/`elif`/`else` → functions and returns → `while` loop → lists and dictionaries → strings and formatting → input/output.

## Exercise

Build a small rule-based chat program *without AI*:

```python
def reply(message: str) -> str:
    normalized = message.strip().lower()
    if normalized in {"hi", "hello"}:
        return "Hello! What can I help with?"
    if "python" in normalized:
        return "Try writing a function and calling it."
    return "I don't know that rule yet."

while True:
    message = input("You (or quit): ")
    if message.lower().strip() == "quit":
        break
    print("Bot:", reply(message))
```

Next: add three new rules, make one mistake deliberately and read the traceback. Move the function into a separate module. Explain how deterministic rule-based responses differ from generated model replies.

## Checkpoint

They can change a branch and predict its result, including one input that takes the default branch.
