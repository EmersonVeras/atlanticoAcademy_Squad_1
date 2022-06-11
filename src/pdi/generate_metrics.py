
import matplotlib.pyplot as plt
from .chan_vese import chan_vese_segmentation
from .otsu import otsu_segmentantion
from .watershed import watershed_segmentation
from .kmeans import kmeans_segmentation

def segment(image):
    technique_01 = chan_vese_segmentation(image)
    technique_02 = otsu_segmentantion(image)
    technique_03 = kmeans_segmentation(image)
    return [technique_01, technique_02, technique_03]
