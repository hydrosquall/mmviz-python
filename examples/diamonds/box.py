import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt

matplotlib.style.use("mmviz")

df = pd.read_csv("../data/diamonds.csv")
df["price"].plot.box()

plt.title("Distribtion of Price")
plt.ylabel("Price")
plt.show()
