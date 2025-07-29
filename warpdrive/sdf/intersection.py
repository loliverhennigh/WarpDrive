"""SDF set operation: intersection (logical AND).

Distance is ``max(d1, d2)``.
"""

from __future__ import annotations

import sympy as sp

__all__ = ["intersection"]


def intersection(d1: sp.Expr, d2: sp.Expr) -> sp.Expr:
    """Return intersection distance field.

    Args:
        d1: First SDF expression.
        d2: Second SDF expression.
    """

    return sp.Max(d1, d2) 