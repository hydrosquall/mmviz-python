# create bin list based on values list and bin_width
def create_bin_list(values, bin_width = 30):

    max_value = values.max()
    min_value = values.min()

    max_bin = (max_value - (max_value % bin_width) + bin_width) + bin_width
    min_bin = (min_value - (min_value % bin_width))

    bin_list = [i for i in range(min_bin, max_bin, bin_width)]
    return bin_list

