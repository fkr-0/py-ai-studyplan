# Course map and prerequisites

**Audience:** beginner with little or no programming. **Estimated effort:** eight facilitated sessions of about 2–3 hours, 25–35 hours total with exercises. A new learner may need additional Python practice. **Primary aim:** explain, build, debug and package a local LLM-powered app.

## Learning goals

1. Distinguish classical search, machine learning, neural networks, LLM training, and inference.
2. Write small Python programs, handle JSON, use packages, exceptions, files, and Git.
3. Understand, at intuition level, layers, weights, loss, gradient descent and backpropagation.
4. Run a small local language model and call it via an explicit Python API.
5. Build a browser-based chat application with history, settings and robust errors.
6. Package its frontend and explain ports, volumes, environment variables and container boundaries.

## Dependency graph

```text
AI motivation ──────────────────────────────────────────────┐
        Python basics → venv/Git/JSON → Ollama client → UI → quality → Docker
                          └→ NN intuition + interactive playground ┘
```

## Sessions and deliverables

| Session | Preparation | In-session exercise | Evidence |
|---|---|---|---|
| 01 AI intuition | 3Blue1Brown introduction (~19 min) | Label examples as classical algorithm, ML, inference | Correct explanations |
| 02 Python | CS50P Week 0–2 excerpts | Terminal rule-based chatbot | Demonstrable branching and function |
| 03 Tooling | Missing Semester shell / Git | Virtualenv + JSON prompt library | Fresh install succeeds |
| 04 NN intuition | 3Blue1Brown gradient + backprop | TensorFlow Playground experiment | Explain what changed |
| 05 Local model | Ollama quickstart | Python model call + JSON messages | Successful response + error path |
| 06 Web UI | Streamlit chat tutorial | Chat UI with history | Runs in a local browser |
| 07 Quality | Read example tests | Model choice, output validation, tests | Automated test passing |
| 08 Docker | Docker Python guide | Containerize UI / connect to host Ollama | Rebuild documented |

## Learner-specific recommendation

The student's **M4 MacBook Pro (24 GB unified memory)** is sufficient to follow the local Ollama path, so skip the cloud/GPU contingency unless an unexpected issue occurs. Sessions stay in **English**. At **1–2 hours per day**, distribute the eight workshops across a [21-day learning schedule](21-day-mac-track.md) rather than scheduling one 2-hour meeting per week.

- Day 1: motivation and mental model.
- Days 2–9: Python and development workflow.
- Days 10–12: neural-network intuition and interactive experiments.
- Days 13–15: local Ollama inference.
- Days 16–19: Streamlit plus quality and testing.
- Days 20–21: optional Docker and independent final demo.

See [macOS installation guide](mac-m4-setup.md). Use `gemma3:4b` as the default first model and `qwen3:8b` only as an optional comparison. Favor mastery over the exact end date.

## Pace options

- **2 hours/week:** about 4 months; focus on one small checkpoint each week.
- **4 hours/week:** about 7–9 weeks; a good default.
- **6–8 hours/week:** about 4–5 weeks, provided Python basics stick.
- **Existing programmer:** compress sessions 02–03; spend the saved time on tests and architecture.

These estimates are deliberately loose, dependent on learner experience and hardware.

## Alternate capstone: Tetris solver

Build a board model, collision checks, rotations, legal placement enumeration, weighted heuristics (holes, height, lines), and optionally depth-limited search. It demonstrates classical AI rather than training or LLM inference. An LLM can narrate or inspect decisions, but is not a reliable real-time solver by itself. Prefer this when they enjoy algorithms more than chat UIs.

## What we consciously defer

Training LLMs, fine-tuning, CUDA, PyTorch internals, embeddings/RAG, LangChain, autonomous agents, cloud deployments, Kubernetes, production authentication. Add any of them only after the basic application is explainable and reproducible.
