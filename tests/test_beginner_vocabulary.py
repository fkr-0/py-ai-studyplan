"""Regression checks: new terminology must be introduced before exercises need it."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SLIDES = (ROOT / "build-revealjs/source.org").read_text(encoding="utf-8")
GLOSSARY = (ROOT / "docs/beginner-glossary.md").read_text(encoding="utf-8")
MAC = (ROOT / "docs/01b-macos-workbench.md").read_text(encoding="utf-8")
AI = (ROOT / "docs/01-ai-intuition.md").read_text(encoding="utf-8")
TOOLS = (ROOT / "docs/03-dev-workflow.md").read_text(encoding="utf-8")


class BeginnerVocabularyTests(unittest.TestCase):
    def test_inference_is_defined_before_first_slide_use(self):
        section = SLIDES.split("* 01 · What is AI doing?", 1)[0].lower()
        self.assertNotIn("inference", section, "Don't use inference on the cover/roadmap")
        chapter = SLIDES.split("* 01 · What is AI doing?", 1)[1].split("* 02 ·", 1)[0]
        self.assertLess(chapter.index("*Training*"), chapter.index("*Inference*"))
        self.assertIn("*Inference* means **using a trained model**", chapter)
        self.assertIn("**Training = learning:**", AI)
        self.assertIn("**Inference = answering:**", AI)

    def test_git_introduced_before_git_commands(self):
        before = SLIDES.split("* 03 · Developer workflow", 1)[0]
        self.assertNotIn("Git", before, "Avoid jargon on the opening slides")
        chapter = SLIDES.split("* 03 · Developer workflow", 1)[1]
        self.assertLess(chapter.index("*Git:*"), chapter.index("git init"))
        self.assertLess(TOOLS.index("**Git** is a tool"), TOOLS.index("    git init"))
        self.assertIn("GitHub", TOOLS)

    def test_control_notation_decoded_before_shortcuts(self):
        pre = SLIDES.split("** How to read Mac keyboard shortcuts", 1)[0]
        self.assertNotIn("⌃P", pre)
        keyboard = SLIDES.split("** How to read Mac keyboard shortcuts", 1)[1]
        self.assertIn("=Ctrl+C= or =Control-C=", keyboard)
        self.assertIn("=⌃C= or =^C=", keyboard)
        self.assertIn("not** the two characters", keyboard)
        self.assertLess(keyboard.index("=⌃C= or =^C="), keyboard.index("** Two-minute shortcut drill"))
        self.assertIn("does not mean typing the characters", MAC)
        self.assertIn("Control+C and Command+C are not interchangeable", MAC)

    def test_glossary_covers_core_terms(self):
        for term in ["Inference", "Training", "**Git**", "**JSON**", "**^C**", "**⌘**",
                     "**⌃**", "**⇧**", "**API**", "**HTTP**", "venv"]:
            with self.subTest(term=term):
                self.assertIn(term, GLOSSARY)

    def test_day_one_exercise_stays_beginner_friendly(self):
        self.assertIn("Mini-exercise: where does my question go?", SLIDES)
        self.assertNotIn("Checkpoint: draw the boxes", SLIDES)
        self.assertNotIn("set **temperature**", AI)
        self.assertIn("No drawing and no Python knowledge are needed", AI)


if __name__ == "__main__":
    unittest.main()
