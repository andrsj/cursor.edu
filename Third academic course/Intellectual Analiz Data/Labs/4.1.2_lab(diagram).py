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
labels = ["Село","Місто"]


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

percent_village = massive_numbers_village[11] / massive_numbers[11]

massive = []
fig = plt.figure()
plt.title("Частка населення України на 2000 рік")
plt.text(0.15,0.3,"Село\n32.6%", fontsize = 10)
plt.text(-0.5,-0.3,"Місто\n67.4%", fontsize = 10)
plt.pie([massive_numbers_village[11],massive_numbers_city[11]], radius = 1, labels = None, shadow = False, explode = (0,0)) # autopct='%1.1f%%')
plt.show()