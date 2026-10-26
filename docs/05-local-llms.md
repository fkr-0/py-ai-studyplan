# 05 — Run a language model locally

**Time:** 2 h. **Milestone:** explain model weights vs serving runtime vs API vs application.

## Resources

- [Ollama quickstart](https://docs.ollama.com/quickstart) · [API documentation](https://docs.ollama.com/api)
- [Ollama Python client](https://github.com/ollama/ollama-python)
- [Model library](https://ollama.com/library)

## For this learner — Apple M4 with 24 GB unified memory

Use **`gemma3:4b`** first. Once the API integration works, optionally compare with **`qwen3:8b`**; both listed quantized downloads fit comfortably on disk if there is adequate free space, although live memory and performance still vary. The 1B model is a lighter fallback, not the main experience on a 24 GB Mac. The full instructions are in [Mac M4 setup](mac-m4-setup.md).

## Hardware decision (approximate starting points, not guarantees)

| Constraint | Possible first try | Caveat |
| --- | --- | --- |
| CPU only / very limited RAM | `qwen3:0.6b` | Compact, weaker answers |
| 8 GB system RAM | `gemma3:1b` | Small model, may be slow |
| 16 GB RAM | `gemma3:4b` | Check disk and memory |
| ~8 GB VRAM plus RAM | `qwen3:8b` | Context/cache overhead; may partly offload to CPU |

Models and requirements evolve. Confirm the exact tags on Ollama's library page before download. In all cases test with low context size first. Local inference can be slow without GPU; don't require performance benchmarks to graduate.

## Install and verify

Use [platform-specific Ollama installation instructions](https://docs.ollama.com/quickstart). On systems where Ollama runs as a background service, start it first; otherwise `ollama serve` in a separate terminal.

    ollama pull gemma3:4b
    ollama run gemma3:4b
    ollama list

In a Python virtual environment:

    python -m pip install ollama
    python examples/cli_chat.py --model gemma3:4b

Run from the repository root. Override model with `--model qwen3:0.6b` if needed.

## API exercise

Inspect an Ollama endpoint via a terminal (local only):

    curl -s http://127.0.0.1:11434/api/tags

Then read [examples/cli_chat.py](../examples/cli_chat.py) and locate the request, model choice, messages, and response handling.

## Distinctions

- A **model** is trained weights and architecture/metadata, often quantized for smaller memory footprint.
- Ollama is a **runtime/server**, not the trained model itself.
- The Python package is a **client** that submits inference requests.
- Chat history lives in the **application**, and must be re-sent when context is needed.
- **Temperature** changes sampling behavior, not training weights.
- **Context window** limits what is processed; large context costs memory.

## Safety

Keep Ollama bound to loopback and do not expose its unauthenticated API publicly; do not assume that model outputs are trusted instructions.

**Exit ticket:** point to the model weights, Python script, local HTTP port, and terminal separately.

[Next: browser UI](06-streamlit.md)
