import sys

sys.path.append("./")

from rich import print

from mathplotlib import Figure, distributions, functions

"""
    This example shows how to create a figure with multiple subplots
"""

# Create a figure with three subplots by specifying a layout
fig = Figure(
    """
    AAC
    BBC
"""
)
# fore more details: https://matplotlib.org/stable/tutorials/provisional/mosaic.html

# add elements to the differen subplots
fig.add_to(
    "A", distributions.Exp(),
)

# you can even add multiple things at the same time
fig.add_to(
    "B",
    functions.Function("exp(x)", style="minimal", xmax=2, xmin=-0.5),
    functions.Function(
        "exp(x*1.5)", style="minimal", xmax=2, xmin=-0.5, linewidth=2
    ),
    functions.Function(
        "exp(x*2)", style="minimal", xmax=2, xmin=-0.5, linewidth=3
    ),
)

fig.add_to("C", distributions.Normal())

# you can view a figure's contents
print("#" * 20, "         MY FIGURE", "#" * 20, sep="\n")
print(fig)

# and a single ax/Canvas
print("\n" * 2, "#" * 20, "         MY CANVAS", "#" * 20, sep="\n")
print(fig.canvases["B"])


# you can make legends/etc by atting on single canvases
fig.draw()  # create graphic elements before adding their legends
fig.canvases["B"].make_legend(ncol=3)

fig.show()
