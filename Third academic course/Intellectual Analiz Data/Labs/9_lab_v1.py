import matplotlib.pyplot as plt
import xlrd
import numpy as np


files = xlrd.open_workbook(filename = "00_0204.xls") # зчитання файлу
sheet = files.sheet_by_index(0) # номер листка

years = []
for row in range(5,31):
    years.append(str(sheet.row(row)[8]))
for year in years:
    years[years.index(year)] = int(float(year.split(":")[1]))

year = str(sheet.row(4)[4]).split(":")[1].split(".")[0]

counts = []
for row in range(5,31):
    counts.append(str(sheet.row(row)[9]))
for count in counts:
    counts[counts.index(count)] = int(float(count.split(":")[1]))

r1 = 0
r2 = 0
for i in range(len(years)):
    r1 += years[i] * counts[i]
    r2 += years[i] ** 2 * counts[i]

F = np.array([
    [sum([i**4 for i in years]),sum([i**3 for i in years]),sum([i**2 for i in years])],
    [sum([i**3 for i in years]),sum([i**2 for i in years]),sum(years)],
    [sum([i**2 for i in years]),sum(years),len(years)]
    ])
G = np.array([
    r2,
    r1,
    sum(counts)])

H = np.linalg.solve(F,G)

y = []

for i in years:
    y.append(H[0] * i**2 + H[1] * i + H[2])

a = []
a.append( (sum(counts) * sum([i*i for i in years]) - r1 * sum(years)) / ( len(years) * sum([i*i for i in years]) - sum(years) * sum(years) ) )
a.append( (len(years) * r1 - sum(years) * sum (counts)) / ( len(years) * sum([i*i for i in years]) - sum(years) * sum(years) ) )

y_ = []

for i in years:
    y_.append(a[1] * i + a[0])

plt.figure()
plt.plot(years,counts)
plt.plot(years,y)
plt.plot(years,y_)
plt.grid()
plt.show()