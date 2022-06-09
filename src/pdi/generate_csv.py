from get_dims import get_dimensions # import get_dims file
import csv
import os

# Create a folder named Golden imgs
# File name of the gold pattern image: img(n)_gold.jpg, where n = {0..19}
# Should we create separate functions here? At least two?

csv_height = []
csv_width = []
csv_max_height = []
csv_max_width = []
csv_area = []
file_names = []

# Count the number of files in the directory Golden imgs
files_list = os.listdir('./Golden imgs') # dir is your directory path
number_files = len(files_list)

# Generate the CSV file - data.csv
csv_file_name = './data.csv'

# Get dimensions of each golden pattern image
with open(csv_file_name,mode= 'w') as csvfile:
    file = csv.writer(csvfile, delimiter= ',', quoting= csv.QUOTE_MINIMAL)
    file.writerow(['File_name','Original_height','Original_width','Max_height','Max_width','Area']) # Header

    for i in range(0, number_files):
        name = './Golden imgs/img(' + str(i) + ')_gold.jpg'
        file_names.insert(i, name)
        h, w, mh, mw = get_dimensions(name)
        
        # Generate lists with the dimensions of each golden pattern image 
        csv_height.insert(i, h)
        csv_width.insert(i, w)
        csv_max_height.insert(i, mh)
        csv_max_width.insert(i, mw)
        
        # Area of the golden pattern image
        csv_area.insert(i, csv_max_height[i] * csv_max_width[i]) 
        
        file.writerow([file_names[i], csv_height[i], csv_width[i], csv_max_height[i], csv_max_width[i], csv_area[i]])
        print('File ' + str(i) + ' ok!') # Progress indicator

print('Done!') # PVPP test print