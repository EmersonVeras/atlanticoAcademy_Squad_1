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

    frequency_count = freq_texts.copy()
    frequency_count[0] = {x: 1.0 for x, y in frequency_count[0].items()}
    frequency_count[1] = {x: 1.0 for x, y in frequency_count[1].items()}
    frequency_count[2] = {x: 1.0 for x, y in frequency_count[2].items()}

    df = dict(Counter(frequency_count[0]) + Counter(frequency_count[1]) + Counter(frequency_count[2])) #DF calculation

    idf = df.copy()
    idf.update((x, math.log10(float(n_docs/y))) for x, y in idf.items()) #IDF calculation

    tf_idf = []
    tf_idf.append({x:y*tf[0][x] for x, y in idf.items() if x in tf[0]}) # TF_IDF calculation from the first document
    tf_idf.append({x:y*tf[1][x] for x, y in idf.items() if x in tf[1]}) # TF_IDF calculation from the second document
    tf_idf.append({x:y*tf[2][x] for x, y in idf.items() if x in tf[2]}) # TF_IDF calculation from the third document

    return tf, df, idf, tf_idf


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
    
    words = []
    words.append([_word for _word in tf[0]] + [_word for _word in tf[1]] + [_word for _word in tf[2]])
    
    tf_list = []
    tf_list.append([_tf for _tf in tf[0].values()] + [_tf for _tf in tf[1].values()] + [_tf for _tf in tf[2].values()])

    df = list(df.values())
   
    idf = list(idf.values())
    
    tf_idf_list = []
    tf_idf_list.append([_tf_idf for _tf_idf in tf_idf[0].values()]+[_tf_idf for _tf_idf in tf_idf[1].values()]+[_tf_idf for _tf_idf in tf_idf[2].values()])
    
    print(len(np.array(words).flatten()), len(np.array(tf_list).flatten()), len(np.array(df).flatten()), 
          len(np.array(idf).flatten()), len(np.array(tf_idf_list).flatten()))
    

    # data = {'Words': np.array(words).flatten(), 'tf': np.array(tf_list).flatten(),
    #         'df': np.array(df_list).flatten(), 'idf': np.array(idf_list).flatten(), 'tf_idf': np.array(tf_idf_list).flatten()}  
    # new_dataframe = pd.DataFrame(data)
    # print(new_dataframe)
    
    
    # print(words)
    # return tf
    
