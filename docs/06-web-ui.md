# Session 06 — Streamlit browser chatbot

**Time:** 2–3 hours. **Output:** browser UI with model response and chat history.

## Read

[Streamlit chat tutorial](https://docs.streamlit.io/develop/tutorials/chat-and-llm-apps/build-conversational-apps). **Important:** parts of this tutorial use a hosted OpenAI client; our sample substitutes Ollama and needs no API key.

## Build

From the **repository root**, install dependencies, start Ollama on the Mac, and run the actual example:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r examples/requirements.txt
ollama pull gemma3:4b
python -m streamlit run examples/chat_app.py --server.address 127.0.0.1
```

See [examples/local-chat](../examples/local-chat/README.md) for packaging and the alternative Docker setup.

Identify these boundaries:

```text
Browser controls
      ↓
Streamlit Python process (session_state + validation)
      ↓
Ollama client (HTTP API)
      ↓
Local model
```

Try two turns; find where history is stored. Clear it and prove the next request has no previous messages. As an extension, **add** a system-prompt control (not yet included in the baseline UI) and observe how behavior changes.

## Checkpoint

The learner can add an input control and explain how its value changes the model request.
