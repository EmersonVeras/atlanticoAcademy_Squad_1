from typing import final
import cv2
from pandas import array

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


    
for i in range(20):
    name = 'Test\Img (' + str(i+1) + ').jpg'
    final_image = convert_to_gold(name)
    cv2.imwrite('Test\img(' + str(i+1) + ')_gold.jpg', final_image)