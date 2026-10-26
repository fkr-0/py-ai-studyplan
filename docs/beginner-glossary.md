# Plain-English glossary — words in the order you meet them

**A guide, not a test.** You don't need to memorize these. The lessons explain each term when it becomes useful; this is a page to revisit when you forget a word.

## Day 1 — AI basics

| Word | Everyday explanation | Small example |
| --- | --- | --- |
| **AI** (artificial intelligence) | Software that performs tasks associated with human thinking. | Playing games, describing pictures, answering questions. |
| **Algorithm** | A set of steps for solving a problem. | Follow a recipe; check whether a number is even. |
| **Rule-based program** | Program follows rules a person wrote directly. | If the message says “hello,” reply “hi.” |
| **Model** | A program whose behavior depends on settings learned from many examples. | A model that suggests the next words of a reply. |
| **Neural network** | One common kind of model built from connected mathematical steps. | Image classification or language generation. |
| **LLM / language model** | LLM = *large language model*. A model that generates text. | An AI-powered chat assistant. |
| **Training** | Teaching a model by changing its learned settings using examples. | Training with a large collection of text. |
| **Inference** | Using a trained model to answer a new request **without updating its learned settings**. | Ask “Why is the sky blue?” and get a reply. |

Notice: asking a model a question does not automatically re-train it. It may use the conversation as context, but the learned settings do not change just from that answer.

## Days 2–3 — Your Mac, editor and keyboard

| Word or symbol | Meaning |
| --- | --- |
| **Terminal.app** | A Mac app that displays a text window where you can give commands. |
| **Shell / zsh** | The program *inside* Terminal that reads the commands you type. The standard macOS shell is called zsh. |
| **Prompt** (in the shell) | The line where the shell is waiting for your next command. |
| **VS Code / editor** | The app you use to type and save source-code files. |
| **Python / interpreter** | The language of your code / the program that reads it and performs its instructions. |
| **Folder / directory** | Two names for the same thing: a place where files live. |
| **Path** | An address pointing to a file or folder, like `~/Projects/example`. |
| **⌘** | **Command** key on a Mac; `⌘C` = Command + C (copy selected text). |
| **⌃** | **Control** key on a Mac; `⌃C` = Control + C. |
| **^C** | Another way of *writing* Control + C. **Do not literally type `^` and `C`.** If it appears after stopping a program, it reports that Control+C was pressed. |
| **Ctrl+C / Control-C** | Hold Control, press C. In a terminal with a running program, this normally interrupts it. |
| **⇧** | **Shift** key, so `⌘⇧P` = Command + Shift + P. |
| **⌥** | **Option** key on a Mac. Not required for the beginner drills. |
| **Command-C vs Control-C** | **Command-C** copies selected text; **Control-C** interrupts a running program in the terminal. |
| **History** | Commands you typed earlier that the shell remembers; find them with Control-P or Control-R. |

## Days 4–9 — Programming and keeping track

| Word | Everyday explanation |
| --- | --- |
| **Function** | A named group of instructions that can be used repeatedly. |
| **Variable** | A name referring to a value, like `name = "Pat"`. |
| **Loop** | Instructions repeated until a condition changes. |
| **Traceback** | Python's report showing where something went wrong. |
| **Package** | Reusable Python code, usually written by someone else, that you can install. |
| **Virtual environment / venv** | A separate place for the Python packages one project needs; avoids mixing projects. |
| **JSON** | A simple text format for structured data, such as `{"name": "Pat"}`. |
| **Git** | A tool that saves versions of your work. You can see changes and go back to earlier versions. |
| **Repository / repo** | A folder of files tracked by Git; often shared online through GitHub. |
| **GitHub** | A website that stores and shares Git repositories; it is *not* the same as Git. |
| **Commit** | A named snapshot of changes recorded by Git. |
| **Markdown / .md** | Text with simple marks for headings, links and code. A readable HTML version is provided in this course. |
| **HTML** | The format browsers use to display web pages. |
| **curl** | A command for downloading data from an address; downloading a text file does not execute it. |

## Days 10–15 — How models work and how apps talk

| Word | Everyday explanation |
| --- | --- |
| **Weight / parameter** | One of the numeric settings inside a learned model. |
| **Loss** | A number measuring how wrong the model's prediction was on an example. |
| **Gradient** | A direction describing how changing settings would affect loss. |
| **Backpropagation** | A method of computing gradients efficiently through a neural network. |
| **Token** | A piece of text the model processes; it may be a word or part of a word. |
| **Temperature** | A setting influencing how varied/unpredictable the model's chosen words can be. |
| **Ollama** | An app that runs a language model on your computer and accepts requests from Python. |
| **Server** | Program that waits to receive requests. |
| **Client** | Program that sends a request and reads a response. |
| **API** | A defined way programs exchange requests and results. |
| **HTTP** | A widely used format for communicating with web services. |
| **Local** | Running on your own computer rather than a remote online server. |

## Days 16–21 — The little web app

| Word | Everyday explanation |
| --- | --- |
| **Streamlit** | A Python tool for creating simple web pages and interactive apps. |
| **Browser** | App such as Safari or Chrome that displays a website. |
| **State / chat history** | Information the app remembers between interactions, such as previous messages. |
| **Test** | An automated check that code behaves as expected. |
| **Docker** (optional) | A tool for packaging an app and its dependencies into something reproducible. |
| **Container** (optional) | A running, isolated instance of a packaged application. |

**In doubt:** stop the video or exercise, say the word in everyday language, try a small example, then continue. There is no need to learn everything on this page in advance.

[Return to the study timetable](21-day-mac-track.md) · [Day 1: AI basics](01-ai-intuition.md) · [Mac editor and terminal](01b-macos-workbench.md)
