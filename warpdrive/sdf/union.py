"""SDF set operation: union (logical OR).

Given two signed-distance expressions *d1* and *d2*, the union is
    ``min(d1, d2)``.
This preserves the convention: negative ⇒ inside, 0 ⇒ surface, positive ⇒ outside.
"""

from __future__ import annotations

import sympy as sp

__all__ = ["union"]


def union(d1: sp.Expr, d2: sp.Expr) -> sp.Expr:  # noqa: D401
    """Return the union of two distance fields.

    Args:
        d1: First SDF expression.
        d2: Second SDF expression.
    """

    return sp.Min(d1, d2) 