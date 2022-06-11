#import src.pdi.get_dims
#import src.pdi.generate_csv
from turtle import title
import cv2 as cv
from src.pdi.file_utils import list_images
from src.pdi.generate_metrics import segment
from src.pdi.plot_utils import plot_images

def main():
    raw_imgs = list_images("data/pdi/Raw imgs")
    golden_pattern_imgs = list_images("data/pdi/golden_patterns")
    
    intersection = [img for img in raw_imgs if img in golden_pattern_imgs]
    print(intersection)

    
    target = "data/pdi/Raw imgs/" + list_images("data/pdi/Raw imgs")[1]
    img = cv.imread(target)
    segmented_images = segment(img)

    images = [img]
    images.extend(segmented_images)
    plot_images(images, ["Original", "1", "2", "3"])



if __name__ == '__main__':
    main()