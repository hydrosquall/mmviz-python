import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt

import mmviz

matplotlib.style.use("mmviz")

df = pd.read_csv("../data/diamonds.csv")

bins = mmviz.create_bin_list(df['price'], 500)

ax = df["price"].plot.hist(bins=bins)
ax.set_title("Distribtion of Diamond Price")
ax.set_yscale("log", basey=2)
mmviz.theme_mm(ax, "histogram")

plt.ylabel("Frequency (log base 2)")
plt.xlabel("Price (bin width = 500)")

plt.savefig("./images/histogram", dpi=100)
plt.show()