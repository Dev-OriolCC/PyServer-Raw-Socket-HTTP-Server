# PyServe — Raw-Socket HTTP Server in Python

PyServe is an HTTP/1.1 server built from raw TCP sockets using **only the Python standard library**: no `http.server`, no frameworks, no third-party packages. It grows feature by feature through versioned milestones, and each feature teaches a real networking or HTTP concept.

> **Status:** v0.0 — Project setup. The package runs, but the HTTP server arrives in **v0.1 — Hello, socket**.

---

## Requirements

- **Python 3.12 or newer** (standard library only, so there is nothing to `pip install`)
- Git
- Optional tools for inspecting the server later: `curl`, `nc` (netcat), Wireshark

### Install Python 3.12

**Windows** (winget):

```powershell
winget install --id Python.Python.3.12 -e
py --list          # should show -V:3.12
```

Or download the installer from <https://www.python.org/downloads/>.

**macOS** (Homebrew):

```bash
brew install python@3.12
```

**Linux** (Debian/Ubuntu):

```bash
sudo apt install python3.12 python3.12-venv
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url> server-http
cd server-http
```

### 2. Create a virtual environment

PyServe has no dependencies. A virtual environment still helps because it makes `python` point to Python 3.12, even if another Python version comes first on your `PATH`.

**Windows (PowerShell):**

```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
```

> If PowerShell blocks the script, run once: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

**Windows (Git Bash):**

```bash
py -3.12 -m venv .venv
source .venv/Scripts/activate
```

**macOS / Linux:**

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

Check the version:

```bash
python --version   # Python 3.12.x
```

### 3. Run PyServe

From the project root:

```bash
python -m pyserve
python -m pyserve --version
python -m pyserve --help
```

Expected output:

```
PyServe 0.0.0: project setup complete. The HTTP server arrives in v0.1.
```

> **Without a virtual environment:** on Windows, `py -3.12 -m pyserve` works too.

### Coming in v0.1 and later

When the server is implemented, it will be started like this:

```bash
python -m pyserve --host 0.0.0.0 --port 8080 --root ./public
curl -v http://localhost:8080/
printf 'GET / HTTP/1.1\r\nHost: x\r\n\r\n' | nc localhost 8080
```

---

## Project Structure

```
pyserve/        # the server package (python -m pyserve)
public/         # demo static site served by PyServe
tests/          # unittest tests (unit + integration)
scripts/        # load tests, slowloris test, fuzzer
benchmarks/     # benchmark results
docs/           # design decisions, packet captures, devlog
```

---

## Roadmap

| Version | Milestone | Teaches |
|---|---|---|
| v0.0 | Project setup | Repo hygiene, CI |
| v0.1 | Hello, socket | Sockets, TCP streams, CRLF framing |
| v0.2 | Static file server | HTTP semantics, MIME types, path traversal |
| v0.3 | Concurrency & hardening | Thread pool, backpressure, timeouts |
| v0.4 | Keep-alive & performance | Connection reuse, pipelining, zero-copy |
| v0.5 | Observability | Access logs, metrics, config |
| v0.6 | Advanced HTTP | Caching, ranges, gzip |
| v0.7 | Routing, API & middleware | How frameworks work under the hood |
| v0.8 | Security & TLS | HTTPS, common web attacks |
| v1.0 | Deploy & polish | Docker, systemd, cloud deploy |

---

## Features

_Coming soon, starting with v0.1._

## Architecture

_Coming soon._

## Benchmarks

_Coming soon (v0.4)._

## Design Decisions

See [docs/decisions.md](docs/decisions.md).

## Known Limitations

- The HTTP server is not implemented yet (v0.0 setup only).

---

## License

[MIT](LICENSE)
