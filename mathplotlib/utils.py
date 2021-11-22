import numpy as np


def angle(x1: float, x2: float, y1: float, y2: float) -> float:
    """
        Given two XY points it returns the angle of the line
        connecting them
    """
    return np.degrees(np.arctan2(y2 - y1, x2 - x1))
