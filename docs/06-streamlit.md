# 06 — Make a browser UI

**Time:** 2–3 h. **Milestone:** build a small local chat interface connected to Ollama.

## Read

- [Streamlit chat tutorial](https://docs.streamlit.io/develop/tutorials/chat-and-llm-apps/build-conversational-apps)
- [Streamlit chat widgets](https://docs.streamlit.io/develop/api-reference/chat)

Streamlit is a Python web UI framework. For this project it avoids requiring JavaScript, HTML routing, or a separate backend framework.

## Run

    python3 -m venv .venv
    . .venv/bin/activate
    python -m pip install -r examples/requirements.txt
    ollama pull gemma3:4b
    python -m streamlit run examples/chat_app.py --server.address 127.0.0.1

The Ollama service must be running separately on `http://127.0.0.1:11434`. Visit the URL printed in the terminal.

## Diagram

    Web browser (Streamlit widgets)
            │
            ▼
    Python process (app + chat history)
            │  HTTP client
            ▼
    Ollama server (127.0.0.1:11434)
            │
            ▼
    Quantized local model → generated text

## Lab

1. Print a title and use `st.chat_input` to accept a question.
2. Render user and assistant messages with `st.chat_message`.
3. Store messages in `st.session_state`; observe how reruns affect the UI.
4. Send the conversation to Ollama; show a friendly error if its server is unavailable.
5. Add model selection; remove or clear history on model changes to avoid confusion.

The starter includes chat history, a fixed model list, temperature, clear-history, a spinner and JSON export. It does not yet clear history automatically on model changes: use **Clear conversation** before comparing models, then implement automatic clearing as an exercise. Read the request code before modifying it. For a no-model warm-up, use the upstream tutorial's echo-bot exercise; the supplied `chat_app.py` itself requires Ollama for replies.

## Independence challenge

Add a system-prompt preset or automatic history clearing on model changes. The spinner is already present; token streaming is a separate extension. Demonstrate how the app behaves when Ollama is stopped.

## Security note

This is a local educational UI: it is **not** a multi-user production chatbot. In particular, do not publish Ollama or Streamlit to an untrusted network without authentication and additional security work.

[Next: polish](07-product-quality.md)
