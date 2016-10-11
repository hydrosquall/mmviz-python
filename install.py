import os
import shutil
import matplotlib

stylefile = "mmviz.mplstyle"

mpl_stylelib_dir = matplotlib.get_configdir() + "/stylelib/"
if not os.path.exists(mpl_stylelib_dir):
    os.makedirs(mpl_stylelib_dir)

print(mpl_stylelib_dir)
shutil.copy("./" + stylefile, mpl_stylelib_dir + stylefile)