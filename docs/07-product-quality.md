# 07 — Turn a demo into a useful tool

**Time:** 2–3 h. **Milestone:** compare models, validate output and make failures understandable.

## Practical improvements

- Model picker populated from `ollama.list()` or a known fallback list.
- Session history that can be cleared or exported as JSON.
- Prompt presets with visible instructions; no hidden magic.
- Configurable temperature; compare responses under the *same prompt*.
- Loading/errors: disabled model, unavailable server, empty answer, malformed JSON.
- Local-only deployment and no accidental API credential logging.

## Experiments

| Experiment | Observation to record |
| --- | --- |
| Same question, temperature 0 vs higher | Diversity / repeatability (not guaranteed determinism) |
| Same question, two model sizes | Quality, speed, factual uncertainty |
| Ask for a JSON object | Can Python parse it? Was its schema validated? |
| Stop the Ollama service | Does the app explain failure without traceback leakage? |
| Ask an arithmetic question | Can the program verify the result separately? |

## Evaluation sheet

Write 5 repeatable prompts (summarization, question answering, exact formatting, counting, and refusal to guess). Log model tag, settings, elapsed time, expected properties and results. Avoid treating confident wording as correctness.

## Add tests

Build unit tests around ordinary Python functions (history serialization, input validation, prompt selection). Avoid tests that depend on the model returning a specific sentence. For integration tests, make explicit whether Ollama is running.

## Optional structured output

Use Ollama's API-supported structured output options where compatible; validate responses with Python rather than trusting that JSON *looks* correct. Introduce Pydantic only if the learner has mastered dictionaries and exceptions.

## Exit ticket

They can independently modify a UI feature, reproduce a bug, explain its cause, and show an automated or manual verification.

[Next: Docker](08-docker.md)
