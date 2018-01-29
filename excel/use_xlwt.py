import xlwt

wbk = xlwt.Workbook()

sheet = wbk.add_sheet('sheet1')

sheet.write(0,1,'test text')
wbk.save('test_xlwt.xls')



