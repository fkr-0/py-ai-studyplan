# macOS setup for Python and local AI

**Audience:** beginners learning Python and local AI on macOS. The commands below use native zsh and Apple Silicon checks; adapt architecture checks for Intel Macs.

## Hardware assumptions

- Check your Mac architecture, available memory and free disk before selecting a local model.
- Apple Silicon's CPU and GPU share unified memory. Model weights and the active KV cache compete with macOS and other running apps.
- Model fit and speed depend on quantization, context length, available memory and runtime backend. Start small and measure.
- Avoid large downloads at first. Complete one small-model request before comparing larger variants.

## Day 2: Python, editor and terminal setup

**Required first practical lesson:** [macOS editor + terminal workbench](01b-macos-workbench.md). Do this *before* Python control flow. Use VS Code to edit/save and zsh in Terminal.app to run/inspect the same file. The lesson covers Control-A/E/P/N/R history/navigation, Command-C/V clipboard, Control-C interrupt, and the `code .` launcher.

For VS Code on Apple Silicon, use **Command + Shift + P → Shell Command: Install 'code' command in PATH**, then reopen Terminal; `code .` should open your folder. Use File → Open Folder if PATH setup is unsuccessful. [Official macOS instructions](https://code.visualstudio.com/docs/setup/mac). Copilot CLI is optional and not needed.


1. Install a recent supported Python from [python.org](https://www.python.org/downloads/macos/) or Homebrew. For beginners who dislike package managers, the official signed Python installer is fine. Never replace/remove the Python owned by macOS.
2. Install VS Code (or another editor). Open **Terminal.app**.
3. Use `uname -m` to verify native `arm64` (if you see `x86_64`, check Rosetta/terminal settings). Use `python3 --version` and `which python3` to find the interpreter. The Python virtual environment comes **later on Day 7**, after the learner can edit and run files.
4. Create a workspace in your own home directory. The sample paths below are suggested folder names; adjust them to your setup.

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
2. In Terminal, pull the balanced starter model `gemma3:4b`. The examples use this tag; choose `gemma3:1b` if memory or performance is limited.
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

Use the standard Ollama application for this course; separate PyTorch configuration is not part of setup. Choose a local model when following the upstream quickstart: its cloud-model/API-key examples are a different route.

## Day 14: Python calls Ollama

From the extracted course root, reuse the Day 7 environment or create one if it is missing. Activate it in every new Terminal tab, then install the declared sample dependencies:

```sh
cd ~/Projects/py-ai-studyplan
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r examples/requirements.txt
python examples/cli_chat.py --model gemma3:4b
```

Check that `pwd` ends in `py-ai-studyplan` and `ls examples/requirements.txt` finds the file before installing. If either check fails, find the extracted course folder first. Type `quit` to leave the CLI chat; use `deactivate` when finished with the virtual environment.

## Optional shell enhancement after Day 7

macOS already ships with zsh; **no framework is needed** for shortcuts. [Zsh for Humans (z4h)](https://github.com/romkatv/zsh4humans) is **macOS-compatible** and offers autosuggestions, fzf history and completions, but its maintainer states that it has *very limited support* and most bugs will go unfixed. It modifies shell startup files with backup prompts. Keep it an **optional, conscious experiment**, not a prerequisite or automatic install. Read [the workbench's tradeoffs](01b-macos-workbench.md#7-zsh-for-humans-z4h-macos-compatible-optional) before using the upstream installer.

## Day 20: Docker Desktop (optional)

Docker Desktop supports Apple Silicon. Install only after the Python program and Streamlit app run without containers; a Docker image contains your UI, not the model weights. Run the sample through the project's Compose configuration. On Docker Desktop, the name `host.docker.internal` usually connects to host services; if it does not, diagnose host reachability and firewall behavior **without making the local inference service internet-facing**.

## Common macOS gotchas

- `python` might not exist outside a venv; `python3` is the correct initial command.
- A model may run out of memory at high context lengths even when the model file fits on disk.
- The background Ollama service may already be running after launching the app; don't spawn a second conflicting server.
- Some third-party video/PDF sites prevent iframe embedding. The Reveal.js presentation includes a separate `Open original` link.
- Use your own workspace path when running commands; check `pwd` before working with files.
