import matplotlib.pyplot as plt
from typing import Tuple, List


class Figure:
    def __init__(self, size: Tuple[int, int] = (12, 8), **kwargs: dict):
        self.figure, self.ax = plt.subplots(figsize=size, **kwargs)

        # initialize empty actors
        self.actors: List = []

    def __repr__(self) -> str:
        return f"({len(self.actors)}) elements:\n      " + "\n      ".join(
            [f"({n+1}) - {a}" for n, a in enumerate(self.actors)]
        )

    def add(self, *actors):
        for actor in actors:
            self.actors.append(actor)

    def style_ax(self):
        self.ax.axis("equal")

    def show(self):
        for actor in self.actors:
            actor.__draw__(self.ax)

        self.style_ax()
        plt.show()
