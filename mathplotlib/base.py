from __future__ import annotations

import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
from typing import Union, Optional
import numpy as np

from mathplotlib.style import Style
import mathplotlib
from mathplotlib.utils import angle


class BaseElement:
    """
        Represents a base element (drawn object)
    """

    style: Style = Style()
    annotation: Optional[mathplotlib.annotations.Text] = None

    def __init__(self, name: str = "base_element", nolegend: bool = False):
        self.name = name if not nolegend else ""

    @property
    def legend(self) -> str:
        return self.name

    def outline(self, *artists: plt.Artist, lw: float = None):
        """
            Applies an outline to a matplotlib artist with path effects
        """
        for artist in artists:
            lw = lw or artist.get_linewidth()
            artist.set_path_effects(
                [
                    path_effects.withStroke(
                        linewidth=lw + self.style.strokewidth,
                        foreground=self.style.strokecolor,
                    ),
                ]
            )


class Curve2D(BaseElement):
    """
        Methods to draw curves on the 2D plane
    """

    def _draw_curve(
        self, x: np.ndarray, y: Union[np.ndarray, list], ax: plt.Axes
    ):
        """
            Draws a 1-D curve (specified by X,Y coordinates) and sets styles/
            effects appropriately
        """
        # draw colored area
        if self.style.filled:
            ax.fill_between(
                x, y, color=self.style.facecolor, alpha=self.style.facealpha,
            )

        # draw line
        lines = ax.plot(
            x,
            y,
            color=self.style.linecolor,
            lw=self.style.linewidth,
            label=self.legend,
            ls=self.style.linestyle,
            clip_on=True,
            zorder=self.style.zorder,
            antialiased=True,
        )

        # apply effects
        if self.style.outlined:
            for line in lines:
                self.outline(line)

        # draw annotation
        if self.annotation is not None:
            self.annotation.draw(ax)

    def angle_at_point(self, at: float = 1) -> float:
        """
            Computes the angle of the curve at a point
        """
        x1, x2 = at - 0.2, at + 0.2
        y1, y2 = self.y_func(x1), self.y_func(x2)  # type: ignore
        return angle(x1, x2, y1, y2)

    def annotate(self, at: float = 1, **kwargs) -> BaseElement:
        """
            Uses a Text annotation to draw its own legend on itself
        """
        self.annotation = mathplotlib.annotations.Text.on_curve(
            self, self.legend, at=at, **kwargs
        )
        return self
