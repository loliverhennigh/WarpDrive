import sympy as sp

from warpdrive.sdf import box_frame


def test_box_frame_surface_x():
    expr = box_frame((1.0, 1.0, 1.0), thickness=0.1)
    val = expr.subs({sp.Symbol("x"): 1.0, sp.Symbol("y"): 0.95, sp.Symbol("z"): 0})
    assert abs(float(val)) < 1e-12


def test_box_frame_corner_outside():
    expr = box_frame((1.0, 1.0, 1.0), thickness=0.1)
    val = expr.subs({sp.Symbol("x"): 2.0, sp.Symbol("y"): 0, sp.Symbol("z"): 0})
    assert val > 0 