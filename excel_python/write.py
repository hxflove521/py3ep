import xlwt

wb = xlwt.Workbook()

ws1 = wb.add_sheet("成绩表")
ws2 = wb.add_sheet("分数表")

ws1.write(0,0,"姓名")
ws1.write(0,1,"性别")
ws1.write(1,0,"张三")
ws1.write(1,1,"男")

wb.save("py_write.xlsx")
