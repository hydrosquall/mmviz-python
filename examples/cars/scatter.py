import pandas as pd

import matplotlib
import matplotlib.pyplot as plt

import mmviz

matplotlib.style.use("mmviz")

df = pd.read_csv("../data/mtcars.csv")

cols = ["cyl", "mpg", "wt", "disp"]

df_cyl_dict = {"Cyl 4": df.loc[df["cyl"] == 4, cols],
               "Cyl 6": df.loc[df["cyl"] == 6, cols],
               "Cyl 8": df.loc[df["cyl"] == 8, cols]}

palette_iter = mmviz.get_palette_iter_mm("qual_fill")

ax = None
for key in df_cyl_dict:
    ax = df_cyl_dict[key].plot.scatter(x="wt", y="mpg", label=key, c=next(palette_iter),
                                       s=df_cyl_dict[key]["disp"], ax=ax, alpha=0.8)

ax.set_title("Weight vs. Miles Per Gallon")
mmviz.theme_mm(ax, "scatter")

plt.xlabel("Car Weight")
plt.ylabel("Miles Per Gallon")

mmviz.place_legend(plt, "Cylinder", 0.2)

plt.savefig("./images/scatter", dpi=100)
plt.show()