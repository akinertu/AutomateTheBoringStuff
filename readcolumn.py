import openpyxl
wb = openpyxl.load_workbook('data/example.xlsx')
sheet = wb.active
list(sheet.columns)[1]
for cellObj in list(sheet.columns)[1]:
    print(cellObj.value)