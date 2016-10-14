import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt

import mmviz

matplotlib.style.use("mmviz")

df = pd.read_csv("../data/diamonds.csv")
df1 = df.groupby('clarity').size()
df1.sort_values(ascending=True, inplace=True)

ax = df1.plot.barh(rot=0)
ax.set_title("Diamonds by Clarity")
mmviz.theme_mm(ax, "bar-horizontal")

plt.xlabel("Clarity")
plt.ylabel("Frequency")

plt.savefig("./images/bar", dpi=100)
plt.show()