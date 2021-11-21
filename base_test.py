import numpy as np
from mathplotlib import Figure, shapes, distributions, functions
from rich import print

fig = Figure(
    """
    AAA
    BBB
"""
)


# add circles
fig.add_to(
    "A",
    shapes.Circle(0.5, 0.5, r=0.25),
    shapes.Circle(0.2, 0.2, r=0.25, style="minimal", linecolor="red"),
)

# add distribution
fig.add_to("A", distributions.Normal(1, 0.2))

# add a curve


def mysin(x: float) -> float:
    return np.sin(2 * x)


fig.add_to(
    "B",
    functions.Function(np.sin, xmin=0, xmax=2 * np.pi),
    functions.Function(
        mysin, xmin=0, xmax=3 * np.pi, linecolor="red", facealpha=0.2
    ),
    functions.Function(
        "- sin(2x)", xmin=0, xmax=2 * np.pi, facecolor="g", linecolor="g"
    ),
)

print(fig)


fig.show()
