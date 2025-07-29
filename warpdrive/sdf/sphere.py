"""Sphere signed-distance function utility."""

from __future__ import annotations

import sympy as sp

from .symbols import x, y, z

__all__ = ["sphere"]

def sphere(
    radius: float,
    center: tuple[float, float, float] = (0.0, 0.0, 0.0),
):
    """Return signed-distance function for a sphere.

    Parameters
    ----------
    radius
        Sphere radius (> 0).
    center
        Center of the sphere.
    """

    cx, cy, cz = map(float, center)
    return sp.sqrt((x - cx) ** 2 + (y - cy) ** 2 + (z - cz) ** 2) - float(radius)