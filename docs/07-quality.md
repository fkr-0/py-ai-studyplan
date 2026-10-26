# Session 07 — Make the application useful and trustworthy

**Time:** 2–3 hours. **Output:** configurable, tested application.

## Features to implement

1. Add a model selector using `ollama.list()` or an explicit known-model list.
2. Add a temperature slider. Avoid representing temperature as truthfulness or intelligence.
3. Add predefined system-prompt presets and a clear-history button.
4. Add a JSON export of history (don't include secrets).
5. Catch connection errors and timeout/failure conditions.
6. Explain why structured model output needs validation rather than blind parsing.

## Exercises

From the repository root, edit [`examples/chat_app.py`](../examples/chat_app.py) to add or remove a setting, then run the tests:

```sh
python -m unittest discover -s examples/tests -v
```

Make a deliberate input validation failure and check that the unit test catches it. Turn off Ollama and confirm that the UI produces a helpful error instead of crashing.

## Critical distinction

- **Software correctness:** predictable state, input validation, reproducible errors, tests.
- **Model output quality:** uncertain sampling, task-specific evaluations, potential hallucinations, prompt injection and errors.
- Tests of the Python client do **not** prove a model's generated statements are true.

## Checkpoint

The learner can articulate a failure mode and show one automated and one manual test.
