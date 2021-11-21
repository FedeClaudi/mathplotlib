import sys

sys.path.append("./")

from mathplotlib import show, shapes

from myterial import blue_dark

"""
    This example shows how to draw basic shapes
"""

show(shapes.Circle(1, 1, r=0.5, facecolor=blue_dark))
