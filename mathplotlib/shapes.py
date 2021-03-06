from __future__ import annotations

import matplotlib.pyplot as plt
from typing import Tuple, Optional
import numpy as np

from mathplotlib.base import BaseElement, Curve2D
from mathplotlib.style import Style


class Line(Curve2D):
    def __init__(
        self,
        slope: float = 1,
        intercept: float = 0,
        nolegend: bool = False,
        p0: Optional[Tuple[float, float]] = None,
        p1: Optional[Tuple[float, float]] = None,
        orientation: str = "angled",
        x: Optional[float] = None,
        y: Optional[float] = None,
        **kwargs,
    ):
        super().__init__("Line", nolegend=nolegend)
        self.slope = slope
        self.intercept = intercept

        self.x, self.y = x, y
        self.orientation = orientation

        self.style = Style(**kwargs)

        # define two points used to draw a line
        if p0 is None:
            p0 = (0, self.y_func(at=0))
        if p1 is None:
            p1 = (1, self.y_func(at=1))
        self.p0, self.p1 = p0, p1

    def __repr__(self) -> str:
        return f"Line with slope {self.slope:.2f}, intercept: {self.intercept:.2f}"

    @property
    def legend(self) -> str:
        if self.orientation == "vertical":
            return f"x = {self.x}"
        elif self.orientation == "horizontal":
            return f"y = {self.y}"
        else:
            return f"y = {self.slope:.1f}x + {self.intercept:.1f}"

    @classmethod
    def between_points(
        cls, p0: Tuple[float, float], p1: Tuple[float, float], **kwargs,
    ) -> Line:
        """
            Creates a line going through two points
        """
        x, y = None, None
        # compute slope and intercept
        if p0[0] == p1[0]:
            # same X -> vertical line
            slope = intercept = np.nan
            x = p0[0]
            orientation = "vertical"
        elif p0[1] == p1[1]:
            # same Y -> horizontal line
            slope = 0
            intercept = p0[1]
            y = p0[1]
            orientation = "horizontal"
        else:
            # angled line
            dx = p1[0] - p0[0]
            dy = p1[1] - p0[1]
            slope = dy / dx
            intercept = p1[1] - slope * p1[0]
            orientation = "angled"

        return Line(
            slope,
            intercept,
            p0=p0,
            p1=p1,
            x=x,
            y=y,
            orientation=orientation,
            **kwargs,
        )

    @classmethod
    def vertical(cls, x: float, **kwargs) -> Line:
        """
            Create a vertical line at an X value
        """
        return Line.between_points((x, 0), (x, 1), **kwargs)

    @classmethod
    def horizontal(cls, y: float, **kwargs) -> Line:
        """
            Create an horizontal line with a Y value
        """
        return Line.between_points((0, y), (1, y), **kwargs)

    def angle_at_point(self, at: float = 1) -> float:
        if self.orientation == "angled":
            return np.degrees(np.arctan(self.slope))
        elif self.orientation == "vertical":
            return 90
        else:
            return 0

    def y_func(self, at: float = 1) -> float:
        if self.orientation == "angled":
            return self.slope * at + self.intercept
        elif self.orientation == "vertical":
            return at
        else:
            return self.intercept

    def point_at(self, at: float = 1) -> Tuple[float, float]:
        """
            Returns the position of a point along the line (for plotting)
        """
        return (at, self.y_func(at))

    def draw(self, ax: plt.Axes):
        ax.axline(
            self.p0,
            xy2=self.p1,
            linewidth=self.style.linewidth,
            linestyle=self.style.linestyle,
            color=self.style.linecolor,
            zorder=self.style.zorder,
            alpha=self.style.alpha,
            antialiased=True,
        )

        # draw annotation
        if self.annotation is not None:
            self.annotation.draw(ax)


class Grid(BaseElement):
    """
        A grid of vertical and horizontal lines
    """

    def __init__(
        self,
        x0: float,
        x1: float,
        y0: float,
        y1: float,
        major_every: float = 2,
        minor_every: Optional[float] = 1,
        major_linewidth: float = 1,
        minor_linewidth: float = 0.25,
        major_kwargs: dict = dict(),
        minor_kwargs: dict = dict(),
        **kwargs,
    ):
        """
            Creates a grid of horizontal and vertical thick and thin lines 
        """
        super().__init__()
        self.lines = []

        # create vertical lines
        vmaj, vmin = self.get_ticks(x0, x1, major_every, minor_every)
        self.lines.extend(
            [
                Line.vertical(
                    x, linewidth=major_linewidth, **major_kwargs, **kwargs
                )
                for x in vmaj
            ]
        )
        if vmin is not None:
            self.lines.extend(
                [
                    Line.vertical(
                        x, linewidth=minor_linewidth, **minor_kwargs, **kwargs
                    )
                    for x in vmin
                ]
            )

        # create horizontal lines
        hmaj, hmin = self.get_ticks(y0, y1, major_every, minor_every)
        self.lines.extend(
            [
                Line.horizontal(
                    y, linewidth=major_linewidth, **major_kwargs, **kwargs
                )
                for y in hmaj
            ]
        )
        if hmin is not None:
            self.lines.extend(
                [
                    Line.horizontal(
                        y, linewidth=minor_linewidth, **minor_kwargs, **kwargs
                    )
                    for y in hmin
                ]
            )

    @staticmethod
    def get_ticks(
        p0: float, p1: float, major_every: float, minor_every: Optional[float]
    ) -> Tuple[np.ndarray, np.ndarray]:
        """
            Computes the position of minor and major lines
        """
        majors = np.arange(p0, p1 + 1, major_every)
        if minor_every is None:
            minors = None
        else:
            minors = np.arange(
                p0 + minor_every, p1 - minor_every + 1, minor_every
            )

            # remove overlaps
            minors = np.array([m for m in minors if m not in majors])

        return majors, minors

    def draw(self, ax: plt.Axes):
        # draw all lines
        for line in self.lines:
            line.draw(ax)


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
