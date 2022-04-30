import read_file as rf

# All three text files in on single array -> pdf_files
pdf_files = [rf.read_file('texto1.pdf'), rf.read_file('texto2.pdf'), rf.read_file('texto3.pdf')]

# Testing the read_file function
print(pdf_files)