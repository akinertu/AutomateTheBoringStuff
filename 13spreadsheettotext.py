#! python3
# spreadsheettotext.py #Reads each row from spreadsheat and creates text file.

import openpyxl
wb = openpyxl.load_workbook('data/lines.xlsx')
sheet = wb['Sheet']
lines = []
text = ''

for rowNum in range(1, sheet.max_row+1):
    text += sheet['A'+str(rowNum)].value + ' '

textFile = open('data/linestotext.txt', 'a')
textFile.write(text)
textFile.close()


