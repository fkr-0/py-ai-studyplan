"""Session 02: deliberately predictable chatbot with zero external dependencies."""

import re


def respond(message: str) -> str:
    text = message.lower().strip()
    if not text:
        return "Type something, or 'quit' to leave."
    if re.search(r"\b(hello|hi|hey)\b", text):
        return "Hello!"
    if "python" in text:
        return "Python is a programming language. What would you like to build?"
    if text.endswith("?"):
        return "I do not know the answer yet; add a rule."
    return "Tell me more."


def main() -> None:
    print("Rule bot (type 'quit' to leave)")
    while True:
        try:
            message = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break
        if message.strip().lower() in ("quit", "exit"):
            print("Goodbye!")
            break
        print("Bot:", respond(message))


if __name__ == "__main__":
    main()
