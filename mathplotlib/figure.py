import matplotlib.pyplot as plt
import seaborn as sns
from typing import Tuple, List, Generator
from loguru import logger

from mathplotlib.base import BaseElement


class Canvas:
    def __init__(self, ax: plt.Axes, axes_params: dict = dict()):

        self.ax = ax
        self.style_ax()
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
        # set equal aspect
        self.ax.axis("equal")

        # clean axis
        sns.despine(ax=self.ax, offset=0, trim=False, left=False, right=True)

    def draw(self):
        for actor in self.actors:
            actor.__draw__(self.ax)


class Figure:
    def __init__(
        self,
        layout: str = "A",
        figsize: Tuple[float, float] = (10, 8),
        axes_params: dict = dict(),
        **kwargs,
    ):
        logger.debug(f"Creating figure with layout: {layout}")
        logger.debug(f"Axes parameters: {axes_params}")
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
        for canvas in self.canvases.values():
            canvas.draw()
            if legend:
                canvas.ax.legend()
        plt.show()


def show(*actors: BaseElement, legend: bool = False, **kwargs):
    fig = Figure(layout="A", **kwargs)
    fig.add_to("A", *actors)
    fig.show(legend=legend)
