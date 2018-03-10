from xlsxwriter import Workbook


wb = Workbook("test_excel.xlsx")

worksheet = wb.add_worksheet()
# worksheet.write(0, 0, "zero row and zero column")
# worksheet.write(0, 1, "zero row and first column")
# worksheet.write(1, 0, "one row and zero column")
# worksheet.write(1, 1, "one row and one column")

for row in range(0,20):
    worksheet.write(row, 0, "Row Number")
    worksheet.write(row, 1, row)

wb.close()