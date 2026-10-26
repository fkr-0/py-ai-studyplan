# Runnable lessons

- `rule_bot.py` — Session 2: deterministic text rules, requires only Python.
- `cli_chat.py` — Session 5: Ollama Python API and preserved messages.
- `chat_app.py` — Sessions 6–7: Streamlit UI, model picker, temperature, history and JSON export.
- `Dockerfile`, `compose.yaml` — Session 8: containerize the frontend only.

## Without Ollama

    python3 examples/rule_bot.py

## With Ollama (installed and started separately)

    ollama pull gemma3:4b
    python3 -m venv .venv
    . .venv/bin/activate
    python -m pip install -r examples/requirements.txt
    python examples/cli_chat.py --model gemma3:4b
    python -m streamlit run examples/chat_app.py --server.address 127.0.0.1

Windows: activate `.venv\Scripts\Activate.ps1`; adapt the Python command.

## Optional Docker workshop

    docker build -t py-ai-studyplan-ui ./examples
    docker compose -f examples/compose.yaml up --build

Visit http://127.0.0.1:8501, and stop with `docker compose -f examples/compose.yaml down`.

The Compose file reaches `host.docker.internal` only if a reachable private Ollama endpoint exists. Docker Engine on Linux maps this to the host gateway; a host-bound loopback Ollama listener generally **will not** be reachable. For the first Docker lesson, seeing a graceful offline error is a valid checkpoint; do not make the Ollama API public to bypass network isolation.

## Independence ideas

1. Extend the rule-based bot without copying an entire file.
2. Print request/response timings in the CLI chatbot.
3. Add a new prompt preset or a response validator to the Streamlit app.
4. Test what happens when Ollama is not running or the chosen model was never pulled.
