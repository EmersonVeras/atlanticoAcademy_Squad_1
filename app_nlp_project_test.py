from encodings import normalize_encoding
from typing import Text
import src.utils.read_file as rf
from src.nlp.preprocessing import TextPreprocessor
import src.nlp.text_processing as txt_process
from src.nlp.text_processing import create_dataframe, generate_csv
from src.nlp.visualization import plot_graph

# All three text files in on single array -> pdf_files
pdf_files = [rf.read_file('data/nlp/texto1.pdf'), rf.read_file('data/nlp/texto2.pdf'), rf.read_file('data/nlp/texto3.pdf')]

preprocessor = TextPreprocessor()

stage0 = preprocessor.transform(pdf_files[0])

text_tokenized = [preprocessor.transform(text) for text in pdf_files]
tf, df, idf, tf_idf, tf_mean, tf_idf_mean = txt_process.get_data_information(text_tokenized)

near_words_list = [txt_process.get_near_terms(text_tokenized[i], tf[i], tf_idf[i]) for i in range(3)]
sum_near_words_list = dict(near_words_list[0], **near_words_list[1], **near_words_list[2])

print(sum_near_words_list)
# near_words_df = {sum_near_words_list.keys(): sum_near_words_list.values()}
# near_words_df = pd.DataFrame(near_words_df)

new_df = create_dataframe(tf_mean, df, idf, tf_idf_mean)

generate_csv('values.csv', new_df)
plot_graph(new_df, sum_near_words_list)