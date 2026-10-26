"""Testable model-independent message preparation for Session 07."""
from __future__ import annotations

def prepare_messages(history: list[dict[str, str]], system_prompt: str = "") -> list[dict[str, str]]:
    """Validate UI-provided chat turns before passing them to the model."""
    result = []
    if system_prompt.strip():
        result.append({"role": "system", "content": system_prompt.strip()})
    for item in history:
        if not isinstance(item, dict) or item.get("role") not in {"user", "assistant"}:
            raise ValueError("History must contain user or assistant message dicts")
        content = item.get("content")
        if not isinstance(content, str) or not content.strip():
            raise ValueError("Messages must have non-empty text")
        result.append({"role": item["role"], "content": content})
    return result
