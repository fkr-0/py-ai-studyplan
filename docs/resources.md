# Resource catalog and embedding policy

Links checked or cross-referenced to primary publishers on **2026-10-26**. External availability, licensing and embedding permissions may change. These resources are **linked/embedded**, never redistributed as local media files.

| ID | Resource | Type | Course | Reveal.js presentation |
| --- | --- | --- | --- | --- |
| NN-01 | [3Blue1Brown: Neural network](https://www.youtube.com/watch?v=aircAruvnKk) | YouTube | 01 | Embedded video + direct link |
| NN-02 | [3Blue1Brown: Gradient descent](https://www.youtube.com/watch?v=IHZwWFHWa-w) | YouTube | 04 | Embedded video + link |
| NN-03 | [3Blue1Brown: Backpropagation](https://www.youtube.com/watch?v=Ilg3gGewQ5U) | YouTube | 04 | Embedded video + link |
| NN-04 | [3Blue1Brown: Transformers](https://www.youtube.com/watch?v=wjZofJX0v4M) | YouTube | 04–05 | Embedded video + link |
| LLM-01 | [Karpathy: Intro to LLMs](https://www.youtube.com/watch?v=zjkBMFhNj_g) | YouTube | 01 optional | Embedded video + link |
| LLM-02 | [Karpathy: Deep Dive into LLMs](https://www.youtube.com/watch?v=7xTGNNLPyMI) | YouTube | 04 optional | Link, to avoid 3+ hour in-class viewing |
| PY-01 | [CS50P Week 0](https://cs50.harvard.edu/python/weeks/0/) | Lecture site | 02 | Link |
| PY-02 | [CS50P Week 0 slides (32-page PDF)](https://cdn.cs50.net/python/2022/x/lectures/0/lecture0.pdf) | PDF | 02 | Inline PDF + download/open link |
| PY-03 | [CS50P Week 0 YouTube](https://www.youtube.com/watch?v=JP7ITIXGpHk) | YouTube | 02 optional | Link |
| PY-04 | [MIT Missing Semester](https://missing.csail.mit.edu/) | Site/lectures | 03 | Link |
| NN-05 | [TensorFlow Playground](https://playground.tensorflow.org/) | Interactive | 04 | Link (iframe may be blocked) |
| NN-06 | [Transformer Explainer](https://poloclub.github.io/transformer-explainer/) | Interactive | 04 | Link (iframe may be blocked) |
| LLM-03 | [Ollama docs](https://docs.ollama.com/quickstart) | Documentation | 05 | Link |
| LLM-04 | [Ollama Python client](https://github.com/ollama/ollama-python) | Documentation | 05 | Link |
| UI-01 | [Streamlit chat tutorial](https://docs.streamlit.io/develop/tutorials/chat-and-llm-apps/build-conversational-apps) | Tutorial | 06 | Link |
| OPS-01 | [Docker Python guide](https://docs.docker.com/guides/python/) | Documentation | 08 | Link |
| AI-01 | [CS50 AI: Search](https://cs50.harvard.edu/ai/weeks/0/) | Lecture | Optional Tetris | Link |

## Reveal.js implementation policy

- YouTube: `youtube-nocookie.com/embed/<video-id>` in an `iframe` with `loading=lazy` and a **separate** link to the canonical video page. Browser privacy protections, embedding settings or origin/referrer rules can prevent playback.
- PDF: inline browser viewer via `iframe src=<publisher PDF URL>` plus independent open/download link. Embedded display may be blocked by the publisher's headers or browser security.
- Third-party interactive sites: link directly by default, not embedded: these frequently block iframes and small screens make them difficult to use.
- Lecture webpages/docs: link only. Use presenter notes for sequencing.
- External `iframe` content and CDN scripts **require internet**. Run the deck using localhost HTTP rather than a `file://` URL; this also supplies an HTTP origin to YouTube.
- Keep external materials optional for *runtime*: core slides, diagrams and written labs are included locally. If a video fails to load, use its `Open video` link.
- Attribution belongs to the originating authors. Never imply the project owns third-party media.

## Why these and not a larger catalog?

A beginner benefits from a small, ordered selection of high-quality videos and **a lot of time writing code**. The entire Karpathy deep dive and full Harvard course are reference material, not an entrance exam.
