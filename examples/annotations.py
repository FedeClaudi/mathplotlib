import sys

sys.path.append("./")

from mathplotlib import show, functions, annotations

from myterial import blue_dark, pink_dark
from math import pi

"""
    This example shows how to draw some annotations on a plot.
"""

# draw two line
sine = functions.Function(
    "sin(x)",
    xmax=2 * pi,
    outlined=True,
    linecolor=blue_dark,
    facecolor=blue_dark,
    facealpha=0.2,
)
cosine = functions.Function(
    "cos(x) - 1", xmax=2 * pi, outlined=True, linecolor=pink_dark, filled=False
)

# draw some text
text = annotations.Text(
    1,
    0.2,
    "base text",
    horizontal_alignment="left",
    size=12,
    outlined=True,
    strokecolor="white",
)

# draw some text at a point along the sine and cosine curves
text_on_sine = annotations.Text.on_curve(
    sine,
    "sine",
    at=2,
    outlined=True,
    strokecolor="white",
    strokewidth=20,
    size=12,
)
text_on_cosine = annotations.Text.on_curve(
    cosine,
    "cosine",
    at=2,
    outlined=True,
    strokecolor="white",
    strokewidth=20,
    size=12,
)


# draw some annotations
annot = annotations.Annotation(pi, 0, "zero point", x_shift=0.25, y_shift=+0.5)

annot_at_point = annotations.Annotation.at_curve(
    cosine, "A point on the cosine", at=3, y_shift=-0.5, size="large"
)


show(sine, cosine, text, text_on_sine, text_on_cosine, annot, annot_at_point)
