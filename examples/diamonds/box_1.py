import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt

matplotlib.style.use("mmviz")

df = pd.read_csv("../data/diamonds.csv")
#print(df.head())

df[['cut','price']].boxplot(by="cut", column = "price")

plt.xlabel("Cut")
plt.ylabel("Price")
plt.title("Distribtion of Price by Cut")

plt.savefig("./images/box_1")
plt.show()