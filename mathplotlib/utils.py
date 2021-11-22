import numpy as np
import math


def pi_2_pi(theta: float) -> float:
    while theta > math.pi:
        theta -= 2.0 * math.pi

    while theta < -math.pi:
        theta += 2.0 * math.pi

    return theta


def angle(x1: float, x2: float, y1: float, y2: float) -> float:
    """
        Given two XY points it returns the angle of the line
        connecting them
    """
    return np.degrees(np.arctan2(y2 - y1, x2 - x1))


def update_with_default(params: dict, default_params: dict) -> dict:
    """
        Fills in a dictionary of paramters with values
        from a dictionary of default parameters
    """
    for key in default_params:
        params[key] = params.pop(key, default_params[key])
    return params
