import sys, fitz
import csv

sys.stdout.reconfigure(encoding='utf-8')


def read_file(file_path):
    """
    This function reads a file and returns its content as a string.
    Author: Paulo Vinicius P. Pinheiro
    Date: April, 2022
    Ver: 1.0

    :param file_path: string with the path to the document.
    :return: the document in string type.

    """

    doc = fitz.open(file_path)  # open document
    for page in doc: 
        text = page.get_text().encode("utf8")  # get plain text (is in UTF-8)

    text_str = text.decode("utf8")
    return text_str


def format_and_generate_csv(all_words, all_tf, all_df, all_idf, all_tf_idf):
    """
    Generate a CSV file with all the words from the documents and the respective nearest words and its weights

    :param all_words: All documents' words (tokens).
    :param all_tf: All documents' TF.
    :param all_df: All documents' DF.
    :param all_idf: All documents' IDF.
    :param all_tf_idf: All documents' TF-IDF.

    """

    print(0)

    # with open('data/nlp/data.csv', 'w', encoding='UTF-8') as f:
    #     writer = csv.writer(f)

