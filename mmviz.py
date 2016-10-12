import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

MMVIZ_BRAND_FONT_SERIF = ["Times", "Times New Roman", "serif"]
MMVIZ_BRAND_FONT_SANS_SERIF = ["Univers 47 Condensed Light", "Univers 57 Condensed", "Arial Narrow", "Arial", "sans-serif"]

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


def theme_mm(chart_type = "default") :

    matplotlib.style.use("mmviz")

    # plt.title("", fontname="Times New Roman")

    if chart_type == "bar" :
        matplotlib.rc('lines', linewidth=2, color='r')