from math import pi

from warpdrive.sdf import sphere, translate, rotate, plot_sdf

if __name__ == "__main__":
    # Build a translated and rotated sphere
    expr = sphere(1.0)
    expr = translate(expr, (1.5, 0.0, 0.0))
    expr = rotate(expr, (0.0, 0.0, pi / 4))

    plot_sdf(expr, bbox=((-1, 3), (-2, 2), (-2, 2)), resolution=60) 