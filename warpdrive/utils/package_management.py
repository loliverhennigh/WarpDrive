from __future__ import annotations

"""Utility helpers for optional runtime dependencies."""

import importlib

__all__ = ["require_package"]


def require_package(pkg: str):
    """Ensure *pkg* is importable; otherwise raise informative ImportError."""
    if importlib.util.find_spec(pkg) is None:
        raise ImportError(f"Optional dependency '{pkg}' is required. Install with 'pip install {pkg}'")
    return importlib.import_module(pkg) 