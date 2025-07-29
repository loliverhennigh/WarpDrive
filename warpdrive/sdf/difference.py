from __future__ import annotations

"""Alias for `subtraction` (A \ B)."""

import sympy as sp

from .subtraction import subtraction

__all__ = ["difference"]

def difference(d1: sp.Expr, d2: sp.Expr) -> sp.Expr:  # noqa: D401
    """Return A\B distance field (alias for subtraction)."""
    return subtraction(d1, d2) 