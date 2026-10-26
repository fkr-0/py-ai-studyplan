"""Didactic regression tests: macOS workflow must precede code examples."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SOURCE = (ROOT / "build-revealjs/source.org").read_text(encoding="utf-8")
WORKBENCH = (ROOT / "docs/01b-macos-workbench.md").read_text(encoding="utf-8")
PLAN = (ROOT / "docs/21-day-mac-track.md").read_text(encoding="utf-8")


class MacCurriculumTests(unittest.TestCase):
    def test_cover_is_first_slide(self) -> None:
        html = (ROOT / "build-revealjs/index.html").read_text(encoding="utf-8")
        first = html.split('<div class="slides">', 1)[1].lstrip()
        self.assertTrue(first.startswith('<section id="python-ai-1"'),
                        "Pandoc phantom empty title slide must not reappear")
        self.assertIn('href="py-ai-studyplan-materials.zip"', first[:1200])

    def test_workbench_precedes_python(self) -> None:
        self.assertLess(SOURCE.index("* 02 · Mac workbench"), SOURCE.index("** Python first steps"))
        self.assertLess(SOURCE.index("** Open the same folder"), SOURCE.index("** Python first steps"))
        self.assertLess(SOURCE.index("** Copy + paste"), SOURCE.index("** Python first steps"))

    def test_core_keyboard_bindings(self) -> None:
        for key in ("Control + A", "Control + E", "Control + P", "Control + N", "Control + R"):
            with self.subTest(key=key):
                self.assertIn(key, WORKBENCH)

    def test_mac_clipboard_and_interrupt(self) -> None:
        self.assertIn("Command + C", WORKBENCH)
        self.assertIn("Command + V", WORKBENCH)
        self.assertIn("Control + C", WORKBENCH)
        self.assertIn("sleep 30", WORKBENCH)

    def test_editor_is_integrated_into_execution(self) -> None:
        for marker in ("code .", "hello.py", "Command + S", "python3 hello.py"):
            self.assertIn(marker, WORKBENCH)

    def test_z4h_is_optional_and_upstream_limited(self) -> None:
        self.assertIn("zsh4humans", WORKBENCH)
        self.assertIn("very limited support", WORKBENCH)
        self.assertIn("optional", WORKBENCH.lower())

    def test_day_two_and_three_practice(self) -> None:
        self.assertIn("| 02 | macOS workbench:", PLAN)
        self.assertIn("| 03 | Keyboard fluency", PLAN)


if __name__ == "__main__":
    unittest.main()
