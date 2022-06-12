
import matplotlib.pyplot as plt
from .chan_vese import chan_vese_segmentation
from .otsu import otsu_segmentantion
from .kmeans import kmeans_segmentation
import numpy as np
from src.pdi.plot_utils import plot_images

def segment(image):
    technique_01 = chan_vese_segmentation(image)
    technique_02 = otsu_segmentantion(image)
    technique_03 = kmeans_segmentation(image)
    return [technique_01, technique_02, technique_03]


def calculate_iof(golden_pattern, comparatives):
    iou_results = []
    for comparative in comparatives:
        intersection = np.logical_and(golden_pattern, comparative)
        union = np.logical_or(golden_pattern, comparative)

        iou_results.append(np.sum(intersection)/np.sum(union))

    return iou_results
