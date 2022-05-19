# Extract text from pdf
This part extracts the text from the required pages of pdf.

If the user has specified a proper value for the end page, the program extracts the text from starting page to end page. It prints the text on each page and then reads it out; once it finishes reading, it prints the contents of next page and reads it out. This continues till the end page.

If the end page value is invalid or not specified, then the program reads the content from starting page to end of the pdf.

Two python libraries were imported to implement this part:
  1. [pyPDF2](https://pypi.org/project/PyPDF2/)   ->  Was used to count the number of pages
  2. [pdfplumber](https://medium.com/analytics-vidhya/how-to-easily-extract-text-from-any-pdf-with-python-fc6efd1dedbe)   ->  Was used to extract the text from each page

> Note: When the extracted text is read out, it seems to put a pause upon encountering a newline. This is not needed as we apply pause only when encountering punctuation marks. So before sending the text to pyttsx3, the newline character (\n) is replaced by white spaces using the replace method.
