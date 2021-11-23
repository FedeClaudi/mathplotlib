import sys

sys.path.append("./")

from numpy import pi

from myterial import (
    blue,
    blue_lighter,
    grey_dark,
    white,
    black,
    grey,
)
from myterial.utils import make_palette

from mathplotlib.shapes import Grid, Line
from mathplotlib.functions import Function
from mathplotlib import show
from mathplotlib.annotations import Text, Annotation
import mathplotlib as mhp

# make shaded sines
N_sines = 15
sines_colors = make_palette(blue, blue_lighter, N_sines)
sines = []
for n in range(N_sines):
    scale = (N_sines - n) / N_sines
    scale_trunc = max(scale, 0.4)
    sines.append(
        Function(
            f"{scale} * sin(.75*{n/N_sines+1}*x)",
            xmin=-4 * pi,
            xmax=4 * pi,
            alpha=max(scale, 0.8),
            linecolor=sines_colors[n],
            filled=False,
            linewidth=7 * scale_trunc,
            outlined=n == 0,
            strokewidth=0.5,
            zorder=N_sines - n,
        ),
    )


# add lines with version  details
lines = [
    Line(
        0.5,
        9,
        linewidth=6,
        linecolor=grey_dark,
        outlined=True,
        strokecolor=white,
    ).annotate(at=-4, text="MATHPLOTLIB"),
    Line(
        0.5,
        8.4,
        linewidth=6,
        linecolor=grey_dark,
        outlined=True,
        strokecolor=white,
    ).annotate(
        at=-3.7,
        text=f"v. {mhp.__version__} - {mhp.__date__}",
        backgroundcolor="white",
    ),
]

# add text and annotations
annotations = [
    Text(
        4,
        6,
        "MathPlotLib",
        outlined=True,
        strokecolor=black,
        strokewidth=4.5,
        size=50,
    ),
    Text(
        4,
        6,
        "MathPlotLib",
        outlined=True,
        strokecolor=white,
        strokewidth=4,
        size=50,
    ),
    Text(
        4.2,
        5.4,
        "    draw maths... easily",
        outlined=True,
        strokecolor=white,
        size=25,
        textcolor=grey_dark,
    ),
    Annotation(
        4,
        5,
        "with annotations!",
        size=20,
        x_shift=-3,
        y_shift=-2,
        textcolor=grey_dark,
        outlined=True,
        strokewidth=3,
        strokecolor=white,
        arrow_params=dict(
            connectionstyle="arc3,rad=0.35", lw=4, fc=grey, ec=grey
        ),
        additional_points=[(2, 1)],
    ),
]

show(
    Grid(
        -3,
        7,
        -3,
        7,
        major_linewidth=0.5,
        minor_every=None,
        major_kwargs=dict(alpha=0.4),
    ),
    *sines,
    *lines,
    *annotations,
    axes_equal=True,
    axes_params=dict(xlim=[-3, 2 * pi], ylim=[-3, 8]),
)
