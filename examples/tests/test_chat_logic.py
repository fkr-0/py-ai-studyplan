"""Unit tests do not require Ollama or the internet."""
import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from chat_logic import prepare_messages


class MessageTests(unittest.TestCase):
    def test_valid(self):
        messages = prepare_messages([{"role": "user", "content": "hi"}], "Tutor")
        self.assertEqual(messages[0]["role"], "system")
        self.assertEqual(messages[1]["content"], "hi")

    def test_bad_role(self):
        with self.assertRaises(ValueError):
            prepare_messages([{"role": "tool", "content": "x"}])

    def test_empty(self):
        with self.assertRaises(ValueError):
            prepare_messages([{"role": "user", "content": ""}])


if __name__ == "__main__":
    unittest.main()
