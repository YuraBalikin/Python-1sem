
from CSV import creating
from Module import writing_csv
from Module import writing_txt


path = 'Телефонная книга.csv'
valid = (path)
if not valid:
    creating()

writing_csv()
writing_txt()