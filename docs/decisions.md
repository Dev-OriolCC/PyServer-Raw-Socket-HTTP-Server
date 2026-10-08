# Design Decisions

One entry per trade-off. Newest at the bottom.

## Python 3.12 as the minimum version  (v0.0)
Context: PyServe uses only the standard library. `tomllib` (config, v0.5) needs Python 3.11+, and the v1.0 Docker image is planned on `python:3.12-slim`.
Decision: Require Python 3.12+. `python -m pyserve` exits with a clear error on older interpreters.
Alternatives considered: 3.11 (minimum for `tomllib`, but would diverge from the Docker image); the newest release (fewer machines and CI images have it preinstalled).
Consequences: Local development, CI and Docker all run the same minor version, so "works on my machine" bugs from version drift are avoided. Modern syntax such as `list[str] | None` is available.
