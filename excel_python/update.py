import xlrd
from xlutils.copy import copy

book = xlrd.open_workbook("py_write.xlsx")

wb = copy(book)

sh1 = wb.get_sheet(0)

sh1.write(0,0,"真实姓名")

wb.save("test.xlsx")
