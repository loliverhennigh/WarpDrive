from __future__ import annotations

"""Marching-cubes helper for SymPy-defined signed-distance fields."""

from typing import Tuple
from warpdrive.utils.package_management import require_package

import numpy as np
import sympy as sp

from .symbols import x, y, z

__all__ = ["sdf_to_mesh"]


def sdf_to_mesh(
    expr: sp.Expr,
    bbox: Tuple[Tuple[float, float], Tuple[float, float], Tuple[float, float]],
    resolution: int,
    *,
    isolevel: float = 0.0,
):
    """Sample *expr* on a regular grid, run marching-cubes and return verts/faces."""

    measure = require_package("skimage").measure
    func = sp.lambdify((x, y, z), expr, modules="numpy")

    (xmin, xmax), (ymin, ymax), (zmin, zmax) = bbox
    xs = np.linspace(xmin, xmax, resolution)
    ys = np.linspace(ymin, ymax, resolution)
    zs = np.linspace(zmin, zmax, resolution)
    X, Y, Z = np.meshgrid(xs, ys, zs, indexing="ij")
    values = func(X, Y, Z)

    vmin, vmax = float(values.min()), float(values.max())
    if not (vmin <= isolevel <= vmax):
        raise ValueError(
            "Iso-level not within sampled value range. "
            "Try enlarging `bbox` or increasing `resolution`. "
            f"Range=({vmin:.3g},{vmax:.3g}), isolevel={isolevel}"
        )

    spacing = (
        (xmax - xmin) / (resolution - 1),
        (ymax - ymin) / (resolution - 1),
        (zmax - zmin) / (resolution - 1),
    )
    verts, faces, *_ = measure.marching_cubes(values, level=isolevel, spacing=spacing)
    verts += np.array([xmin, ymin, zmin])
    return verts, faces 