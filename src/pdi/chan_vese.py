# Reference docs: https://scikit-image.org/docs/dev/auto_examples/segmentation/plot_chan_vese.html

from skimage.segmentation import chan_vese
import cv2


def chan_vese_segmentation(image):
    #image = img_as_float(image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv = chan_vese(image, mu=0.25, lambda1=1, lambda2=1, tol=1e-3,
               max_num_iter=200, dt=0.5, init_level_set="checkerboard",
               extended_output=True)
    # as last step, apply a limiar to the segmented image
    segmented = cv[0] > 0.5
    return segmented