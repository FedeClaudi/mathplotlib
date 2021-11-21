import matplotlib.pyplot as plt

from mathplotlib.base import BaseElement
from mathplotlib.style import Style


# class Line:
#     slope: float
#     intercept: float


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
