
'''
Program to read/write on excel files
Price = [ Total Value (Lacs) multiplied by 100000 ] divided by [Quantity (000’s) multiplied by 100]
'''

import xlrd


li = []
di = {}
file_path = input('Enter file path:')

wb = xlrd.open_workbook(file_path)
sheet = wb.sheet_by_index(0)
headers = [(i,sheet.cell_value(0,i)) for i in range(sheet.ncols)]
di['dates'] = [sheet.cell_value(i,1) for i in range(1,sheet.nrows)]
di['qty'] = [sheet.cell_value(i,3) for i in range(1,sheet.nrows)]
di['total values'] = [sheet.cell_value(i,4) for i in range(1,sheet.nrows)]

print(di)