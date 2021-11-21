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

from mathplotlib.base import BaseElement
from mathplotlib.style import Style


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


class Function(BaseElement):
    def __init__(
        self,
        func: Union[Callable, str],
        xmin: float = 0,
        xmax: float = 1,
        nolegend: bool = False,
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

        self.func = parse(func) if isinstance(func, str) else func
        self.xmin = xmin
        self.xmax = xmax
        self.style = Style(**kwargs)

    def __repr__(self) -> str:
        return f'Function with function: {self.func.__name__} - style "{self.style.style_name}"'

    def draw(self, ax: plt.Axes):
        """
            Applies the mathematical function to a set of points
            and draws the resulting curve
        """
        x = np.linspace(self.xmin, self.xmax, 200)
        y = [self.func(x_t) for x_t in x]
        self._draw_curve(x, y, ax)
