# Environment, model choice and fallbacks

## Known learner: MacBook Pro M4 (2024), 24 GB unified memory

**Primary recommendation:** follow the [step-by-step M4 macOS guide](mac-m4-setup.md) and [21-day plan](21-day-mac-track.md). This computer is well-suited to locally run small and medium quantized LLMs; external GPU/cloud setup is unnecessary for the planned exercises.

Use **`gemma3:4b` (~3.4 GB download)** for the default chatbot, try **`qwen3:8b` (~5.2 GB download)** as a comparative second model, and fall back to **`gemma3:1b`** if troubleshooting startup or memory use. Published download sizes are not RAM footprints; active context, backend and other applications consume memory. Apple Silicon uses unified memory, not a separately allocated 24 GB VRAM pool. See [Ollama Gemma 3](https://ollama.com/library/gemma3), [Ollama Qwen 3](https://ollama.com/library/qwen3).

First setup commands on **the student's Mac**:

```sh
uname -m     # expect arm64 with native Apple Silicon Terminal
python3 --version
python3 -m venv .venv
source .venv/bin/activate
ollama pull gemma3:4b
ollama run gemma3:4b
```

Install Python first from the official macOS release or package manager and install Ollama from [ollama.com/download](https://ollama.com/download) before the Ollama commands. Do not modify macOS' system Python.

## Before installing anything

Record operating system, RAM, GPU/VRAM (if present), available disk space, and comfortable weekly time. No GPU is required for Python, the interactive NN tools, or a rule-based chatbot. Local LLM inference speed is hardware-dependent.

| Configuration | Starting point | Comment |
|---|---|---|
| Low-end CPU machine | `qwen3:0.6b` | Fastest test of wiring, lower response quality |
| ~8 GB RAM laptop | `gemma3:1b` | Good small-model starting point |
| ~16 GB RAM | `gemma3:4b` | Try if performance permits |
| Dedicated GPU / enough RAM | `qwen3:8b` | Larger and heavier; not a prerequisite |

Model tags, availability and size change: check the official [Ollama library](https://ollama.com/library) before class. Download size is **not** peak runtime memory. Quantization affects memory use and quality. GPU inference is optional.

## Cross-platform environment

1. Install Python using the OS-approved installer/package manager.
2. Make a virtual environment: `python3 -m venv .venv` (Windows: `py -m venv .venv`).
3. Activate it: POSIX `. .venv/bin/activate`, Windows PowerShell `.venv\Scripts\Activate.ps1`.
4. From the extracted course root, use `python -m pip install -r examples/requirements.txt` inside the venv.
5. Use Git for source. Ignore `.venv`, secrets and generated files.
6. Install [Ollama](https://ollama.com/download), then `ollama pull gemma3:4b` on the learner's 24 GB Mac; use `gemma3:1b` as a smaller fallback.

## Fallback routes

- **No model fits:** use an external hosted inference endpoint if permitted and affordable, behind a small client adapter; otherwise use the deterministic bot for UI work.
- **Offline:** use pre-downloaded videos/resources and an already-pulled model; the slides' CDN runtime and YouTube embeds do require internet, whereas the Markdown does not.
- **Docker unavailable:** skip Session 08 until later. Package with `requirements.txt` and a short README.
- **Small screen:** don't force the video+code slide together; use the original source in a separate browser tab.

## Basic safety

Don't paste tokens or private files into an LLM. Keep Ollama on loopback; avoid exposing port 11434 or an unauthenticated Streamlit UI to untrusted networks. Treat model text as untrusted and always validate structured output.
