"""Sessions 06–08: beginner-friendly local chatbot with a Streamlit UI.

Local only: Ollama must already be serving the selected model.
Do not expose this demo or an unauthenticated Ollama API publicly.
"""
from __future__ import annotations

import json
import os
from typing import Any

import streamlit as st
from ollama import Client, ResponseError

DEFAULT_MODELS = ["gemma3:4b", "qwen3:8b", "gemma3:1b", "qwen3:0.6b"]
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://127.0.0.1:11434")

st.set_page_config(page_title="Python + AI Lab", page_icon="🧪", layout="centered")
st.title("Python + AI · Local Chat")
st.caption("Streamlit → Python Ollama client → local model. No hosted LLM API.")

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.subheader("Model settings")
    model = st.selectbox("Model (must be pulled first)", DEFAULT_MODELS, index=0)
    temperature = st.slider("Temperature", 0.0, 1.5, 0.6, 0.1)
    st.caption(f"Server: `{OLLAMA_HOST}`")
    if st.button("Clear conversation"):
        st.session_state.messages = []
        st.rerun()
    st.download_button(
        label="Export conversation JSON",
        data=json.dumps(st.session_state.messages, indent=2, ensure_ascii=False),
        file_name="chat-history.json",
        mime="application/json",
    )

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask something...")
if prompt and prompt.strip():
    prompt = prompt.strip()
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        with st.spinner(f"Generating with {model}..."):
            try:
                client = Client(host=OLLAMA_HOST, timeout=120.0)
                response: Any = client.chat(
                    model=model,
                    messages=st.session_state.messages,
                    options={"temperature": temperature},
                )
                answer = response.message.content or "(The model returned an empty response.)"
            except (ResponseError, ConnectionError, OSError) as exc:
                st.error(
                    "Ollama is unavailable or the model is missing. "
                    "Start Ollama, pull the selected model and try again."
                )
                st.code(str(exc))
                # Remove unsuccessful user turn; context is not silently corrupted.
                st.session_state.messages.pop()
            else:
                st.markdown(answer)
                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )
