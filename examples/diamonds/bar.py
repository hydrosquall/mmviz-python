import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt

import mmviz_utils

matplotlib.style.use("mmviz")

# mmviz_utils.theme_mm("bar")

df = pd.read_csv("../data/diamonds.csv")
df1 = df.groupby('clarity').size()
df1.sort_values(ascending=False, inplace=True)

df1.plot.bar(rot=0)

plt.xlabel("Clarity")
plt.ylabel("Frequency")
plt.title("Diamonds by Clarity")

plt.savefig("./images/bar")
plt.show()