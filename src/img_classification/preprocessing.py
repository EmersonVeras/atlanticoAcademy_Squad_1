""""
Preprocessing functions.
"""

# Imports from third parties
import numpy as np
import cv2 as cv
from PIL import Image

# Imports from our own code
from file_utils import list_all_inputs


"""

See: https://arxiv.org/pdf/1409.1556.pdf
    VERY DEEP CONVOLUTIONAL NETWORKS FOR LARGE-SCALE IMAGE RECOGNITION
    https://machinelearningmastery.com/best-practices-for-preparing-and-augmenting-image-data-for-convolutional-neural-networks/
    https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html
"""
def subtract_mean_rgb_value(*images):
    pass

"""
See 
    https://stackoverflow.com/questions/15007304/histogram-equalization-not-working-on-color-image-opencv
    However, when we have a color image, we first need to convert the image to the YUV
    color format. The Y is the luma, or brightness, and U and V denote the color. After
    the conversion, we can apply equalizeHist to the image and then convert it back to
    BGR or RGB:
"""
def histogram_equalization(img):
    image_bgr = img
    image_yuv = cv.cvtColor(image_bgr, cv.COLOR_BGR2YUV)
    image_yuv[:, :, 0] = cv.equalizeHist(image_yuv[:, :, 0])

    image_bgr = cv.cvtColor(image_yuv, cv.COLOR_YUV2BGR)
    return image_bgr



def read_normalize_img(f):
    x = np.array(cv.resize(cv.imread(f), (224,224), interpolation = cv.INTER_AREA))
    #x = cv.imread(f)
    #x = x/255
    return x
    

def test_subtract_mean_rgb_value():
    (folders, labels) = list_all_inputs()
    sample = folders[0][0]
    print(sample)
    x = read_normalize_img(sample)
    #Image.fromarray(x, 'RGB').show()
    #cv.imshow("sample", x)
    #cv.waitKey(0)
    equalized = histogram_equalization(x)
    cv.imshow("equalized", np.concatenate((x, equalized), axis=1))
    cv.waitKey(0)

if __name__ == '__main__':
    test_subtract_mean_rgb_value()