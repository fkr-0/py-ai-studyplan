# Facilitator's guide

## Current teaching setup

The [21-day schedule](21-day-mac-track.md) translates the eight topic groups into daily blocks. Use [macOS setup](macos-setup.md) for Mac walkthroughs and adapt commands for other platforms. Choose model size according to available resources; examples use `gemma3:4b`.

Before any coding, run the [macOS editor + Terminal workbench](01b-macos-workbench.md) with the learner at the keyboard: VS Code, Terminal.app, **Command-C/V vs Control-C**, **Control-A/E/P/N/R**. Decode symbol spelling aloud first: **^C, ⌃C and Ctrl+C all mean hold Control and press C; ⌘C means Command+C (copy)**. Don't assume the keyboard glyphs are self-explanatory. zsh4humans is an optional bonus, not a prerequisite.

## Before session 1

Ask about the learner's goal, prior coding experience, operating system and study time. Check available resources before local inference. **Do not delay the first theory/Python lesson while waiting for a GPU.**

Prepare Python 3.11+, a code editor, a terminal, browser, and (later) Ollama. Use an ordinary user account. Never require root for teaching exercises.

## Suggested rhythm for each workshop

| Minutes | Activity |
|---:|---|
| 0–10 | Retrieve previous milestone from memory; learner predicts what will happen |
| 10–25 | One visual or concept (often a video segment) |
| 25–80 | Pair programming, learner at keyboard |
| 80–105 | Unguided modification or bug hunt |
| 105–120 | Demo, explanation in own words, assign a stretch task |

Begin with an interesting AI demo, then backfill syntax. The one invariant is that the learner **types and debugs their own changes**.

## Instructor prompts

- “Which part is deterministic code and which part is a model prediction?”
- “What would happen if the model process were stopped?”
- “Where does the message history live?”
- “Which part changes model weights: training or inference?”
- “If this errors, what is the smallest step we can test?”
- “What is different about binding a web server to 127.0.0.1 vs 0.0.0.0?”

## Media presentation

Open slide deck on localhost, rather than a file URL, for reliable embeds and presenter notes. YouTube videos are lazy-loaded; PDF slides use a browser-native PDF iframe, plus a separate open link. Interactive sites are deliberately links when frame restrictions are likely. Always keep a tab ready for the original source.

Notes: `S` opens speaker notes; the reference template includes whiteboard/chalkboard controls. Check browser plugin loading before class.

## Assessment

See [assessment.md](assessment.md). Don't assess by whether copied code runs alone; ask the student to change one behavior and explain the request/response flow. Finish with an install/reproduce task.

## Troubleshooting

- Ollama not running: `ollama list`, `ollama ps`; on platforms that require it start `ollama serve` (do not launch a second instance if already running).
- Slow CPU inference: switch to a smaller model; reduce context length.
- Network unavailable: use the small deterministic echo/rule-based bot and lessons 01–04; Markdown remains local.
- Iframe blank: click the source link below it; site policies or privacy settings may prevent embedding.
- Port collision: check existing processes and choose a different local port; don't expose the Ollama API publicly.
