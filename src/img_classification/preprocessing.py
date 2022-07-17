""""
Preprocessing functions.
"""

# Imports from third parties

# Imports from our own code
from file_utils import list_all_inputs

print(list_all_inputs())

"""

See: https://arxiv.org/pdf/1409.1556.pdf
    VERY DEEP CONVOLUTIONAL NETWORKS FOR LARGE-SCALE IMAGE RECOGNITION
    https://machinelearningmastery.com/best-practices-for-preparing-and-augmenting-image-data-for-convolutional-neural-networks/
    https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html
"""
def subtract_mean_rgb_value(*images):
    pass