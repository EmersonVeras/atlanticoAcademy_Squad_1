import cv2
from file_utils import list_images

def convert_to_gold(name: str):
    """
    Converts an image to a gold standard.
    """
    image = cv2.imread(name)
    # image = image[::4,::4] # Diminui a imagem	
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
    suave = cv2.GaussianBlur(img_gray, (7, 7), 0) # aplica blur  
    (T, binI) = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY_INV)
    return binI

base_dir = "data/pdi/Raw imgs/"    
for img in list_images(base_dir):
    #name = 'Test\Img (' + str(i+1) + ').jpg'
    original = base_dir + img
    processed = "data/pdi/golden_patterns/" + img
    print(original,  " => ", processed)
    final_image = convert_to_gold(original)

    # uncomment the following line to write the image
    #cv2.imwrite(processed, final_image)