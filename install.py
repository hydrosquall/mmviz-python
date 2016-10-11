import shutil
import matplotlib.pyplot as plt

stylefile = "mmviz.mplstyle"
matplotlib_loc = plt.__file__.replace("pyplot.py", "mpl-data/stylelib/" + stylefile)
print(matplotlib_loc)

shutil.copy("./" + stylefile, matplotlib_loc)