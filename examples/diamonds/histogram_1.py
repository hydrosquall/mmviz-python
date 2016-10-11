import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt

import mmviz_utils

matplotlib.style.use("mmviz")

df = pd.read_csv("../data/diamonds.csv")

bin_width = 500
bins = mmviz_utils.create_bin_list(df['price'], bin_width)

df = df.pivot(columns='cut', values="price")
df.plot.hist(stacked=True, bins=bins)

plt.legend()
plt.show()


