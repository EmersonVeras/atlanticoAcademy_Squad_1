from .chan_vese import chan_vese_segmentation
from .otsu import otsu_segmentantion
from .kmeans import kmeans_segmentation
import numpy as np
from src.pdi.plot_utils import plot_images
import pandas as pd

def segment(image, technique = None):
    """
    Apply one or all segmentation techniques to a given image.
    """
    techniques = [chan_vese_segmentation, otsu_segmentantion, kmeans_segmentation]
    if technique is None:
        return [f(image) for f in techniques]    
    elif technique >=0 and technique<=2:
        return [techniques[technique](image)]
    else:
        raise Exception("Unknown technique " + str(technique))
        
def name(technique):
    if technique >=0 and technique<=2:
        names = ["Chan Vese", "Otsu", "K-Means"]
        return names[technique]
    else:
        raise Exception("Unknown technique " + str(technique))

def calculate_iou(golden_pattern, comparatives):
    iou_results = []
    for comparative in comparatives:
        intersection = np.logical_and(golden_pattern, comparative)
        union = np.logical_or(golden_pattern, comparative)

        iou_results.append(np.sum(intersection)/np.sum(union))

    return iou_results


def best_score(iou_results_matrix):
    """
    Given a matrix of IOU metrics, find the index of the best score based on the mean
    """
    df = pd.DataFrame(iou_results_matrix)
    return df.mean().idxmax()    