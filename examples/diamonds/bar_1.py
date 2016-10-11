import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt

matplotlib.style.use("mmviz")

df = pd.read_csv("../data/diamonds.csv")
# print(df.head())

df1 = df.groupby(['clarity', 'cut'])['price'].count().reset_index().pivot(index='clarity', columns='cut', values="price")
# print(df1.head(100))

df1.plot.bar(stacked = True)
plt.show()