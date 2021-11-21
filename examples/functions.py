import sys

sys.path.append("./")

from mathplotlib import show, functions

from myterial import blue_dark
from math import sin, pi

"""
    This example shows how to draw basic mathematical functions.

    Functions can be passed as string expressions or as python functions
"""


show(
    functions.Function(sin, xmax=2 * pi),
    functions.Function(  # dotted interval
        "2sin(x)",
        xmin=0,
        xmax=1,
        style="minimal",
        linestyle=":",
        linewidth=3,
        nolegend=True,
    ),
    functions.Function(  # solid interval
        "2sin(x)",
        xmin=1,
        xmax=2 * pi - 1,
        style="minimal",
        linewidth=3,
        linecolor=blue_dark,
        outlined=True,
    ),
    functions.Function(  # dotted interval
        "2sin(x)",
        xmin=2 * pi - 1,
        xmax=2 * pi,
        style="minimal",
        linestyle=":",
        linewidth=3,
        nolegend=True,
    ),
    axes_params=dict(xlabel="Angle", ylabel="Value"),
    legend=True,
)
