import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt

import mmviz_utils

matplotlib.style.use("mmviz")

df = pd.read_csv("../data/diamonds.csv")

bins = mmviz_utils.create_bin_list(df['price'], 500)
df["price"].plot.hist(bins=bins)

plt.title("Distribtion of Diamond Price")
plt.xlabel("Price (bin width = 500)")

plt.savefig("./images/histogram")
plt.show()