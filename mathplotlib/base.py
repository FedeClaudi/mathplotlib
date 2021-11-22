import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
from typing import Union
import numpy as np

from mathplotlib.style import Style


class BaseElement:
    """
        Represents a base element (drawn object)
    """

    style: Style = Style()

    def __init__(self, name: str = "base_element", nolegend: bool = False):
        self.name = name if not nolegend else ""

    @property
    def legend(self) -> str:
        return self.name

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
            clip_on=False,
        )

        # apply effects
        if self.style.outlined:
            for line in lines:
                self.outline(line)

    def outline(self, *artists: plt.Artist, lw: float = None):
        """
            Applies an outline to a matplotlib artist with path effects
        """
        for artist in artists:
            lw = lw or artist.get_linewidth()
            artist.set_path_effects(
                [
                    path_effects.withStroke(
                        linewidth=lw + self.style.strokewwidth,
                        foreground=self.style.strokecolor,
                    ),
                ]
            )
