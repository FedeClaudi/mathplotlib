from myterial import grey_darker, black
from loguru import logger
from typing import Union, Optional

blue_purple = "#a9a9cc"


cartoon_defaults = dict(
    alpha=1,
    facecolor=blue_purple,
    facealpha=1,
    linecolor=grey_darker,
    linewidth=2,
    linestyle="-",
    strokecolor="k",
    strokewidth=2,
    backgroundcolor=None,
    fontweight="regular",
    textcolor="k",
    filled=True,
    outlined=False,
    zorder=1,
)

minimal_defaults = dict(
    alpha=1,
    facecolor=blue_purple,
    facealpha=1,
    linecolor=black,
    linewidth=1,
    linestyle="-",
    strokecolor="k",
    strokewidth=2,
    backgroundcolor=None,
    fontweight="regular",
    textcolor="k",
    filled=False,
    outlined=False,
    zorder=1,
)


class Style:
    alpha: float = 1
    facecolor: str = blue_purple  # for shapes and shaded areas
    facealpha: float = 1  # for shapes and shaded areas
    linecolor: str = black  # for all lines
    linewidth: float = 1  # for all lines
    linestyle: str = "-"  # for all lines
    strokecolor: str = "k"  # for outline of lines
    strokewidth: int = 2  # for outline of lines
    fontweight: Union[str, int] = "regular"  # for Text
    textcolor: str = "k"  # for Text object
    backgroundcolor: Optional[str] = None  # for Text object
    filled: bool = False  # shade inside of shape
    outlined: bool = False  # add colored outline
    zorder: int = 1  # Z stack order

    def __init__(self, style: str = "cartoon", **kwargs: dict):
        """
            Default styles set by the choice of style
        """
        self.style_name = style

        # fetch defaults
        if style == "cartoon":
            parameters = cartoon_defaults.copy()
        elif style == "minimal":
            parameters = minimal_defaults.copy()
        else:
            raise ValueError(f'Unrecognized style "{style}"')

        # get user inputs
        for key, value in kwargs.items():
            if key not in parameters:
                logger.debug(f'User style parameter: "{key}" not recognized')
            parameters[key] = value

        # set parameters
        for key, value in parameters.items():
            setattr(self, key, value)
