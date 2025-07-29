"""Rounded box (box with beveled edges) signed-distance expression.

Implements the exact SDF given by Inigo Quilez (see YouTube derivation).
Formula translated from GLSL to SymPy.

Code reference (GLSL):

```
vec3 q = abs(p) - b + r;
return length(max(q,0.0)) + min(max(q.x,max(q.y,q.z)),0.0) - r;
```
"""

from __future__ import annotations

import sympy as sp

from .symbols import x, y, z

__all__ = ["round_box"]


def round_box(half_extents: tuple[float, float, float], radius: float):
    """Signed-distance to a rounded box centred at the origin.

    Args:
        half_extents: Tuple ``(hx, hy, hz)`` giving the half-size of the box.
        radius: Edge rounding radius ``r`` (> 0).

    Returns:
        sympy.Expr: Expression ``d(x, y, z)``.
    """

    hx, hy, hz = map(float, half_extents)
    r = float(radius)

    qx = sp.Abs(x) - hx + r
    qy = sp.Abs(y) - hy + r
    qz = sp.Abs(z) - hz + r

    outside = sp.sqrt(sp.Max(qx, 0) ** 2 + sp.Max(qy, 0) ** 2 + sp.Max(qz, 0) ** 2)
    inside = sp.Min(sp.Max(qx, sp.Max(qy, qz)), 0)
    return outside + inside - r 