from myterial import grey_darker, black
from loguru import logger

blue_purple = "#a9a9cc"


cartoon_defaults = dict(
    facecolor=blue_purple,  # inside of shape
    facealpha=1,
    linecolor=grey_darker,  # line
    linewidth=2,
    linestyle="-",
    filled=True,
    outlined=False,
)

minimal_defaults = dict(
    facecolor=blue_purple,  # inside of shape
    facealpha=1,
    linecolor=black,  # line
    linewidth=1,
    linestyle="-",
    filled=False,
    outlined=False,
)


class Style:

    facecolor: str = blue_purple
    facealpha: float = 1
    linecolor: str = black
    linewidth: float = 1
    linestyle: str = "-"
    filled: bool = False
    outlined: bool = False

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
