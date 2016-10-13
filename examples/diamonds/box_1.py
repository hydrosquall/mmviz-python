import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt

import mmviz

matplotlib.style.use("mmviz")

df = pd.read_csv("../data/diamonds.csv")

ax = df[['cut','price']].boxplot(by="cut", column = "price")
ax.set_title("Distribtion of Price by Cut")
mmviz.theme_mm(ax, "box")

plt.xlabel("Cut")
plt.ylabel("Price")

plt.savefig("./images/box_1", dpi=100)

plt.show()