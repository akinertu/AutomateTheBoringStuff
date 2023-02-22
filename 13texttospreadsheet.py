#! python3
# texttospreadsheat.py #Reads each line from text and paste it each row in spreadsheet.
import re, openpyxl
text = open('data/exampletext.txt', encoding="utf8")
textContent = text.read().replace('\n', ' ')
lines = re.split('(?<=[.!?]) +',textContent)

wb = openpyxl.Workbook()
sheet = wb['Sheet']

for i in range (1, len(lines)):
    sheet['A'+str(i)] = lines[i]
wb.save(('data/lines.xlsx'))

