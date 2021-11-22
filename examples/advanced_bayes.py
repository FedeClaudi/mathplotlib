import sys

sys.path.append("./")

from math import sqrt

# import matplotlib.pyplot as plt

from mathplotlib import show, distributions
from mathplotlib.annotations import Text, Annotation

from myterial import (
    green_lighter,
    indigo_lighter,
    teal_light,
    green,
    indigo,
    teal,
    grey_dark,
)

# plt.rcParams['text.usetex'] = True


prior_mu, prior_sigma = 1, 0.3
like_mu, like_sigma = 3, 0.2

# Prior
prior = distributions.Normal(
    mean=prior_mu,
    sigma=prior_sigma,
    facecolor=green_lighter,
    linecolor=green,
    linewidth=3,
)
prior_label = Text.on_curve(
    prior, "prior", at=0.6, size=16, backgroundcolor=None
)
prior_annot = Annotation.at_curve(
    prior,
    "$P(A)$",
    at=prior_mu - 0.2,
    x_shift=-0.25,
    y_shift=0.45,
    size=12,
    textcolor=grey_dark,
    arrow_params=dict(connectionstyle="arc3,rad=0.2"),
)

# Likelihoood
likelihoood = distributions.Normal(
    mean=like_mu,
    sigma=like_sigma,
    facecolor=indigo_lighter,
    linecolor=indigo,
    linewidth=3,
)
likelihood_label = Text.on_curve(
    likelihoood, "likelihoood", at=3.2, size=16, backgroundcolor=None
)
likelihood_annot = Annotation.at_curve(
    likelihoood,
    "$P(B|A)$",
    at=like_mu + 0.1,
    x_shift=0.15,
    y_shift=0.3,
    size=12,
    textcolor=grey_dark,
)

# posterior
mu = (prior_mu / prior_sigma ** 2 + like_mu / like_sigma ** 2) / (
    1 / prior_sigma ** 2 + 1 / like_sigma ** 2
)
sigma = 1 / (1 / (prior_sigma ** 2) + 1 / (like_sigma ** 2))
posterior = distributions.Normal(
    mean=mu,
    sigma=sqrt(sigma),
    facecolor=teal_light,
    linecolor=teal,
    linewidth=3,
    facealpha=0.4,
)
posterior_label = Text.on_curve(
    posterior, "posterior", at=2.2, size=16, backgroundcolor=None
)
posterior_annot = Annotation.at_curve(
    posterior,
    "$P(A|B)$",
    at=mu - 0.1,
    x_shift=-0.8,
    y_shift=-0.3,
    size=12,
    textcolor=grey_dark,
    arrow_params=dict(connectionstyle="arc3,rad=0.2"),
)


# text
norm_eq = Text(
    0.1,
    2.5,
    r"Normal distribution: $p(y)=\frac{1}{\sqrt{2 \pi \sigma^{2}}} e^{-\frac{\left(y-\mu\right)^{2}}{2 \sigma^{2}}}$",
    horizontal_alignment="left",
    size=16,
    alpha=0.5,
)
post_mean = Text(
    0.1,
    2.25,
    r"Posterior mean: $\frac{\frac{\mu_{1}}{\sigma_{1}^{2}}+\frac{\mu_{2}}{\sigma_{2}^{2}}}{\frac{1}{\sigma_{1}^{2}}+\frac{1}{\sigma_{2}^{2}}}$",
    horizontal_alignment="left",
    size=16,
    alpha=0.5,
)
post_std = Text(
    0.1,
    2,
    r"Posterior sigma: $\frac{1}{\frac{1}{\sigma_{1}^{2}}+\frac{1}{\sigma_{2}^{2}}}$",
    horizontal_alignment="left",
    size=16,
    alpha=0.5,
    fontweight="bold",
)

# TODO add latex annotations

# ----------------------------------- plot ----------------------------------- #
show(
    prior,
    prior_label,
    prior_annot,
    likelihoood,
    likelihood_label,
    likelihood_annot,
    posterior,
    posterior_label,
    posterior_annot,
    norm_eq,
    post_mean,
    post_std,
    axes_equal=True,
    figsize=(18, 12),
    axes_params=dict(xlabel="x value", ylabel="probability"),
)
