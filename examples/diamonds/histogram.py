import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt

matplotlib.style.use("mmviz")

df = pd.read_csv("../data/diamonds.csv")
df["price"].plot.hist(bins=100)

plt.title("Distribtion of Diamond Price")
plt.xlabel("Price (bins = 100)")
plt.show()