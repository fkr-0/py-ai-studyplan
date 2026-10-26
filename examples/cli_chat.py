"""Session 05: a tiny Ollama command-line client.

Usage: python examples/cli_chat.py --model gemma3:1b
The Ollama server and model must already be available.
"""
from __future__ import annotations

import argparse
import sys

from ollama import Client, ResponseError


def main() -> int:
    parser = argparse.ArgumentParser(description="Local Ollama chat")
    parser.add_argument("--model", default="gemma3:4b")
    parser.add_argument("--host", default="http://127.0.0.1:11434")
    args = parser.parse_args()
    client = Client(host=args.host, timeout=120.0)
    messages: list[dict[str, str]] = []
    print(f"Chatting with {args.model} at {args.host}; type /quit to stop.")
    while True:
        try:
            prompt = input("You> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return 0
        if prompt in {"/quit", "/exit"}:
            return 0
        if not prompt:
            continue
        messages.append({"role": "user", "content": prompt})
        try:
            response = client.chat(model=args.model, messages=messages)
            content = response.message.content or ""
        except (ResponseError, ConnectionError, OSError) as exc:
            messages.pop()
            print(f"Could not reach/model Ollama: {exc}", file=sys.stderr)
            continue
        messages.append({"role": "assistant", "content": content})
        print(f"Model> {content}")


if __name__ == "__main__":
    raise SystemExit(main())
