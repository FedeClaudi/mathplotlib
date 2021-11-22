import matplotlib.pyplot as plt

from mathplotlib.base import BaseElement
from mathplotlib.style import Style
from mathplotlib.utils import angle


class Text(BaseElement):
    """
        Draws a bit of text
    """

    def __init__(
        self,
        x: float,
        y: float,
        text: str,
        size: int = 12,
        rotation: int = 0,
        horizontal_alignment: str = "center",
        vertical_alignment: str = "center",
        **kwargs,
    ):
        super().__init__("Text", nolegend=True)
        self.x, self.y = x, y
        self.size, self.rotation = size, rotation
        self.horizontal_alignment = horizontal_alignment
        self.vertical_alignment = vertical_alignment
        self.text = text
        self.style = Style(**kwargs)

    def __repr__(self) -> str:
        return f"Text @ ({self.x:.2f}, {self.y:.2f})"

    def draw(self, ax: plt.Axes):
        text_actor = ax.text(
            self.x,
            self.y,
            self.text,
            size=self.size,
            rotation=self.rotation,
            ha=self.horizontal_alignment,
            va=self.vertical_alignment,
            color=self.style.textcolor,
        )

        if self.style.outlined:
            self.outline(text_actor, lw=2)

    @classmethod
    def on_curve(cls, curve: BaseElement, text: str, at: float = 1, **kwargs):
        """
            Adds a text on a curve at a given X position along it
        """
        try:
            y_func = curve.y_func  # type: ignore
        except AttributeError:
            raise AttributeError(
                f'The curve object {curve} has no "y_func" method, cant reconstruct text position'
            )

        # compute the angle of the curve at the point
        x1, x2 = at - 0.2, at + 0.2
        y1, y2 = y_func(x1), y_func(x2)
        curve_angle = angle(x1, x2, y1, y2)
        rotation = kwargs.pop("rotation", curve_angle - 10)

        # get the color based on the curve
        color = kwargs.pop("textcolor", curve.style.linecolor)

        return Text(
            at, y_func(at), text, rotation=rotation, textcolor=color, **kwargs
        )


class Annotation(BaseElement):
    _default_arrow_params = dict(
        arrowstyle="->",
        connectionstyle="arc3,rad=-0.4",
        shrinkA=6,
        shrinkB=6,
        lw=2,
    )

    def __init__(
        self,
        x: float,
        y: float,
        text: str,
        x_shift: float = 1,
        y_shift: float = 1,
        size: str = "medium",
        textcoords: str = "data",
        arrow_params: dict = None,
        **kwargs,
    ):

        super().__init__("Annotation", nolegend=True)
        self.style = Style(**kwargs)

        # get/set arrow paramters
        if arrow_params is None:
            arrow_params = self._default_arrow_params.copy()
        arrow_params["color"] = kwargs.pop("textcolor", self.style.textcolor)

        self.x, self.y = x, y
        self.x_shift, self.y_shift = x_shift, y_shift
        self.size = size
        self.textcoords = textcoords
        self.arrow_params = arrow_params
        self.text = text
        self.arrow_params["color"] = self.arrow_params.pop(
            "color", self.style.textcolor
        )

    def draw(self, ax: plt.Axes):
        ax.annotate(
            self.text,
            (self.x, self.y),
            size=self.size,
            color=self.style.textcolor,
            xytext=(self.x + self.x_shift, self.y + self.y_shift),
            textcoords=self.textcoords,
            arrowprops=self.arrow_params,
        )

    @classmethod
    def at_curve(cls, curve: BaseElement, text: str, at: float = 1, **kwargs):
        """
            Draws an annotation pointing at a point along a curve
        """
        try:
            y_func = curve.y_func  # type: ignore
        except AttributeError:
            raise AttributeError(
                f'The curve object {curve} has no "y_func" method, cant reconstruct text position'
            )

        # get color
        color = kwargs.pop("textcolor", curve.style.linecolor)

        return Annotation(at, y_func(at), text, textcolor=color, **kwargs)