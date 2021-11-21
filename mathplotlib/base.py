class BaseElement:
    """
        Represents a base element (drawn object)
    """

    def __init__(self, name: str = "base_element", nolegend: bool = False):
        self.name = name if not nolegend else ""

    @property
    def legend(self) -> str:
        return self.name
