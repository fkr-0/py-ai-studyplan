# Session 05 — Ollama and a local inference API

**Time:** ~2 hours. **Output:** a Python program that calls a local model.

This is a supplementary API exercise. Follow [the main local-model lesson](05-local-llms.md) for setup and the daily schedule.

## Materials

- [Official Ollama quickstart](https://docs.ollama.com/quickstart)
- [Ollama Python client](https://github.com/ollama/ollama-python)
- [Ollama REST API](https://docs.ollama.com/api/introduction)
- [Hardware options](hardware.md)

## Install and test

```sh
ollama pull gemma3:4b
ollama run gemma3:4b
```

In another shell, in the project venv:

```sh
python -m pip install ollama
```

```python
from ollama import chat

response = chat(
    model="gemma3:4b",
    messages=[
        {"role": "system", "content": "Answer succinctly."},
        {"role": "user", "content": "What is gradient descent?"},
    ],
)
print(response["message"]["content"])
```

## What is running where?

```text
Python script -- HTTP localhost:11434 --> Ollama runtime --> model weights
               <-- JSON response / tokens <--
```

Experiment with prompts, temperature, and shorter vs. longer inputs. Test the Ollama-down case and handle it without a full traceback to the learner. Never bind an unauthenticated Ollama API to the public internet.

## Checkpoint

The student can identify *model*, *runtime*, *API*, *client* and *application* as distinct components.
