import numpy as np
import matplotlib.pyplot as plt
from typing import Callable, Union
from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.sympy_parser import (
    function_exponentiation,
    standard_transformations,
    implicit_application,
    implicit_multiplication_application,
    convert_equals_signs,
)
from sympy.utilities.lambdify import lambdify

import mathplotlib as mhplt


def parse(expr: str) -> Callable:
    """ 
        Parses a string with a mathematical expression returning a python function that computes it.
    """
    transformations = standard_transformations + (
        function_exponentiation,
        implicit_multiplication_application,
        implicit_application,
        convert_equals_signs,
    )

    expression = parse_expr(
        expr, transformations=transformations, evaluate=True
    )

    if len(expression.free_symbols) > 1:
        raise ValueError(
            "Found mathematical function of more than one argument."
        )

    return lambdify(*expression.free_symbols, expression)


class Function(mhplt.base.Curve2D):
    def __init__(
        self,
        func: Union[Callable, str],
        xmin: float = 0,
        xmax: float = 1,
        nolegend: bool = False,
        n_draw_points: int = 200,
        **kwargs,
    ):
        """
            Plots a function (of one variable). The function can either
            be a python callable (function) that accepts a single float variable and outputs a single
            float variable, or a string with a mathematical expression in one variable (which is 
            converted to a function)
        """
        name = func if isinstance(func, str) else func.__name__
        super().__init__(name, nolegend=nolegend)

        self.y_func = parse(func) if isinstance(func, str) else func
        self.xmin = xmin
        self.xmax = xmax
        self.style = mhplt.style.Style(**kwargs)
        self.n_draw_points = n_draw_points

    def __repr__(self) -> str:
        return f'Function with function: "{self.name}" - style "{self.style.style_name}"'

    def draw(self, ax: plt.Axes):
        """
            Applies the mathematical function to a set of points
            and draws the resulting curve
        """
        x = np.linspace(self.xmin, self.xmax, self.n_draw_points)
        y = [self.y_func(x_t) for x_t in x]
        self._draw_curve(x, y, ax)
