# Instructor guide

## This learner

English throughout. 2024 MacBook Pro M4-family chip with 24 GB unified memory, studying 1–2 hours daily. Work from the [21-day Mac study plan](21-day-mac-track.md). The local model default is `gemma3:4b`, with `qwen3:8b` for optional comparison. Reserve more days for Python syntax if needed.

## Principles

- Demonstrate a **purpose**, then explain terms, then let the student change code on their own.
- Lead with the distinction *deterministic computation / learned parameters / generative inference*.
- After each video, pause for one question and one experiment.
- Treat progress as demonstrable behavior, not videos watched.
- Check Python understanding *without* LLM auto-completion at least once per session.
- Do not conflate API-driven apps with ML model training.

## Teaching sessions

| Session | 10–25 min explanation | 45–65 min guided lab | Independent extension | Exit question |
| --- | --- | --- | --- | --- |
| 01 | What is AI? NN video | Compare rule vs LLM | Draw architecture | Training vs inference? |
| 02 | Variables, functions, loops | Rule chatbot | New rules and tests | What does `return` do? |
| 03 | CLI, venv, files, Git | JSON prompt library | Recover from traceback | What is in a venv? |
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

In 2 h/week schedule, assign one 15–20 minute video plus a 20 minute coding exercise between meetings. For experienced programmers, omit beginner Python labs but retain local inference, safety and architecture lessons.

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
