import pytest
import sympy as sp

# Skip if optional deps absent
matplotlib = pytest.importorskip("matplotlib")
pytest.importorskip("skimage")

# Use non-interactive backend to avoid window pop-ups
matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402  (after backend set)
from warpdrive.sdf import sphere, box, plot_sdf  # noqa: E402  (after backend set)


def test_plot_sdf_runs():
    """plot_sdf should execute without raising an exception."""
    expr = sphere(0.3)

    # single expression
    plot_sdf(expr, bbox=((-0.5, 0.5),) * 3, resolution=8)

    # list of two expressions with colors
    plot_sdf([expr, box((0.2, 0.2, 0.2))], bbox=((-0.6, 0.6),) * 3, resolution=8, color=["cyan", "magenta"])

    matplotlib.pyplot.close("all") 