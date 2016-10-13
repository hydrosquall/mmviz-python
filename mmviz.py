import matplotlib
import matplotlib.pyplot as plt

from cycler import cycler
from matplotlib.font_manager import FontProperties

MMVIZ_BRAND_FONT_SERIF = ["Times", "Times New Roman", "serif"]
MMVIZ_BRAND_FONT_SANS_SERIF = ["Univers 47 Condensed Light", "Univers 57 Condensed",
                               "Arial Narrow", "Arial", "sans-serif"]

MMVIZ_COLOR_PALETTE_QUAL_1 = ["#7570b3", "#d95f02", "#1b9e77", "#a6761d", "#e6ab02", "#666666", "#e7298a", "#66a61e"]
MMVIZ_COLOR_PALETTE_QUAL_2 = ["#8da0cb", "#fc8d62", "#66c2a5", "#e5c494", "#ffd92f", "#b3b3b3", "#e78ac3", "#a6d854"]
MMVIZ_COLOR_PALETTE_QUAL_3 = MMVIZ_COLOR_PALETTE_QUAL_1 + MMVIZ_COLOR_PALETTE_QUAL_2

MMVIZ_COLOR_PALETTE_SEQ  = ["#fff7fb", "#ece7f2", "#d0d1e6", "#a6bddb", "#74a9cf",
                           "#3690c0", "#0570b0", "#045a8d", "#023858"]

MMVIZ_COLOR_PALETTE_DIV = ["#a50026", "#d73027", "#f46d43", "#fdae61", "#fee090", "#ffffbf",
                           "#e0f3f8", "#abd9e9", "#74add1", "#4575b4", "#313695"]

TITLE_FONT_PROPERTIES = FontProperties()
TITLE_FONT_PROPERTIES.set_family(MMVIZ_BRAND_FONT_SERIF)
TITLE_FONT_PROPERTIES.set_size("xx-large")

# create bin list based on values list and bin_width
def create_bin_list(values, bin_width = 30):

    max_value = values.max()
    min_value = values.min()

    max_bin = (max_value - (max_value % bin_width) + bin_width) + bin_width
    min_bin = (min_value - (min_value % bin_width))

    bin_list = [i for i in range(min_bin, max_bin, bin_width)]
    return bin_list

# create space in the chart for the legend
def place_legend(plt, title, width = 0.2) :

    plt.legend(title = title, bbox_to_anchor=(1, 0.5), loc='center left', ncol=1)
    plt.subplots_adjust(right= 1 - width)

# use MassMutual theme and customize the chart to the given chart_type
def theme_mm(ax, chart_type = "default") :

    print(ax)
    ax.set_title(ax.get_title(), fontproperties=TITLE_FONT_PROPERTIES)

    if chart_type == 'bar' or chart_type == 'bar-vertical' or chart_type == 'column' or chart_type == 'freqpoly' \
            or chart_type == 'histogram' or chart_type == 'boxplot' or chart_type == 'box' \
            or chart_type == 'jitter' :

        ax.xaxis.grid(False)

    elif chart_type == 'bar-horizontal' or chart_type == 'boxplot-horizontal':

        ax.yaxis.grid(False)


# Setup scale color based on type
def scale_color_mm(type = "qual"):

    palette = None

    if type == "qual":
        palette = get_color_palette("qual1")
    else:
        palette = get_color_palette(type)

    if palette != None:
        plt.rc('axes', prop_cycle=(cycler('color', palette)))


# Setup scale fill based on type
def scale_fill_mm(type="qual"):

    palette = None

    if type == "qual":
        palette = get_color_palette("qual2")
    else:
        palette = get_color_palette(type)

    if palette != None:
        plt.rc('axes', prop_cycle=(cycler('color', palette)))


def get_color_palette(type = "qual3"):

    if type == "qual1":
        return MMVIZ_COLOR_PALETTE_QUAL_1

    if type == "qual2":
        return MMVIZ_COLOR_PALETTE_QUAL_2

    if type == "qual3":
        return MMVIZ_COLOR_PALETTE_QUAL_3

    if type == "seq":
        return MMVIZ_COLOR_PALETTE_SEQ

    if type == "div":
        return MMVIZ_COLOR_PALETTE_DIV

    return None

