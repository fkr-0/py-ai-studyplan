# Capstone briefs

## A — Local LLM playground (default)

**Why:** Covers Python, API clients, state, browser UI, model configuration and validation.

**Minimum acceptance:** 1) Start local model; 2) choose a model; 3) send text through Python to Ollama; 4) render response and previous turns; 5) show useful error when offline; 6) explain the architecture diagram; 7) README with fresh-machine steps.

**Extensions:** history as JSON; model parameters; saved prompt presets; message streaming; latency measurements; structured output validation; Docker packaging.

**Explicitly out of scope:** public authentication, RAG/vector database, model training, internet-facing service.

Starter: [examples/chat_app.py](../examples/chat_app.py).

## B — Classical AI: Tetris placement advisor (optional)

**Why:** Show that algorithms and heuristic search are AI too, without a trained LLM.

**Data:** rectangular board grid (0/1 cells), piece orientations, legal placements. Game state is deterministic and testable.

**Milestones:**

1. Represent board as rows of booleans and draw as ASCII.
2. Compute legal placements of one piece; do not allow overlap or overflow.
3. Drop piece, clear filled rows.
4. Score a resulting board: completed lines, holes, aggregate column heights, bumpiness.
5. Enumerate all legal placements; choose the highest score (1-ply search).
6. Try a one-piece lookahead, compare scores with baseline.

**Verification:** known fixture boards, line-clear tests, forbidden moves rejected, deterministic tie-breaking; compare with random strategy over seeded sequences.

**Optional LLM:** use the model to *explain* why a move was preferred; evaluate its explanation against the true computed heuristic. Never let unvalidated natural-language output control the game state.

**Caution:** A general optimal Tetris solver is a much harder problem. The assignment is a placement advisor, not a guarantee of optimal play.

## Suggested demo rubric

| Category | Requirement |
| --- | --- |
| Understanding | Explains all key components without memorized phrases |
| Reproducibility | Another learner follows README to run it |
| Debuggability | Can intentionally break & fix one feature |
| Validation | Tests deterministic logic independently of LLM |
| Safety | Only local endpoints; sensitive data not committed |
| Reflection | Lists 2 limitations and next steps |
