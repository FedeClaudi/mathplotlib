import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from dataclasses import dataclass

from mathplotlib.style import get_style


@dataclass
class Normal:
    mean: float = 0
    sigma: float = 1
    filled: bool = True
    style: str = "cartoon"

    @property
    def xmin(self) -> float:
        """
            computes the xmin such that we can plot
            the entire distribution.
        """
        return stats.norm.ppf(0.0001, self.mean, self.sigma)

    @property
    def xmax(self) -> float:
        """
            computes the xmax such that we can plot
            the entire distribution.
        """
        return stats.norm.ppf(0.9999, self.mean, self.sigma)

    def __draw__(self, ax: plt.Axes):
        style = get_style(self.style)

        # compute x range
        x_range = np.linspace(self.xmin, self.xmax, 200)

        # compute y range
        y = stats.norm.pdf(x_range, self.mean, self.sigma)

        # draw colored area
        if self.filled:
            ax.fill_between(
                x_range,
                y,
                color=style.face_color,
                alpha=style.curve_area_alpha,
            )

        # draw line
        ax.plot(x_range, y, color=style.line_color, lw=style.line_weight)
