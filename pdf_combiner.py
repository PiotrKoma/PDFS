import PyPDF2
import sys

inputs = sys.argv[1:]


def pdf_combiner(pdf_lits):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_lits:
        print(pdf)
        merger.append(pdf)
    merger.write("GIGA.pdf")


pdf_combiner(inputs)