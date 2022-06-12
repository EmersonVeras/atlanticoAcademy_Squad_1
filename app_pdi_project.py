#import src.pdi.get_dims
#import src.pdi.generate_csv
from turtle import title
import cv2 as cv
from src.pdi.file_utils import list_images
from src.pdi.generate_metrics import segment
from src.pdi.generate_metrics import calculate_iof
from src.pdi.plot_utils import plot_images
from src.pdi.get_dims import get_dimensions
import matplotlib.pyplot as plt

def main():
    raw_imgs = list_images("data/pdi/Raw imgs")
    golden_pattern_imgs = list_images("data/pdi/golden_patterns")
    
    intersection = [img for img in raw_imgs if img in golden_pattern_imgs]
    print("Images that have a golden pattern of segmentation")
    print(intersection)
    
    target = intersection[0]
    img = cv.imread("data/pdi/Raw imgs/" +  target)
    golden_pattern = plt.imread("data/pdi/golden_patterns/" +  target).astype(int)[:,:,0]

    segmented_images = segment(img)

    images = [img, golden_pattern]
    images.extend(segmented_images)
    iou_results = calculate_iof(golden_pattern, segmented_images)
    print(iou_results)
    plot_images(images, ["Original", "Golden Pattern", "Chan vese", "Otsu", "KMeans"])



if __name__ == '__main__':
    main()
