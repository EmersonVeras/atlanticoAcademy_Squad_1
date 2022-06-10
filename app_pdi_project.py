#import src.pdi.get_dims
#import src.pdi.generate_csv
from turtle import title
import cv2 as cv
from src.pdi.file_utils import list_images
#from src.pdi.generate_metrics import segment
from src.pdi.plot_utils import plot_images

def main():
    raw_imgs = list_images("data/pdi/Raw imgs")
    #print(raw_imgs[0:10])
    golden_pattern_imgs = list_images("data/pdi/Golden pattern imgs")
    #print(golden_pattern_imgs[0:10])
    
    intersection = [img for img in raw_imgs if img.replace('.jpg', '') + '_gold.jpg' in golden_pattern_imgs]
    print(intersection)

    #print([img.replace('.jpg', '') + '_gold.jpg' for img in raw_imgs])
    paths = ["data/pdi/Raw imgs/" + img for img in list_images("data/pdi/Raw imgs")[0:3]]
    images = [cv.imread(path) for path in paths]
    

    plot_images(images, paths)



if __name__ == '__main__':
    main()