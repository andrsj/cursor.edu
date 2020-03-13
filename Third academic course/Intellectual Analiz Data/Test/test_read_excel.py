from openpyxl import load_workbook

wb_val = load_workbook(filename = '000_0201.xls', data_only = True)

sheet_val = wb_val['matrix']

B5_val = sheet_val['B5'].value

print(B5_val)