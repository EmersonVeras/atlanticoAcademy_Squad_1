import sys, fitz
sys.stdout.reconfigure(encoding='utf-8')

def read_file(fname):
    '''
    This function reads a file and returns its content as a string.
    Author: Paulo Vinicius P. Pinheiro
    Date: April, 2022
    Ver: 1.0
    '''
    doc = fitz.open(fname)  # open document
    for page in doc: 
        text = page.get_text().encode("utf8")  # get plain text (is in UTF-8)

    text_str = text.decode("utf8")
    return text_str

