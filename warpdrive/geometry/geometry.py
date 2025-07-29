from __future__ import annotations
from typing import Dict

import sympy

from warpdrive.material.material import Material
from warpdrive.sdf.union import union


class Geometry:

    def __init__(
        self,
        solids: Dict[Material, sympy.Expr],
    ):
        self.solids = solids

    def __add__(self, other: 'Geometry') -> 'Geometry':
        solids = {**self.solids}

        for material, expr in other.solids.items():
            if material in solids:
                solids[material] = union(solids[material], expr)
            else:
                solids[material] = expr

        return Geometry(
            solids=solids,
        )
    
    def plot(
        self,
        *,
        bbox=((-1, 1), (-1, 1), (-1, 1)),
        resolution: int = 50,
        isolevel: float = 0.0,
        color_by_material: bool = True,
    ) -> None:
        """Render the geometry with `plot_sdf`.

        Parameters
        ----------
        color_by_material
            If *True* use the RGBA colour stored in each `Material`.  Otherwise a
            default colour is used for all solids.
        """

        try:
            from warpdrive.sdf import plot_sdf  # runtime import keeps heavy deps optional
        except ImportError as exc:  # pragma: no cover
            raise RuntimeError("plot_sdf optional dependencies missing") from exc

        if not self.solids:
            raise ValueError("No solids defined in geometry.")

        exprs = list(self.solids.values())

        if color_by_material:
            def _rgba_to_mpl(rgba):
                r, g, b, a = rgba
                return (r / 255, g / 255, b / 255, a / 255)

            colors = [_rgba_to_mpl(mat.color) for mat in self.solids.keys()]
        else:
            colors = "cyan"

        plot_sdf(exprs, bbox=bbox, resolution=resolution, isolevel=isolevel, color=colors)
    
