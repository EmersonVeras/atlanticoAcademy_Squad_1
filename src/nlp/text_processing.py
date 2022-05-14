from collections import Counter
import math
from nltk import FreqDist
import pandas as pd
import numpy as np

def calculate_tf(frequency, total_words):
    """
    This function is used to calculate the TF value using the frequency and the frequency sum from the words.

    :param frequency: Is the frequency of the words on a document.
    :param total_words: Is the total of words on this document.
    :return: The TF value.
    """
    freq = frequency.copy()
    freq.update((x, y/total_words) for x, y in freq.items())
    return freq


def get_data_information(texts):
    """
    This function is used to extract information from a set of documents (TF, IDF, TF_IDF).

    :return: TF, DF, IDF and TF_IDF values.
    """

    n_docs = 3.0 #number of documents

    freq_texts = [dict(FreqDist(text)) for text in texts]
    sum_words = [sum(list(freq.values())) for freq in freq_texts]
    tf = [calculate_tf(frequency, sum) for frequency, sum in zip(freq_texts, sum_words)] #TF calculation

    tf_mean = dict(Counter(tf[0]) + Counter(tf[1]) + Counter(tf[2]))
    for item, count in tf_mean.items():
        tf_mean[item] /= 3

    frequency_count = freq_texts.copy()
    frequency_count[0] = {x: 1.0 for x, y in frequency_count[0].items()}
    frequency_count[1] = {x: 1.0 for x, y in frequency_count[1].items()}
    frequency_count[2] = {x: 1.0 for x, y in frequency_count[2].items()}

    df = dict(Counter(frequency_count[0]) + Counter(frequency_count[1]) + Counter(frequency_count[2])) #DF calculation

    idf = df.copy()
    idf.update((x, math.log10(float(n_docs/y))) for x, y in idf.items()) #IDF calculation

    tf_idf = []
    tf_idf.append({x:y*tf_mean[x] for x, y in idf.items() if x in tf[0]}) # TF_IDF calculation from the first document
    tf_idf.append({x:y*tf_mean[x] for x, y in idf.items() if x in tf[1]}) # TF_IDF calculation from the second document
    tf_idf.append({x:y*tf_mean[x] for x, y in idf.items() if x in tf[2]}) # TF_IDF calculation from the third document

    # tf_idf_mean = dict(Counter(tf_idf[0]) + Counter(tf_idf[1]) + Counter(tf_idf[2]))

    tf_idf_mean = {x:y*tf_mean[x] for x, y in idf.items()}

    return tf, df, idf, tf_idf, tf_mean, tf_idf_mean


def get_near_terms(words, tf, tf_idf):
    """
    Get the two nearest terms from the 5 main words from a document.

    :param words: Document tokens pre-processed.
    :param tf: TF from the document.
    :param tf_idf: TF-IDF from the document.

    :return: A dictionary with the nearest words and the respective tf.
    """

    near_words_list = {}
    tf_idf_counter = Counter(tf_idf)
    five_most_common = dict(tf_idf_counter.most_common(5)).keys()

    for word in five_most_common:
        near_word = {}
        for i, word_compare in enumerate(words):
            if i != 0 and i<len(words) and word_compare==word:
                near_word[words[i+1]] = tf[words[i+1]]
                near_word[words[i-1]] = tf[words[i-1]]
            elif i == 0 and word_compare==word:
                near_word[words[i+1]] = tf[words[i+1]]
            elif i == len(words) and word_compare==word:
                near_word[words[i-1]] = tf[words[i-1]]

            near_words_list[word] = near_word

    return near_words_list

def create_dataframe(tf, df, idf, tf_idf):
    
    words = list(tf.keys())
    tf_list = list(tf.values())
    df_list = list(df.values())
   
    idf_list = list(idf.values())
    
    tf_idf_list = list(tf_idf.values())

    # print(len(words), len(tf_list), len(np.array(df_list).flatten()), 
    #       len(np.array(idf_list).flatten()), len(np.array(tf_idf_list).flatten()))
    

    data = {'Words': words, 'tf': tf_list,
            'df': np.array(df_list).flatten(), 'idf': np.array(idf_list).flatten(), 'tf_idf': np.array(tf_idf_list).flatten()}  
    new_dataframe = pd.DataFrame(data)
    return new_dataframe
    
def generate_csv(file, database):
    df = database
    return df.to_csv(file, index = False)
    
