import os 
import glob

"""
Returns:
    A list with one list of filenames for every input directory
    A list with the corresponding labels for each directory
"""
def list_all_inputs():
  base_dir = '../../data/faces-classification/'
  felipe_dir = glob.glob(os.path.join(base_dir + 'felipe/', '*'))
  emerson_dir = glob.glob(os.path.join(base_dir + 'emerson/', '*'))
  luan_dir = glob.glob(os.path.join(base_dir + 'luan/', '*'))
  X_path = [felipe_dir, emerson_dir, luan_dir]
  return X_path, ['felipe', 'emerson', 'luan']