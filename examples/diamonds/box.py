import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt

import mmviz

matplotlib.style.use("mmviz")

df = pd.read_csv("../data/diamonds.csv")
ax = df["price"].plot.box()
ax.set_title("Distribtion of Price")
mmviz.theme_mm(ax, "box")

plt.xlabel("")
plt.ylabel("Price")

plt.savefig("./images/box", dpi=100)
plt.show()
