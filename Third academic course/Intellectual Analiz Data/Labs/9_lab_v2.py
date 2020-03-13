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
c = []
for row in range(5,31):
    counts.append(str(sheet.row(row)[9]))
    c.append(str(sheet.row(row)[9]))
for count in counts:
    counts[counts.index(count)] = int(float(count.split(":")[1]))
    c[c.index(count)] = int(float(count.split(":")[1]))



for i in range(3):
    del years[-1]
    del counts[-1]

# for i,j in zip(years,counts):
#     print(i,'\t',j)

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


for i in range(2012,2015):
    y.append(H[0] * i**2 + H[1] * i + H[2])

a = []
a.append( (sum(counts) * sum([i*i for i in years]) - r1 * sum(years)) / ( len(years) * sum([i*i for i in years]) - sum(years) * sum(years) ) )
a.append( (len(years) * r1 - sum(years) * sum (counts)) / ( len(years) * sum([i*i for i in years]) - sum(years) * sum(years) ) )

y_ = []

for i in years:
    y_.append(a[1] * i + a[0])
for i in range(2012,2015):
    y_.append(a[1] * i + a[0])




plt.figure()

for i in range(2012,2015):
    years.append(i)
    counts.append(a[1] * i + a[0])

plt.plot(years,counts,"-x")


f = open("9lab.txt","w")
f.write("Прямий тренд\n")
for i,j,k in zip(years[-3:], counts[-3:], c[-3:]):
	f.write(f"{i}\t{int(j)}\t{k}\n")


for i in range(2012,2015):
    del counts[-1]

for i in range(2012,2015):
    counts.append(H[0] * i**2 + H[1] * i + H[2])

f.write("\n\nПараболічний тренд\n")
for i,j,k in zip(years[-3:], counts[-3:], c[-3:]):
	f.write(f"{i}\t{int(j)}\t{k}\n")
f.close()


plt.plot(years,counts,"-x")





plt.plot(years,y,alpha = 0.5)
plt.plot(years,y_,alpha = 0.5)

plt.plot(years,c,'-o',alpha = 0.5)

plt.grid()

for i,j in zip(years,counts):
    print(i,'\t',j)

plt.show()


