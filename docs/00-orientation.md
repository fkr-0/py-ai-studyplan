# Orientation: plan for the learner, not the machine

## Suggested starting route

- **Platform:** macOS walkthroughs are provided; adapt commands for other operating systems.
- **Study blocks:** allow 1–2 hours, with breaks and catch-up days.
- **Course language:** English.
- **Suggested route:** [21-day Mac study track](21-day-mac-track.md), [editor + terminal first](01b-macos-workbench.md), then [Mac setup](macos-setup.md); approximately 3 weeks at 1–2 hours daily, plus catch-up if completely new to programming.
- Adjust Python practice to prior coding experience and observed progress.

## First conversation (10 minutes)

Ask only what changes the plan:

- **Goal**: general understanding, build an app, automate daily tasks, or career exploration?
- **Background**: no code, spreadsheets, scripting, or another programming language?
- **Study time**: what daily or weekly practice budget is realistic, and which days need a shorter block or a break?
- **Computer**: OS, RAM, free disk, CPU/GPU (VRAM if known); may software be installed?
- **Constraints**: internet availability, accessibility needs, willingness to use cloud resources.

Do not turn missing hardware details into a blocker. Do sessions 1–4 with any ordinary computer; introduce Ollama only after checking the system.

## Possible schedules

| Background | Approx. total effort | 2h/week | 4h/week | 6h/week |
| --- | ---: | ---: | ---: | ---: |
| New to programming | ~30–35 h | 15–18 weeks | 8–9 weeks | 5–6 weeks |
| Some scripting | ~23–28 h | 12–14 weeks | 6–7 weeks | 4–5 weeks |
| Already a developer | ~17–22 h | 9–11 weeks | 5–6 weeks | 3–4 weeks |

The eight sessions are *milestones*; split or merge as needed. A conceptual video is not a substitute for writing code.

## Prior knowledge / success rubric

Before: Can they find a terminal? Make a directory? Write `print("hello")`? Explain the difference between a website and a program running on their PC?

After: Can they (1) explain inference vs training, (2) implement and debug simple Python functions, (3) isolate dependencies with `venv`, (4) run a local model if hardware permits, (5) connect Python → Ollama → browser UI, (6) check output and handle an offline model? Docker packaging is an optional extension.

## Minimum setup

- Computer with an up-to-date browser and Python 3.11+ (or current supported Python).
- Plain text editor; VS Code is a beginner-friendly option, but not mandatory.
- Internet for slides, downloads and documentation. The sample apps can be developed offline after installation.
- Local model phase: sufficient *available* RAM/disk for the chosen quantized model, **not** a promised GPU requirement.

## If local inference is impossible

Use a hosted inference API *only with explicit understanding of privacy/cost*, or replace the Ollama call with the deterministic `examples/rule_bot.py` while learning Streamlit and web architecture. Do not upload sensitive documents/prompts.

## Working agreement

In each meeting: 10 min recap → 15–25 min concept → 45–65 min guided lab → 15 min independent modification → 10 min review. Prefer short review questions to exams.

[Course index](../README.md)
