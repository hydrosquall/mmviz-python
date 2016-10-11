import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt

import mmviz_utils

matplotlib.style.use("mmviz")

df = pd.read_csv("../data/diamonds.csv")

df1 = df.groupby(['clarity', 'cut'])['price'].count().reset_index().pivot(index='clarity', columns='cut', values="price")
df1.plot.bar(stacked = True, rot=0)

mmviz_utils.place_legend(plt, "Cut", 0.2)

plt.xlabel("Clarity")
plt.ylabel("Frequency")
plt.title("Diamonds by Clarity and Cut")

plt.savefig("./images/bar_1")
plt.show()