#import src.pdi.get_dims
#import src.pdi.generate_csv
from src.pdi.file_utils import list_images

def main():
    raw_imgs = list_images("data/pdi/Raw imgs")
    print(raw_imgs[0:10])
    golden_pattern_imgs = list_images("data/pdi/Golden pattern imgs")
    print(golden_pattern_imgs[0:10])
    intersection = [img for img in raw_imgs if img.replace('.jpg', '') + '_gold.jpg' in golden_pattern_imgs]
    print(intersection)

if __name__ == '__main__':
    main()