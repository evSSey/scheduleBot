import xlsxwriter
from main import *

# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()


row = "ABCDEFGHIJKLMNOP"
column = "123456789"
# Write some simple text.
worksheet.write('A1', '')

row_grade = 0
for grade in schedule:
    row_grade += 1
    worksheet.write(row[row_grade] + "1", grade)

    column_lesson = 2
    for lesson in schedule[grade]["Понедельник"]:
        worksheet.write(row[row_grade] + str(column_lesson), schedule[grade]["Понедельник"][lesson])
        column_lesson += 1


workbook.close()