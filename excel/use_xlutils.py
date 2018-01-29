import xlrd
from xlutils.copy import copy

workbook=xlrd.open_workbook('yangben.xls')
workbooknew = copy(workbook)
ws = workbooknew.get_sheet(0)
ws.write(3,0,'changed!')

workbooknew.save('yangben_update.xls')