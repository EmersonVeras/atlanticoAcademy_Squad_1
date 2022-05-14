from collections import Counter
import math
from nltk import FreqDist


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

    :return: TF, IDF and TF_IDF values.
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

    return tf, idf, tf_idf


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
            if i != 0 and word_compare==word:
                near_word[words[i+1]] = tf[words[i+1]]
                near_word[words[i-1]] = tf[words[i-1]]
            near_words_list[word] = near_word

    return near_words_list
