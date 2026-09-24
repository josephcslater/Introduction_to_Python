"""
Pytest configuration shared across the test/doctest session.

Force a non-interactive matplotlib backend before any module under test
(e.g. newton_raphson.py) imports pyplot, so doctest collection works
headlessly (in CI, or any environment without a display).
"""

import matplotlib

matplotlib.use("Agg")
