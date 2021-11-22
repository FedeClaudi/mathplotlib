import matplotlib.pyplot as plt
from typing import Tuple, List, Generator

from myterial import grey_darker

from mathplotlib.base import BaseElement
from mathplotlib.utils import update_with_default


class Canvas:
    default_legend_params = dict(
        edgecolor="None", ncol=2, loc="upper right", borderaxespad=0,
    )

    def __init__(
        self,
        ax: plt.Axes,
        axes_params: dict = dict(),
        axes_equal: bool = False,
    ):
        self.axes_equal = axes_equal
        self.ax = ax
        self.axes_params = axes_params

        # initialize empty actors
        self.actors: List = []
        self.drawn: bool = False

    def __repr__(self) -> str:
        return (
            f"Canvas - {len(self.actors)} elements:\n      "
            + "\n      ".join(
                [f"({n+1}) - {a}" for n, a in enumerate(self.actors)]
            )
        )

    def add(self, *actors: BaseElement):
        for actor in actors:
            self.actors.append(actor)

    def style_ax(self):
        # move spines to center
        self.ax.spines["bottom"].set_position(("data", 0))
        self.ax.spines["left"].set_position(("data", 0))

        # draw axes as arrows
        if not self.axes_equal:
            self.ax.plot(
                1.005,
                0,
                ">",
                color=grey_darker,
                alpha=1,
                zorder=100,
                transform=self.ax.get_yaxis_transform(),
                clip_on=False,
            )
            self.ax.plot(
                0,
                1.005,
                "^",
                color=grey_darker,
                alpha=1,
                zorder=100,
                transform=self.ax.get_xaxis_transform(),
                clip_on=False,
            )
        else:
            self.ax.axis("equal")

        # set parameters
        self.ax.set(**self.axes_params)

    def make_legend(self, **legend_kwargs):
        legend_kwargs = update_with_default(
            legend_kwargs, self.default_legend_params
        )
        self.ax.legend(**legend_kwargs)

    def draw(self):
        if not self.drawn:
            for actor in self.actors:
                actor.draw(self.ax)
            self.drawn = True


class Figure:
    def __init__(
        self,
        layout: str = "A",
        figsize: Tuple[float, float] = (10, 8),
        axes_params: dict = dict(),
        axes_equal: bool = False,
        **kwargs,
    ):
        self.figure = plt.figure(figsize=figsize, **kwargs)

        self.canvases = dict()
        axes = self.figure.subplot_mosaic(layout)
        for ax_name, ax in axes.items():
            self.canvases[ax_name] = Canvas(
                ax, axes_params=axes_params, axes_equal=axes_equal
            )

    def __repr__(self) -> str:
        return f"Figure with {len(self.canvases)} Canvases"

    def __rich_repr__(self) -> Generator:
        for n, (canvas_name, canvas) in enumerate(self.canvases.items()):
            yield f'\n"{canvas_name}" ', canvas

    def add_to(self, canvas_name: str, *actors: BaseElement):
        self.canvases[canvas_name].add(*actors)

    def draw(self):
        """
            Just draws all canvases without showing
        """
        for canvas in self.canvases.values():
            canvas.draw()

    def show(self, legend: bool = False, legend_kwargs: dict = dict()):
        """
            Draws all actors and styles the axes
        """
        self.draw()

        for canvas in self.canvases.values():
            # create legend and style ax
            if legend:
                canvas.make_legend(**legend_kwargs)
            canvas.style_ax()
        plt.show()


def show(
    *actors: BaseElement,
    legend: bool = False,
    legend_kwargs: dict = dict(),
    **kwargs,
):
    fig = Figure(layout="A", **kwargs)
    fig.add_to("A", *actors)
    fig.show(legend=legend, legend_kwargs=legend_kwargs)
