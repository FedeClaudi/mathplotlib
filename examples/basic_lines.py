import sys

sys.path.append("./")

from mathplotlib import show
from mathplotlib.shapes import Line

from myterial import blue, green_dark

"""
    This example shows how to draw lines using various methods
"""

fig = show(
    # crate two angled lines
    Line(slope=3, intercept=-2, linecolor=green_dark).annotate(at=1.5),
    Line(slope=-1, intercept=2, linecolor=green_dark).annotate(at=3),
    # create lines defined by two points
    Line.between_points((2, 4.5), (3, 4.5), linecolor=blue).annotate(
        at=5, text="horizontal"
    ),
    Line.between_points((-1.5, 1), (-1.5, -2), linecolor=blue).annotate(
        at=-1.5, text="vertical"
    ),
    # create vertical/horizontal lines directly
    Line.vertical(-1, linewidth=0.5, linestyle="--", linecolor="k"),
    Line.vertical(-2, linewidth=0.5, linestyle="--", linecolor="k"),
    Line.horizontal(4, linewidth=0.5, linestyle="--", linecolor="k"),
    Line.horizontal(5, linewidth=0.5, linestyle="--", linecolor="k"),
    axes_equal=True,
    axes_params=dict(xlim=[-4, 6], ylim=[-4, 7]),
)

print(fig.canvases["A"])
