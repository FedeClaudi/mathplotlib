from myterial import grey_dark, white

blue_purple = "#a9a9cc"


class Cartoon:
    # lineas
    line_color: str = grey_dark
    line_weight: float = 2

    # curves
    curve_area_alpha: float = 0.5

    # faces/shapes
    face_alpha: float = 1
    face_color: str = blue_purple


class Minimal:
    # lines
    line_color: str = grey_dark
    line_weight: float = 1

    # curves
    curve_area_alpha: float = 0.5

    # faces/shapes
    face_alpha: float = 0
    face_color: str = white


def get_style(style: str):
    if style == "cartoon":
        return Cartoon
    else:
        return Minimal
