from email.mime import base
from src.pdi.get_dims import get_dimensions # import get_dims file
import csv
import os
from src.pdi.file_utils import list_images
import cv2 as cv

# Create a folder named Golden imgs
# File name of the gold pattern image: img(n)_gold.jpg, where n = {0..19}

def report_image_dimensions(base_dir, csv_file_name="data.csv"):
    csv_height = []
    csv_width = []
    csv_max_height = []
    csv_max_width = []
    csv_area = []
    file_names = []
    files_list = list_images(base_dir)

    # Get dimensions of each golden pattern image
    with open(csv_file_name,mode= 'w') as csvfile:
        csv_file = csv.writer(csvfile, delimiter= ',', quoting= csv.QUOTE_MINIMAL)
        csv_file.writerow(['filename', 'original_height', 'original_width', 'max_height', 'max_width', 'area']) # Header

        for i, file in enumerate(files_list):
            full_path = base_dir + file
            file_names.insert(i, file)
            
            image = cv.imread(full_path, cv.IMREAD_GRAYSCALE)
            
            image = image > (127) # binary image
            h, w, mh, mw, area = get_dimensions(image)
            
            # Generate lists with the dimensions of each golden pattern image 
            csv_height.insert(i, h)
            csv_width.insert(i, w)
            csv_max_height.insert(i, mh)
            csv_max_width.insert(i, mw)
            
            # Area of the golden pattern image

            csv_area.insert(i, area) 
            
            csv_file.writerow([file_names[i], csv_height[i], csv_width[i], csv_max_height[i], csv_max_width[i], csv_area[i]])
            print('File ' + str(i) + ' - ' + full_path +' ok!') # Progress indicator

    print('Done!') # PVPP test print


if __name__ == '__main__':
    print('reporting metrics for golden pattern images')    
    report_image_dimensions('data/pdi/golden_patterns/', 'golden_patterns_dims.csv')