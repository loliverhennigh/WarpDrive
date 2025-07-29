"""Utility to translate a signed-distance expression.

For an original distance field *d(x, y, z)* and an offset *(ox, oy, oz)*,
translation is performed by evaluating the original at shifted coordinates:

.. math::
    d'(x, y, z) = d(x - o_x,\; y - o_y,\; z - o_z).

This keeps the analytical form symbolic and exact.
"""

from __future__ import annotations

import sympy as sp

from .symbols import x, y, z

__all__ = ["translate"]


def translate(expr: sp.Expr, offset: tuple[float, float, float]):
    """Translate a distance expression by the given offset.

    Args:
        expr: SymPy expression ``d(x, y, z)``.
        offset: Tuple ``(ox, oy, oz)`` – positive values move the shape in
            the +x/+y/+z directions.

    Returns:
        sympy.Expr: Translated distance expression.
    """

    ox, oy, oz = offset
    subs_map = {
        x: x - float(ox),
        y: y - float(oy),
        z: z - float(oz),
    }
    return expr.xreplace(subs_map) 