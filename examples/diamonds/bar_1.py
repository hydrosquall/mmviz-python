import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt

import mmviz

mmviz.theme_mm("bar")

df = pd.read_csv("../data/diamonds.csv")
df1 = df.groupby(['clarity', 'cut'])['price'].count().reset_index().pivot(index='clarity', columns='cut', values="price")

ax = df1.plot.bar(stacked = True, rot=0)
ax.set_title("Diamonds by Clarity and Cut", fontproperties=mmviz.TITLE_FONT_PROPERTIES)

plt.xlabel("Clarity")
plt.ylabel("Frequency")

mmviz.place_legend(plt, "Cut", 0.2)

plt.savefig("./images/bar_1", dpi=100)
plt.show()