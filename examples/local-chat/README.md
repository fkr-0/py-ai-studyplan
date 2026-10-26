# Local chat capstone

The canonical UI source is [../chat_app.py](../chat_app.py); its testable pure helper is [../chat_logic.py](../chat_logic.py). This folder contains Docker packaging for that same application.

## Start without Docker

From the **project root**:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r examples/requirements.txt
ollama pull gemma3:4b
python -m streamlit run examples/chat_app.py --server.address 127.0.0.1
```

Visit http://127.0.0.1:8501/. If Ollama is not already managed by a desktop app/service, launch `ollama serve` separately. The example catches model connection errors.

## Optional container

Prefer the single canonical Docker build at the repository root:

```sh
docker compose -f examples/compose.yaml up --build
```

The `examples/local-chat` Compose setup below provides a second, equivalent teaching entrypoint.

```sh
cd examples/local-chat
docker compose up --build
```

The image contains the Streamlit UI, not model weights. Port 8501 is only published on host loopback. Docker routes to host-running Ollama via `host.docker.internal` with a Linux host-gateway mapping. **On some systems, host Ollama only listens on loopback and is unreachable from a container.** This is an intentional troubleshooting exercise; do not solve it by exposing unauthenticated Ollama to the public network.

## Exercises

Add another prompt preset; test switching models; disconnect the model and explain the UI error. Confirm that JSON export contains only visible chat turns.
