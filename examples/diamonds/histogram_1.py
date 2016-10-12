import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt

import mmviz

mmviz.theme_mm("histogram")

df = pd.read_csv("../data/diamonds.csv")

bin_width = 500
bins = mmviz.create_bin_list(df['price'], bin_width)

df = df.pivot(columns='cut', values="price")
ax = df.plot.hist(stacked=True, bins=bins)
ax.set_title("Distribtion of Diamond Price by Cut", fontproperties=mmviz.TITLE_FONT_PROPERTIES)

plt.xlabel("Price (bin width = 500)")

mmviz.place_legend(plt, "Cut", 0.2)

plt.savefig("./images/histogram_1", dpi=100)
plt.show()


