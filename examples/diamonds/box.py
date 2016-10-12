import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt

import mmviz

mmviz.theme_mm("box")

df = pd.read_csv("../data/diamonds.csv")
ax = df["price"].plot.box()
ax.set_title("Distribtion of Price", fontproperties=mmviz.TITLE_FONT_PROPERTIES)

plt.xlabel("")
plt.ylabel("Price")

plt.savefig("./images/box", dpi=100)
plt.show()
