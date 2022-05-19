# This module is to extract the pages from pdf as well as to find the total number of pages

import pdfplumber
import PyPDF2
# The files above ☝️ are needed to extract pages from pdf
import audio
# ☝ This is the module to read extracted text

# ************** Function to get the total pages in the pdf **********************


def extract_page_no(file_name):
    """
    Returns the number of pages in the pdf file \n
    :param file_name: Name of pdf file, including path
    :return: Number of pages in the pdf
    """
    file = open(file_name, 'rb')
    pages = PyPDF2.PdfFileReader(file).numPages
    file.close()
    return pages
# ***************** Function ends here *************************

# ****************** Function to extract text from each page of pdf **********************

def extract_page(file_name, start, end):
    """
    Function extracts the text in the pdf "file_name", starting from page number "start" to page number "end".\n
    :param file_name: name of the pdf file, including file path
    :param start: page number of first page to be extracted
    :param end: page number of last page to be extracted.
    :return: None
    """
    try:
        end_pg = int(end)
    except ValueError:
        end_pg = extract_page_no(file_name)     # The total pages in pdf is calculated and store in 'end_pg' variable

    with pdfplumber.open(file_name) as pdf:     # Extracting pages from pdf
        for pages in pdf.pages[start-1: end_pg]:
            print(pages.extract_text())         # After extraction the text is printed
            audio.audio(pages.extract_text())   # The audio module is called here

# ****************** Function ends here ********************************
