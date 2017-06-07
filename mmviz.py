import matplotlib
import matplotlib.pyplot as plt

from cycler import cycler
from matplotlib.font_manager import FontProperties

#MMVIZ_BRAND_FONT_SERIF = ["Times", "Times New Roman", "serif"]
MMVIZ_BRAND_FONT_SERIF = ["FreightText", "Georgia", "Times New Roman", "Times", "serif"]
#MMVIZ_BRAND_FONT_SANS_SERIF = ["Univers 47 Condensed Light", "Univers 57 Condensed",
#                               "Arial Narrow", "Arial", "sans-serif"]
MMVIZ_BRAND_FONT_SANS_SERIF = ["BrandonText", "Helvetica", "Arial", "sans-serif"]

#MMVIZ_COLOR_PALETTE_QUAL_DARK = ["#7570b3", "#d95f02", "#1b9e77", "#a6761d", "#e6ab02", "#666666", "#e7298a", "#66a61e"]
MMVIZ_COLOR_PALETTE_QUAL_DARK = ["#232E53", "#DF6035", "#42A44C", "#EFB83B", "#855AA1", "#69A5AC", "#D7313E", "#318FBF"]

#MMVIZ_COLOR_PALETTE_QUAL_LIGHT = ["#8da0cb", "#fc8d62", "#66c2a5", "#e5c494", "#ffd92f", "#b3b3b3", "#e78ac3", "#a6d854"]
MMVIZ_COLOR_PALETTE_QUAL_LIGHT = ["#5F6781", "#E78B6C", "#75BC7C", "#F3CB70", "#A687BA", "#94BFC2", "#E16972", "#69ADD0"]

MMVIZ_COLOR_PALETTE_QUAL_ALT_DARK = MMVIZ_COLOR_PALETTE_QUAL_DARK + MMVIZ_COLOR_PALETTE_QUAL_LIGHT
MMVIZ_COLOR_PALETTE_QUAL_ALT_LIGHT = MMVIZ_COLOR_PALETTE_QUAL_LIGHT + MMVIZ_COLOR_PALETTE_QUAL_DARK

MMVIZ_COLOR_PALETTE_SEQ  = ["#fff7fb", "#ece7f2", "#d0d1e6", "#a6bddb", "#74a9cf",
                           "#3690c0", "#0570b0", "#045a8d", "#023858"]

MMVIZ_COLOR_PALETTE_DIV = ["#a50026", "#d73027", "#f46d43", "#fdae61", "#fee090", "#ffffbf",
                           "#e0f3f8", "#abd9e9", "#74add1", "#4575b4", "#313695"]
#new variables added
MMVIZ_COLOR_NEUTRAL_LIGHT = "#E8E8E7"
MMVIZ_COLOR_NEUTRAL_MID = "#ACABA8"
MMVIZ_COLOR_NEUTRAL_DARK = "#555555"
MMVIZ_COLOR_BLUE_LIGHT = "#C1C9D5"
MMVIZ_COLOR_BLUE_DARK = "#5C6B7E"



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

    ax.set_title(ax.get_title(), fontproperties=TITLE_FONT_PROPERTIES)

    if chart_type == 'bar' or chart_type == 'bar-vertical' or chart_type == 'column' or chart_type == 'freqpoly' \
            or chart_type == 'histogram' or chart_type == 'boxplot' or chart_type == 'box' \
            or chart_type == 'jitter' :

        ax.xaxis.grid(False)

    elif chart_type == 'bar-horizontal' or chart_type == 'boxplot-horizontal':

        ax.yaxis.grid(False)

# Setup scale color based on type
def scale_palette_mm(type = "qual"):

    palette = get_palette(type)

    if palette != None:
        plt.rc('axes', prop_cycle=(cycler('color', palette)))


def get_palette(type = "qual"):

    if type == "qual_color" or type == "qual_dark":
        return MMVIZ_COLOR_PALETTE_QUAL_DARK

    if type == "qual" or type == "qual_fill" or type == "qual_light":
        return MMVIZ_COLOR_PALETTE_QUAL_LIGHT

    if type == "qual_alt_dark":
        return MMVIZ_COLOR_PALETTE_QUAL_ALT_DARK

    if type == "qual_alt" or type == "qual_alt_light":
        return MMVIZ_COLOR_PALETTE_QUAL_ALT_LIGHT

    if type == "seq":
        return MMVIZ_COLOR_PALETTE_SEQ

    if type == "div":
        return MMVIZ_COLOR_PALETTE_DIV

    return None

def get_palette_iter_mm(type = "qual"):
    return iter(get_palette(type))

