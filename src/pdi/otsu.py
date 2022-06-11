# See https://scikit-image.org/docs/dev/auto_examples/segmentation/plot_thresholding.html#sphx-glr-auto-examples-segmentation-plot-thresholding-py


import matplotlib.pyplot as plt
from skimage import data
from skimage.filters import threshold_otsu
import cv2

def otsu_segmentantion(image):
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    b, g, r = cv2.split(image)
    thresh = threshold_otsu(g)
    binary = g > thresh
    return binary
