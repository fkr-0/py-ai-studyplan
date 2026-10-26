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
| Robustness | Demonstrate model-offline error and passing deterministic tests; explain one model-output check |
| Optional extensions | Validate structured output if implemented; explain image/container and ports if taking Docker |

## Graduation exercise

Use a fresh extraction or checkout in a separate folder on the same Mac; a second machine is optional. With Python and Ollama installed, create a new virtual environment, install `examples/requirements.txt`, pull or select a local model, and launch the chatbot using [the example instructions](../examples/README.md). Demonstrate two-turn history, clear it, change temperature, then explain the request flow. Make one small code change without a complete solution and verify its effect. Optionally rebuild the Docker image.

Passing example tests shows only the functions those tests exercise. The UI, model connection, and the learner's new code still need their own checks. Record one expected result, the observed result, and any remaining limitation.

**Stretch:** add a system-prompt preset and test its message preparation, or import an exported conversation with validation. The starter already has a CLI `--model` option, JSON export, and invalid-role unit tests; explain those before extending them.

## Instructor observation

If they can only reproduce step-by-step commands, revisit the underlying Python concepts. If they can diagnose a connection refused error, explain the data flow, and change the UI independently, the goal has been achieved.
