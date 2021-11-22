import matplotlib.pyplot as plt
from typing import Tuple, List, Generator

from myterial import grey_darker

from mathplotlib.base import BaseElement


class Canvas:
    def __init__(self, ax: plt.Axes, axes_params: dict = dict()):

        self.ax = ax
        ax.set(**axes_params)

        # initialize empty actors
        self.actors: List = []

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

    def draw(self):
        for actor in self.actors:
            actor.draw(self.ax)


class Figure:
    def __init__(
        self,
        layout: str = "A",
        figsize: Tuple[float, float] = (10, 8),
        axes_params: dict = dict(),
        **kwargs,
    ):
        self.figure = plt.figure(figsize=figsize, **kwargs)

        self.canvases = dict()
        axes = self.figure.subplot_mosaic(layout)
        for ax_name, ax in axes.items():
            self.canvases[ax_name] = Canvas(ax, axes_params=axes_params)

    def __repr__(self) -> str:
        return f"Figure with {len(self.canvases)} Canvases"

    def __rich_repr__(self) -> Generator:
        for n, (canvas_name, canvas) in enumerate(self.canvases.items()):
            yield f'\n"{canvas_name}" ', canvas

    def add_to(self, canvas_name: str, *actors: BaseElement):
        self.canvases[canvas_name].add(*actors)

    def show(self, legend: bool = False):
        """
            Draws all actors and styles the axes
        """
        for canvas in self.canvases.values():
            canvas.draw()

            # create legend and style ax
            if legend:
                canvas.ax.legend(
                    edgecolor="None",
                    ncol=2,
                    loc="upper right",
                    borderaxespad=0,
                )
            canvas.style_ax()
        plt.show()


def show(*actors: BaseElement, legend: bool = False, **kwargs):
    fig = Figure(layout="A", **kwargs)
    fig.add_to("A", *actors)
    fig.show(legend=legend)
