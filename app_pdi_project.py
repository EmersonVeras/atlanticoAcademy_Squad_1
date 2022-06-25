#import src.pdi.get_dims
#import src.pdi.generate_csv
from fileinput import filename
from turtle import title
import cv2 as cv
from src.pdi.file_utils import list_images
from src.pdi.generate_metrics import segment
from src.pdi.generate_metrics import calculate_iou, best_score, name
from src.pdi.plot_utils import plot_images
from src.pdi.get_dims import get_dimensions
import matplotlib.pyplot as plt

def main():
    raw_imgs = list_images("data/pdi/Raw imgs")
    golden_pattern_imgs = list_images("data/pdi/golden_patterns")
    
    intersection = [img for img in raw_imgs if img in golden_pattern_imgs]
    print("Images that have a golden pattern of segmentation[" + str(len(intersection)) + "]:")
    print(intersection)
    
    target = intersection[0]

    iou_results = []
    for target in intersection:
        print("Processing " + target)
        img = cv.imread("data/pdi/Raw imgs/" +  target)
        golden_pattern = plt.imread("data/pdi/golden_patterns/" +  target).astype(int)[:,:,0]
        filename = "data/pdi/segmented/" + target
        segmented_images = segment(img)    
        iou_results.append(calculate_iou(golden_pattern, segmented_images))

        images = [img, golden_pattern]
        images.extend(segmented_images)
        plot_images(images, ["Original", "Golden Pattern", "Chan vese", "Otsu", "KMeans"], filename)

    best = best_score(iou_results)
    print("Best technique is " + name(best))
    
    



if __name__ == '__main__':
    main()
