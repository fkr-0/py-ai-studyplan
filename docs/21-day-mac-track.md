# 21-day guided track — MacBook Pro M4 / 24 GB

**Language:** English for the entire course (discussion, code, slides, assignment notes).
**Hardware:** 2024 MacBook Pro with Apple M4-family chip, 24 GB unified memory.
**Study time:** 1–2 hours/day. A realistic target is **three weeks of daily practice**, with optional catch-up days. Estimated core effort: 25–35 hours; experience and debugging can extend it.

This is a *recommended sequence*, not a hard deadline. A day is complete only when the student can explain and modify the exercise unaided. If a day runs long, finish it before proceeding.

## How to use the timetable

The eight sessions are topic groups, not eight additional meetings on top of these days. Video excerpts, guided work and independent exercises all count toward the daily time budget. Start each day at the previous checkpoint; stop after 1–2 hours and note the next small step.

At one hour per day, 21 days provides only 21 hours, below the 25–35 hour core estimate. Plan for **25–35 study days** at that pace. At two hours per day, leave room for breaks and catch-up rather than filling every block with new material. Docker is optional; the final independent demo is the core finish line.

Keep two folders distinct: `~/Projects/prompt-library` for the Days 7–9 exercise, and `~/Projects/py-ai-studyplan` for downloaded course examples. Check the working directory before running commands.

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
| 02 | macOS workbench: Terminal + VS Code | Install tools; open same folder in both; save/run `hello.py` | [Mac workbench](01b-macos-workbench.md) |
| 03 | Keyboard fluency + first Python functions | Drill **Ctrl-A/E/P/N/R**, Cmd-C/V vs Ctrl-C; then formatter | [Mac workbench](01b-macos-workbench.md) + [Python](02-python-foundations.md) |
| 04 | Conditions and loops | Rule-based terminal chatbot | [Session 02](02-python-foundations.md) |
| 05 | Lists, dictionaries and modules | Refactor chatbot rules into data | [Session 02](02-python-foundations.md) |
| 06 | Errors and debugging | Reproduce and fix a deliberate exception | [Session 02](02-python-foundations.md) |
| 07 | Shell history, `venv`, `pip` | Repeat shortcuts, create a clean environment; **optional** z4h discussion | [Developer workflow](03-dev-workflow.md) |
| 08 | Files and JSON | Persist prompt templates in JSON | [Session 03](03-dev-workflow.md) |
| 09 | Git, reproducibility and debugging | Commit, diff, restore; inspect an intentional error in VS Code/Terminal | [Developer workflow](03-dev-workflow.md) |
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
| 20 | Catch-up or optional Docker | Close an unfinished core checkpoint; optionally build the UI image | [Session 08](08-docker.md) |
| 21 | Graduation and reflection | Start app from instructions, make one independent change, explain boundaries | [Assessment](assessment.md) |

## Mac workbench gate before Python exercises

Before Day 4, the learner must independently open a folder from Terminal in VS Code (`code .`, or File → Open Folder), save `hello.py` (Command-S), execute it (`python3 hello.py`), recall/revise a previous command (Control-P, A, E), search history (Control-R), copy/paste between terminal and editor (Command-C/V), and interrupt a command (Control-C). These are different contexts; the learner should explain which program owns each shortcut. See the [hands-on workbench lesson](01b-macos-workbench.md).

## Scope adjustments

- **One hour most days:** allow 25–35 study days for core work; add optional Docker time separately if needed.
- **Two hours most days:** use leftover time for debugging, better documentation, and a feature of the learner’s choosing. Do not rush through the fundamentals.
- **Already comfortable with programming:** compress Days 03–09; spend longer on evaluating model responses.
- **Docker becomes distracting:** stop at Day 19, demo the app, and leave Docker as a bonus workshop.
- **A 2024 Mac with 24 GB unified memory** is capable of running meaningful small/mid-size quantized LLMs locally; it does not require renting cloud GPUs. See [hardware notes](hardware.md) for caveats.

## Completion checklist

- [ ] Can use Terminal.app and VS Code together, and explain Command-C/V vs Control-C and Control-A/E/P/N/R.
- [ ] Can run and explain a Python function, loop and dictionary.
- [ ] Can create a venv and run with declared dependencies.
- [ ] Can articulate loss, gradient and inference without requiring calculus.
- [ ] Can call Ollama from Python and see a returned message.
- [ ] Can independently add a new Streamlit UI control.
- [ ] Can identify a failure at the model server, API or UI layer.
- [ ] Can repeat the demo on a clean checkout with documented commands.
