# Session 07 — Make the application useful and trustworthy

**Time:** 2–3 hours. **Output:** configurable, tested application.

## Inspect the starter, then extend it

1. Explain the existing fixed model list; optionally populate it from installed models.
2. Compare responses using the existing temperature slider. Temperature is not truthfulness or intelligence.
3. Use the existing clear-history and JSON export controls; avoid exporting private conversations.
4. Add a system-prompt preset or clear history automatically when the model changes.
5. Inspect the existing error handling, then test offline, missing-model and timeout behavior separately.
6. Explain why structured model output needs validation; implement a validator as an optional extension.

## Exercises

From the repository root, edit [`examples/chat_app.py`](../examples/chat_app.py) to add or remove a setting, then run the tests:

```sh
python -m unittest discover -s examples/tests -v
```

Make a deliberate input validation failure and check that the unit test catches it. Turn off Ollama and confirm that the UI produces a helpful error instead of crashing.

The tests cover `chat_logic.prepare_messages`, a standalone teaching helper. The starter UI does not call it yet. To test a new prompt preset through this helper, wire it into the request path and verify both the function and a real UI interaction; green helper tests alone do not verify the UI.

## Critical distinction

- **Software correctness:** predictable state, input validation, reproducible errors, tests.
- **Model output quality:** uncertain sampling, task-specific evaluations, potential hallucinations, prompt injection and errors.
- Tests of the Python client do **not** prove a model's generated statements are true.

## Checkpoint

The learner can articulate a failure mode and show one automated and one manual test.
