# Reference docs: https://scikit-image.org/docs/dev/auto_examples/segmentation/plot_chan_vese.html

from skimage.segmentation import chan_vese
import cv2

def chan_vese_segmentation(image):    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv = chan_vese(image, mu=0.25, lambda1=1, lambda2=1, tol=1e-3,
               max_num_iter=200, dt=0.5, init_level_set="checkerboard",
               extended_output=True)
    
    # apply a limiar to the segmented image
    segmented = cv[0] > 0.5

    # invert segmentation when needed
    invert = False
    if segmented.mean() > 0.5:
        invert = True
    if invert:
        segmented = ~segmented

    return segmented