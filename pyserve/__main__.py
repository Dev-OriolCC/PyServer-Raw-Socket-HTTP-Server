"""Entry point for `python -m pyserve`.

The socket server arrives in v0.1; for now this only confirms the package runs
on a supported Python version.
"""

import argparse
import sys

from pyserve import __version__

# tomllib needs 3.11+; we standardise on 3.12 to match the Docker image planned for v1.0.
MIN_PYTHON = (3, 12)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        prog="pyserve",
        description="PyServe: a raw-socket HTTP/1.1 server (standard library only).",
    )
    parser.add_argument("--version", action="version", version=f"PyServe {__version__}")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    """Run PyServe and return a process exit code."""
    if sys.version_info < MIN_PYTHON:
        required = ".".join(map(str, MIN_PYTHON))
        print(f"PyServe requires Python {required}+, found {sys.version.split()[0]}.", file=sys.stderr)
        return 1

    parse_args(argv)
    print(f"PyServe {__version__}: project setup complete. The HTTP server arrives in v0.1.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
