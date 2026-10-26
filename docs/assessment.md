# Definition of done and independent checks

The learner demonstrates **understanding and modification**, not just a working installation.

| Competency | Minimum evidence |
|---|---|
| AI distinction | Explain why a Tetris search algorithm need not use a neural net |
| Python | Change a function, list/dictionary transformation and error handling unaided |
| Environment | Create venv and run an application from a clean checkout |
| Training intuition | Explain loss, gradient descent and backprop qualitatively |
| LLM invocation | Name the server, model, Python client, HTTP boundary and prompt history |
| UI | Modify a Streamlit control and show the updated behavior |
| Robustness | Demonstrate model-offline error, rejected structured output, passing tests |
| Ops | Explain image vs. container, host vs. container port and why volumes exist |

## Graduation exercise

On a new machine that has Python and Ollama installed: clone/copy the repo, create virtualenv, install requirements, pull or select a model, launch the local chatbot, demonstrate two-turn history, change a prompt preset, then explain the request flow. Optionally rebuild the Docker image.

**Stretch:** provide a `--model` CLI option, persisted JSON chat export, and a short test of invalid message roles.

## Instructor observation

If they can only reproduce step-by-step commands, revisit the underlying Python concepts. If they can diagnose a connection refused error, explain the data flow, and change the UI independently, the goal has been achieved.
