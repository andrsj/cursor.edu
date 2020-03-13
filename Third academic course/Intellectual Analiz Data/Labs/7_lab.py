import xlrd
import xlwt
import matplotlib.pyplot as plt


files = xlrd.open_workbook(filename = "00_0204.xls") # зчитання файлу
sheet = files.sheet_by_index(0) # номер листка

# sheet.nrows 
# к-сть записаних рядків

# print(sheet.nrows)
# print(sheet.row(0)[0]) # (Рядок)[Стовбець]
# print(sheet.row(3)[0]) # (Рядок)[Стовбець]

years = []
for row in range(5,31):
    years.append(str(sheet.row(row)[0]))
for year in years:
    years[years.index(year)] = int(float(year.split(":")[1]))

years.append(2015)

year = str(sheet.row(4)[0]).split(":")[1].split(".")[0]

counts = []
for row in range(5,31):
    counts.append(str(sheet.row(row)[1]))
for count in counts:
    counts[counts.index(count)] = int(float(count.split(":")[1]))



y7_1 = counts

y7_2 = []
i = 1
while i < len(counts):
    y7_2.append(counts[i] + (counts[i] - counts[i-1]))
    i += 1

y7_3 = []
i = 1
while i < len(counts):
    y7_3.append(counts[i] * counts[i] / counts[i-1])
    i += 1

y7_4 = []
for j in counts:
    y7_4.append( (1/len(counts[ : counts.index(j) + 1])) * sum(counts[ : counts.index(j) + 1]))


# fig = plt.figure()
# fig.suptitle(year + " років " + str(sheet.row(3)[0]).split(":")[1] + "\nКовзне середнє")
K = 4
y7_5 = []
k = K
for j in range(k , len(counts)):
    sum = 0
    for i in range(k + 1):

        sum += counts[j-i]
    y7_5.append( (1/(k+1)) * sum )


plt.plot(years[:-1],counts, "-x")
plt.plot(years[ k+1 :],y7_5,"--o")
plt.grid()


plt.figure()
plt.suptitle(year + " років " + str(sheet.row(3)[0]).split(":")[1] + "\nЕкспоненціальне середнє")

y7_6 = []
alpha = [0.1,0.3,0.5,0.7,0.9]

for j in range(len(alpha)):
    i = 1
    y7_6.append([counts[0],])
    while i < len(counts):
        y7_6[j].append(alpha[j] * counts[i] + (1 - alpha[j]) * y7_6[j][i-1])
        i += 1

    plt.plot(years[1:],y7_6[j][:], label = str(alpha[j]))

plt.plot(years[:-1],counts , "--")
plt.grid()
plt.legend()


plt.figure()
plt.suptitle(year + " років " + str(sheet.row(3)[0]).split(":")[1] + "\n 'Завтра буде як сьогодні'")

plt.plot(years[1:],y7_1)
plt.plot(years[:-1],counts, "--")
plt.grid()
plt.figure()
plt.suptitle("7.2")

plt.plot(years[2:],y7_2)
plt.plot(years[:-1],counts, "--")
plt.grid()
plt.figure()
plt.suptitle("7.3")

plt.plot(years[2:],y7_3)
plt.plot(years[:-1],counts, "--")
plt.grid()
plt.figure()
plt.suptitle("7.4")

plt.plot(years[1:],y7_4)
plt.plot(years[:-1],counts, "--")
plt.grid()



c = 0
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet("Test")
for i,j,k in zip(years[1:-1],counts[1:],y7_1[:-1]):
    worksheet.write(c,0,i)
    worksheet.write(c,1,j)
    worksheet.write(c,2,k)
    c += 1
worksheet.write(c,2,"7.1")

c = 0
for i,j,k in zip(years[2:-1],counts[2:],y7_2[:-1]):
    worksheet.write(c,4,i)
    worksheet.write(c,5,j)
    worksheet.write(c,6,k)
    c += 1
worksheet.write(c,6,"7.2")
c = 0
for i,j,k in zip(years[2:-1],counts[2:],y7_3[:-1]):
    worksheet.write(c,8,i)
    worksheet.write(c,9,j)
    worksheet.write(c,10,k)
    c += 1
worksheet.write(c,10,"7.3")
c = 0
for i,j,k in zip(years[1:-1],counts[1:],y7_4[:-1]):
    worksheet.write(c,12,i)
    worksheet.write(c,13,j)
    worksheet.write(c,14,k)
    c += 1
worksheet.write(c,14,"7.4")
c = 0
for i,j,k in zip(years[K + 1:-1],counts[K + 1:],y7_5[:-1]):
    worksheet.write(c,16,i)
    worksheet.write(c,17,j)
    worksheet.write(c,18,k)
    c += 1
worksheet.write(c,18,"7.5")
c = 0
for i,j,k in zip(years[1:-1],counts[1:],y7_6[4][:-1]):
    worksheet.write(c,20,i)
    worksheet.write(c,21,j)
    worksheet.write(c,22,k)
    c += 1
worksheet.write(c,22,"7.6")
workbook.save("7.xls")
plt.show()

