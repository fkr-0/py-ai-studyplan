# Instructor guide

## Planning the course

Work from the [21-day study plan](21-day-mac-track.md), adapting the pace and setup to the group. The examples use `gemma3:4b`; choose a smaller model when resources are limited. Reserve more days for Python practice if needed.

## Principles

- Demonstrate a **purpose**, then explain terms, then let the student change code on their own.
- **Essential early dependency:** [Mac editor + terminal workbench](01b-macos-workbench.md) before the first Python function. Do not assume understanding of Save vs Run, editor vs shell, or Command vs Control.
- Observe a learner using **Control-A/E/P/N/R**, copying terminal output with **Command-C/V**, and interrupting `sleep` with **Control-C**. z4h is an optional extension after native zsh.
- Lead with the distinction *deterministic computation / learned parameters / generative inference*.
- After each video, pause for one question and one experiment.
- Treat progress as demonstrable behavior, not videos watched.
- Check Python understanding *without* LLM auto-completion at least once per session.
- Do not conflate API-driven apps with ML model training.

## Teaching sessions

| Session | 10–25 min explanation | 45–65 min guided lab | Independent extension | Exit question |
| --- | --- | --- | --- | --- |
| 01 | What is AI? NN video | Compare rule vs LLM | Draw architecture | Training vs inference? |
| 02 | VS Code + Terminal.app, shortcuts; then functions | `hello.py` save/run, then rule chatbot | Recall with Control-P and explain Command-C/V vs Control-C | Which program handles each key? |
| 03 | zsh history/search, venv, files, Git | JSON prompt library | Recover from traceback; optional z4h discussion | What is in a venv? |
| 04 | Gradients, backprop, tokens | Neural Playground | Tune rate / layers | Why need held-out tests? |
| 05 | Local runtime architecture | Ollama chat from Python | Change model tag | What does the client send? |
| 06 | Request/state/response | Streamlit chat | Clear conversation | Where does state live? |
| 07 | Validation and failure modes | Extend app | Structured output tests | Why distrust fluent output? |
| 08 | Image/container/network/volume | Dockerize UI | Explain network failure | Why not expose Ollama? |

## Presentation route

Open [the deck](../build-revealjs/README.md). Main sections are grouped by session, vertical sub-slides hold a resource, demo, or exercise. Some resources are designed for asynchronous watching: do not play every video in one sitting.

### When hardware is missing

Sessions 1–4 can run on a modest computer. Run session 6 initially against a deterministic fake responder if no model can be loaded, then optionally replace it with Ollama later. Hardware limitations must not block learning UI and Python control flow.

### When learning time is limited

Use the [21-day schedule](21-day-mac-track.md) as a sequence, leaving extra time for terminal/editor fluency on Days 2–3. If lessons run long, split them instead of skipping independent practice. For experienced programmers, omit beginner Python labs but retain local inference, safety and architecture lessons.

### Ethical/software boundaries

Explain hallucinations, personal data/privacy, open licenses, unsafe network exposure, prompt injection, and that the program validates model-produced data like other untrusted input.

## Questions to ask in the final demo

1. Which code runs in browser, Python process and model runtime?
2. What happens on a missing model, wrong port, or empty prompt?
3. How is saved conversation history different from context sent to the model?
4. Can the application verify arithmetic or JSON without asking the LLM?
5. What would be needed to run it on a public website?

## Resource permissions

Reference video/pdf links from [resources.md](resources.md). Opening a resource in a slide does not mean republishing/copying it. If an iframe breaks, the learner uses the adjacent direct link.
