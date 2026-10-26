"""Dependency-free tests: python -m unittest discover -s tests -v"""
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "examples"))

from rule_bot import respond


class RuleBotTests(unittest.TestCase):
    def test_greeting(self) -> None:
        self.assertEqual(respond(" HELLO! "), "Hello!")

    def test_unknown_question(self) -> None:
        self.assertIn("do not know", respond("Why?"))

    def test_empty(self) -> None:
        self.assertIn("Type something", respond("  "))

    def test_python(self) -> None:
        self.assertIn("programming language", respond("I like PYTHON"))

    def test_unknown_statement(self) -> None:
        self.assertEqual(respond("Something new."), "Tell me more.")


if __name__ == "__main__":
    unittest.main()
