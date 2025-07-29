from __future__ import annotations

"""Circular RLC circuit geometry built with warpdrive SDF utilities.

This is a **minimal**/illustrative re-implementation of the legacy
`CircularRLC` generator using only the light-weight functionality that
exists in this repository (`warpdrive.sdf` and `warpdrive.geometry`).

The goal is to demonstrate how one could compose a relatively complex
parametric shape from the primitive SDFs and boolean operations provided
in `warpdrive.sdf`, and bundle the resulting symbolic fields into the
`Geometry` container so they can be consumed by a voxeliser / solver.

Design notes
------------
*   Materials:  We keep the data structure simple – here a *material* is
    merely a dict of constitutive parameters (permittivity, etc.).  You
    can replace this with your own richer class later.
*   Electromagnetic parameters (ε, μ, σ, initial **E/B**) are collected
    into lists of ``(value, sdf_expr)`` as expected by
    `warpdrive.geometry.Geometry`.
*   All rotations are performed with the `rotate` helper.  Translation is
    done via `translate` for clarity even when a primitive’s *center*
    parameter could do the same.
*   Compared to the legacy generator we omit the time-dependent switch
    conductivity to keep the example self-contained.  You can still add
    such behaviour by making `σ` a callable instead of a scalar.
"""

# pylint: disable=relative-beyond-top-level
from typing import List, Tuple

from math import pi
import sympy as sp

from warpdrive.geometry import Geometry  # sibling package
from warpdrive.material.material import VACUUM, COPPER, QUARTZ
from warpdrive.sdf import (
    box,
    cylinder,
    difference,
    union,
    translate,
    rotate,
)

class CircularRLC(Geometry):
    """Factory that builds a `Geometry` object representing the circuit."""

    def __init__(
        self,
        coil_radius: float = 1e-3,
        cable_thickness_r: float = 1e-4,
        cable_thickness_y: float = 1e-4,
        insulator_thickness: float = 5e-5,
        dielectric_thickness: float = 5e-5,
    ) -> Geometry:
        """Return assembled `Geometry`."""

        # Build components
        conductor = CircularRLC._sdf_conductor(
            coil_radius,
            cable_thickness_r,
            cable_thickness_y,
            insulator_thickness,
            dielectric_thickness,
        )
        resistor = CircularRLC._sdf_resistor(coil_radius, cable_thickness_r, cable_thickness_y)
        dielectric = CircularRLC._sdf_dielectric(coil_radius, cable_thickness_r, cable_thickness_y, dielectric_thickness)
        insulator = CircularRLC._sdf_insulator(coil_radius, cable_thickness_r, cable_thickness_y, insulator_thickness)
        switch_top, switch_bot = CircularRLC._sdf_switches(
            coil_radius, cable_thickness_r, cable_thickness_y, insulator_thickness
        )

        # ------------------------------------------------------------------
        # Assemble Geometry (new API expects solids dict)
        # ------------------------------------------------------------------

        # Combine copper parts
        copper_expr = union(conductor, union(resistor, union(switch_top, switch_bot)))
        dielectric_expr = dielectric
        insulator_expr = insulator

        solids = {
            COPPER: conductor,
            QUARTZ: switch_top,
        }

        #solids: dict[Material, sp.Expr] = {
        #    COPPER: copper_expr,
        #    QUARTZ: union(dielectric_expr, insulator_expr),
        #}

        super().__init__(solids)

    # ------------------------------------------------------------------
    # Static helpers creating individual component SDFs
    # ------------------------------------------------------------------

    @staticmethod
    def _sdf_conductor(R: float, t_r: float, t_y: float, ins_t: float, diel_t: float) -> sp.Expr:
        outer = rotate(cylinder(radius=R + t_r, height=t_y / 2), (pi / 2, 0.0, 0.0))
        inner = rotate(cylinder(radius=R, height=t_y / 2), (pi / 2, 0.0, 0.0))
        ring = difference(outer, inner)

        # stubs
        stub_res = translate(box((2 * t_r, t_y / 2, t_r + 0.5 * ins_t)), (R + 2 * t_r, 0, 0))
        stub_cap = translate(box((1.5 * t_r, t_y / 2, 2 * t_r + 0.5 * ins_t + 0.5 * diel_t)), (R + 5.5 * t_r, 0, 0))
        ring = union(ring, union(stub_res, stub_cap))

        # cut-outs
        cut_res = translate(box((3 * t_r, t_y / 2, 0.5 * ins_t)), (R + 2.5 * t_r, 0, 0))
        cut_sw = translate(box((0.5 * t_r, t_y / 2, 1.5 * t_r + 0.5 * ins_t)), (R + 5.5 * t_r, 0, 0))
        cut_cap = translate(box((0.5 * t_r, t_y / 2, 0.5 * diel_t)), (R + 6.5 * t_r, 0, 0))
        ring = difference(difference(difference(ring, cut_res), cut_sw), cut_cap)

        # Cut out resistor, top and bottom switch
        resistor = CircularRLC._sdf_resistor(R, t_r, t_y)
        top_switch, bot_switch = CircularRLC._sdf_switches(R, t_r, t_y, ins_t)

        return difference(difference(difference(ring, resistor), top_switch), bot_switch)

    @staticmethod
    def _sdf_resistor(R: float, t_r: float, t_y: float) -> sp.Expr:
        return translate(box((0.5 * t_r, t_y / 2, 0.5 * t_r)), (R + 2.5 * t_r, 0, 0))

    @staticmethod
    def _sdf_dielectric(R: float, t_r: float, t_y: float, diel_t: float) -> sp.Expr:
        return translate(box((0.5 * t_r, t_y / 2, diel_t / 2)), (R + 6.5 * t_r, 0, 0))

    @staticmethod
    def _sdf_insulator(R: float, t_r: float, t_y: float, ins_t: float) -> sp.Expr:
        return translate(box((1.0 * t_r, t_y / 2, ins_t / 2)), (R + 1.0 * t_r, 0, 0))

    @staticmethod
    def _sdf_switches(R: float, t_r: float, t_y: float, ins_t: float) -> Tuple[sp.Expr, sp.Expr]:
        base = translate(box((0.5 * t_r, t_y / 2, 0.5 * t_r)), (R + 3.5 * t_r, 0, 0))
        top = translate(base, (0, 0, 0.5 * ins_t + 0.5 * t_r))
        bot = translate(base, (0, 0, -(0.5 * ins_t + 0.5 * t_r)))
        return top, bot 
        
