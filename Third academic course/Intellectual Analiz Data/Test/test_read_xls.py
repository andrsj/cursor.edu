import xlrd
print(xlrd.__version__)

# excel_data_file = xlrd.open_wordbook("database_Ukraine.xlsx")
# sheet = excel_data_file.sheet_by_index(0)

# massive = []
# row_number = sheet.nrows

# if row_number > 0:
#     for row in range(0,row_number):
#         massive.append(str(sheet.row(row)[0]))
#     print(len(massive))
# else:
#     print("suck my dick")

# print("\n".join(massive))