# Session 08 — Enough Docker to be dangerous

**Time:** 2–3 hours, optional. **Output:** a reproducible containerized frontend.

## Read

[Docker Python language guide](https://docs.docker.com/guides/python/). Focus on image vs. container, Dockerfile, build context, ports, environment variables and volumes. Leave Kubernetes, public deployments and registries out.

## Exercise

From the repository root:

```sh
docker build -t py-ai-studyplan-ui ./examples
# On macOS, install Docker Desktop; Ollama stays on the host.
docker compose -f examples/compose.yaml up --build
```

The Compose file uses `host.docker.internal` as an explicit route to host-running Ollama. Docker Desktop on macOS generally provides this hostname; on Linux a host-gateway mapping is configured. **The Ollama service still needs to listen on an address reachable from the container.** This is platform- and firewall-dependent and must not be solved by opening an unauthenticated API to an untrusted network. The safer first Docker checkpoint is simply seeing the UI load while it gracefully reports Ollama unreachable.

## What to be able to explain

- The image packages the app, the container is a running instance.
- `-p 127.0.0.1:8501:8501` controls UI publication to the host.
- `OLLAMA_HOST` in the Streamlit client's environment selects the Ollama endpoint; it doesn't start the runtime.
- Bind mounts and named volumes are different ways to persist state.
- Rebuilding a container is not the same as re-pulling model weights.

## Checkpoint

Build, run, inspect logs, stop, and explain a connection-refused result without exposing the local model API publicly.
