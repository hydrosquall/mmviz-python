import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt

import mmviz

matplotlib.style.use("mmviz")

mmviz.scale_palette_mm("qual_color")

df = pd.DataFrame(np.random.randn(1000, 4), index=pd.date_range('1/1/2000', periods=1000), columns=list('ABCD'))
df = df.cumsum()
ax = df.plot()
ax.set_title("Random Value Over Time")
mmviz.theme_mm(ax, "line")

plt.xlabel("Time")
plt.ylabel("Value")

mmviz.place_legend(plt, "Category", 0.15)

plt.savefig("./images/series", dpi=100)
plt.show()