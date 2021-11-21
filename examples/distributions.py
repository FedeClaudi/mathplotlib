import sys

sys.path.append("./")

from mathplotlib import show, distributions

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
betas = []
for a, b, color in zip(As, Bs, colors):
    betas.append(
        distributions.Beta(
            a, b, linecolor=color, linewidth=3, filled=False, outlined=True
        )
    )


# plot
show(
    *betas, axes_params=dict(xlim=[0, 1], ylim=[0, 3]), legend=True,
)
