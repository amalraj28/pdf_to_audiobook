# main code

from page_extraction import *   # page_extraction is a module which I created
file = input('Enter the file name (with path): ')   # file path

start = 'default'   # variable to store starting page number

while True:
    try:
        start = int(input('Enter the starting page number to read: '))
        break
    except ValueError:
        print('Invalid Entry! Try again')
        continue

end = input('Enter the last page number to be read(skip to read all pages): ')
extract_page(file, start, end)
