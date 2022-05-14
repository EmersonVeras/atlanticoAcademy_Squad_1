from typing import Text
import src.utils.read_file as rf
from src.nlp.preprocessing import TextPreprocessor
import src.nlp.text_processing as txt_process
from src.nlp.cloud import create_cloud

# All three text files in on single array -> pdf_files
pdf_files = [rf.read_file('data/nlp/texto1.pdf'), rf.read_file('data/nlp/texto2.pdf'), rf.read_file('data/nlp/texto3.pdf')]

# Testing the read_file function
print(pdf_files[0])

preprocessor = TextPreprocessor()

stage0 = preprocessor.transform(pdf_files[0])

text_tokenized = [preprocessor.transform(text) for text in pdf_files]
tf, df, idf, tf_idf = txt_process.get_data_information(text_tokenized)
# print(df.values())
near_words_list = [txt_process.get_near_terms(text_tokenized[i], tf[i], tf_idf[i]) for i in range(3)]
# print(tf)

sum_near_words_list = dict(near_words_list[0], **near_words_list[1], **near_words_list[2])


txt_process.create_dataframe(tf, df, idf, tf_idf)


