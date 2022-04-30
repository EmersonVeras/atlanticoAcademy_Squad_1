import sys, fitz
sys.stdout.reconfigure(encoding='utf-8')

def read_file(fname):
    '''
    This function reads a file and returns its content as a string.
    Author: Paulo Vinicius P. Pinheiro
    Date: April, 2020
    Ver: 1.0
    '''
    doc = fitz.open(fname)  # open document
    out = open(fname + ".txt", "wb")  # open text output
    for page in doc:  # iterate the document pages
        text = page.get_text().encode("utf8")  # get plain text (is in UTF-8)
        out.write(text)  # write text of page
        out.write(bytes((12,)))  # write page delimiter (form feed 0x0C)
    out.close()

    text_str = text.decode("utf8")
    return text_str

