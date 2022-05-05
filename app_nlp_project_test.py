from typing import Text
import src.utils.read_file as rf
from src.nlp.preprocessing import TextPreprocessor

# All three text files in on single array -> pdf_files
pdf_files = [rf.read_file('data/nlp/texto1.pdf'), rf.read_file('data/nlp/texto2.pdf'), rf.read_file('data/nlp/texto3.pdf')]

# Testing the read_file function
#print(pdf_files)

preprocessor = TextPreprocessor()

stage0 = preprocessor.transform(pdf_files[0])
print(sorted(stage0))
    

