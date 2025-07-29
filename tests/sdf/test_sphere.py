import sympy as sp

from warpdrive.sdf import sphere


def test_sphere_origin():
    """Value at center should be negative radius."""
    expr = sphere(1.0)
    val = expr.subs({sp.Symbol("x"): 0, sp.Symbol("y"): 0, sp.Symbol("z"): 0})
    assert val == sp.Float(-1)

def test_sphere_surface():
    expr = sphere(2.5)
    val = expr.subs({sp.Symbol("x"): 2.5, sp.Symbol("y"): 0, sp.Symbol("z"): 0})
    assert val == 0 