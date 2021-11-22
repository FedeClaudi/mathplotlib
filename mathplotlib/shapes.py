import matplotlib.pyplot as plt
from typing import Tuple
import numpy as np

from mathplotlib.base import BaseElement, Curve2D
from mathplotlib.style import Style


class Line(Curve2D):
    def __init__(
        self,
        slope: float = 1,
        intercept: float = 0,
        nolegend: bool = False,
        **kwargs,
    ):
        super().__init__("Line", nolegend=nolegend)
        self.slope = slope
        self.intercept = intercept

    def __repr__(self) -> str:
        return f"Line with slope {self.slope:.2f}, intercept: {self.intercept:.2f}"

    @property
    def legend(self) -> str:
        return f"y = {self.slope:.1f}x + {self.intercept:.1f}"

    def angle_at_point(self, at: float = 1) -> float:
        return np.degrees(np.arctan(self.slope))

    def y_func(self, at: float = 1) -> float:
        return self.slope * at + self.intercept

    def point_at(self, at: float = 1) -> Tuple[float, float]:
        """
            Returns the position of a point along the line (for plotting)
        """
        return (at, self.y_func(at))

    def draw(self, ax: plt.Axes):
        ax.axline(
            self.point_at(0),
            xy2=self.point_at(1),
            linewidth=self.style.linewidth,
            color=self.style.linecolor,
            zorder=self.style.zorder,
            antialiased=True,
        )

        # draw annotation
        if self.annotation is not None:
            self.annotation.draw(ax)


class Circle(BaseElement):
    def __init__(
        self,
        x: float = 0,
        y: float = 0,
        r: float = 1.0,
        nolegend: bool = False,
        **kwargs,
    ):
        super().__init__("Circle", nolegend=nolegend)

        self.x, self.y, self.r = x, y, r
        self.style = Style(**kwargs)

    def __repr__(self) -> str:
        return f"Circle @ ({self.x:.2f}, {self.y:.2f}) - style: '{self.style.style_name}'"

    def draw(self, ax: plt.Axes) -> plt.Circle:
        ax.add_patch(
            plt.Circle(
                (self.x, self.y),
                self.r,
                facecolor=self.style.facecolor,
                edgecolor=self.style.linecolor,
                linewidth=self.style.linewidth,
                fill=self.style.filled if self.style.facealpha > 0 else False,
                label=self.legend,
            ),
        )


if __name__ == "__main__":
    from rich import print

    print(Circle(1, 1))
    print(str(Circle))
