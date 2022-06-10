from .chan_vese import chan_vese_segmentation
from .otsu import otsu_segmentantion
import matplotlib.pyplot as plt


def segment(image):
    technique_01 = chan_vese_segmentation(image)
    technique_02 = otsu_segmentantion(image)
    return [technique_01, technique_02]
