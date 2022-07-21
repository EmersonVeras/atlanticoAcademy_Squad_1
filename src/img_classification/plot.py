"""
Plot of several grapths
"""
import pandas as pd
from matplotlib import pyplot as plt

def plot_metric(file, metric='accuracy'):
    df = pd.read_csv(file)
    plt.plot(df[metric])
    plt.plot(df['val_' + metric])
    plt.title('model ' + metric)
    plt.ylabel(metric)
    plt.xlabel('epoch')
    plt.legend(['train', 'val'], loc='upper left')
    plt.show()


if __name__ == "__main__":
    plot_metric('output/bilat_filter_hist_equalization_log.csv', metric='precision')