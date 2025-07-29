import sympy as sp

from warpdrive.sdf import cylinder


def test_cylinder_infinite_origin():
    """Infinite cylinder of radius 1: at origin distance should be -1."""
    expr = cylinder(1.0)
    val = expr.subs({sp.Symbol("x"): 0, sp.Symbol("y"): 0, sp.Symbol("z"): 10})
    assert val == sp.Float(-1)


def test_cylinder_finite_surface():
    """Finite cylinder radius 1 height 2: point on side surface at mid-height returns 0."""
    expr = cylinder(1.0, height=2.0)
    val = expr.subs({sp.Symbol("x"): 1.0, sp.Symbol("y"): 0, sp.Symbol("z"): 0})
    assert val == 0


def test_cylinder_top_cap():
    expr = cylinder(0.5, height=2.0)
    val = expr.subs({sp.Symbol("x"): 0, sp.Symbol("y"): 0, sp.Symbol("z"): 1.0})
    assert val == 0 