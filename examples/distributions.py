import sys

sys.path.append("./")

from mathplotlib import show, distributions
from mathplotlib.annotations import Text

from myterial import blue_dark, pink
from myterial.utils import make_palette

"""
    This example shows how to draw basic distributions by plotting
    Beta functions with different parameters
"""

# generate function
colors = make_palette(blue_dark, pink, 5)
As = [0.5, 5, 1, 2, 2]
Bs = [0.5, 1, 3, 2, 5]
Xs = [0.3, 0.15, 0.2, 0.25, 0.3]
artists = []
for a, b, color, x in zip(As, Bs, colors, Xs):

    beta = distributions.Beta(
        a, b, linecolor=color, linewidth=3, filled=False, outlined=True
    )
    annotation = Text.on_curve(beta, f"a: {a} b: {b}", at=x)

    artists.extend([beta, annotation])


# plot
show(
    *artists,
    axes_params=dict(xlim=[0, 1], ylim=[0, 3]),
    legend=True,
    legend_kwargs=dict(loc="best", ncol=3),
)
