import xlrd

workbook = xlrd.open_workbook('yangben.xls')
sheet_names = workbook.sheet_names()
for sheet_name in sheet_names:
    sheet2 = workbook.sheet_by_name(sheet_name)
    print(sheet_name)
    rows =sheet2.row_values(3) ## fourth  content
    cols = sheet2.col_values(1) ## second
    print(rows)
    print(cols)

