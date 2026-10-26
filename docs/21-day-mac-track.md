# 21-day guided track — MacBook Pro M4 / 24 GB

**Language:** English for the entire course (discussion, code, slides, assignment notes).
**Hardware:** 2024 MacBook Pro with Apple M4-family chip, 24 GB unified memory.
**Study time:** 1–2 hours/day. A realistic target is **three weeks of daily practice**, with optional catch-up days. Estimated core effort: 25–35 hours; experience and debugging can extend it.

This is a *recommended sequence*, not a hard deadline. A day is complete only when the student can explain and modify the exercise unaided. If a day runs long, finish it before proceeding.

## Daily structure

- **5–10 min:** recall yesterday’s ideas; predict what code should do.
- **15–20 min:** watch part of one high-quality video or work through a concept.
- **35–65 min:** hands-on coding with the learner typing.
- **10–20 min:** one independent change, one failed case, and a short written explanation.
- For a 1-hour day, split the lesson at a meaningful checkpoint instead of racing.

## Day-by-day study plan

| Day | Focus | Concrete deliverable | Reference |
|---:|---|---|---|
| 01 | What are algorithms, ML and LLMs? | Draw the AI stack and distinguish training from inference | [Session 01](01-ai-intuition.md) |
| 02 | Install and meet Python on macOS | Terminal, editor, `python3 --version`, `hello.py` | [Mac setup](mac-m4-setup.md) |
| 03 | Variables, strings and functions | Prompt/response formatter | [Session 02](02-python-foundations.md) |
| 04 | Conditions and loops | Rule-based terminal chatbot | [Session 02](02-python-foundations.md) |
| 05 | Lists, dictionaries and modules | Refactor chatbot rules into data | [Session 02](02-python-foundations.md) |
| 06 | Errors and debugging | Reproduce and fix a deliberate exception | [Session 02](02-python-foundations.md) |
| 07 | Shell, `venv`, `pip` | Fresh environment and clean run | [Session 03](03-dev-workflow.md) |
| 08 | Files and JSON | Persist prompt templates in JSON | [Session 03](03-dev-workflow.md) |
| 09 | Git and reproducibility | Commit, change, diff, restore one change | [Session 03](03-dev-workflow.md) |
| 10 | Neural-network intuition | Sketch neurons, weights and a loss | [Session 04](04-neural-networks.md) |
| 11 | Gradient descent / backprop | Run three TensorFlow Playground variations | [Session 04](04-neural-networks.md) |
| 12 | Tokens and Transformers | Explain next-token generation using an interactive demo | [Session 04](04-neural-networks.md) |
| 13 | Ollama on Apple Silicon | Pull and compare `gemma3:4b` / optional `qwen3:8b` | [Session 05](05-local-llms.md) |
| 14 | Python → local LLM | CLI chat with short message history | [Session 05](05-local-llms.md) |
| 15 | HTTP and error handling | Distinguish model, runtime, client and network errors | [Session 05](05-local-llms.md) |
| 16 | Streamlit fundamentals | Render input and messages in a browser | [Session 06](06-streamlit.md) |
| 17 | Chat history and model selection | Multi-turn chatbot with a model picker | [Session 06](06-streamlit.md) |
| 18 | UI refinement | Prompt presets, temperature and clear-history | [Session 07](07-product-quality.md) |
| 19 | Tests and validation | Run tests; reproduce Ollama-offline failure | [Session 07](07-product-quality.md) |
| 20 | Docker fundamentals | Build the UI image and inspect ports and logs | [Session 08](08-docker.md) |
| 21 | Graduation and reflection | Start app from instructions; explain every boundary | [Assessment](assessment.md) |

## Scope adjustments

- **One hour most days:** reserve four additional catch-up days (Python basics, JSON, UI, Docker) and extend to about 25 days.
- **Two hours most days:** use leftover time for debugging, better documentation, and a feature of the learner’s choosing. Do not rush through the fundamentals.
- **Already comfortable with programming:** compress Days 03–09; spend longer on evaluating model responses.
- **Docker becomes distracting:** stop at Day 19, demo the app, and leave Docker as a bonus workshop.
- **A 2024 Mac with 24 GB unified memory** is capable of running meaningful small/mid-size quantized LLMs locally; it does not require renting cloud GPUs. See [hardware notes](hardware.md) for caveats.

## Completion checklist

- [ ] Can run and explain a Python function, loop and dictionary.
- [ ] Can create a venv and run with declared dependencies.
- [ ] Can articulate loss, gradient and inference without requiring calculus.
- [ ] Can call Ollama from Python and see a returned message.
- [ ] Can independently add a new Streamlit UI control.
- [ ] Can identify a failure at the model server, API or UI layer.
- [ ] Can repeat the demo on a clean checkout with documented commands.
