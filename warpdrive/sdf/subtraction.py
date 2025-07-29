"""SDF set operation: subtraction (A \ B).

Given two SDFs *d1* (A) and *d2* (B), subtraction is implemented as
    ``max(-d1, d2)`` according to IQ’s conventions.
"""

from __future__ import annotations

import sympy as sp

__all__ = ["subtraction"]


def subtraction(d1: sp.Expr, d2: sp.Expr) -> sp.Expr:
    """Return the difference distance field *A \ B*.

    Args:
        d1: SDF of the solid to keep (A).
        d2: SDF of the solid to subtract (B).
    """

    return sp.Max(d1, -d2) 