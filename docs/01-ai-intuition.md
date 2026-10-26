# 01 — What is AI actually doing?

**Time:** about 2 h. **Prerequisites:** none. **Milestone:** explain in everyday words how a program that follows fixed rules differs from a program that learned from examples.

## First: the new words

**AI** means *artificial intelligence*: software that does tasks such as recognizing pictures or generating responses. An **algorithm** is simply a series of instructions. A **rule-based program** follows instructions someone wrote, such as “if the answer contains hello, reply hi.”

A **model** is a program whose behavior depends on settings it learned from examples. A **language model** produces text. An **LLM** is a *large language model*.

Two words that sound complicated but describe everyday actions:

- **Training = learning:** a model is given many examples and its numerical settings change.
- **Inference = answering:** someone asks a trained model a question and it uses the settings it already learned. That request does not itself retrain those settings.

We will study the details—neural networks, tokens and the math—later, after Python basics. See the [plain-English glossary](beginner-glossary.md) whenever you encounter an unfamiliar word.

## Teaching storyline

1. Start with a calculator and a chat assistant: one follows fixed calculation rules, the other generates text based on learned settings.
2. Give one example of training (learning from examples) and one of inference (answering with existing settings).
3. A model can produce a convincing sentence that is incorrect. Its confidence of tone does not prove truth.
4. The *app* shows messages; the *model* generates a possible answer. They are not the same program.

## Watch (pause and discuss)

- **3Blue1Brown — But what is a Neural Network? (~19 min)** [video](https://www.youtube.com/watch?v=aircAruvnKk) / [illustrated article](https://www.3blue1brown.com/lessons/neural-networks/).
- Optional **Andrej Karpathy — Intro to Large Language Models** [video](https://www.youtube.com/watch?v=zjkBMFhNj_g), especially 00:00–18:00; security segment later.
- Slides: [course presentation](../build-revealjs/README.md), chapter 1.

## Lab: same task, different strategies

Ask: "Is the number 34 even?" A two-line Python rule answers exactly; a text model is overkill. Compare with "Explain parity to a 10-year-old": an LLM might be useful, but the answer needs checking.

Open [rule_bot.py](../examples/rule_bot.py) after learning the minimal Python syntax; use the browser for discussions now.

## Check understanding

- Which activity changes what a model has learned: **training** or **inference**?
- Can a Tetris solver follow explicit rules instead of using a learned model?
- If the LLM says 17 × 19 = 324, is that sufficient evidence?

**Exit ticket (2 minutes):** Imagine asking a chatbot, **“Why is the sky blue?”** Put these three cards into the order in which they participate: **You**, **chat app**, **language model**. Say who types the question, who generates the response, and who displays it. No drawing and no Python knowledge are needed. **Example answer:** You type → chat app sends the question → language model produces words → chat app displays the words to you. **For later:** Ollama is the program that runs the language model on the Mac. A rule-based chatbot can use `if`/`else` instead of a model.

[Next: Mac editor + terminal workbench](01b-macos-workbench.md), then [Python foundations](02-python-foundations.md).
