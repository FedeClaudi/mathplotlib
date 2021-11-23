import sys

sys.path.append("./")


from mathplotlib import Figure
from mathplotlib.shapes import Grid

from myterial import blue

"""
    This example shows how to create a figure with multiple subplots
"""

# Create a figure with three subplots by specifying a layout
fig = Figure(
    """
    AB
    CD
""",
    figsize=(12, 12),
    axes_equal=True,
)

# create grids spanning different ranges and with different paramters
fig.add_to("A", Grid(-10, 10, -10, 10, minor_kwargs=dict(linestyle=":")))

# don't draw minor lines
fig.add_to(
    "C",
    Grid(
        -100,
        100,
        -100,
        100,
        major_every=20,
        minor_every=None,
        major_kwargs=dict(linecolor=blue),
    ),
)


fig.show()
