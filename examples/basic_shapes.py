import sys

sys.path.append("./")

from mathplotlib import show, shapes


"""
    This example shows how to draw basic shapes
"""

fig = show(
    shapes.Circle(1, 1, r=0.5, facecolor="white", linewidth=4),
    shapes.Line().annotate(at=3),
    shapes.Line(slope=2.5, intercept=+2).annotate(),
    shapes.Line(slope=-0.4, intercept=-1.9).annotate(at=2),
    axes_equal=True,
)

print(fig.canvases["A"])
