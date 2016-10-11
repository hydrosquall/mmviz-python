import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt

matplotlib.style.use("mmviz")

df = pd.read_csv("../data/diamonds.csv")
df["price"].plot.box()

plt.xlabel("")
plt.ylabel("Price")
plt.title("Distribtion of Price")

plt.savefig("./images/box")
plt.show()
