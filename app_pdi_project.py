import cv2 as cv
from src.pdi.file_utils import list_images
from src.pdi.generate_metrics import segment
from src.pdi.generate_metrics import calculate_iou, best_score, name
from src.pdi.plot_utils import plot_images
from src.pdi.generate_csv import report_image_dimensions
import matplotlib.pyplot as plt
import pandas as pd

def main():
    raw_imgs = list_images("data/pdi/Raw imgs")
    golden_pattern_imgs = list_images("data/pdi/golden_patterns")
    
    intersection = [img for img in raw_imgs if img in golden_pattern_imgs]
    print("Images that have a golden pattern of segmentation[" + str(len(intersection)) + "]:")
    print(intersection)
    print()
    
    report_image_dimensions('data/pdi/golden_patterns/', 'golden_patterns_dims.csv')
    
    #intersection = ['Imgs (40).jpg', 'IMG_20220604_082844.jpg']
    iou_results = []
    total_images = len(intersection)
    for i, target in enumerate(intersection):
        print("Processing {} | ({} of {})".format(target, i, total_images))
        img = cv.imread("data/pdi/Raw imgs/" +  target)
        golden_pattern = plt.imread("data/pdi/golden_patterns/" +  target).astype(int)[:,:,0]
        filename = "data/pdi/segmented/" + target
        segmented_images = segment(img) 
        
        iou_results.append([target] + calculate_iou(golden_pattern, segmented_images))

        images = [img, golden_pattern] + segmented_images
        plot_images(images, ["Original", "Golden Pattern", "Chan Vese", "Otsu", "K-Means"], filename)
    
    df = pd.DataFrame(iou_results, columns=["file"] + [name(i) for i in range(0, 3)])
    df.to_csv('iou_metrics.csv')

    best = best_score(iou_results)
    #best = 2
    print("\nBest technique is " + name(best))

    for i, target in enumerate(intersection):        
        print("Processing {} with {} | ({} of {})".format(target, name(best), i, total_images))
        img = cv.imread("data/pdi/Raw imgs/" +  target)        
        filename = "data/pdi/best/" + target
        segmented_images = segment(img, technique=best)

        images = [img, segmented_images[0]]
        plot_images(images, ["Original", name(best)], filename)
        cv.imwrite("data/pdi/raw_segmented_best/" +  target, segmented_images[0]*255)

    report_image_dimensions('data/pdi/raw_segmented_best/', 'best_seg_dims.csv')
    

if __name__ == '__main__':
    main()
