import sympy as sp

from warpdrive.sdf import round_box


def test_round_box_center():
    expr = round_box((1.0, 1.0, 1.0), radius=0.2)
    val = expr.subs({sp.Symbol("x"): 0, sp.Symbol("y"): 0, sp.Symbol("z"): 0})
    # At center, distance should be -1 (half-extent plus rounding)
    assert val == sp.Float(-1)


def test_round_box_surface():
    expr = round_box((1.0, 1.0, 1.0), radius=0.2)
    val = expr.subs({sp.Symbol("x"): 1.0, sp.Symbol("y"): 0, sp.Symbol("z"): 0})
    # Allow small symbolic floating error
    assert abs(float(val)) < 1e-12 