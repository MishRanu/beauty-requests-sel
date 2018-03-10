import xlrd


wb = xlrd.open_workbook("test_excel.xlsx")


worksheet = wb.sheet_by_index(0)

print(worksheet.nrows)

for row in range(worksheet.nrows):
    first_col, second_col = worksheet.row_values(row)
    print(first_col, ' ', second_col)

