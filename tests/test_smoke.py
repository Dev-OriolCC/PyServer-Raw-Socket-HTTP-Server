"""Smoke tests: the package imports and the entry point runs.

Why: `python -m unittest` exits with code 5 when no tests run (Python 3.12+),
so CI needs at least one real test to go green on an otherwise empty project.
"""

import contextlib
import io
import unittest

import pyserve
from pyserve.__main__ import main


class SmokeTest(unittest.TestCase):
    """Minimal checks that the project is wired up correctly."""

    def test_package_has_version(self) -> None:
        self.assertIsInstance(pyserve.__version__, str)
        self.assertTrue(pyserve.__version__)

    def test_main_exits_cleanly(self) -> None:
        # Capture stdout so the startup message does not clutter test output.
        with contextlib.redirect_stdout(io.StringIO()):
            exit_code = main([])
        self.assertEqual(exit_code, 0)


if __name__ == "__main__":
    unittest.main()
