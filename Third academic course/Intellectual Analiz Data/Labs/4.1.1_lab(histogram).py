import xlrd
import matplotlib.pyplot as plt
import numpy as np

files = xlrd.open_workbook(filename = "database_Ukraine.xls") # зчитання файлу
sheet = files.sheet_by_index(0) # номер листка
row_number = sheet.nrows # к-сть записаних рядків


massive = []
massive_numbers = []
massive_years = []
massive_numbers_village = []
massive_numbers_city = []




for row in range(4,row_number-10): # з (*N*,row_number) рядка до останього записаного
    massive.append(str(sheet.row(row)[1])) # [Номер стовпця] - числа(значення)
for i in massive:
    massive_numbers.append(float(i.split(":")[1])) # Взяти число з масиву (а не текст)
# print(massive_numbers)
    
    
massive = []
for row in range(4,row_number-10):
    massive.append(str(sheet.row(row)[0]))  # Роки   
# for i in massive:
#     print(i.split(":")[1][1:-1]) # Обрізати лапки скраю    
for i in massive:
    massive_years.append(int(i.split(":")[1][1:-1]))  # [1:-1] - обрізати лапки по краю числа
# print(massive_years)

massive = []
for row in range(4,row_number-10):
    massive.append(str(sheet.row(row)[2]))
for i in massive:
    massive_numbers_city.append(float(i.split(":")[1]))
# print(massive_numbers_city)

massive = []
for row in range(4,row_number-10):
    massive.append(str(sheet.row(row)[3]))
for i in massive:
    massive_numbers_village.append(float(i.split(":")[1]))
# print(massive_numbers_village)

massive = []

# y = np.random.random(26) 
# # print(y)
# y1 = [i * 1e8 for i in y]
# # print(y1)
massive_numbers_city = [i - 3.0e7 for i in massive_numbers_city]
massive_numbers_village = [i - 1.2e7 for i in massive_numbers_village]

plt.figure()
plt.bar(massive_years, massive_numbers_village, label="Село", color="red", alpha = 0.3)
# plt.figure()
plt.bar(massive_years, massive_numbers_city, label="Місто", alpha = 0.3 , color="blue")
# plt.bar(massive_years, y1, label="Рандом", alpha = 0.7, color="orange")
plt.title('Порівняння жителів України в містах і селах')
plt.legend(loc='upper right')
plt.grid(True)
plt.show()