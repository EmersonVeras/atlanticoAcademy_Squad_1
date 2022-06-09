# import doctest
from pydoc import doc
from turtle import width
import cv2
import numpy as np
from pandas import array
# from matplotlib import pyplot as plt

# name = 'Test\img(' + str(1+1) + ')_gold.jpg'

def get_dimensions(name: str):
    """
    Gets the dimensions of an golden pattern image.
docstring
    Args:
        name (_type_): _description_

    Returns:
        _type_: _description_
    """    
    count = []
    hor = 0
    image = cv2.imread(name)

    for y in range(0, image.shape[0]):
        for x in range(0, image.shape[1]):
            if (image[y, x] == 255).any():
                hor+=1
        count.append((hor))
        hor = 0

    height = image.shape[0]
    width = image.shape[1]
    max_height = image.shape[0] - count.count(0)
    max_width = max(count)
    return height, width, max_height, max_width