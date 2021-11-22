import sys

sys.path.append("./")

from mathplotlib import show, functions, annotations

from myterial import blue_dark, pink_dark
from math import pi

"""
    This example shows how to draw some annotations on a plot.
"""

# draw two lines
sine = functions.Function(
    "sin(x)",
    xmax=2 * pi,
    outlined=True,
    linecolor=blue_dark,
    facecolor=blue_dark,
    facealpha=0.2,
).annotate(
    at=1
)  # the annotate method draws the function over the plotted line

cosine = functions.Function(
    "cos(x) - 1", xmax=2 * pi, outlined=True, linecolor=pink_dark, filled=False
).annotate(at=1, backgroundcolor="w")

# add some text
text = annotations.Text(
    1,
    0.2,
    "shaded area",
    horizontal_alignment="left",
    size=12,
    outlined=True,
    strokecolor="white",
)

# draw some annotations arrows pointing at two different points.
annot = annotations.Annotation(
    pi,
    0,
    "zero points",
    x_shift=0.25,
    y_shift=+0.5,
    additional_points=[(6.28, 0)],  # coordinates of additional points
)

# draw an annotation arrow pointing at the cosine curve
annot_at_point = annotations.Annotation.at_curve(
    cosine, "A point on the cosine", at=3, y_shift=-0.5, size="large"
)


show(
    sine, cosine, text, annot, annot_at_point, axes_equal=True,
)
