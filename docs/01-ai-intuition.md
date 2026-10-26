# 01 — What is AI actually doing?

**Time:** 2 h. **Prerequisites:** none. **Milestone:** explain the difference between classical search, machine learning, and a language model.

## Teaching storyline

1. AI includes rule-based systems, search, planning, machine learning and neural networks; not every AI problem uses an LLM.
2. A neural network is a parametrized function. Training changes those parameters. Inference computes outputs using existing parameters.
3. Language models turn text into tokens, evaluate probabilities for the next token, and repeatedly sample/select tokens.
4. Fluent output is **not** a reliability guarantee. Distinguish models' abilities from the surrounding application's checks.

## Watch (pause and discuss)

- **3Blue1Brown — But what is a Neural Network? (~19 min)** [video](https://www.youtube.com/watch?v=aircAruvnKk) / [illustrated article](https://www.3blue1brown.com/lessons/neural-networks/).
- Optional **Andrej Karpathy — Intro to Large Language Models** [video](https://www.youtube.com/watch?v=zjkBMFhNj_g), especially 00:00–18:00; security segment later.
- Slides: [course presentation](../build-revealjs/README.md), chapter 1.

## Lab: same task, different strategies

Ask: "Is the number 34 even?" A two-line Python rule answers exactly; a text model is overkill. Compare with "Explain parity to a 10-year-old": an LLM might be useful, but the answer needs checking.

Open [rule_bot.py](../examples/rule_bot.py) after learning the minimal Python syntax; use the browser for discussions now.

## Check understanding

- What changes when an LLM is **trained**? What changes when you set **temperature**?
- Can a Tetris solver use search instead of a trained network?
- If the LLM says 17 × 19 = 324, is that sufficient evidence?

**Exit ticket (2 minutes):** Imagine asking a chatbot, **“Why is the sky blue?”** Put these three cards into the order in which they participate: **You**, **chat app**, **language model**. Say who types the question, who generates the response, and who displays it. No drawing and no Python knowledge are needed. **Example answer:** You type → chat app sends the question → language model produces words → chat app displays the words to you. **For later:** Ollama is the program that runs the language model on the Mac. A rule-based chatbot can use `if`/`else` instead of a model.

[Next: Mac editor + terminal workbench](01b-macos-workbench.md), then [Python foundations](02-python-foundations.md).
