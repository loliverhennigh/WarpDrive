import sympy as sp

from warpdrive.sdf import box


def test_box_inside():
    expr = box((1.0, 1.0, 1.0))
    val = expr.subs({sp.Symbol("x"): 0, sp.Symbol("y"): 0, sp.Symbol("z"): 0})
    assert val == sp.Float(-1)


def test_box_surface():
    expr = box((1.0, 1.0, 1.0))
    val = expr.subs({sp.Symbol("x"): 1.0, sp.Symbol("y"): 0, sp.Symbol("z"): 0})
    assert val == 0


def test_box_outside():
    expr = box((1.0, 1.0, 1.0))
    val = expr.subs({sp.Symbol("x"): 2.0, sp.Symbol("y"): 0, sp.Symbol("z"): 0})
    assert val == sp.Float(1) 