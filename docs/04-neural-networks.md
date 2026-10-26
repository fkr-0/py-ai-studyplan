# 04 — How networks learn

**Time:** 2 h. **Milestone:** explain a loss function, gradients, backpropagation and the train/test distinction without requiring calculus.

## Watch & experiment

1. [3Blue1Brown: Gradient descent](https://www.youtube.com/watch?v=IHZwWFHWa-w) (~21 min).
2. [3Blue1Brown: Backpropagation, intuitively](https://www.youtube.com/watch?v=Ilg3gGewQ5U) (~14 min).
3. [TensorFlow Playground](https://playground.tensorflow.org/): change hidden layers, noise, activation and learning rate; note which settings lead to over/under-fitting.
4. [3Blue1Brown: Transformers](https://www.youtube.com/watch?v=wjZofJX0v4M) (~27 min), followed by optional [Transformer Explainer](https://poloclub.github.io/transformer-explainer/).

## Minimal conceptual vocabulary

- Neuron: applies weights, bias and an activation.
- Loss: numerical measure of prediction error on examples.
- Gradient: directions of local sensitivity of loss to weights.
- Backpropagation: efficient computation of gradients through a chain of operations.
- Optimizer: chooses parameter updates, often via gradient descent.
- Generalization: performance on examples not seen during training.

## Mini experiments

- Playground: try 1 hidden neuron vs 8; record validation error and what visually changes.
- Increase learning rate until training becomes unstable.
- In Transformer Explainer, type a partial sentence and inspect possible next tokens. Change sampling temperature. Compare with the weight-changing training process.

## Questions

- Is backpropagation the same as gradient descent? (No: gradients vs parameter updates.)
- Does increasing model temperature retrain it? (No.)
- Is training accuracy alone evidence of generalization? (No.)
- Why can two models with similar architecture produce different answers? (Training data, parameters, sampling, prompts, and settings.)

## Optional deeper study

- [Karpathy: Deep Dive into LLMs](https://www.youtube.com/watch?v=7xTGNNLPyMI) — advanced long-form overview.
- [3Blue1Brown illustrated backprop lesson](https://www.3blue1brown.com/lessons/backpropagation/).

[Next: local inference](05-local-llms.md)
