# See https://scikit-image.org/docs/dev/auto_examples/segmentation/plot_thresholding.html#sphx-glr-auto-examples-segmentation-plot-thresholding-py


import matplotlib.pyplot as plt
from skimage import data
from skimage.filters import threshold_otsu

def otsu_segmentantion(image):
    thresh = threshold_otsu(image)
    binary = image > thresh
    return binary
