# Reference docs: https://scikit-image.org/docs/dev/auto_examples/segmentation/plot_chan_vese.html

import matplotlib.pyplot as plt
from skimage import data, img_as_float
from skimage.segmentation import chan_vese


def chan_vese_segmentation(image):
    image = img_as_float(image)
    cv = chan_vese(image, mu=0.25, lambda1=1, lambda2=1, tol=1e-3,
               max_num_iter=200, dt=0.5, init_level_set="checkerboard",
               extended_output=True)
    return cv[0]