from rich.traceback import install

install()


import matplotlib.pyplot as plt

plt.style.use("mathplotlib/style_plt.txt")
plt.rcParams.update(
    {"font.family": "sans-serif", "font.sans-serif": ["Helvetica"]}
)


import mathplotlib.annotations
import mathplotlib.base
import mathplotlib.style
import mathplotlib.figure
import mathplotlib.functions
import mathplotlib.shapes
import mathplotlib.utils


from mathplotlib.figure import Figure, show


__version__ = 0.1
__date__ = "23.11.21"
