# macOS setup — 2024 MacBook Pro (M4 family, 24 GB)

**Audience:** student learning Python and local AI on a Mac. This is the primary platform for this cohort. **All instructions and work remain in English.**

## Hardware assumptions

- MacBook Pro (2024), reported M4 chip, **24 GB unified memory**; exact base M4 vs M4 Pro variant is not yet specified and does not need to be for this course.
- Apple Silicon's CPU and GPU share unified memory. Do not treat 24 GB as discrete GPU VRAM. Model weights and the active KV cache compete with macOS and other running apps.
- This is sufficient to try 4B and 8B quantized model variants. Actual speed depends on selected model, quantization, context length, RAM pressure and Ollama backend.
- Avoid large models at first; a 30B/32B download is not a sensible entry exercise on 24 GB.

## Day 2: Python, editor and terminal setup

**Required first practical lesson:** [macOS editor + terminal workbench](01b-macos-workbench.md). Do this *before* Python control flow. Use VS Code to edit/save and zsh in Terminal.app to run/inspect the same file. The lesson covers Control-A/E/P/N/R history/navigation, Command-C/V clipboard, Control-C interrupt, and the `code .` launcher.

For VS Code on Apple Silicon, use **Command + Shift + P → Shell Command: Install 'code' command in PATH**, then reopen Terminal; `code .` should open your folder. Use File → Open Folder if PATH setup is unsuccessful. [Official macOS instructions](https://code.visualstudio.com/docs/setup/mac). Copilot CLI is optional and not needed.


1. Install a recent supported Python from [python.org](https://www.python.org/downloads/macos/) or Homebrew. For beginners who dislike package managers, the official signed Python installer is fine. Never replace/remove the Python owned by macOS.
2. Install VS Code (or another editor). Open **Terminal.app**.
3. Use `uname -m` to verify native `arm64` (if you see `x86_64`, check Rosetta/terminal settings). Use `python3 --version` and `which python3` to find the interpreter. The Python virtual environment comes **later on Day 7**, after the learner can edit and run files.
4. Create a workspace in your home directory. Do not attempt to create files in someone else’s `/home/user` directory on macOS; that path belongs to the instructor’s machine.

```sh
uname -m
python3 --version
which python3

mkdir -p ~/Projects/python-ai-playground
cd ~/Projects/python-ai-playground
# After installing the VS Code 'code' launcher:
code .
# Create hello.py in the editor, save with Command-S, then run:
python3 hello.py
```

The `python-ai-playground` folder is a *scratch playground*. When the learner downloads the course ZIP from the opening slide, extract it into `~/Projects/py-ai-studyplan` and open **that** folder in VS Code. See the [exact download/unzip path](01b-macos-workbench.md#6-continue-with-the-downloaded-course). Subsequent `examples/` commands run from this extracted course root, **not** from an empty scratch folder.

For learners who want it later, [Homebrew](https://brew.sh/) is an optional, useful package manager. Its native Apple Silicon default installation prefix is `/opt/homebrew`. Do not make Homebrew a prerequisite for the first Python exercise.

## Day 13: Install Ollama (desktop app)

1. Download the macOS application from [ollama.com/download](https://ollama.com/download). Launch it so its local service is running.
2. In Terminal, pull the balanced starter model `gemma3:4b`. This is the course default for a 24 GB Mac; `gemma3:1b` is a faster/lightweight troubleshooting fallback.
3. Optionally compare answers against `qwen3:8b`; do not pre-download multiple models before they have understood the first one.

```sh
ollama --version
ollama pull gemma3:4b
ollama run gemma3:4b

# Later, for comparative evaluation, optionally:
ollama pull qwen3:8b
ollama run qwen3:8b

# Confirm which models have been downloaded:
ollama list
```

As of 2026-10-26, the Ollama catalog lists `gemma3:4b` at about 3.4 GB and `qwen3:8b` at about 5.2 GB of model download data; these are **not** peak live RAM requirements. See [Gemma 3](https://ollama.com/library/gemma3) and [Qwen 3](https://ollama.com/library/qwen3) for current tags.

Ollama has Apple Silicon acceleration support, including a newer MLX-based path in recent releases. No separate PyTorch/MPS/Metal configuration is required just to use the standard Ollama application.

## Day 14: Python calls Ollama

From the course project directory, create a virtual environment and install the sample dependencies:

```sh
cd ~/projects/python-ai-lab
python3 -m venv .venv
source .venv/bin/activate
python -m pip install "ollama>=0.4,<1" "streamlit>=1.40,<2"
```

Once the course files are extracted under `~/Projects/py-ai-studyplan`, use `python -m pip install -r examples/requirements.txt`, then start `python examples/cli_chat.py --model gemma3:4b` from that project root. Reuse the Day 7 `venv` practice to understand the installation; note that every fresh Terminal tab needs its own `source .venv/bin/activate`.

## Optional shell enhancement after Day 7

macOS already ships with zsh; **no framework is needed** for shortcuts. [Zsh for Humans (z4h)](https://github.com/romkatv/zsh4humans) is **macOS-compatible** and offers autosuggestions, fzf history and completions, but its maintainer states that it has *very limited support* and most bugs will go unfixed. It modifies shell startup files with backup prompts. Keep it an **optional, conscious experiment**, not a prerequisite or automatic install. Read [the workbench's tradeoffs](01b-macos-workbench.md#7-zsh-for-humans-z4h-macos-compatible-optional) before using the upstream installer.

## Day 20: Docker Desktop (optional)

Docker Desktop supports Apple Silicon. Install only after the Python program and Streamlit app run without containers; a Docker image contains your UI, not the model weights. Run the sample through the project's Compose configuration. On Docker Desktop, the name `host.docker.internal` usually connects to host services; if it does not, diagnose host reachability and firewall behavior **without making the local inference service internet-facing**.

## Common macOS gotchas

- `python` might not exist outside a venv; `python3` is the correct initial command.
- A model may run out of memory at high context lengths even when the model file fits on disk.
- The background Ollama service may already be running after launching the app; don't spawn a second conflicting server.
- Some third-party video/PDF sites prevent iframe embedding. The Reveal.js presentation includes a separate `Open original` link.
- Paths under `/home/user/writing/py-ai-studyplan` are instructor-side; the student should work under their own macOS home directory.
