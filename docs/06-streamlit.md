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

The example implements the above with minimal code; read it before modifying.

## Independence challenge

Add a system prompt preset, a clear-history button and a spinner/streaming indicator. Demonstrate how the app behaves when Ollama is stopped.

## Security note

This is a local educational UI: it is **not** a multi-user production chatbot. In particular, do not publish Ollama or Streamlit to an untrusted network without authentication and additional security work.

[Next: polish](07-product-quality.md)
