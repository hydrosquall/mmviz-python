import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt

import mmviz

mmviz.theme_mm("histogram")

df = pd.read_csv("../data/diamonds.csv")

bins = mmviz.create_bin_list(df['price'], 500)

ax = df["price"].plot.hist(bins=bins)
ax.set_title("Distribtion of Diamond Price", fontproperties=mmviz.TITLE_FONT_PROPERTIES)

plt.xlabel("Price (bin width = 500)")

plt.savefig("./images/histogram", dpi=100)
plt.show()