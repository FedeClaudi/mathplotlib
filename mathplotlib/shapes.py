import matplotlib.pyplot as plt
from dataclasses import dataclass

from mathplotlib.style import get_style


@dataclass
class Line:
    slope: float
    intercept: float


@dataclass
class Circle:
    x: float = 0
    y: float = 0
    r: float = 1.0
    filled: bool = True
    style: str = "cartoon"  # or minimal or base

    def __repr__(self) -> str:
        return f"Circle @ ({self.x:.2f}, {self.y:.2f}) - style: {self.style}"

    def __draw__(self, ax: plt.Axes) -> plt.Circle:
        style = get_style(self.style)
        ax.add_patch(
            plt.Circle(
                (self.x, self.y),
                self.r,
                facecolor=style.face_color,
                edgecolor=style.line_color,
                linewidth=style.line_weight,
                fill=self.filled if style.face_alpha > 0 else False,
            )
        )


if __name__ == "__main__":
    from rich import print

    print(Circle(1, 1))
    print(str(Circle))
