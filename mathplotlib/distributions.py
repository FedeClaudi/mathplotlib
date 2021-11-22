import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

import mathplotlib as mhplt


class StatisticalDistribution(mhplt.base.BaseElement):
    """
        Baseclass do draw a statistical distribution based
        on scipy.stats distributions
    """

    params: dict = dict()

    def __init__(
        self, distribution: stats.rv_continuous, nolegend: bool = False
    ):
        super().__init__(nolegend=nolegend)
        self.distribution = distribution

    @property
    def xmin(self) -> float:
        """
            computes the xmin such that we can plot
            the entire distribution.
        """
        return self.distribution.ppf(0.0001, *self.params.values())

    @property
    def xmax(self) -> float:
        """
            computes the xmax such that we can plot
            the entire distribution.
        """
        return self.distribution.ppf(0.9999, *self.params.values())

    @property
    def legend(self) -> str:
        dname = self.distribution.name.capitalize()
        params_str = ", ".join(f"{k}:{v:.2f}" for k, v in self.params.items())
        return f"{dname}: ({params_str})"

    def y_func(self, x: float) -> float:
        return self.distribution.pdf(x, *self.params.values())

    def draw(self, ax: plt.Axes):
        # compute x range
        x = np.linspace(self.xmin, self.xmax, 200)

        # compute y range
        y = self.distribution.pdf(x, *self.params.values())

        # draw
        self._draw_curve(x, y, ax)


class Normal(StatisticalDistribution):
    _distribution = stats.norm

    def __init__(
        self,
        mean: float = 0,
        sigma: float = 1,
        nolegend: bool = False,
        **kwargs,
    ):
        super().__init__(self._distribution, nolegend=nolegend)

        # set params
        self.mean = mean
        self.sigma = sigma
        self.params = dict(mean=mean, sigma=sigma)

        # set style
        self.style = mhplt.style.Style(**kwargs)

    def __repr__(self) -> str:
        return f"Normal distribution @ {self.mean:.2f}, std:{self.sigma:.2f} - style: '{self.style.style_name}'"


class Beta(StatisticalDistribution):
    _distribution = stats.beta

    def __init__(
        self, a: float = 0.5, b: float = 0.5, nolegend: bool = False, **kwargs
    ):
        super().__init__(self._distribution, nolegend=nolegend)

        # set params
        self.a = a
        self.b = b
        self.params = dict(a=a, b=b)

        # set style
        self.style = mhplt.style.Style(**kwargs)

    def __repr__(self) -> str:
        return f"Beta distribution (shape params: {self.a:.2f}, {self.b:.2f}) - style: '{self.style.style_name}'"


class Exp(StatisticalDistribution):
    _distribution = stats.expon

    def __init__(
        self,
        loc: float = 0,
        scale: float = 1,
        nolegend: bool = False,
        **kwargs,
    ):
        super().__init__(self._distribution, nolegend=nolegend)

        # set params
        self.loc = loc
        self.scale = scale
        self.params = dict(loc=loc, scale=scale)

        # set style
        self.style = mhplt.style.Style(**kwargs)

    def __repr__(self) -> str:
        return f"Exponential distribution (loc: {self.loc:.2f}, scale: {self.scale:.2f}) - style: '{self.style.style_name}'"
