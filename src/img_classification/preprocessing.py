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

    A mean pixel value was then subtracted from each pixel, referred to as centering. 
    It is believed that this was performed per-channel: that is mean pixel values were estimated 
    from the training dataset, one for each of the red, green, and blue channels of the color images.
"""
def subtract_mean_bgr_value(img):
    b, g, r = cv.split(img)

    b = b - int(b.mean())

    g = g - int(g.mean())

    r = r - int(r.mean())

    return cv.merge((b, g, r))


def subtract_mean_yuv_value(image_bgr):
    image_yuv = cv.cvtColor(image_bgr, cv.COLOR_BGR2YUV)
    image_yuv[:, :, 0] = image_yuv[:, :, 0] - image_yuv[:, :, 0].mean()
    return cv.cvtColor(image_yuv, cv.COLOR_YUV2BGR)

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

def bilateral_filter(img):
    return cv.bilateralFilter(img, 15, 75, 75)

def median_filter(img):
    return cv.medianBlur(img, 5)

def sharpen(img):
    kernel_sharpening = np.array([[-1,-1,-1], 
                              [-1,9,-1], 
                              [-1,-1,-1]])
    return cv.filter2D(img, -1, kernel_sharpening)

def sobel_filter(img):
    image_bgr = img
    image_yuv = cv.cvtColor(image_bgr, cv.COLOR_BGR2YUV)
    image_yuv[:, :, 0] = cv.Sobel(image_yuv[:, :, 0], cv.CV_64F, 1, 0, ksize=5)

    image_bgr = cv.cvtColor(image_yuv, cv.COLOR_YUV2BGR)
    return image_bgr

def blur(img):
    return cv.blur(img,(5,5))

def read_normalize_img(f):
    x = np.array(cv.resize(cv.imread(f), (224,224), interpolation = cv.INTER_AREA))
    #x = cv.imread(f)
    #x = x/255
    return x
    

# Tests

def get_sample_image():
    (folders, labels) = list_all_inputs()
    sample = folders[0][0]    
    return read_normalize_img(sample)


def test_histogram_equalization():    
    x = get_sample_image()
    equalized = histogram_equalization(x)
    cv.imshow("equalized", np.concatenate((x, equalized), axis=1))
    cv.waitKey(0)

def test_subtract_mean_bgr_value():
    x = get_sample_image()
    centered = subtract_mean_bgr_value(x)
    cv.imshow("centered", np.concatenate((x, centered), axis=1))
    print(x.dtype)
    print(x.max())

    print(centered.dtype)
    print(centered.max())

    #cv.imshow("centered", x)
    cv.waitKey(0)

def test_subtract_mean_yuv_value():
    x = get_sample_image()
    centered = subtract_mean_yuv_value(x)
    cv.imshow("centered", np.concatenate((x, centered), axis=1))
    print(x.dtype)
    print(x.max())

    print(centered.dtype)
    print(centered.max())


    #cv.imshow("centered", x)
    cv.waitKey(0)

def test_blur():
    x = get_sample_image()
    blurred = blur(x)
    cv.imshow("blurred", np.concatenate((x, blurred), axis=1))
    cv.waitKey(0)
    

def test_median_filter():
    x = get_sample_image()
    median = median_filter(x)
    cv.imshow("median", np.concatenate((x, median), axis=1))
    cv.waitKey(0)


def test_bilateral_filter():
    x = get_sample_image()
    bilateral = bilateral_filter(x)
    cv.imshow("bilateral", np.concatenate((x, bilateral), axis=1))
    cv.waitKey(0)

def test_sobel_filter():
    x = get_sample_image()
    sobel = sobel_filter(x)
    cv.imshow("sobel", np.concatenate((x, sobel), axis=1))
    cv.waitKey(0)


def test_hist_equ_bilat_filter():
    x = get_sample_image()
    
    x2 = bilateral_filter(x)
    x2 = histogram_equalization(x2)
    
    cv.imshow("hist_equ_bilat_filter", np.concatenate((x, x2), axis=1))
    cv.waitKey(0)

def test_sharpen():
    x = get_sample_image()    
    cv.imshow("sharpen", np.concatenate((x, sharpen(x)), axis=1))
    cv.waitKey(0)

if __name__ == '__main__':
    #test_histogram_equalization()
    #test_subtract_mean_bgr_value()
    #test_subtract_mean_yuv_value()
    #test_blur()
    #test_median_filter()
    test_sharpen()
    #test_bilateral_filter()
    #test_hist_equ_bilat_filter()
    #test_sobel_filter()