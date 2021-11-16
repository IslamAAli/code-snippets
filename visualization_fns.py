import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# --------------------------------------------------------------
# read the file list data and return them as a single list of lists for drawing
def read_files(files_list):
    data= []
    for filename in files_list:
        fn = os.path.join(dirname, filename)
        with open(fn) as f:
            lines = f.read().splitlines()

        data.append(list(map(float, lines)))

    return data

# --------------------------------------------------------------
# requires a figure to be already open
# takes location of the subplot in the format of 211, 2 rows, 1 column, 1st subplot
# list of files of data to be read and plotted
# option to include labels or not
# the plots can be either vertical or horizontal if needed
def draw_boxplot_figure(data_file_names, labels, tag, location, x_label, y_label, skip_labels, vertical):

    data = read_files(data_file_names)

    empty_labels= [''] * len(dlabels)
    plt.subplot(location)
    if not skip_labels:
        plt.boxplot(data, labels=labels, vert=vertical)
        plt.ylabel(y_label)
    else:
        plt.boxplot(data, labels=empty_labels, vert=vertical)
    plt.grid('major', axis='y')
    plt.xlabel(x_label)

# --------------------------------------------------------------
