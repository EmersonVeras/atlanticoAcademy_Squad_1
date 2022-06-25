# import doctest
from pydoc import doc
from turtle import width
import cv2
import numpy as np
from pandas import array
# from matplotlib import pyplot as plt

# name = 'Test\img(' + str(1+1) + ')_gold.jpg'

def get_dimensions(image):
    """
    Gets the dimensions of a binary image.
    By default we assume that the objet being measured is white, and the background is black.
    Args:
        image: binary image
    Returns:
        tuple with width, heigth and area of the image.
    """    
    count = []
    hor = 0
    #image = cv2.imread(name)

    for y in range(0, image.shape[0]):
        for x in range(0, image.shape[1]):
            if (image[y, x] == True).any():
                hor+=1
        count.append((hor))
        hor = 0

    height = image.shape[0]
    width = image.shape[1]
    max_height = image.shape[0] - count.count(0)
    max_width = max(count)

    # since this is a binary image, sum will return the number of white pixels 
    area = sum(sum(image))
    return height, width, max_height, max_width, area